numbers=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    ele=int(input())
    numbers.append(ele)
    print(numbers)
def is_even(num):
    return num%2==0
even_numbers=list(filter(is_even,numbers))
print("The even numbers are: ",even_numbers)