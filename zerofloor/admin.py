from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse

from .models import Flat
from .models import ExpenseType
from .models import ApartmentBankAccounts
from .models import MonthlyDetails
from .models import MonthlyCollections
from .models import MonthlyExpenses
from .models import VendorDetails
from .models import Report


admin.site.site_header = "ZERO FLOOR";
admin.site.site_title = "ZERO FLOOR";


# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    def get_urls(self):

        # get the default urls
        urls = super(ReportAdmin, self).get_urls()
        # define security urls
        report_urls = [
            url(r'^report/$', self.admin_site.admin_view(self.report_page))
            # Add here more urls if you want following same logic
        ]

        # Make sure here you place your added urls first than the admin default urls
        return report_urls + urls

    # Your view definition fn
    def report_page(self, request):
        context = dict(
            self.admin_site.each_context(request), # Include common variables for rendering the admin template.
            something="test",
        )
       
        return TemplateResponse(request, "report.html", context)

# admin.register(ReportAdmin)

# admin.site.register(Report)
admin.site.register(Flat)
admin.site.register(ExpenseType)
admin.site.register(ApartmentBankAccounts)
admin.site.register(MonthlyDetails)

@admin.register(VendorDetails)
class VendorDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(MonthlyCollections)
class MonthlyCollectionsAdmin(admin.ModelAdmin):
    class Media:
        js = ("monthlyCollections.js",)

        
# admin.register(MonthlyCollections,MonthlyCollectionsAdmin)
@admin.register(MonthlyExpenses)
class MonthlyExpensessAdmin(admin.ModelAdmin):
    class Media:
        js = ("monthlyCollections.js",)