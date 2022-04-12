#Q. Read a text file, find vowels and count the words?

def find_vowels(txt_file):

    """this function takes the text_file as an input and
    finds the vowels count, print the result"""

    txt_file = open(path, "r")  #open the text file in read mode
    counter = 0
    #declaring the vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for alpha in txt_file.read():
        #this loop iterate over the each word in the text file
        if alpha in vowels:
            #if the word has any of the vowels it couts
            counter += 1           

    #print the result
    print("Number of vowels in ", path, " = ", counter)


def find_word_occu(path):

    """this function takes text file as an input and count
    the repeated words in the file and print the results"""

    text = open(path, "r") #read the file in read mode
    dictionary = dict()   #create a dictionary to store count of the word
  
    for line in text:  #iterate over the each line in text file
        line = line.strip() #remove the empty spaces in a line
        line = line.lower() #converted into lower case
        words = line.split(" ")   #each line splits with the space

        for word in words: #this is iterate over the each word
            if word in dictionary: #stores the word:count in the dictionary 
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1
    
    #iterate over the dictionary keys and converted in to list
    for key in list(dictionary.keys()):
        #print the results
        print(key, ":", dictionary[key])

path="file.txt"   #read text file
find_vowels(path)  #calling the fun. to find vowels
find_word_occu(path) #calling the fun. to find the count of words

