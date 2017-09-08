#Author: Rushabh Shah
#Original creation date: 04/27/2017
#Last modification date: 04/28/2017
#Description: The program takes the string which contains all the abstracts of 15 urls and perfroms scrubbing on the data. The program 1st preserves compound words, then performs normalization
             #to replace all synonyms with just one word on the result of compound words function, later it also stems the result of normalization operation to standardize verbs to
             #present tense and nouns to singular forms, and at last removes punctuations and stopords and any other cleansing required and saves the data to a text file.


from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk

#this fucntion preserves the compound words
def perform_compoundwords(compound):
    #create a dictionary to 
    comp_dict = make_dictionary()  # makes dictionary of compound words
    #for loop to loop over all keys and replace those keys present in the string by the value corresponding to the key
    abscompound = open('Abstract_Compounds.txt','w')
    #this for loop replaces the words in the abstract data with it's compound words if the word has any otherwise don't replace
    for key in comp_dict:
        compound = compound.replace(key, comp_dict[key])
    abscompound.write(compound)  #write the compound words to the external file 'Abstract_Compounds.txt'
    return compound
                         
    


#this function prepares a dictionary identify all compound words as key and their replacement as valueand returns the dictinary to the calling function
def make_dictionary():
    dummy =  {'bulk grain': 'bulk_grain', 'classification score':'classification_score','classification scores':'classification_scores','sampling locations':'sampling_locations',\
                'transfer device':'transfer_device','electronic control unit':'electronic_control_unit','crop flow':'crop_flow','user interface':'user_interface','output signal':'output_signal',\
                'image feature':'image_feature','image processing system':'image_processing_system','electric characteristic':'electric_characteristic',\
                 'physical unclonable function':'physical_unclonable_function','bias magnitude':'bias_magnitude','limp mode':'limp_mode','jet engine':'jet_engine',\
                 'highly articulated robotic probe':'highly_articulated_robotic_probe','support material':'support_material','structure material':'structure_material',\
                 'stress_level':'stress_level','proximal link':'proximal_link','overtube mechanism':'overtube_mechanism','emotion recognition system':'emotion_recognition_system',\
                 'intelligent systems':'intelligent_systems','virtual coach':'virtual_coach','user experience':'user_experience','human speech':'human_speech',\
                 'culturing cells':'culturing_cells','classification systems':'classification_systems','probe arrays':'probe_arrays','brain tissue':'brain_tissue',\
                 'cell dimensions':'cell_dimensions','switching cell':'switching_cell','polylactic acid':'polylactic_acid','geometric features':'geometric_features',\
                 'network circuit':'network_circuit','electronic system':'electronic_system','neural network':'neural_network','supply voltage':'supply_voltage',\
                 'Bayesian network':'Bayesian_network','statistical methods':'statistical_methods','vector quantization':'vector_quantization','algae cells':'algae_cells',\
                 'intermediate link':'intermediate_link','intermediate links':'intermediate_links','3D object':'3D_object','3D objects':'3D_objects','probability_models':'probability_models',\
                 '2D image':'2D_image','Bayesian network-based':'Bayesian_network-based'}
    return dummy
   

#this function performs normalization on the string normalize passed to it as an arguement from the main fucntion and relaces the synonyms with one common word. This fucntion creates 2
#lists one to store the word for which we are replacing them with synonyms and one which stores the words which are not getting replaced and in the end concatenate both the lists
def perform_normalization(normalize):
    words = normalize.split()  #creates a list of words
    word_replace = []  #list to store words replaced
    word_not_replaced = []  #list to store words not replaced
    #for each words in the words list, check if it has synonyms and if it has replace it with the one selected synonym from the synsets list
    for each in words:
        if(len(wordnet.synsets(each)) > 0):  #this condition makes sure that only the words that have more than one synonym must be replaced with the one selected synonym
            syn = wordnet.synsets(each)[0]  #gets all the synonyms for the word
            lemmas = syn.lemmas()  #list lemmas will store lemmas for all the synonyms
            for i in range(len(lemmas)):
                replaceWord = lemmas[0].name()  #thhe 1st word in the lemma list is selected as the word that will replace all the synonyms in the abstract data
                if(each.lower() == lemmas[i].name().lower()):  #this condition checks if the word equals any of the lemma then replace it with synonym
                    each = lemmas[i].name() 
                    word_replace.append(each)
        else:
            word_not_replaced.append(each)
        
    total_list = word_not_replaced + word_replace  #merge both the lists of words that were and weren't replaced
    afternorm = open('Normalized.txt','w')  #create a file 'Normalized.txt' to save all the words after normalizing the abstract data
    dummystring = ''  #this string stores words after normalizing 
    #this for loop, appends all the words after normalizing to the external text file created and also adds all the words to string dummystring to be used in the next fucntions
    for each in total_list:
        dummystring = dummystring + each +' '
        afternorm.write(each.lower() + '\n')
    return dummystring
    


#performs stemming on the abstract data passed to it in normalizedstring arguement, after performing normalization
def perform_stemming(normalizedstring):
    ps= PorterStemmer()
    norm = ''
    words = nltk.word_tokenize(normalizedstring)  #tokenizes the words
    stemmedtxt = open('Stemmed.txt', 'w')  #text file to store the result after performing stemming
    #this loop, finds the root word for each word in the tokenized list and adds it to the external text file, and saves it to a string which will be passed back to main funciton
    for w in words:
        norm = norm + ps.stem(w)+' '
        stemmedtxt.write(ps.stem(w) + '\n')
    return norm



#this method removes stop words from the data after doing stemming on it and passed to it as an arguement from the main function
def removestopwords(stopstring):
    stop_words = set(stopwords.words("english"))  #gets all the stopwords from nltk's stopwords library
    #creating another set to include more stopwords and remove the stopwords from mabstract data more intensively 
    extras = set(['about','after','all','also','an','and','another','any','are','as','at','be','because','been','before','being','between','both','but','by','came','can','come',\
                  'could','did','do','each','for','from','get','got','has','had','he','have','her','here','him','his','how','if','in','into','is','it','like','make','many','me',\
                  'might','more','most','much','must','my','never','now','of','on','only','or','other','our','out','over','said','same','see','should','since','some','still','such','take',\
                  'than','that','the','their','them','then','there','these','they','this','those','through','to','too','under','up','very','was','way','we','well','were','what','where',\
                  'which','while','who','with','would','you','your','-','"'])
    #perform set operations to exclude common stopwords from both sets and make a final set with all stopwords to be removed from the abstract data
    one = extras.difference(stop_words)
    combined = one.union(stop_words)
    words = nltk.word_tokenize(stopstring)
    filtered = []  #a list that will store the non-stop words
    filter = ''
    #this for loop adds the non-stop words in the list 'filtered' and also adds the same to a string 'filter' which is passed back to mai fucntion and used in the below funtions
    for each in words:
        if each not in combined:
            filter = filter + each + ' '
            filtered.append(each.lower())
    filter = filter.lower()
    #save the results after removing stop words in a txt file 'Stopword.txt'
    afterstop = open('Stopword.txt','w')
    for each in filtered:
        afterstop.write(each.lower() + '\n')
    return filter  


#this method is used to remove all the punctuations for better analysis
def removepunctuations(punc):
    afterpunclist = open('Afterpunctuations.txt', 'w')
    words = nltk.word_tokenize(punc)
    punctuations = string.punctuation  #gets all the punctuations of string and store in a list
    afterpunc = []  #list to append the words those are not string 
    puncstr = ''
    #this loop, checks each word in the file whether its a punctuation and it's length is greater than 1 and apends those word to the list
    for line in words:
        #this condition checks if the word is any of the punctuation and the condition > 1 makes sure that single character word are ignored and not added to the list
        if line not in punctuations and len(line) > 1:
            if(line != "''" and line != "``" and line!= "'s"):  #while checking the output file, these 3 characters appeared and the library missed them
                #so apply this check to ensure these characters aren't added to the final list
                afterpunc.append(line)
    #this for loop adds all the non-punctuation words to a string puncstar and adds those words to a list 'Afterpunctaations.txt'
    for each in afterpunc:
        puncstr = puncstr + each + ' '
        afterpunclist.write(each.lower() + '\n')
    puncstr.lower()
    return puncstr



#this fucntion reads the scrubbed data and checks a condition to make sure that words with 2 or less characters are eliminated, and prints the tokens/concepts on the screen
def print_tokens(before):
    words = nltk.word_tokenize(before)
    last = []
    finalscrubbed = open('Final_Scrubbed.txt','w')  #file that stores the final abstract data after scrubbing 
    #this for loop checks that the word has more than 2 characters, copies all the words to a text file and prints the words/tokens on the screen
    total = 0
    #finalscrubbed.write('The list of all the concept words are as follows: \n')
    for each in words:
        if len(each) > 2 :  #this condition ensures that stopwords or irrelevant words missed by above funcitons are also eliminated
            last.append(each.lower())
            finalscrubbed.write(each.lower() + '\n')
            total = total + 1
    #prints the tokens on the screen
    print('After suucessful scrubbing there are total ',total,' concept words that are important for analysis, are as follows:')
    #prints all the concept words on the screen
    print('*******************************************************************')
    for each in last:
        print(each)
    print('*******************************************************************')
            

#is the main function that calls other function and controls the flow of this program
def main():
    allurl_abstract = open('URL_Abstract.txt', 'r')  #read the file of abstracts generated in the 1st task
    allurl_string = ''
    #this for loop eliminates the whitespaces and '\n' to perform better analysis
    for line in allurl_abstract:
        allurl_string = allurl_string + line.strip() + ' '  #just formating the string such that there are no '\n' in the string
    allurl_string = allurl_string.lower()  #converts all the words in the abstract to lowercase

    #calls all other functions, and each function returns a string which will be passed to the next function. Below all lines are the function calls
    done_compound = perform_compoundwords(allurl_string)
    dummy = perform_normalization(done_compound)
    dummystemmed = perform_stemming(dummy)
    dummystop = removestopwords(dummystemmed)
    dummypunct = removepunctuations(dummystop)
    print_tokens(dummypunct)
    

#starting point of the program
main()
