class classproperty(object):
   def __init__(self, getter):
     self.getter = getter

   def __get__(self, instance, owner):
     return self.getter(owner)


class BonusPlanAlgorithm(object):
  """
  Class that stores all the Bonus Plan Algorithms that businesses can select
  to use.
  """

  _algorithms = {}

  @classmethod
  def register_algorithm(cls, algorithm):
    setattr(cls, algorithm.enum_value_name, algorithm.name)
    cls._algorithms[algorithm.name] = algorithm.name

  @classproperty
  def BONUS_PLAN_ALGORITHMS(cls):
    return list(cls._algorithms)


from .percentage import FixedPercentageAlgorithm
BonusPlanAlgorithm.register_algorithm(FixedPercentageAlgorithm())
