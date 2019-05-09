# encoding: utf-8
from django.contrib import admin
from .models import Carrier, CarrierRequirement


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):

    readonly_fields = ["created", ]
    fieldsets = (("Carrier", {"fields": ("company_name", "address", "phone",
                                         "email", "owner_name", "owner_surname", "status", )}), )
    list_display = ["company_name", "address", "email", "phone", "get_status", "view_requirements", ]
    search_fields = ["company_name", ]


@admin.register(CarrierRequirement)
class CarrierRequirementAdmin(admin.ModelAdmin):

    exclude = ["category", ]
    list_filter = ["carrier", "category", "requirement", ]
    readonly_fields = ["created", ]
    list_display = ["carrier", "category", "requirement"]
