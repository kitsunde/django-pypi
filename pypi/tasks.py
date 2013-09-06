from datetime import datetime
import xmlrpclib
from celery.task import task
from django.utils import timezone
import pytz
import requests
from pypi.models import Package


def deserialize_pypi(obj):
    iso_time_fields = frozenset(('upload_time',))

    for time_field in iso_time_fields.intersection(obj.keys()):
        date_time = datetime.strptime(
            obj[time_field],
            "%Y-%m-%dT%H:%M:%S"
        )
        obj[time_field] = timezone.make_aware(date_time, pytz.UTC)

    return obj


@task()
def update_version_details(package, version):
    if Package.objects.filter(name=package, version=version).exists():
        return

    response = requests.get('https://pypi.python.org/pypi/%s/%s/json' % (
        package, version
    ))

    package_data = response.json(object_hook=deserialize_pypi)

    Package.objects.create(
        name=package,
        version=version,
        released_at=package_data['urls'][-1]['upload_time']
    )


@task()
def update_package_versions(package):
    client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi',
                                   use_datetime=True)
    for version in client.package_releases(package):
        update_version_details.apply_async((package, version,))


@task()
def update_packages():
    client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi',
                                   use_datetime=True)
    for package in client.list_packages():
        update_package_versions.apply_async((package,))