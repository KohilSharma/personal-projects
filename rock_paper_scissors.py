"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. It is extensible via computer classes."""

import random


class Player:

    my_move = None
    their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Pick an option > ")
        while choice.lower() not in moves:
            choice = input("Pick a valid option > ")
        return choice


class RockyPlayer(Player):
    def move(self):
        return 'rock'


class ReflectPlayer(Player):

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        pos = moves.index(self.my_move) + 1
        if pos == len(moves):
            pos = 0
        return moves[pos]


def beats(m1, m2):
    case1 = (m1 == 'rock' and m2 == 'scissors')
    case2 = (m1 == 'paper' and m2 == 'rock')
    case3 = (m1 == 'scissors' and m2 == 'paper')
    return case1 or case2 or case3


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You chose {move1}.\nComputer chose {move2}.")
        if move1 == move2:
            print("Tied.")
            print(f"Scores So Far> You: {self.count1} Computer: {self.count2}")
        elif beats(move1, move2):
            print("You Have Won!")
            self.count1 += 1
            print(f"Scores So Far> You: {self.count1} Computer: {self.count2}")
        else:
            print("Computer Won.")
            self.count2 += 1
            print(f"Scores So Far> You: {self.count1} Computer: {self.count2}")
        self.p2.learn(move2, move1)

    def play_game(self):
        self.games = input("\nHow many rounds do you want to play? > ")
        while not self.games.isnumeric():
            self.games = input("Enter a number please > ")
        self.games = int(self.games)
        print(f"\nThe Game Has Begun!! Round of {self.games}")
        for round in range(self.games):
            print(f"\nRound {round+1}:")
            self.play_round()
        print("\nGame Over!\n\nFinal Scores")
        print(f"You: {self.count1}\tComputer: {self.count2}")
        if self.count1 > self.count2:
            print("\nYOU have won this game! Hurray!! :D\n")
        elif self.count1 == self.count2:
            print("\nTIED. Nobody Won.")
        else:
            print("\nCOMPUTER has won this game. :'(\n")


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    players = [RandomPlayer(), ReflectPlayer(), CyclePlayer(), RockyPlayer()]
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()
