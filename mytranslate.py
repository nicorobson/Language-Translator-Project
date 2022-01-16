#!/usr/bin/python3
'''
This program is from p. 81 Figure 5.9 "Translating text (badly)" of 
our Gutag textbook.
You can use it as a starter program for assignment 2.

The output from the program is:
--------------------------------------
Input: I love animals. My favourite animals are reptiles such as lizards and snakes.
Output: Io amore animali. Mio preferito animali sono retilli ad esempio lucertole e serpenti.
--------------------------------------
Input: Io amore animali. Mio preferito animali sono retilli ad esempio lucertole e serpenti.
Output: I love animals. My favourite animals are reptiles such as lizards and snakes.
--------------------------------------
'''
EtoI = {'I' : 'Io', 'love' : 'amore', 'animals' : 'animali', 'My' : 'Mio',
        'favourite' : 'preferito', 'are' : 'siamo', 'reptiles' : 'retilli', 'such' : 'ad', 'as' : 'esempio', 'lizards' : 'lucertole', 'and' : 'e', 'snakes' : 'serpenti', 
            'you' : 'tu', 'hello': 'ciao', 'goodbye' : 'addio', 'good' : 'bene', 'have' : 'avere', 'open' : 'aperto', 'please' : 'per favore', 'thanks' : 'grazie', 'what' : 'che cosa', 'thing' : 'cosa', 
                'high' : 'alto', 'low' : 'basso', 'grandmother' : 'nonna', 'grandfather' : 'nonno',
                    'brother' : 'fratella', 'sister' : 'sorella', 'girl' : 'ragazza', 'boy' : 'ragazzo', 'man' : 'uomo', 'woman' : 'donna', 'dad' : 'papa', 'mom' : 'mamma', 
                        'eyes' : 'occhi', 'drink' : 'bevanda', 'we' : 'noi', 'for' : 'per', 'number' : 'numero', 'they' : 'essi', 'phone' : 'telefono', 'is' : 'e', 
                            'there' : 'la', 'can' : 'puo', 'colour' : 'colore', 'word' : 'parola', 'find' : 'trova', 'not' : 'non', 'more' : 'di piu', 'play' : 'giocare'}
#Creating a dictionary to store 50 english words translated into Italian                            

#Creating an interactive component where the user enters their gender to make the translations more accurate with masculine and feminine translations
gender = str(input('Are you a male or female? Enter M or F: '))
#this while loop ensures that the user eventually enters a valid input for their gender
while gender != 'M' and gender != 'm' and gender != 'F' and gender != 'f':      
    gender = str(input('Invalid. Enter M for male, F for female: '))

if gender == 'F' or gender == 'f':
    EtoI.update({'favourite' : 'preferita', 'open' : 'aperta', 'high' : 'alta', 'low' : 'bassa', 'they' : 'esse'})
#by default the dictionary has masculine translations, if the user is female, the dictionary will update the certain words that have a feminine alternative

#this function takes the keys and values to the initial dictionary and flips them, creating an Italian to English dictionary.
def reversedDictionary(EtoI):
    reverse_dict = {value: key for key, value in EtoI.items()}
    return reverse_dict
ItoE = (reversedDictionary(EtoI))   #assigning a variable to this newly created dictionary, calling the function

dicts = {'English to Italian' : EtoI, 'Italian to English' : ItoE}

def translateWord(word, dictionary) :
    if word in dictionary.keys() :
        return dictionary[word]
    elif word != '' :
        return '"' + word + '"'
    return word
                                                    #These are the translational functions.
def translate(phrase, dicts, direction) :           #the translate function takes three parameters including the sentence you want to translate,
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'        #-and returns the translated version
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for character in phrase :
        if character in letters :
            word = word + character
        else : 
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary) ##+ character   <<<<<<<< Commenting out this part of the program, eliminating the double period "glitch".
    return translation

#This next section accounts for a more accurate translation, depending on the context of the sentence surrounding 'are'.
#'are' is either 'sono' or 'siamo' in Italian, but it depends on certain words associated with it.
sentence = 'I love animals. My favourite animals are reptiles such as lizards and snakes.'
#splitting the sentence into multiple parts (splitting by each period)
sentence_parts1 = sentence.split('.')
for i in sentence_parts1:
    if 'are' not in i:                      #finding the particular sentence with 'are' and singling out this sentence for further correction.
        sentence_parts1.remove(i)
sentence_parts1_string = (''.join(str(x) for x in sentence_parts1))
sentence_toTest1 = sentence_parts1_string.split(' ')                    #splitting this specific sentence into a word list

#if 'my', 'I', or 'they' is associated with 'are', we must update the dictionary's translation to 'sono' instead of 'siamo'
if 'My' in sentence_toTest1 or 'I' in sentence_toTest1 or 'they' in sentence_toTest1:
    del EtoI['are'] 
    EtoI['are'] = 'sono'
#deleting and replacing it within the dictionary

translated = translate(sentence, dicts, 'English to Italian')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')

#changing the domain to use masculine or feminine translations, depending on the user's gender.
if gender == 'm' or gender == 'M':
    sentence = 'Io amore animali. Mio preferito animali siamo retilli ad esempio lucertole e serpenti.'
else:
    sentence = 'Io amore animali. Mio preferita animali siamo retilli ad esempio lucertole e serpenti.'
    
#this next section basically repeats the process of making the translation more accurate regarding the use of 'are',
#except this time we are updating the Italian to English dictionary. In doing so, again we must consider the differences between masculine and feminine.
sentence_parts2 = sentence.split('.')
for i in sentence_parts2:
    if 'siamo' not in i:
        sentence_parts2.remove(i)
sentence_parts2_string = (''.join(str(x) for x in sentence_parts2))
sentence_toTest2 = sentence_parts2_string.split(' ')

if ('Mio' in sentence_toTest2 or 'Io' in sentence_toTest2 or 'essi' in sentence_toTest2) and gender == 'm' or gender == 'M':
    sentence = 'Io amore animali. Mio preferito animali sono retilli ad esempio lucertole e serpenti.'
    del ItoE['siamo']
    ItoE['sono'] = 'are'
    
elif ('Mio' in sentence_toTest2 or 'Io' in sentence_toTest2 or 'esse' in sentence_toTest2) and gender == 'f' or gender == 'F':
    sentence = 'Io amore animali. Mio preferita animali sono retilli ad esempio lucertole e serpenti.'
    del ItoE['siamo']
    ItoE['sono'] = 'are'
    
translated = translate(sentence, dicts, 'Italian to English')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')



