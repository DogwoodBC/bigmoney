from django.shortcuts import render
from rest_framework import viewsets, filters

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


class DonationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_fields = ('amount', 'contributor__contributor_class', 'filer__affiliation', 'filer__type')
    search_fields = ('contributor__organization__name', 'contributor__individual__name', 'filer__name')
    ordering_fields = ('id', 'amount', 'date',)


class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    filter_fields = ('contributor_class',)
    search_fields = ('individual__name', 'organization__name')
    ordering_fields = ('id', 'individual__name', 'organization__name')


class ContributorOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContributorOrganization.objects.all()
    serializer_class = ContributorOrganizationSerializer
    search_fields = ('name',)
    filter_fields = ()
    ordering_fields = ('id', 'name')


class ContributorIndividualViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContributorIndividual.objects.all()
    serializer_class = ContributorIndividualSerializer
    search_fields = ('name',)
    filter_fields = ()
    ordering_fields = ('id', 'name')


class UniqueIndividualViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniqueIndividualSerializer

    def get_queryset(self):
        queryset = UniqueIndividual.objects.all().order_by('id')

        return queryset


class UniqueOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniqueOrganizationSerializer

    def get_queryset(self):
        queryset = UniqueOrganization.objects.all().order_by('id')

        return queryset


class ElectoralDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ElectoralDistrict.objects.all()
    serializer_class = ElectoralDistrictSerializer
    search_fields = ('name',)
    filter_fields = ('boundary_set',)
    ordering_fields = ('id', 'name')
