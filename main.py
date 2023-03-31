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







#print(new_list)

#print(len(new_list))


#commons=[]
#for sentence in new_list:
    #for words in sentence:
        #for word in Pereira_concept_corrected:
            #commons = list(set(sentence) & set(Pereira_concept_corrected))

#print(commons)

