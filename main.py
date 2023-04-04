# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

vico_sentences=open("/Users/ilkeasal/Desktop/CLC/Sandro_Github/multimodal-evaluation-main/data/VICO.txt","r").readlines()

#print(vico_sentences.readlines())

#print(len(vico_sentences.readlines())) #1.018.367 #sentences

#print(vico_sentences)

Pereira_concept_words=open("/Users/ilkeasal/Desktop/CLC/Sandro_Github/multimodal-evaluation-main/data/stimuli_180concepts copy.txt","r").readlines()


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


str_one="I love Python Programming"

str_two=("Python")

str_three="Java"



if str_two in str_one:
    print("word found")  #this works for single words.



sentence_try=("Lets see if it works")

sentence_split=(sentence_try.split()) #with this sentences became words.

print(sentence_split)
words_try=["I","think","Lets","works","see"]

common_words=list(set(sentence_split)&set(words_try)) #and this way I can find the common words.

#for sentence in Vico_sentences_corrected:
    #sentences =Vico_sentences_corrected.split() #this does not work.

new_list =[]

for sentence in Vico_sentences_corrected:
    new_list.append(sentence.split())

#print(new_list)

print(len(new_list))








#print(new_list)

#print(len(new_list))


#commons=[]
#for sentence in new_list:
    #for words in sentence:
        #for word in Pereira_concept_corrected:
            #commons = list(set(sentence) & set(Pereira_concept_corrected))
#print(commons)

# I am going to try something :


new_list_subset=new_list[0:10]
print(new_list_subset)

Pereira_subset=Pereira_concept_corrected[0:10]

print(Pereira_subset)

for sentence in new_list_subset:
    for words in sentence:
        print(words) #this works!

commons_subset=[]
for sentence in new_list_subset:
    for words in sentence:
        for word in Pereira_subset:
            if word in words:
                print(word)    #Weird enough the art word is not in the sentences. one sentence finish with car and the other start with train maybe it combined them into "art"?
    else:
        print("NO!")


import re

str=(("an example word:cat!!","is that also gonna work"))




print(new_list_subset)



list2=[["hello","we","are","learning","python"],["oh","good","for","you","art"]]

for list in list2:
    new_string=(" ".join(list))


print(new_string)



list2=[["hello","we","are","learning","python"],["oh","good","for","you","art","attitude"]]





for elems2 in list2:
    for elem in elems2:
        if elem in Pereira_subset:
            print(elem)
        else:
            print("NAYY")


print(Pereira_subset)


for subset in new_list_subset:
    for words in subset:
        if words in Pereira_subset:
            print(words)
        else:
            print("NAYYY")

print(Pereira_subset)

print(new_list_subset)

print(len(new_list_subset))

new_list_subset[8]=["You","bag","to","argument"]

#for subset in new_list_subset:
    #for words in subset:
        #if words in Pereira_subset:
            #print(words)
        #else:
            #print("NAYYY")   #OKAY THIS WORKED FOR THE SUBSET


print(len(Pereira_concept_corrected)) #180
print(len(new_list)) #1.018.367


#count=0
#for list in new_list:
    #for words in list:
        #if words in Pereira_concept_corrected:
            #print(words)
            #count=count+1
        #else:
            #print("NAYYY")

#print(count) #362.295 words.



#print(new_list)

sent_ids=[]
for sentence in Vico_sentences_corrected:
    sent_ids.append(sentence[:sentence.index(',')])

print(sent_ids[-1])  #Correct sentence ids' :)) it works!

sent_text=[]
for sentence in Vico_sentences_corrected:
    sent_text.append(sentence[sentence.index(',')+1:].rstrip("\n"))

print(sent_text[-1]) #Sentences! this works as well! :)


import pandas as pd
vico_df=pd.DataFrame.from_dict({"id":sent_ids, "text":sent_text})

print(vico_df) #the dataframe works as well! :)








