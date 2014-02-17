import phonenumbers
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#from django_facebook import FacebookCustomUser
class Venue(models.Model):
  class VenueCategory:
	RESTAURANT = 1
	SHOP = 2
	SPA = 3
	SALON = 4
	OTHER = 99
	#..more categories
  
  Category_Types = (
	(VenueCategory.RESTAURANT, 'Restaurant'),
	(VenueCategory.SHOP, 'Shop'),
	(VenueCategory.RESTAURANT,'SPA Centre'),
	(VenueCategory.SALON,'Salon'),
	(VenueCategory.OTHER,'Other'),
  ) 
		
  user 	       = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'venue') 	  
  # Human readable string to use in urls for SEO
  str_id       = models.CharField(verbose_name='String ID',
                                  max_length=1024,
                                  unique=True,
                                  null=True,
                                  blank=True,
                                  db_index=True)
  hash_id      = models.CharField(verbose_name='hash_id',
                                  max_length=1024,
                                  null=True,
                                  blank=True,
                                  db_index=True)

  name         = models.CharField(verbose_name='Name',
                                  max_length=1024,
                                  db_index=True)
  category     = models.IntegerField(verbose_name = 'Category',
			 	     choices = Category_Types)	
						
  subtitle     = models.CharField(verbose_name='Subtitle',
                                  max_length=1024,
                                  null=True,
                                  blank=True)
  description  = models.TextField(verbose_name='Description',
                                  null=True,
                                  blank=True)

  date_created = models.DateTimeField(verbose_name='Date Created',
                                      auto_now_add=True)

  # Location Related Fields.
  address1     = models.CharField(verbose_name='Street Address',
                                  max_length=1024,
                                  default='')
  address2     = models.CharField(verbose_name='Address2',
                                  max_length=1024,
                                  null=True,
                                  blank=True)
  address3     = models.CharField(verbose_name='Address3',
                                  max_length=1024,
                                  null=True,
                                  blank=True)
  neighborhood = models.CharField(verbose_name='Neighborhood',
                                  max_length=1024,
                                  db_index=True,
                                  default='')
  locality     = models.CharField(verbose_name='Locality',
                                  max_length=1024,
                                  db_index=True,
                                  default='')
  region       = models.CharField(verbose_name='Region',
                                  max_length=1024,
                                  db_index=True,
                                  default='')
  postal_code  = models.CharField(verbose_name='Postal Code',
                                  max_length=32,
                                  db_index=True,
                                  null=True,
                                  blank=True)
  country_name = models.CharField(verbose_name='Country Name',
                                  max_length=1024,
                                  db_index=True,
                                  default='')
  lat          = models.FloatField(verbose_name='Latitude',
                                   null=True,
                                   blank=True,
                                   db_index=True)
  lng          = models.FloatField(verbose_name='Longitude',
                                   null=True,
                                   blank=True,
                                   db_index=True)

  # Leave phone field for PhoneNumberField in the future.
  raw_phone    = models.CharField(verbose_name='Raw phone',
                                  max_length=1024,
                                  null=True,
                                  blank=True)
  website_url  = models.URLField(verbose_name='Website URL',
                                 null=True,
                                 blank=True)
  # TODO: images
  # TODO: payment
  def __str__(self):
	return self.name

  @property
  def phone(self):
    try:
      return phonenumbers.parse(self.raw_phone, 'AM')
    except:
      return self.raw_phone
