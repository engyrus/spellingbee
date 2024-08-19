# bee.py - using UNIX word list, create a puzzle like the New York Times' 
#          "Spelling Bee," along with all possible solutions

# The UNIX word list is more extensive than the Times' list; you'll see
# some mighty obscure words, and also some totally inappropriate ones.

import random, itertools

all_words = open("/usr/share/dict/words").read().splitlines()

# read potential seed words: at least 7 unique letters and no uppercase or punctuation
seed_words = [word for word in all_words if len(word) > 6 and word.isalpha() and 
              len(set(word)) == 7 and word.lower() == word]
print(len(seed_words), "seed words")

# get or randomly choose seed word for puzzle
seed_word = ""
while seed_word not in seed_words:
    seed_word = input("seed word, exactly 7 unique letters (enter for random): " ).lower()
    if seed_word == "":
        required_letters = input(
            "... substring the random word must contain: ").lower()
        seed_word = random.choice(seed_words)
        while required_letters != "" and required_letters not in seed_word:
            seed_word = random.choice(seed_words)
        print("seed word:", seed_word.upper())
    else:
        # the user entered a word but it is not a seed word
        if seed_word not in seed_words:
            seed_word = set(seed_word.lower())
            if len(seed_word) == 7:
                seed_word = min(itertools.chain((word for word in seed_words if set(word) == seed_word), ""), key=len)
                if seed_word:
                    print("seed word:", seed_word.upper())
            else:
                seed_word = ""

# get or choose center letter for puzzle.
# this letter must appear in all answers
seed_letters = set(seed_word)
center_letter = ""
while len(center_letter) != 1 or center_letter not in seed_letters:
    center_letter = input("center letter (enter for random): ").lower()
    if center_letter == "":
        center_letter = random.choice(seed_word)
        print("center letter:", center_letter.upper())

# print puzzle, randomized but withc enter letter in middle
puzzle_letters = list(set(seed_word.upper()))
random.shuffle(puzzle_letters)
# put the center letter in the center
center_index = puzzle_letters.index(center_letter.upper())
puzzle_letters[center_index], puzzle_letters[3] = puzzle_letters[3], puzzle_letters[center_index]
print("puzzle:  {0} {1}\n        {2} {3} {4}\n         {5} {6}".format(*puzzle_letters))

# generate solution words. print with pangrams in caps
solution_words = [word for word in all_words if len(word) > 3 and center_letter in word 
                  and not set(word).difference(seed_word)]
print(len(solution_words), "solution words:", sorted(
    word.upper() if len(set(word)) == 7 else word for word in solution_words))
