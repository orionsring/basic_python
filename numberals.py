
from fractions import Fraction

def mixed_numeral(vulgar):
    try:
	    integer = vulgar.numerator // vulgar.denominator
		fraction = Fraction(vulgar.numerator - integer * vulgar.denominator, vulgar.denominator)
		return integer, fraction
	except AttributeError as e:
		raise TypeError("{} is not a rational number".format(vulgar))
		# Example function
		# 17/3  ---> 5 2/3


		