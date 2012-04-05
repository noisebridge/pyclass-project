import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

JSON = 1
XML = 2
FORMAT_CHOICES = (
    (JSON, "JSON"),
    (XML, "XML"),
)

class ProviderRule(models.Model):
    name = models.CharField(_("name"), max_length=128, null=True, blank=True)
    regex = models.CharField(_("regex"), max_length=2000)
    endpoint = models.CharField(_("endpoint"), max_length=2000)
    format = models.IntegerField(_("format"), choices=FORMAT_CHOICES)
    
    def __unicode__(self):
        return self.name or self.endpoint
    

class StoredOEmbed(models.Model):
    match = models.TextField(_("match"))
    max_width = models.IntegerField(_("max width"))
    max_height = models.IntegerField(_("max height"))
    html = models.TextField(_("html"))
    date_added = models.DateTimeField(_("date added"), default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.match
    
