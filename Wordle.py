

# Libraries importation
import pandas as pd # Use of database
import random # Generate random values
import itertools # Operations with lists based on iteration

url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt" # URL with the txt list of 5-length words

df = pd.read_table(url, sep="\t+", engine='python') # Load the 5-length words as a data frame

words = list(itertools.chain(*df.values.tolist())) # Convert the dataframe to list

word = random.choice(words) # A random word selected from the list

tries = 6 # Number of tries

print("Guess the 5-length word: *****")
print(" ")

guesses = [] # Array to save the guess form user

# While Loop which works if the number of tries is bigger than 0 
while tries > 0:
    
    text = "*****" # Str to save the letters that are in the word
    position = "-----" # Str to show the position correct (1) or incorrect (0) of a letter inside the word
    
    guess = input("Write a 5-length word: ") # Guess Word
    print(" ")
    
    if guess in words: # Validation that the guess word exists
        
        if guess == word: # Validation if the guess word is the secret word
            print("You found the word, GG!!")
            break
        
        if guess in guesses: # Validation if the user write that word already
            print("You alredy input that word, write another")
            print(" ")
            
        else:
            for pos, i in enumerate(guess):
                
                if i in word: # Replace * by a correct letter
                    text_list = list(text)
                    text_list[pos] = i
                    text = "".join(text_list)
                    
                    # Replace position str by 1 if the letter is in the correct position, 0 otherwise
                    if word.find(i) == pos:
                        position_list = list(position)
                        position_list[pos] = "1"
                        position = "".join(position_list)
                    else:
                        position_list = list(position)
                        position_list[pos] = "0"
                        position = "".join(position_list)
                                       
            guesses.append(guess)
            print(text)
            print(position)  
            print(" ")      
             
            tries -= 1
            print(f"You have: {tries} tries")
            print() 
    else:
        print("The input Word is not in the list")
        print("Please write a correct word")
        print(" ")

print("The word was:", word)





