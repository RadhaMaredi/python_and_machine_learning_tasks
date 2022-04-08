#read a text file, find vowels and count the words?

def find_vowels(txt_file):
    txt_file = open(path, "r")
    counter = 0    

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for alpha in txt_file.read():
        if alpha in vowels:
            counter += 1              
    print("Number of vowels in ", path, " = ", counter)

def find_word_occu(path):
    text = open(path, "r")
    dictionary = dict()
  
    for line in text:  #reading each line in text
        line = line.strip()
        line = line.lower()
        words = line.split(" ")

        for word in words:
            if word in dictionary:
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1

    for key in list(dictionary.keys()):
        print(key, ":", dictionary[key])


path="file.txt"
find_vowels(path)
find_word_occu(path)

