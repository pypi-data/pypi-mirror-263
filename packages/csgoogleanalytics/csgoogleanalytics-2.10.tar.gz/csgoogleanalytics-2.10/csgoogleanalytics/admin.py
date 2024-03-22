from django.contrib import admin
from django.urls import reverse
from django.db.models import Max
from django.http import HttpResponseRedirect
from django_object_actions import DjangoObjectActions
from .models import Analytics, AnalyticsProfile


# class CredentialsModelAdmin(admin.ModelAdmin):
#     list_display = ("id", "credential", "is_valid", "token_expiry", "has_refresh_token")

#     def token_expiry(self, obj):
#         try:
#             return obj.credential.token_expiry
#         except:
#             return ""


class AnalyticsProfileAdmin(admin.ModelAdmin):
    list_display = ("tracking_code", "site")


class AnalyticsAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ("path", "title", "pageviews", "is_valid", "site")
    list_filter = ("site", "is_valid")
    date_hierarchy = "date_added"
    ordering = ("-pageviews",)

    # def authorize(self, request, queryset):
    #     return HttpResponseRedirect(reverse("set_google"))

    # authorize.label = "Authorize GAnalytics"

    def refresh(self, request, queryset):
        from .utils import create_analytics

        create_analytics()

    refresh.label = "Update URLs"

    # def get_changelist_actions(self, request):
    #     credentialsmodel = CredentialsModel.objects.first()
    #     actions = ("authorize",)
    #     if credentialsmodel and credentialsmodel.is_valid:
    #         actions = ("refresh",)
    #     return actions

    # changelist_actions = ("refresh", "authorize")


# class PageAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(PageAdmin, self).get_queryset(request)
#         qs = qs.annotate(bisitak=Max("pagestats__pageviews"))
#         return qs

#     def bisitak(self, obj):
#         return obj.bisitak

#     bisitak.short_description = "Bisitak"
#     bisitak.admin_order_field = "bisitak"

#     def bisita_guztiak(self, obj):
#         stats = (
#             obj.pagestats_set.all()
#             .order_by("period")
#             .values_list("pageviews", flat=True)
#         )
#         return list(stats)

#     bisita_guztiak.short_description = "Bisita guztiak"

#     list_display = ("added_day", "pagepath", "bisitak", "bisita_guztiak")
#     date_hierarchy = "added_at"


admin.site.register(Analytics, AnalyticsAdmin)
admin.site.register(AnalyticsProfile, AnalyticsProfileAdmin)
# admin.site.register(Page, PageAdmin)
