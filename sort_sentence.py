# slip 24

# slip 24 : Write a python program to sort the sentence in alphabetical order?
def selection(words):
    n = len(words)
    for i in range(n-1):
        for j in range(i+1, n):
            
            # Compare adjacent words and swap if they are in the wrong order
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]

def sort_sentence(sentence):
    # Split the sentence into words
    words = sentence.split(' ')
    
    # Sort the words alphabetically

    # words.sort()
    print('before sorting words : ',words)
    selection(words)
    print(' after sorting words : ',words)


    # Join the sorted words back into a sentence

    # sorted_sentence = ' '.join(words)
    sorted_sentence = ''
    for word in words:
        sorted_sentence +=  word + ' '
    
    return sorted_sentence

# Example usage
sentence = input("Enter a sentence: ")
print("Sentence : ", sentence)
print("Sorted sentence:", sort_sentence(sentence))
