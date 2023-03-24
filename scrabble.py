"""Technical interview code to create a game of scrabble """
import random


letter_score = {
    'A':1,
    'E':1,
    'I':1,
    'O':1,
    'N':1,
    'R':1,
    'T':1,
    'L':1,
    'S':1,
    'U':1,
    'D':2,
    'G':2,
    'B':3,
    'C':3,
    'M':3,
    'P':3,
    "F":4,
    "H":4,
    "V":4,
    "W":4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10

}

letters_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_points(word: str) -> int:
    """function to calculate the score of a players chosen word"""
    score = 0
    for letter in word:
        score += letter_score[letter]
    return score

def assign_seven_tiles(letters_string: str) -> list:
    """function to randomly assign each player a stack of 7 letters"""
    player_rack = []
    for letter in range(0,7):
        player_rack.append(random.choice(letters_string))
    return player_rack




print(calculate_points('GUARDIAN'))
print(assign_seven_tiles(letters_string))




