from rest_framework import serializers

from .models import Donation, Contributor, ContributorIndividual, ContributorOrganization, Filer, ElectoralDistrict, \
    UniqueIndividual, UniqueOrganization


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor


class ContributorOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorOrganization


class ContributorIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorIndividual


class FilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer


class ElectoralDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralDistrict


class UniqueIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueIndividual


class UniqueOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueOrganization
