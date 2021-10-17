# Memory Game

## Story

You're tasked with a terminal implementation of the [Memory Game](https://en.wikipedia.org/wiki/A_Game_of_Concentration) aka Concentration, for a single player.

## What are you going to learn?

- Use nested lists.
- Design a simple game application in terminal.
- Use functions.


## Tasks

1. Implement `generate_board(height, width)` to return a randomly generated matrix of alphabet letters (a list of lists). The inner lists are columns.
    - A list of lists is returned, representing a list of columns.
    - If the amount of letters required to generate the board (based on the height and width) is greater than the amount of letters in latin alphabet, raise a `ValueError`.
    - If the amount of letters required to generate the board (based on the height and width) is an odd number, raise a `ValueError`.
    - The board consists of pairs of letters from latin alphabet, similar to
the following example.
```
AFCH
DFED
CBAE
GBGH
```

2. The user can select a field on the board, by typing in its coordinates, such as `B2`. The letter denotes the column (A is 0, B is 1, and so on...) and the number denotes the row. Do not forget that 1 actually refers to 0 index.
    - The program checks whether the user input is in the `LETTERNUMBER` format, such as `B2` or `F10`.
    - The program checks whether the input number is positive and does not exceed the number of rows on the board.
    - The program checks whether the position of the input letter in the alphabet does not exceed the number of columns on the board.
    - The program keeps asking the user for a field until receiving valid input.
    - After the input is validated, coordinates of the selected field are passed further into the program logic as an integer tuple `(row, column)`.

3. The user can select the difficulty level before starting the game. The difficulty level dictates the size of the board.
    - One of the three difficulty levels can be picked, easy, medium, and hard.
    - At the Easy difficulty level, the size of the board is `5x4`.
    - At the Medium difficulty level, the size of the board is `5x6`
    - At the Hard difficulty level, the size of the board is `5x10`

4. Implement the board drawing mechanic, according to the following requirements.
    - When drawing the board, the coordinates of fields are also be displayed
(numbers of rows and letters of columns), similar to the following example:
```
  A B C D E

1 # # # # #

2 # # # # #

3 # # # # #

4 # # # # #
```
    - During the game, the fields can be either concealed or revealed. The letter of the field is displayed only when the field is revealed. When the field is concealed, `#` is displayed.
    - The terminal window is cleaned every time the board is redrawn.

5. Implement the game logic, to put all parts together into a functioning game.
    - The game opens with "Welcome to Memory Game!".
    - The game asks to select a difficulty level.
    - The letter board is generated, based on the selected difficulty level.
    - The fields of the letter board are all concealed by default.
    - The board is displayed to the user.
    - The game asks asked to select a field, which is then revealed (its letter is being shown on the redrawn board).
    - The game asks to select another field, which is then revealed (its letter is being shown on the redrawn board).
    - If the two selected fields are a match (have the same letter), they remain revealed for the rest of the game.
    - If the two selected fields are not a match (do not have the same letters), the user is asked to press Enter. After that, the fields are concealed again.
    - The game ends when all fields are revealed.
    - The game counts the number of steps taken to complete the game and displays this number after winning the game.

## General requirements

None

## Hints

- None

## Background materials

- None
