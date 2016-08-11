from django.db import models


class Donation(models.Model):
    contributor = models.ForeignKey('Contributor', related_name='donations')
    filer = models.ForeignKey('Filer', related_name='donations')
    date = models.DateField('Date', help_text='The date on which the contribution was received')
    amount = models.FloatField('Amount', help_text='Size of the donation in dollars')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.contributor, self.filer, self.date, self.amount)


class Filer(models.Model):
    AFFILIATIONS = (('BC LIBERAL PARTY', 'Liberal'), ('BC NDP', 'NDP'), ('BC CONSERVATIVE PARTY', 'Conservative'))

    FILER_TYPES = (('CANDIDATE', 'candidate'), ('CONSTITUENCY', 'constituency'), ('ASSOCIATION', 'association'),
                   ('POLITICAL PARTY', 'political party'))

    affiliation = models.CharField(max_length=40, choices=AFFILIATIONS)
    type = models.CharField(max_length=30, choices=FILER_TYPES)
    electoral_district = models.ForeignKey('ElectoralDistrict', related_name='filers', blank=True, null=True)
    name = models.CharField(max_length=200, help_text='Name of the person who reported the donation.')

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

    individual = models.ForeignKey('ContributorIndividual', blank=True, null=True,
                                   help_text='Individual who contributed this donation. Only for class 1 donations.')
    organization = models.ForeignKey('ContributorOrganization', blank=True, null=True,
                                     help_text='Organization that contributed this donation.')
    contributor_class = models.CharField(max_length=1, choices=CONTRIBUTOR_CLASSES)

    def __str__(self):
        if self.individual:
            return self.individual.name
        else:
            return self.organization.name


class ContributorIndividual(models.Model):
    name = models.CharField(max_length=100)
    name_first_middle = models.CharField(max_length=100, help_text='First and any middle parts of the name provided.')
    name_last = models.CharField(max_length=100, help_text='Last part of the name provided.')
    unique_individual = models.ForeignKey('UniqueIndividual', blank=True, null=True)

    def __str__(self):
        return self.name

    # Whenever a new entry being saved to the database, first split the name up into first/middle and last components.
    def save(self, *args, **kwargs):
        parts = self.name.split()
        self.name_last = parts[-1]
        self.name_first_middle = ' '.join(parts[:-1])
        super(ContributorIndividual, self).save(*args, **kwargs)


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
