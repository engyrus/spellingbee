# Spelling Bee

*Python generator/solver for Spelling Bee puzzles (New York Times)*

I enjoy playing the New York Times' game [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee). I wondered about how to write a Python script that creates and solves Spelling Bee puzzles and decided to take a stab at it.

For those who aren't familiar, each puzzle is built on a seed word containing exactly seven unique letters. These are randomly arranged in a hexagon format resembling a honeycomb. You make words at least four letters long from these letters (you can use letters more than once) and the puzzle judges them as real words or not. One letter is placed in the center of the puzzle and must appear in all words. The words are scored based on their lengths and the game designates you as a genius (or lesser skill levels) based on your score. Every puzzle has one or more pangrams that use all the letters in the puzzle at least once; one is the seed word. although there can be others.

It turns out you don't need much code at all to generate a puzzle that meets the criteria. Given a list of English words, you can easily identify all the ones that could be a seed word (contain only letters and have exactly seven unique ones). Then you can either pick one at random or ask the user to enter one (making sure it qualifies) as the seed for a puzzle.

Most Unix-like systems have a word list at `/usr/share/dict/words`. This list exists on Mac OS X, so I've used it. The list does have a flaw: it's much bigger than the one the New York Times uses. (I've often been surprised by the words that aren't recognized by the official Spelling Bee puzzle.) This means that not only will the solution set be somewhat different from the Times' answers, you'll see a number of obscure and naughty words that you'd never see in theirs. No big deal, it'll work with any word list so you can substitute whatever you want. Exercise for the reader and all that.

The basic approach I took is:

1. Read all the words into a list. Make a second list containing only the words that could be seed words (exactly seven unique letters).

2. Ask the user to select a seed word or allow the script to choose one randomly. If the user enters one, it is validated against the seed word list. If the user allows the script to choose one, they're further asked for a sequence of letters that should appear in the seed (I have noticed that puzzles often contain "ing" or another sequence of letters that constrains the solutions, so I added the ability to do that, if you want).

    - The user may also just enter a string of 7 unique letters that are not a word. (You might have this instead of the actual seed word if you are trying to solve an existing puzzle.) The script will find the first pangram made of those letters and use that as the seed word.

3. Ask the user to choose which letter should be in the center of the puzzle, or again choose it randomly.
Find all the words in the word list that are solutions to the puzzle. These are the ones that are at least four letters long, contain only letters from the seed word, and contain the center letter.
The script can be used either to generate puzzles (by finding good seed words, trying to solve, then checking your answers) or to help solve a puzzle, including the ones in the Times.

You could expand it into an actual game that you can play, with a GUI and all that, but I'll leave that for you.
