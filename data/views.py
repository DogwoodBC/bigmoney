from django.shortcuts import render
from rest_framework import viewsets

from .models import Donation, Contributor, ContributorOrganization, ContributorIndividual, Filer, UniqueOrganization, \
    UniqueIndividual, ElectoralDistrict
from .serializers import DonationSerializer, ContributorSerializer, ContributorIndividualSerializer, \
    ContributorOrganizationSerializer, FilerSerializer, UniqueIndividualSerializer, UniqueOrganizationSerializer, \
    ElectoralDistrictSerializer


class FilerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FilerSerializer
    filter_fields = ('id', 'type', 'affiliation', 'name', 'electoral_district')
    # search_fields = ('id', 'type', 'affiliation', 'name', 'electoral_district')

    def get_queryset(self):
        queryset = Filer.objects.all().order_by('id')

        return queryset


class DonationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DonationSerializer

    def get_queryset(self):
        queryset = Donation.objects.all().order_by('id')

        return queryset


class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        queryset = Contributor.objects.all().order_by('id')

        return queryset


class ContributorOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorOrganizationSerializer

    def get_queryset(self):
        queryset = ContributorOrganization.objects.all().order_by('id')

        return queryset


class ContributorIndividualViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorIndividualSerializer

    def get_queryset(self):
        queryset = ContributorIndividual.objects.all().order_by('id')

        return queryset


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
    serializer_class = ElectoralDistrictSerializer

    def get_queryset(self):
        queryset = ElectoralDistrict.objects.all().order_by('id')

        return queryset
