'''
This program helps us choosing pet when provided with pet features.
So far the AI we build seems flawless!
'''

# Importing our AI model for making prediction
from ai_classifier import *


'''
Should I adopt a pet that is not Energetic (lazy), Cuddly, Soft, and Quiet? That can be encoded as:

Not Energetic =  0
Cuddly        =  1
Soft          =  1
Quiet         =  1

Features      =  [[0, 1, 1, 1]]
'''

# Columns: Energetic, Cuddly, Soft, Quiet
features = [[0, 1, 1, 1]]    # Pet features
print("Yes!" if mlp.predict(features)[0] else "No!")   

# if mlp.predict(features)[0]:
#     print("Yes!")
# else:
#     print("No!")


# Output: NO!  (Interesting)


'''
Let's give another one a shot. Should I get an energetic, not cuddly, not soft, and not quiet pet?

Energetic    =  1
Not Cuddly   =  0
Not Soft     =  0
Not Quiet    =  0

Features     =  [[1, 0, 0, 0]]
'''


# Columns: Energetic, Cuddly, Soft, Quiet
features = [[1, 0, 0, 0]]    # Pet features
print("Yes!" if mlp.predict(features)[0] else "No!")

# Output: YES!  (??)