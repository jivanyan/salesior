import phonenumbers
import datetime
from django.db import models
from django.contrib.auth.models import User
from venue.models import *
from django.conf import settings

class Patron(models.Model):
	user            = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='patron')

	picture         = models.ImageField(upload_to = 'profile_pictures',
				      blank = True)

	# Leave phone field for PhoneNumberField in the future.
	raw_phone       = models.CharField(verbose_name='Raw phone',
                                     max_length=1024,
                                     null=True,
                                     blank=True)
	all_venues      = models.ManyToManyField('venue.Venue',
                                           related_name='all_patrons',
                                           blank=True,
                                           through='VenueRelationship')
	all_connections     = models.ManyToManyField('self',
					   related_name = 'all_friends',
					   blank = True,
					   symmetrical = False,
					   through = 'Friendship')
	@property
	def self_url(self):
		try:
      			return '/home/%s' %self.username	
    		except:
      			return '/home/'
	
  	@property
  	def phone(self):
    		try:
      			return phonenumbers.parse(self.raw_phone, 'AM')
    		except:
      			return self.raw_phone
	
	def __str__(self):
		return self.user.username 

	def request_join(self, v):
		vr = VenueRelationship.objects.get_or_create(patron = self, venue = v, inviter = self.user )
		if vr.state == 4:
			vr.state = 1
			vr.invited_at = datetime.datetime.now()
			vr.canceled_at = None
			vr.save()
			return vr
		elif vr.state == 1 and r.invited_at == None:	
			vr.invited_at = datetime.datetime.now()
			vr.save()
			return vr
		else:	
			return None
			 
	def accept_join_invitation(self, vr):
		vr.state = 2
		vr.accepted_at = datetime.datetime.now()
		vr.save()
		return vr
	
	def reject_join_invitation(self, vr):
                vr.state = 3
                vr.rejected_at = datetime.datetime.now()
                vr.save()
                return vr

	def cancel_join(self, vr):
                vr.state = 4
                vr.canceled_at = datetime.datetime.now()
                vr.save()
                return vr


	def send_join_invitation(self, v, p):
		vr = VenueRelationship(patron = p, venue = v, inviter = self.user, state = 1, invited_at = datetime.datetime.now())
		vr.save()
		return vr
	def get_join_invitations(self):
		vr = VenueRelationship.objects.filter(patron = self, state = 1)	
		return vr
	

class VenueRelationship(models.Model):
  """
		  Defines a relationship between a Patron and a Venue.
  """
  class RelationshipState:
    PENDING    = 1
    ACCEPTED   = 2
    REJECTED   = 3
    CANCELED   = 4
    

  RELATIONSHIP_STATES = (
    (RelationshipState.PENDING, 'Pending'),
    (RelationshipState.ACCEPTED, 'Accepted'),
    (RelationshipState.REJECTED, 'Rejected'),
    (RelationshipState.CANCELED, 'Canceled')	
  )

  _relationship_states = dict(RELATIONSHIP_STATES)

  venue        = models.ForeignKey(Venue, related_name='venue_relationships')
  patron       = models.ForeignKey(Patron, related_name='patron_relationships')
  inviter      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'inviter')
  state        = models.IntegerField(verbose_name='Relationship State',
                                     choices=RELATIONSHIP_STATES,
				     default  = 1)
  invited_at   = models.DateTimeField(blank = True, null = True)
  responded_at = models.DateTimeField(blank = True, null = True)
  canceled_at  = models.DateTimeField(blank = True, null = True)
  class Meta:
    unique_together = ('venue', 'patron','inviter',)	


class Friendship(models.Model):
	"""
		Defines the friendship between two Patrons
	"""
	class FriendshipState:
		PENDING	   = 1
		ACCEPTED   = 2
		REJECTED   = 3
		CANCELED   = 4

	FRIENDSHIP_STATES = (
		(FriendshipState.PENDING, 'Pending'),
		(FriendshipState.ACCEPTED, 'Accepted'),
		(FriendshipState.REJECTED, 'Rejected'),
		(FriendshipState.CANCELED, 'Canceled')
	)
		
	source		= models.ForeignKey(Patron, related_name = 'source')
	target		= models.ForeignKey(Patron, related_name = 'target')
	state		= models.IntegerField(verbose_name = 'Friendship state',
					choices = FRIENDSHIP_STATES,
					default = 1)
	invited_at   	= models.DateTimeField(blank = True, null = True)
	responded_at 	= models.DateTimeField(blank = True, null = True)
	canceled_at  	= models.DateTimeField(blank = True, null = True)
	class Meta:
		unique_together = ('source','target',)
	
