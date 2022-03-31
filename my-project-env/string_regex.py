#Q. remove the special characters from given string?
import re  #rejex used to remove special symbols

string_a ="This#string%contains^special*characters&."
result = re.sub("[#%^*&.]", " ", string_a)
print(result)
