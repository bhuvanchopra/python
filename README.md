Docstring for Problem Set 4:

This folder contains programmes written in python to implement a wordgame.This game is a lot like Scrabble or Words With Friends.
Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

Dealing
A player is dealt a hand of n letters chosen at random (assume n=7 for now).The player arranges the hand into as many words as they want out of the letters,using each letter at most once. Some letters may remain unused (these won't be scored).

Scoring
The score for the hand is the sum of the scores for each word formed. The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created. Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value. For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word! As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).


Docstring for python file "ps3_hangman.py":

This python file is a programme based on the word guessing game called 'Hangman'.It is a game of two or more players in which one player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, within a certain number ofguesses.
In this programme and as well as in the stadard format of the game, 8 guesses are given to the player to correctl guess the word. The programme is writtten in such a way that the computer tells the player the number of letters in the word beforehand.
If the player guesses correctly,he/she wins. If not, then at the end of the programme, when no more guesses are available with the player, the computer reveals the word.


Docstring for python file "is_list_permutation.py":

This python file contains a programme that implements a function that takes in two listsand calculates whether they are permutations of each other. The lists can contain both integers and strings. A permutation is defined as follows:

  1. The lists have the same number of elements.
  2. List elements appear the same number of times in both lists.
  
If the lists are not permutations of each other, the function returns False. If they are permutations of each other, the function returns a tuple consisting of the following elements:

  1. The element occuring the most times
  2. How many times that element occurs
  3. The type of the element that occurs the most times
  
If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.



Docstring for python file "dict_invert.py":

This python file contains a programme of a function called dict_invert which takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The 
value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d.



Docstring for python file "largest_odd_times.py":

This python file contains a programme that takes a non-empty list of integers and returns the largest element of the list that occurs an odd number of times in the list. If no such element exists, then it returns None. For example, if the input list is [2,2,4,4], then the function returns None. If the input list is [3,9,5,3,5,3], then the function returns 9.



Docstring for python file "triangular.py":

This python file contains a programme that takes an integer as an input and returns True or False based on whether the given number is triangular or not. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.



Docstring for python file "general_poly.py":

This python file contains a programme that takes input as a list,L (a list of numbers: [n0, n1, n2, ... nk]) and return a function which when applied to x, returns the value n0 * x^k + n1 * x^(k-1) + ... nk * x^0. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234.


Docstring for ps6:

This problem set is about decrypting a story using the Caeser cypher encryption/decryption technique.

