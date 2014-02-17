from .base import BonusAlgorithmBase
from ..models import * 


class FixedPercentageAlgorithm(BonusAlgorithmBase):
  name = 'FixedPercentageAlgorithm-v1'

  def referral_bonus(self, referer, refered, venue):
    # TODO(arsen): Implement
    return Bonus(), Bonus()

