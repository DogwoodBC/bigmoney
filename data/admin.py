from django.contrib import admin
from .models import Donation, Filer, ElectoralDistrict, Contributor, ContributorIndividual, ContributorOrganization, \
    UniqueIndividual, UniqueOrganization


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'contributor', 'filer', 'date', 'amount']
    search_fields = ['id', 'contributor__organization__name', 'contributor__individual__name', 'filer__name', 'date', 'amount']
    list_filter = ['filer__affiliation', 'filer__electoral_district__name']


@admin.register(Filer)
class FilerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'affiliation', 'type', 'electoral_district']
    list_filter = ['type', 'affiliation', 'electoral_district']


@admin.register(ElectoralDistrict)
class ElectoralDistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'boundary_set']
    search_fields = ['name']


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'contributor_class', 'individual', 'organization']
    search_fields = ['individual__name', 'individual__name_first_middle', 'individual__name_last', 'organization__name']
    list_filter = ['contributor_class']
    actions = ['accept_as_unique']

    def accept_as_unique(self, request, queryset):
        # Load the entry into the corresponding "unique" table, as-is.
        new = 0
        existing = 0

        for obj in queryset:
            if obj.contributor_class == '1':
                contributor_individual = obj.individual
                unique_individual, created = UniqueIndividual.objects.get_or_create(
                    name=contributor_individual.name,
                    name_first_middle=contributor_individual.name_first_middle,
                    name_last=contributor_individual.name_last)
                # I don't understand why I need to use `update` rather than just saving the relationship
                ContributorIndividual.objects.filter(id=contributor_individual.id)\
                    .update(unique_individual=unique_individual)
                if created:
                    new += 1
                else:
                    existing += 1

            else:
                contributor_organization = obj.organization
                unique_organization, created = UniqueOrganization.objects.get_or_create(name=contributor_organization.name)
                contributor_organization.unique_organization = unique_organization
                ContributorOrganization.objects.filter(id=contributor_organization.id)\
                    .update(unique_organization=unique_organization)
                if created:
                    new += 1
                else:
                    existing += 1

        if request:
            message = 'Added {} new unique entries, skipped {} existing ones.'.format(new, existing)
            self.message_user(request, message)
    accept_as_unique.short_description = 'Load into unique table(s)'


@admin.register(ContributorIndividual)
class ContributorIndividualAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_first_middle', 'name_last', 'unique_individual']
    search_fields = ['id', 'name', 'name_first_middle', 'name_last', 'unique_individual__name',
                     'unique_individual__name_first_middle', 'unique_individual__name_last']


class ContributorIndividualInline(admin.TabularInline):
    model = ContributorIndividual


@admin.register(ContributorOrganization)
class ContributorOrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unique_organization']
    search_fields = ['id', 'name', 'unique_organization__name']


@admin.register(UniqueIndividual)
class UniqueIndividualAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_first_middle', 'name_last']
    search_fields = ['id', 'name', 'name_first_middle', 'name_last']
    actions = ['delete_if_orphan']

    def delete_if_orphan(self, request, queryset):
        # If this unique individual isn't linked to any contributors any more, delete it.
        # This is done so there aren't ghost entries with donation totals of "0".
        deleted = 0
        preserved = 0

        for obj in queryset:
            contributors = ContributorIndividual.objects.filter(unique_individual=obj)
            if len(contributors) == 0:
                obj.delete()
                deleted += 1
            else:
                preserved += 1

        if request:
            message = 'Deleted {} orphaned unique individual(s), preserved {} with connections.'.format(
                deleted, preserved)
            self.message_user(request, message)
    delete_if_orphan.short_description = 'Delete if orphaned'


@admin.register(UniqueOrganization)
class UniqueOrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    actions = ['delete_if_orphan']

    def delete_if_orphan(self, request, queryset):
        # If this unique individual isn't linked to any contributors any more, delete it.
        # This is done so there aren't ghost entries with donation totals of "0".
        deleted = 0
        preserved = 0

        for obj in queryset:
            contributors = ContributorOrganization.objects.filter(unique_organization=obj)
            if len(contributors) == 0:
                obj.delete()
                deleted += 1
            else:
                preserved += 1

        if request:
            message = 'Deleted {} orphaned unique organization(s), preserved {} with connections.'.format(
                deleted, preserved)
            self.message_user(request, message)
    delete_if_orphan.short_description = 'Delete if orphaned'
