def insert_in_serted(x, sorted_list):
   new_list = []
   i = 0
   inserted = False

   while i < len(sorted_list):
       if not inserted and x < sorted_list[i]:
           new_list.append(x)
           inserted = True
       new_list.append(sorted_list[i])
       i += 1
   if not inserted:
     new_list.append(x)
   return new_list

def insertion_sort(my_list):
   out = []
   for x in my_list:
       out = insert_in_serted(x, out)
   return out


print(insert_in_serted(2, []))
print(insert_in_serted(5, [1, 2, 3, 4]))
print(insert_in_serted(2, [0, 1, 2, 3, 4]))
print(insert_in_serted(2, [2, 2]))


print(insertion_sort([4, 3, 2, 1]))
print(insertion_sort([5, 1, 4, 2, 8]))
print(insertion_sort([1, 1, 1, 1]))
print(insertion_sort([]))
print(insertion_sort([12, 4, 3, -1]))