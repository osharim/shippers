# encoding: utf-8
from django.contrib import admin
from .models import CatalogCategory, CatalogRequirement


@admin.register(CatalogCategory)
class CatalogCategoryAdmin(admin.ModelAdmin):

    readonly_fields = ["created", ]
    fieldsets = (("Catalog", {"fields": ("name", )}), )
    list_display = ["name",]
    search_fields = ["name", ]


@admin.register(CatalogRequirement)
class CatalogRequirementAdmin(admin.ModelAdmin):

    readonly_fields = ["created", ]
    list_display = ["category", "name", ]
    list_filter = ["category", ]
