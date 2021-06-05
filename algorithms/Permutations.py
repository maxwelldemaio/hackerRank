from itertools import permutations    

myTest = "1,2,1,4"

elements = list(myTest.split(',')) #makes a list of the input elements,
                                      #splitting them at ','

p = permutations(elements, 3)         #stores all possible permutations in p

x = list(set(p))                      #set removes duplicates, stores a list in x

list = []

for i in x:                           #i iterates the elements in x, here a tuple
    p = ''.join(i)                    #join concatenates the strings inside tuple
    list.append(int(p))

list.sort()
print(str(list[-1])+','+str(len(list))) #prints the last element and length