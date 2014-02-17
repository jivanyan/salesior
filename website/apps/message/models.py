from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MessageManager(models.Manager):
	
	def inbox_for(self, user):
		return self.filter(recipient = user, deleted_by_recipient_at__isnull = True,)
	def outbox_for(self, user):
		return self.filter(sender = user, deleted_by_sender_at__isnull = True,)
	def trash_for(self, user):
		pass
	



class Message(models.Model):
	subject = models.CharField(max_length = 120)
	body = models.TextField()
	sender = models.ForeignKey(User, related_name = 'sent_messages')
	recipient = models.ForeignKey(User, related_name = 'received_messages')
	sent_at = models.DateTimeField(null = True, blank = True)
	read_at = models.DateTimeField(null = True, blank = True)
	deleted_by_sender_at = models.DateTimeField(null=True, blank=True)
	deleted_by_recipient_at = models.DateTimeField(null=True, blank=True)

	objects = MessageManager()
	def new(self):
		if self.read_at is not None:
			return False
		return True
	def __unicode__(self):
		return self.subject
	class Meta:
		ordering = ['-sent_at'] 

def inbox_count_for(user):
	"""
	returns the number of unread messages for the given user but does not
	mark them seen
	"""
	return Message.objects.filter(recipient=user, read_at__isnull=True, deleted_by_recipient_at__isnull=True).count()
