test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
new=[]
# using set() to remove duplicated from list
new = list(set(test_list))
print(new)