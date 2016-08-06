from django.contrib import admin
from .models import Donation, Filer, ElectoralDistrict, Contributor, ContributorIndividual, ContributorOrganization, \
    UniqueIndividual, UniqueOrganization


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass


@admin.register(Filer)
class FilerAdmin(admin.ModelAdmin):
    pass


@admin.register(ElectoralDistrict)
class ElectoralDistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    pass


@admin.register(ContributorIndividual)
class ContributorIndividualAdmin(admin.ModelAdmin):
    pass


@admin.register(ContributorOrganization)
class ContributorOrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(UniqueIndividual)
class UniqueIndividualAdmin(admin.ModelAdmin):
    pass


@admin.register(UniqueOrganization)
class UniqueOrganizationAdmin(admin.ModelAdmin):
    pass
