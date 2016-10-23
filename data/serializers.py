from rest_framework import serializers

from .models import Donation, Contributor, ContributorIndividual, ContributorOrganization, Filer, ElectoralDistrict, \
    UniqueIndividual, UniqueOrganization


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        depth = 2  # Show the contributor org/individual, and the filer details.


class ContributorOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorOrganization


class ContributorIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorIndividual
        exclude = ['name']  # Leave name out since first/middle and last name are included.


class ContributorSerializer(serializers.ModelSerializer):
    contributions_total = serializers.FloatField(read_only=True)
    contributions_count = serializers.IntegerField(read_only=True)
    individual = ContributorIndividualSerializer()
    organization = ContributorOrganizationSerializer()

    class Meta:
        model = Contributor
        # No need to specify depth because the individual and organization serializers are called explicitly.


class FilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer
        depth = 1  # Show the electoral district information.


class ElectoralDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralDistrict


class UniqueIndividualSerializer(serializers.ModelSerializer):
    donations_total = serializers.FloatField(read_only=True)
    donations_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UniqueIndividual


class UniqueOrganizationSerializer(serializers.ModelSerializer):
    donations_total = serializers.FloatField(read_only=True)
    donations_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UniqueOrganization
