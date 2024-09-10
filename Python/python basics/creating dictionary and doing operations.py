#creating Dictionary
student={"name":"Mary","age":20,"grade":"A"}
#print using items
print("Dictionary items using items(): ",student.items())
#traversing items
print("Dictionary items by traversing: ")
for key,value in student.items():
    print(key,":",value)
#get()
print("Grade of student: ",student.get("grade"))
#change value
student["grade"]="B"
print("Updated dictionary: ",student)
#length
print("Length of dictionary: ",len(student))