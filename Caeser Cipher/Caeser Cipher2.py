letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word="hello" 
holder=[]
for char in word:
    holder+=char
print(len(holder))
print(holder)    

for x in range(len(holder)):
    for y in range(len(letters)):
        if holder[x] == letters[y]:
            stored= y
            print(holder[x], "in position", stored) #add the position
        #print(x,holder[x])
    


    
# Get user input into the variable
#list=word.split()
# Split it into an array



#print(list[0])


