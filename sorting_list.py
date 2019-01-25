# Sorting a Normal List
test_list1 = [1,5,4,3,7,2]
test_list1.sort()
print (test_list1)

# Sorting nested list
test_list2 = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]] 
test_list2.sort(key = lambda x:x[2]) # This will sort the list according 3rd element of s=nested list
print test_list2
