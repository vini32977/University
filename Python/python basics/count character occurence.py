def count_characters(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

string=input("Enter a string: ")
result=count_characters(string)
print("Characters count in "+string+" is:\n"+str(result))