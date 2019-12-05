import csv

from django.cor.management.base import BaseCommand


class Command(BaseCommand):
    def  add_arguments(self,parser):
        parser.add_argument('csv_file')
    
    def handle(self,*args,**options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader (fp)
            data = list (reader)

        for item in data:
            p= Pet (
                    name=item['name'],
                    species=item['specoes'],
                    birth_date=item['birth_date'],
                    sex=item['sex'],
            )
            p.save()


