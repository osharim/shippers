from django.contrib import admin
from .models import Shipper, ShipperRequirement


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):

    readonly_fields = ["created", ]
    fieldsets = (("Shipper", {"fields": ("company_name", "address", "phone", "email", )}), )
    list_display = ["company_name", "address", "email", "phone", "view_requirements", "num_requirements"]
    search_fields = ["company_name", ]


@admin.register(ShipperRequirement)
class ShipperRequirementAdmin(admin.ModelAdmin):

    exclude = ["category", ]
    list_filter = ["shipper", "category", "requirement", ]
    readonly_fields = ["created", ]
    list_display = ["shipper", "category", "requirement"]
