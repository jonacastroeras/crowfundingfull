from django.contrib import admin

from projects.models import Project, Donation


# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "amount",)
    search_fields = ("name",)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donant", "amount",)
    search_fields = ("donant",)
