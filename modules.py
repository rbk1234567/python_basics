import math as mathematics  # import module but use alias for its name
from examplemodule1 import power # import function or variable from module
from examplemodule1 import golden_thught as thought # import function or variable from module but use alias for its name


print(dir(mathematics))
print(mathematics.sqrt(2))
print(power(5))
print(thought)

# import can be done only once. to use import module function again use imp.reload()
import imp
import examplemodule2
imp.reload(examplemodule2)

