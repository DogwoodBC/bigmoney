from django.db import models


class Donation(models.Model):
    contributor = models.ForeignKey('Contributor', related_name='donations')
    filer = models.ForeignKey('Filer', related_name='donations')
    date = models.DateField('Date', help_text='The date on which the contribution was received')
    amount = models.IntegerField('Amount')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.contributor, self.filer, self.data, self.amount)


class Filer(models.Model):
    AFFILIATIONS = (('BC LIBERAL PARTY', 'Liberal'), ('BC NDP', 'NDP'))

    FILER_TYPES = (('CANDIDATE', 'candidate'), ('CONSTITUENCY', 'constituency'), ('ASSOCIATION', 'association'),
                   ('POLITICAL PARTY', 'political party'))

    affiliation = models.CharField(max_length=16, choices=AFFILIATIONS)
    type = models.CharField(max_length=20, choices=FILER_TYPES)
    electoral_district = models.ForeignKey('ElectoralDistrict', related_name='filers')
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.electoral_district, self.affiliation)


class ElectoralDistrict(models.Model):
    BOUNDARY_SETS = (('2008', '2008'),)

    name = models.CharField(max_length=100)
    boundary_set = models.CharField(max_length=4, choices=BOUNDARY_SETS)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    CONTRIBUTOR_CLASSES = (('1', 'individuals'), ('2', 'corporations'), ('3', 'unincorporated business'),
                           ('4', 'trade union'), ('5', 'non-profit organizations'), ('6', 'other'))

    individual = models.ForeignKey('ContributorIndividual', blank=True, null=True)
    organization = models.ForeignKey('ContributorOrganization', blank=True, null=True)
    contributor_class = models.CharField(max_length=1, choices=CONTRIBUTOR_CLASSES)

    def __str__(self):
        if self.individual:
            return self.individual
        else:
            return self.organization


class ContributorIndividual(models.Model):
    name = models.CharField(max_length=100)
    unique_individual = models.ForeignKey('UniqueIndividual', blank=True, null=True)

    def __str__(self):
        return self.name


class ContributorOrganization(models.Model):
    name = models.CharField(max_length=100)
    unique_organizations = models.ForeignKey('UniqueOrganization', blank=True, null=True)

    def __str__(self):
        return self.name


class UniqueIndividual(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UniqueOrganization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name