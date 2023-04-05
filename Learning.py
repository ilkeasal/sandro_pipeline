

#Converting from a list to a string :

list=["hello","we","are","learning","python"]

counting=["hello","we","python","good","you"]

list2=[["hello","we","are","learning","python"],["oh","good","for","you"]]


count=0
for words in list2:
    count+=words.count(counting) for values in counting
print(counting)
print(count)


seasons=["Spring","Summer","Fall","Winter"]



#for x,element in enumerate(seasons):
    #print(x,element)    #so with enumerate we also get the indexes. We loop over the indexes and the elements in the seasons list.



#for words in list:
    #print(words)



#for x, count in enumerate(counting):
    #print(list.count(count))
    #print(count) #this works.

#so here I actually did not loop over the list.
#but I looped over the concept words that I want to check if they are in.
#the important part is the thing inside the .count function needs to be looped over.
#but the sentences or the original list that you are searching the occurance of these words can be a list.
#so for my case, Pereira concepts need to be looped over whereas the VICO sentences should not be looped over.



#for x, count in enumerate(counting):
    #print(list.count(count))
    #print(count)









