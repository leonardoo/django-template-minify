from django.core.management.base import BaseCommand

from templatemin.management.mixins import TemplateCachedClear


class Command(TemplateCachedClear, BaseCommand):
    help = 'Reset template cached'

    def handle(self, *args, **options):
        self.reset_loaders()
        self.stdout.write('Successfully reset all cached template')
