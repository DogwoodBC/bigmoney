from django.contrib import admin
from .models import Donation, Filer, ElectoralDistrict, Contributor, ContributorIndividual, ContributorOrganization, \
    UniqueIndividual, UniqueOrganization


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'contributor', 'filer', 'date', 'amount']


@admin.register(Filer)
class FilerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'affiliation', 'type', 'electoral_district']


@admin.register(ElectoralDistrict)
class ElectoralDistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'boundary_set']


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'contributor_class', 'individual', 'organization']


@admin.register(ContributorIndividual)
class ContributorIndividualAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unique_individual']


@admin.register(ContributorOrganization)
class ContributorOrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(UniqueIndividual)
class UniqueIndividualAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(UniqueOrganization)
class UniqueOrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
