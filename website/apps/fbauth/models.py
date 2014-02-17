from django.db import models
from django.contrib.auth.models import User
class FacebookProfile(models.Model):
    user = models.ForeignKey(User, related_name = 'fb_user')
    facebook_id = models.BigIntegerField()
    access_token = models.CharField(
        max_length=150
        )

    def __unicode__(self):
        return "{0}".format(self.user)
