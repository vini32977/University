my_list=[1,2,3,4,5]
print("Original List: ",my_list)

#insert
my_list.insert(2,10)
print("List after inserting 10 at index 2: ",my_list)
#remove
my_list.remove(5)
print("List after removing 5: ",my_list)
#append
my_list.append(20)
print("List after appending 20: ",my_list)
#length
print("Length of list: ",len(my_list))
#pop
l=my_list.pop()
print("Last element removed from list: ",l)
print("List after removing list: ",my_list)
#clear
my_list.clear()
print("List after clearing the list: ",my_list)