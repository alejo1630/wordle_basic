# Wordle (Basic Version)

This Python code is a basic vesion of the Wordle 5-Letter words game in english language

## 🔰 How does it work?

- A list of 5-letters words is load from [Stanford CS Faculty website](https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt). There are **5757** different words.
- A single word is selected randomly.
- User has 6 tries to guess the word.
- The initial text is showed in the console using the format "*****".
- User uses the console to input its guesses. In each try the word must be exist in the original list and be different from previous guesses.
- If one or more letters are in the word to guess the "*" symbols change for that or those letters. 
- Below the text, a position information is showed using the format "-----". If one or more letters is in the word to guess the "." symbols change for **1** if the letter is in the correct spot, or **0** if the letter is in the word to guess but in a different spot. 
- Above process continues until the user finds the word to guess or the tries are over, in this case, the word to guess is showed in console.

## 🔶 What is next?
- Create the code for several languages
- System of points
- Use words with n-letters
- Creat an interface or app
