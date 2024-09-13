letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word="hello" 
holder=[]
for char in word:
    holder+=char
print(len(holder))
print(holder)    

length = len(holder)

for element in holder:
        if holder[element] in letters[element]:
            print(holder[element], "in position", letters.index(element))
        #print(x,holder[x])
    


    
# Get user input into the variable
#list=word.split()
# Split it into an array



#print(list[0])


