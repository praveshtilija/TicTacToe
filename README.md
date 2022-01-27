# Tic Tac Toe with a computer

This project will output on the console, a single player game of tic tac toe with a computer

## Functions

```python
def display_board(my_board):
```
This function display_board(my_board) prints out the 3 by 3 game board used for tic tac toe on the console

```python
def valid_space(index):
```
This function valid_space(index) returns whether if a space on the game board is free

```python
def input_to_board(num, index):
```
This function input_to_board(num, index) takes the user's input from the console and assigns it to the game board

```python
def player_input():
```
This function player_input() checks if  the player's input is valid and assigns it to the game board. 

```python
def random_input(ri):
```
This function random_input(ri) generates a random input for the computer's move

```python
def valid_winner(my_board, my_input):
```
This function valid_winner(my_board, my_input) checks if the current move has won the game or not

```python
def computer_input():
```
This function computer_input() checks if the computer's input is valid and assigns it to the game board

```python
def full_board(board):
```
This function full_board(board) checks if the game board is full

## main()
- call the function display_board(my_board) to print out the game board on the console
- while the game board is not full, if not a winner, let the player/computer place their markers and display the updated game board, tie game can happen

- if full board, print out that the game is tied
