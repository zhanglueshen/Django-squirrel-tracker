from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv
import pandas as pd

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('database')

    def handle(self, *args, **options):
        csv_file = list()
        for item in Squirrel.objects.all():
            csv_file.append(
                {'latitude':item.latitude,
                'longitude':item.longitude,
                'squirrel_id':item.squirrel_id,
                'shift':item.shift,
                'date':item.date,
                'age':item.age,
                'color':item.color,
                'location':item.location,
                'specific_location':item.specific_location,
                'running':item.running,
                'chasing':item.chasing,
                'climbing':item.climbing,
                'eating':item.eating,
                'foraging':item.foraging,
                'other_activities':item.other_activities,
                'kuks':item.kuks,
                'quaas':item.quaas,
                'moans':item.moans,
                'tail_flag':item.tail_flag,
                'tail_twitches':item.tail_twitches,
                'approaches':item.approaches,
                'indifferent':item.indifferent,
                'runs_from':item.runs_from}
            )
        df = pd.DataFrame(csv_file)
        df.to_csv('squirrel.csv')
