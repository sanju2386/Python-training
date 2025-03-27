'''
'Jumbled word : "otpcomure"
Your guess: "computer"'
'''
# get word and proccessed

import random
 
#function to jumble the word
import random
 
# Function to jumble the word
def jumble(w):
    temp = list(w)  # Convert word to a list of characters
    random.shuffle(temp)
    return ''.join(temp)

# File path
path = r"C:\Users\292593\Desktop\master\python training\python_code_submit\Python-training\word.txt"

# Read file
with open(path, 'r') as f:
    content = f.read()

print("Info content:", content)  # Debug output

# Split content into a list of words (assuming comma-separated words)
words = content.strip().split(',')

# Shuffle the word list
random.shuffle(words)

# Jumble each word and print
for word in words:
    jumbled_word = jumble(word)
    print(f"Original: {word}, Jumbled: {jumbled_word}")
f.close()

 
   #ask user input
 
   #compare user input an dupdate points
 
 
 

# path= r""
# f=open("word.txt")
# content=f.read()
# f.close
# print("what is the content" , content )
# # for every word in list of words

# # jumble the word
# def jumble(w) :
#     l=list(w)
#     random.shuffle(l)
#     return l



f=open("word.txt")





#show to user

#ask user input


# compare user input and update points


# show the results

