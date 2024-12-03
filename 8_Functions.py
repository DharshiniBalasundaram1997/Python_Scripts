# We are importing the another file
"""import Modules

Modules.f1()
square = Modules.power(2)
print(square(2))"""



#we setting a name for Modules
"""import Modules as m

m.f1()

square = m.power(2)
print(square(2))"""


# we are importing th power as well
"""import Modules as m
from Modules import power

m.f1()

square = power(2)
print(square(2))"""

#we are importing f1 as well
# import Modules as m
# from Modules import power, f1
#
# f1()
#
# square = power(2)
# print(square(2))


# If we are having many functions, then we cannot import all the functions:
import Modules as m

# Using * (astreick)

# astreick is not recommended . Bcoz it will consume lot of memory

from Modules import *

f1()

square = power(2)
print(square(2))

















