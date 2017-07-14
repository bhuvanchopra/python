Docstring for python file "ps3_hangman.py":

This python file is a programme based on the word guessing game called 'Hangman'.
It is a game of two or more players in which one player thinks of a word, phrase 
or sentence and the other tries to guess it by suggesting letters or numbers, 
within a certain number of guesses.

In this programme and as well as in the stadard format of the game, 8 guesses are
given to the player to correctl guess the word. The programme is writtten in 
such a way that the computer tells the player the number of letters in the word
beforehand.

If the player guesses correctly,he/she wins. If not, then at the end of the programme,
when no more guesses are available with the player, the computer reveals the word.



Docstring for python file "is_list_permutation.py":

This python file contains a programme that implements a function that takes in two lists
and calculates whether they are permutations of each other. The lists can contain both 
integers and strings. A permutation is defined as follows:

  1. The lists have the same number of elements.
  2. List elements appear the same number of times in both lists.
  
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the 
following elements:

  1. The element occuring the most times
  2. How many times that element occurs
  3. The type of the element that occurs the most times
  
If both lists are empty return the tuple (None, None, None). If more than one element occurs
the most number of times, you can return any of them.



Docstring for python file "dict_invert.py":

This python file contains a programme of a function called dict_invert which takes in a 
dictionary with immutable values and returns the inverse of the dictionary. The inverse of 
a dictionary d is another dictionary whose keys are the unique dictionary values in d. The 
value for a key in the inverse dictionary is a sorted list (increasing order) of all keys 
in d that have the same value in d.



Docstring for python file "triangular.py":

This python file contains a programme that takes an integer as an input and returns True
or False based on whether the given number is triangular or not.
A triangular number is a number obtained by the continued summation of integers starting 
from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., 
are triangular numbers.



Docstring for python file "general_poly.py":

This python file contains a programme that takes input as a list,L (a list of numbers: 
[n0, n1, n2, ... nk]) and return a function which when applied to x, returns the value
n0 * x^k + n1 * x^(k-1) + ... nk * x^0.
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234.
