from django.db import models


class Transaction(models.Model):
	patron 		= models.ForeignKey(Patron, related_name = 'patron_transactions')
	venue  		= models.ForeignKey(Venue, related_name = 'venue_transactions')
	spending_time 	= models.DateTimeField()
	amount 		= models.DecimalField(default = 0)

class CashBack(models.Model):
	transaction 	= models.OneToOneField(Transaction, related_name = 'cashback')
	bonusplan	= models.ForeignKey(BonusPlan, related_name = 'used_in_cashbacks')
	
