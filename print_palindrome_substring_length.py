#Input
#12345354987
#Output
#6

import collections
lst = []
list_of_duplicates = []
item_palindorm_count = 0
n =input()
list_of_input_values = list(n)

list_of_duplicates = [[item,count] for item, count in collections.Counter(list_of_input_values).items() if count > 1]
for item,count in list_of_duplicates:
    if count % 2 != 0:
        item_palindorm_count += count -1;
    else:
        item_palindorm_count += count

print(item_palindorm_count,end = '')
