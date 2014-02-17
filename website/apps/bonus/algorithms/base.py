import re


class BonusAlgorithmBase(object):
  """
  Interface for all Bonus Plans.
  """
  def referral_bonus(self, referer, refered, venue):
    """
    Returns a tuple with a Bonus for referrer, and a Bonus
    for referred in that order.
    """
    raise NotImplementedError()

  @property
  def enum_value_name(self):
    name = self.__class__.__name__
    # add an underline in before un uppercase caracter if it's not after
    # another uppercase caracter.
    # e.g.
    # >> re.sub('(?<!^)(?=[A-Z])(?<![A-Z])', '_', 'AbcdEFGhIJ')
    # == Abcd_EFGh_IJ
    return re.sub('(?<!^)(?=[A-Z])(?<![A-Z])', '_', name).upper()
