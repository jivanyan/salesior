from django.db import models
from patron.models import Patron
from venue.models import Venue
from datetime import datetime
from bonus.algorithms import BonusPlanAlgorithm



class Bonus(models.Model):

  class BonusType:
    PERCENTAGE = 1
    CASH       = 2

  BONUS_TYPES = (
    (BonusType.PERCENTAGE, 'Percentage'),
    (BonusType.CASH, 'Cash'),
  )

  _bonus_types = dict(BONUS_TYPES)

  patron        = models.ForeignKey(Patron, related_name='bonuses')
  venue         = models.ForeignKey(Venue, related_name='bonuses')

  date_created  = models.DateTimeField(auto_now_add=True)
  issue_date    = models.DateTimeField()
  expiry_date   = models.DateTimeField()
  exercise_date = models.DateTimeField(null=True, blank=True)

  bonus_type    = models.IntegerField(verbose_name='Bonus Type',
                                      choices=BONUS_TYPES)
  bonus_value   = models.FloatField(verbose_name='Bonus Value')

  def is_valid(self):
    return self.exercise_date is None and self.expiry_date > datetime.utcnow()


class BonusPlan(models.Model):

  PLAN_ALGORITHMS = BonusPlanAlgorithm.BONUS_PLAN_ALGORITHMS

  venue      = models.ForeignKey(Venue,
                                 related_name='bonus_plans')
  algorithm  = models.CharField(verbose_name='Plan Algorithm',
                                max_length=256)
  #, choices=PLAN_ALGORITHMS)
