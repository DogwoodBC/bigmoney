from django.shortcuts import render
from django.db.models import Sum, Count

import django_filters
from rest_framework import viewsets
from rest_framework import filters

from .models import Donation, Contributor, ContributorOrganization, ContributorIndividual, Filer, UniqueOrganization, \
    UniqueIndividual, ElectoralDistrict
from .serializers import DonationSerializer, ContributorSerializer, ContributorIndividualSerializer, \
    ContributorOrganizationSerializer, FilerSerializer, UniqueIndividualSerializer, UniqueOrganizationSerializer, \
    ElectoralDistrictSerializer


class FilerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filer.objects.all()
    serializer_class = FilerSerializer
    filter_fields = ('type', 'affiliation', 'electoral_district')
    search_fields = ('name',)
    ordering_fields = ('id',)


class DonationFilter(filters.FilterSet):
    min = django_filters.NumberFilter(name='amount', lookup_expr='gte')
    max = django_filters.NumberFilter(name='amount', lookup_expr='lte')
    after = django_filters.DateFilter(name='date', lookup_expr='gte')
    before = django_filters.DateFilter(name='date', lookup_expr='lte')

    class Meta:
        model = Donation
        fields = ('min', 'max', 'after', 'before', 'contributor__id', 'contributor__contributor_class',
                  'filer__affiliation', 'filer__type',)


class DonationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    search_fields = ('contributor__organization__name', 'contributor__individual__name', 'filer__name')
    ordering_fields = ('id', 'amount', 'date',)
    filter_class = DonationFilter


class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    # This works because Donations.contributor has related_name='donations':
    queryset = Contributor.objects\
        .annotate(contributions_count=Count('donations'))\
        .annotate(contributions_total=Sum('donations__amount'))
    serializer_class = ContributorSerializer
    filter_fields = ('contributor_class', 'organization__name', 'individual__name_first_middle', 'individual__name_last')
    search_fields = ('individual__name_first_middle', 'individual__name_last', 'organization__name')
    ordering_fields = ('id', 'individual__name_first_middle', 'individual__name_last', 'organization__name',
                       'contributions_count', 'contributions_total')


class ContributorOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContributorOrganization.objects.all()
    serializer_class = ContributorOrganizationSerializer
    search_fields = ('name',)
    filter_fields = ()
    ordering_fields = ('id', 'name')


class ContributorIndividualViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContributorIndividual.objects.all()
    serializer_class = ContributorIndividualSerializer
    search_fields = ('name', 'name_first_middle', 'name_last')
    filter_fields = ()
    ordering_fields = ('id', 'name')


class UniqueIndividualViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniqueIndividualSerializer
    search_fields = ('name', 'name_first_middle', 'name_last')

    def get_queryset(self):
        queryset = UniqueIndividual.objects\
            .annotate(donations_count=Count('contributorindividual__contributor__donations')) \
            .annotate(donations_total=Sum('contributorindividual__contributor__donations__amount')) \
            .order_by('id')
        print(queryset.query)
        return queryset


class UniqueOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniqueOrganizationSerializer
    search_fields = ('name')

    def get_queryset(self):
        queryset = UniqueOrganization.objects\
            .annotate(donations_count=Count('contributororganization__contributor__donations')) \
            .annotate(donations_total=Sum('contributororganization__contributor__donations__amount')) \
            .order_by('id')

        return queryset


class ElectoralDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ElectoralDistrict.objects.all()
    serializer_class = ElectoralDistrictSerializer
    search_fields = ('name',)
    filter_fields = ('boundary_set',)
    ordering_fields = ('id', 'name')
