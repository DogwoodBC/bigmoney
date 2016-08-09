from rest_framework import serializers

from .models import Donation, Contributor, ContributorIndividual, ContributorOrganization, Filer, ElectoralDistrict, \
    UniqueIndividual, UniqueOrganization


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        depth = 2  # Show the contributor org/individual, and the filer details.


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        depth = 1  # Show the organization or individual.


class ContributorOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorOrganization


class ContributorIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorIndividual


class FilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer
        depth = 1  # Show the electoral district information.


class ElectoralDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralDistrict


class UniqueIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueIndividual


class UniqueOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueOrganization
