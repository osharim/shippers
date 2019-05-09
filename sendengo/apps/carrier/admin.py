# encoding: utf-8
from django.contrib import admin
from .models import Carrier, CarrierRequirement, Driver, Vehicle


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):

    readonly_fields = ["created", ]
    fieldsets = (("Carrier", {"fields": ("company_name", "address", "phone",
                                         "email", "owner_name", "owner_surname", "status", )}), )
    list_display = ["company_name", "address", "email", "phone", "get_status", "view_requirements", "get_shippers_in_compliance_count" ]
    search_fields = ["company_name", ]


@admin.register(CarrierRequirement)
class CarrierRequirementAdmin(admin.ModelAdmin):

    exclude = ["category", ]
    list_filter = ["carrier", "category", "requirement", ]
    readonly_fields = ["created", ]
    list_display = ["carrier", "category", "requirement"]


@admin.register(Driver)
class CarrierDriverAdmin(admin.ModelAdmin):

    list_filter = ["license_type", ]

    exclude = ["created", ]
    list_display = ["carrier", "name", "license_type", "license_number", "license_expiration", "get_status" ]


@admin.register(Vehicle)
class CarrierVehicleAdmin(admin.ModelAdmin):

    list_filter = ["type", ]

    exclude = ["created", ]
    list_display = ["carrier", "license_plate", "make", "model_type", "year", "type", "get_status", ]
