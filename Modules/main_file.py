import os
import sys
sys.path.append(os.path.abspath("./Modules"))
from package import calculation
a, b = 10, 20
add = calculation.add(a, b)

print(add)