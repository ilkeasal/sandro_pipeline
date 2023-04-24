

#Converting from a list to a string :

#list=["hello","we","are","learning","python"]

#counting=["hello","we","python","good","you"]

#list2=[["hello","we","are","learning","python"],["oh","good","for","you"]]


#count=0
#for words in list2:
    #count+=words.count(counting) for values in counting
#print(counting)
#print(count)


#seasons=["Spring","Summer","Fall","Winter"]



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



import pandas as pd
import numpy as np

#For loop in a DataFrame :

df = pd.DataFrame({"age":[24,28],"name":["Ilke","Firfir"]})

print(df)

#for column_name in df:
    #print(column_name)

for index, row in df.iterrows():
    print(index)
    print(row)


home="I am going HOME"

print(home.lower())

my_dict={"home":"Amsterdam", "time":"IDK"}


#.items() function
print(my_dict.items()) #returns the key value pairs of the dictionary.



#I am at def parse_args



trial_list=[[['train-72157623606067692-4426712667-3'], ['train-72157623392052135-4391219004-3']], ['test-72157625830823704-5357539959-4'], ['test-72157629972234013-7145640279-2'], ['test-72157630655378016-7605582080-4'], [['test-72157600124891007-472195090-4'], ['test-72157623213948893-4326098467-4'], ['test-72157594326560194-268647884-3']], ['test-72157623145509240-4247704215-4'], ['test-1443082-66884411-4'], ['test-72157625671844609-5344790579-1']]

print(type(trial_list))

# np.savetxt("TrialFileeee.csv",trial_list,delimiter=",",fmt="%s")

# print(trial_list[-3:])


from collections.abc import Iterable
def flatten_list(items,ignore_types=(str,bytes)):
    for v in items:
        if isinstance(v,Iterable) and not isinstance(v, ignore_types):
            yield from flatten_list(v)
        else:
            yield v


flattened_list=list(flatten_list(trial_list))

print(flattened_list)

import numpy as np
print(len(np.unique(flattened_list)))

print(len(flattened_list))

np.random.seed(123)

x=np.random.randint(9,size=(3,3))

print(x)

print(x.item(0,1))

import json
