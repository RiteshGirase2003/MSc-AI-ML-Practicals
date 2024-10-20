import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
stw = stopwords.words('english')

# ex = """This is a Sample Sentence,
# showing off the stop words filtration."""
ex = ''
file = open("slip6.txt", "r") # r stands for read means we can only read the file 
# open will open the file in r ( read ) form and store it in file 
# but all the content is store in form of list
# line in txt file is element of list
# total number line in txt file = total number of element in list 

for f in file:
    ex += f
file.close()


words = word_tokenize(ex)
# words will look like this : ['This', 'is', 'a', 'sample', 'sentence', ',', 'showing', 'off', 'the', 'stop', 'words', 'filtration', '.']
print( words)

fil = [] # create an empty list to store non stop words 

for word in words: # it will choose a words sequentially at a time 
    # now we are checking that 
    #  is that word not present in stw 
    # if it is not present in stw then we will put it into fil

    if word.lower() not in stw: # .lower() make that word to lower case 
        fil.append(word.lower())

print(fil)


