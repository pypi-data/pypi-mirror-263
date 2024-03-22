import os
from django.db.models import Max
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

from .models import (
    AnalyticsProfile,
    Analytics,
    PageStats,
    Page,
)
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.paginator import Paginator

SECRETS = os.path.join(
    settings.SECRET_ROOT, "secrets/csgoogleanalytics_secrets.json"
)

URL_VALIDATOR = getattr(
    settings,
    "CSGOOGLEANALYTICS_URL_VALIDATOR",
    "csgoogleanalytics.validators.default_validator",
)


def _load_validator():
    validator = __import__(".".join(URL_VALIDATOR.split(".")[:-1]))
    for n in URL_VALIDATOR.split(".")[1:]:
        validator = getattr(validator, n)
    return validator


def get_most_viewed_urls():
    client = BetaAnalyticsDataClient.from_service_account_file(SECRETS)
    profile = AnalyticsProfile.siteobjects.first()

    request = RunReportRequest(
        property="properties/{}".format(profile.tracking_code),
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date="yesterday", end_date="today")],
    )
    return client.run_report(request)


def create_analytics(max_results=100):
    Analytics.siteobjects.all().delete()
    data = get_most_viewed_urls()
    validator = _load_validator()
    for row in data.rows[:max_results]:
        an = Analytics(
            path=row.dimension_values[0].value,
            title=row.dimension_values[0].value,
            pageviews=row.metric_values[0].value,
            site=Site.objects.get_current(),
        )
        try:
            is_valid, title, photo_src, content_type, object_id = validator(
                row.dimension_values[0].value
            )
            an.is_valid = is_valid
            an.title = title
            an.photo_src = photo_src
            an.content_type = content_type
            an.object_id = object_id
        except:
            pass
        an.save()


def get_pageviews_from_urls(pagepaths, start_date, end_date):
    """
    https://www.googleapis.com/analytics/v3/data/ga?ids=ga%3A14407&start-date=2017-05-08&end-date=2018-05-08&metrics=ga%3Apageviews&dimensions=ga%3ApagePath&filters=ga%3ApagePath%3D%3D%2Faktualitatea%2F1524904927196%2Cga%3ApagePath%3D%3D%2Faktualitatea%2F1525336600
    """
    service = _build_analytics_service()
    profile = AnalyticsProfile.siteobjects.first()
    strpagepaths = ",".join(["ga:pagePath=={}".format(a) for a in pagepaths])
    max_results = len(pagepaths)
    return (
        service.data()
        .ga()
        .get(
            ids="ga:{}".format(profile.tracking_code),
            start_date=start_date,
            end_date=end_date,
            metrics="ga:pageviews",
            dimensions="ga:pagePath",
            filters=strpagepaths,
            sort="-ga:pageviews",
            max_results=max_results,
        )
        .execute()
    )


def create_page_stats(pagepaths_list, start_date_str, end_date_str, period_id):
    """ """
    pager = Paginator(pagepaths_list, 10)
    for i in pager.page_range:
        pagepaths = pager.page(i).object_list
        results = get_pageviews_from_urls(
            pagepaths, start_date_str, end_date_str
        )
        for row in results.get("rows", []):
            page = Page.objects.get(pagepath=row[0])
            PageStats.objects.filter(page=page, period=period_id).delete()
            pstats = PageStats()
            pstats.page = page
            pstats.period = period_id
            pstats.pageviews = row[1]
            pstats.save()

    return True


def page_stats_years():
    return list(
        Page.objects.all().distinct().values_list("added_year", flat=True)
    )


def page_stats_months(year):
    return list(
        Page.objects.filter(added_year=year)
        .distinct()
        .values_list("added_month", flat=True)
    )


def page_stats_weeks(year):
    return list(
        Page.objects.filter(added_year=year)
        .distinct()
        .values_list("added_week", flat=True)
    )


def page_stats_days(month):
    return list(
        Page.objects.filter(added_month=month)
        .distinct()
        .values_list("added_day", flat=True)
    )


def page_year(year):
    qs = Page.objects.filter(added_year=year)
    qs = qs.annotate(bisitak=Max("pagestats__pageviews"))
    qs = qs.order_by("-bisitak")
    return qs


def page_month(month):
    qs = Page.objects.filter(added_month=month)
    qs = qs.annotate(bisitak=Max("pagestats__pageviews"))
    qs = qs.order_by("-bisitak")
    return qs
