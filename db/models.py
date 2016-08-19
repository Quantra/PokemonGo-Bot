import sys
from datetime import datetime

try:
    from django.db import models
except  Exception:
    print "There was an error loading django modules. Do you have django installed?"
    sys.exit()


class AutoDateModel(models.Model):
    create_date = models.DateTimeField('Creation Date', null=True)
    mod_date = models.DateTimeField('Last Modified', null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.mod_date = now
        if not self.pk:
            self.create_date = now
        super(AutoDateModel, self).save(*args, **kwargs)


class Login(AutoDateModel):
    username = models.CharField(max_length=255)


class CatchLog(AutoDateModel):
    username = models.CharField(max_length=255)
    encounter_id = models.CharField(max_length=255)
