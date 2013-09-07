from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    released_at = models.DateTimeField()

    class Meta:
        get_latest_by = 'released_at'
        ordering = ('-version',)
        unique_together = ('name', 'version')

    def __unicode__(self):
        return "%s %s" % (self.name, self.version)
