"""
Takes BC Elections SA1 political contributions data in tab-separated format,
parses it and saves it into various data tables as appropriate.
"""

import os
import django
import argparse
import codecs
import csv
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigmoney.settings')
# sys.path.append('/data/web/placespeak.com/webapps/place')
django.setup()

from data.models import ElectoralDistrict, Filer, ContributorIndividual, ContributorOrganization, Contributor, Donation


def main(args):
    print('Beginning import')

    file = codecs.open(args.input, 'r', args.encoding)
    num_rows = sum(1 for row in csv.reader(file))
    file.seek(0)
    reader = csv.DictReader(file, delimiter=args.delimiter, quotechar='\n')
    for i, row in enumerate(reader):
        print('line {}/{}'.format(i + 1, num_rows))

        if row['ELECTORAL_DISTRICT']:
            electoral_district, created = ElectoralDistrict.objects.get_or_create(name=row['ELECTORAL_DISTRICT'],
                                                                                  boundary_set=row['BOUNDARY_SET'])
            if created:
                prefix = '+'
            else:
                prefix = '.'
            print('{} ED #{} {} {}'.format(prefix, electoral_district.id, electoral_district.name, electoral_district.boundary_set))

        else:
            electoral_district = None
            print('x ED')

        filer, created = Filer.objects.get_or_create(
            name=row['FILER_NAME'],
            affiliation=row['\ufeffAFFILIATION'],
            electoral_district=electoral_district,
            type=row['FILER_TYPE']
        )
        if created:
            prefix = '+'
        else:
            prefix = '.'
        if created:
            print('{} Filer #{} {} {} {}'.format(prefix, filer.id, filer.name, filer.affiliation, filer.electoral_district))

        if row['CLASS'] == '1':
            contributor_individual, created = ContributorIndividual.objects.get_or_create(name=row['CONTRIBUTOR_NAME'])
            if created:
                prefix = '+'
            else:
                prefix = '.'
            print('{} Individual #{} {}'.format(prefix, contributor_individual.id, contributor_individual.name))

            contributor, created = Contributor.objects.get_or_create(contributor_class=row['CLASS'],
                                                                     individual=contributor_individual,
                                                                     organization=None)

            if created:
                prefix = '+'
            else:
                prefix = '.'
            print('{} Contributor #{} {}'.format(prefix, contributor.id, contributor.contributor_class))

        else:
            contributor_organization, created = \
                ContributorOrganization.objects.get_or_create(name=row['CONTRIBUTOR_NAME'])
            if created:
                prefix = '+'
            else:
                prefix = '.'
            print('{} Organization {} {}'.format(prefix, contributor_organization.id, contributor_organization.name))

            contributor, created = Contributor.objects.get_or_create(contributor_class=row['CLASS'],
                                                                     individual=None,
                                                                     organization=contributor_organization)

            if created:
                prefix = '+'
            else:
                prefix = '.'
            print('{} Contributor #{} {}'.format(prefix, contributor.id, contributor.contributor_class))

        amount = float(row['AMOUNT'])
        date = datetime.strptime(row['DATE'], '%Y/%m/%d')
        donation, created = Donation.objects.get_or_create(contributor=contributor, filer=filer, amount=amount,
                                                           date=date)

        if created:
            prefix = '+'
        else:
            prefix = '.'
        print('{} Donation #{} {}'.format(prefix, donation.id, donation.amount, donation.date))

    print('All done.')





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Takes BC Elections SA1 political contributions data in tab-separated '
                                                 'format, parses it and saves it into various data tables as appropriate.')

    parser.add_argument('-i', '--input', default='SA1_SearchResults_2016_07_04_34.tsv', action='store',
                        help='Path to the input file.')
    parser.add_argument('-e', '--encoding', action='store', default='utf_8',
                        help='Encoding of the input file. E.g. "iso8859_2"(aka Latin-2.), "utf_8".')
    parser.add_argument('-d', '--delimiter', action='store', default='\t',
                        help='The delimiter used in the file, e.g. ",", "\t".')

    args = parser.parse_args()
    main(args)
