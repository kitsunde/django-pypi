from django.core.management.base import NoArgsCommand
from pypi.tasks import update_latest_releases


class Command(NoArgsCommand):
    default_apps = None

    def handle_noargs(self, **options):
        print "Scheduling Celery to download latest releases."
        update_latest_releases.apply_async()
        print "Done"
