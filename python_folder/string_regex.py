#Q. remove the special characters from given string?

import re  #regex used to remove special symbols

string_a ="This#string%contains^special*characters&."

#removing the special characters from the string
result = re.sub("[#%^*&.]", " ", string_a)

#print the result
print(result)
