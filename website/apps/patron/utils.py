import datetime
from website.apps.patron.models import Patron, VenueRelationship
from website.apps.venue.models import Venue


def add_vr(P, V, I):
        v = VenueRelationship(patron = P, venue = V, inviter = I, state = 1, invited_at = datetime.datetime.now())
        v.save()
	return v
