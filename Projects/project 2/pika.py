from nltk.corpus import wordnet
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string


def abra():
    ps= PorterStemmer()
    allurl_abstract = open('abs_compound.txt', 'r') 
    allurl_string = ''
    for line in allurl_abstract:
        allurl_string = allurl_string + line.strip() + ' '
    return allurl_string


    
#trying normalization on just one line string, and it works fine for it. but for the whole abstract it isnt.
def trial(allurl_string):
    str = 'program has many plan and it is the future of program to broadcast the tjyl'
    l = nltk.word_tokenize(str)
    print(type(allurl_string))
    print(l)
    #words = nltk.word_tokenize(allurl_string)
    #print(len(words))
    for w in l:
        if len(w) >=3:
            syns = wordnet.synsets(w)
            if len(syns) !=0:
                replacelist = list()
                for each in syns:
                    replacelist.append(each.lemmas()[0].name())
                print(replacelist)
                replace = syns[0].lemmas()[0].name()
                print(replace)
                for s in replacelist:
                    str = str.replace(s, replace)


    print(str)

#perfoms normalization on the main file
def main_trial(str):
    synonyms_list = list()
    words = nltk.word_tokenize(str) #tokenizes the word
    #print(words)
    #loops through each word
    ablist = []
    for w in words:
        syns = wordnet.synsets(w)  #for each word finds synonyms
        if len(syns) > 1:  #if a word just has more than one synonym
            replacelist = list()
            #for each synonym get the actual synonym using lemmas and append it to a list
            for each in syns:
                replacelist.append(each.lemmas()[0].name())
            replaced = syns[0].lemmas()[0].name()  #replace all synonym with this word
            synonyms_list.append(replaced)  #a list to have all the synonyms with which text file was replaced
            #for each synonym in the list, check the string for this one and replace it with selected, and repeat this procedure for all words
            ablist = []
            
            for s in replacelist:
                str = str.replace(s,replaced)

    after_norm = nltk.word_tokenize(str)
    #print(after_norm)
    print(str)
    return synonyms_list

        
#performs stemming
def perform_stemming(normalizedstring):
    ps= PorterStemmer()
    norm = ''
    words = nltk.word_tokenize(normalizedstring)
    for w in words:
        norm = norm + ps.stem(w)+' '
        #print(ps.stem(w))
    print(norm)
    return norm
    

def removestopwords(stopstring):
    stop_words = set(stopwords.words("english"))
    extras = set(['about','after','all','also','an','and','another','any','are','as','at','be','because','been','before','being','between','both','but','by','came','can','come',\
                  'could','did','do','each','for','from','get','got','has','had','he','have','her','here','him','his','how','if','in','into','is','it','like','make','many','me',\
                  'might','more','most','much','must','my','never','now','of','on','only','or','other','our','out','over','said','same','see','should','since','some','still','such','take',\
                  'than','that','the','their','them','then','there','these','they','this','those','through','to','too','under','up','very','was','way','we','well','were','what','where',\
                  'which','while','who','with','would','you','your','-','"'])
    combined = stop_words.union(extras)
    #one = extras.difference(stop_words)
    print(stopwords)
    #combined = one.union(stop_words)
    print(combined)
    print('*-------------------------------------------------------------------------------------*')
    str = 'I am rushabh and I wanyt you to love me extremely bad, not hate me but try and be nice - to yourself, me too.!! Okay? we will live happily'
    words = nltk.word_tokenize(stopstring)
    filtered = []
    finalfiltered = []
    for each in words:
        if each not in combined:
            filtered.append(each)
    print(filtered)

    #save 
    afterstop = open('Stopword.txt','w')
    for each in filtered:
        afterstop.write(each + '\n')
        #print(each)

    #for each in filtered:
    #  if len(each) > 1:
    #       finalfiltered.append(each)
    #print(finalfiltered)
           
           
def removepunctuations():
    punc = open('Normalized.txt', 'r')
    punctuations = string.punctuation
    print(punctuations)
    afterpunc = []
    print('***********************************************')
    for line in punc:
        if line not in punctuations and len(line) > 1:
            afterpunc.append(line)
            print(line)
            

    
def abcdef():
    beforenorm = open('abs_compound.txt' , 'r')
    words = beforenorm.read().split()
    word_replace = []
    word_not_replaced = []
    for each in words:
        if(len(wordnet.synsets(each)) > 0):
            syn = wordnet.synsets(each)[0]
            lemmas = syn.lemmas()
            for i in range(len(lemmas)):
                replaceWord = lemmas[0].name()
                if(each.lower() == lemmas[i].name().lower()):
                    each = lemmas[i].name() 
                    word_replace.append(each)
        else:
            word_not_replaced.append(each)
        
    total_list = word_not_replaced + word_replace

    afternorm = open('Normalized.txt','w')
    for each in total_list:
        afternorm.write(each + '\n')
   







   





     

def main():
    print('hi')
    finalstring = abra()
    #trial(finalstring)
    #synonyms = main_trial(finalstring)
    #stemmed = perform_stemming(finalstring)
    removestopwords(finalstring)
    #removepunctuations()
    abcdef()

main()


