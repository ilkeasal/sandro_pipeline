# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
#nltk.download('punkt')

from nltk import word_tokenize

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

vico_sentences=open("/Users/ilkeasal/Desktop/Internship_project/multimodal-evaluation-main/data/VICO.txt","r").readlines()

#print(vico_sentences.readlines())

#print(len(vico_sentences.readlines())) #1.018.367 #sentences

#print(vico_sentences)

Pereira_concept_words=open("/Users/ilkeasal/Desktop/Internship_project/multimodal-evaluation-main/data/stimuli_180concepts copy.txt","r").readlines()


#now I will create a function to get rid of the '\n'

def read_file(file):
    texts=[]
    for word in file:
        text=word.rstrip('\n')
        texts.append(text)
    return texts

Pereira_concept_corrected=read_file(Pereira_concept_words)

#print(Pereira_concept_corrected)

#print(len(Pereira_concept_corrected)) #180 words

Vico_sentences_corrected=read_file(vico_sentences)

#print(Vico_sentences_corrected)


# for sentence in Vico_sentences_corrected:
#     print(sentence)


#sentence_try=("Lets see if it works")

#sentence_split=(sentence_try.split()) #with this sentences became words.

#print(sentence_split)
#words_try=["I","think","Lets","works","see"]

#common_words=list(set(sentence_split)&set(words_try)) #and this way I can find the common words.

#for sentence in Vico_sentences_corrected:
    #sentences =Vico_sentences_corrected.split() #this does not work.

#new_list =[]

#for sentence in Vico_sentences_corrected:
    #new_list.append(sentence.split())

#print(new_list)

#print(len(new_list))

#print(word_tokenize(Vico_sentences_corrected[0]))
#
#
# #print(new_list)
#
# #print(len(new_list))
#
#
# #commons=[]
# #for sentence in new_list:
#     #for words in sentence:
#         #for word in Pereira_concept_corrected:
#             #commons = list(set(sentence) & set(Pereira_concept_corrected))
# #print(commons)
#
#
# for sentence in new_list_subset:
#     for words in sentence:
#         print(words) #this works!

#
#
#
#
#
#
#


#
#
#

#
#
#
#

#
#

#
#

#

#
#
# print(len(Pereira_concept_corrected)) #180
# print(len(new_list)) #1.018.367
#
#

#
#
#

#
sent_ids=[]
for sentence in Vico_sentences_corrected:
    sent_ids.append(sentence[:sentence.index(',')])

print(sent_ids[-1])  #Correct sentence ids' :)) it works!
#
sent_text=[]
for sentence in Vico_sentences_corrected:
    sent_text.append(sentence[sentence.index(',')+1:].rstrip("\n"))

print(sent_text[-1]) #Sentences! this works as well! :)


import pandas as pd
vico_df=pd.DataFrame.from_dict({"id":sent_ids, "text":sent_text})

print(vico_df) #the dataframe works as well! :)
#
#
#
#
#
#
# count=0
# Pereira_Vico_177_Concepts=[]
# # count_of_concepts=[]
# for x, sentence in enumerate(new_list):
#      for y, concept in enumerate(Pereira_concept_corrected):
#       if concept in sentence:
# #             print(x,y,sentence,concept) #this works
#        Pereira_Vico_177_Concepts.append(concept)
#
# print(Pereira_Vico_177_Concepts)
#
#
#
#
#
#
# import numpy as np
# occured_concept_ids_Pereira=np.unique(concepts)
#
# print(occured_concept_ids_Pereira)
# print(len(occured_concept_ids_Pereira))  #177 of the Pereira concept words occured in the VICO sentences.
#
#
#
# #for concept_words in Pereira_concept_corrected:
#     #print(new_list.count(concept_words)) #not working. It keeps giving 0
#     #print(concept_words)
#
#

#
# import pandas as pd
#
#
# #for concept in Pereira_concept_corrected:
#     #for sentence in new_list:
#         #for words in sentence:
#             #if concept==words:
#                 #concept_words.append(concept) #WORKS
#
#
# import numpy as np
# #print(np.unique(concept_words))
# #print(len(np.unique(concept_words))) #177 of the Pereira concept words appear in the VICO sentences.
#
# import nltk
#
# #Initialize dictionaries to keep track of counts for every Pereira word

total_occurances={concept:0 for concept in Pereira_concept_corrected}
sentence_ids={concept:[] for concept in Pereira_concept_corrected}
total_sentences={concept:0 for concept in Pereira_concept_corrected}

# #Looping Over VICO sentences and counting :
#
for line in Vico_sentences_corrected:
    tokenized_line = word_tokenize(line)
    sentence_id = tokenized_line[:tokenized_line.index(',')]
    sentence_text = tokenized_line[tokenized_line.index(',')+1:]
    for sentence_word in sentence_text:
        for pereira_concepts in Pereira_concept_corrected:
            if sentence_word == pereira_concepts:
                total_occurances[pereira_concepts]+=1
                sentence_ids[pereira_concepts].append(sentence_id) #works for ids and word_occurances

#print(sentence_ids)
print(total_occurances) #this is the Frequency Distribution

import numpy as np



#unique_ids=np.unique(sentence_ids)
#print(unique_ids)
# print(sentence_ids)

Vico_subset_sentence_ids=sentence_ids.values() #these are the sentence ids in which the Pereira words appeared.
#print(Vico_subset_sentence_ids) #okay this is the subset of Vico sentence ids.

#now I need to select VİCO sentences with this ids and this will be the subset of Vico_subset_sentences.

#print(type(Vico_subset_sentence_ids))

#print(Vico_subset_sentence_ids_listed)

Vico_subset_sentence_ids_listed=list(Vico_subset_sentence_ids)

print(Vico_subset_sentence_ids_listed[:10])
print(Vico_subset_sentence_ids_listed[-10:])








#import numpy as np
#print(sentence_ids)
#print(total_occurances)


Vico_Pereira_df=pd.DataFrame.from_dict({"concept_occurances":total_occurances, "sentence_ids":sentence_ids})

# print(Vico_Pereira_df["concept_occurances"]["weather"]) #this is to access the specific key value from concept_occurances / weather.


tokenized_Vico_lines=[]
for line in Vico_sentences_corrected:
    tokenized_Vico_lines.append(word_tokenize(line))



# Pereira_Vico_177_Concepts=[]
#
# for concept in Pereira_concept_corrected:
#     for sentence in tokenized_Vico_lines:
#          for words in sentence:
#             if concept==words:
#                 Pereira_Vico_177_Concepts.append((concept)) #WORKS #177 Pereira_concepts.
# #
# print(np.unique(Pereira_Vico_177_Concepts))
# print(len(np.unique(Pereira_Vico_177_Concepts))) #alright these are the unique filtered words. There are 177 of them.


#Now I need to create a subset of VICO that contain the sentence_ids.



# print(vico_df)
#
# print(Vico_subset_sentence_ids)

import pandas as pd


# ids_indexes=[]
# sentences_ids=[]
# for x,ids in enumerate(Vico_subset_sentence_ids):
#     for y, id in enumerate(ids):
#         if id in vico_df["id"].values:
#             print(id) #okay that works
#             ids_indexes.append(y)
#             sentences_ids.append(vico_df.iloc[y]) #this works! that gives me the ids and the sentences :) but now I need to make it a dataFrame.
# #
#
# #
# #
# print(ids_indexes)
#
# print(sentences_ids)



# unique_concept_words=(np.unique(Pereira_Vico_177_Concepts)) #okay this works I need to save it as a file. Thats missing.
#
# import numpy as np





# np.savetxt("Vicosubset.txt",Vico_subset_sentence_ids_listed,delimiter=",",fmt="%s")



from collections.abc import Iterable
def flatten_list(items,ignore_types=(str,bytes)):
    for v in items:
        if isinstance(v,Iterable) and not isinstance(v, ignore_types):
            yield from flatten_list(v)
        else:
            yield v  #this is a function to flatten the Vico_subset_sentence_ids_listed list so that I can save it as csv finally!





flattened_Vicosubset_sentence_ids=list(flatten_list(Vico_subset_sentence_ids_listed))



np.savetxt("Vicosubset.csv",flattened_Vicosubset_sentence_ids,delimiter=",",fmt="%s")




















