import pygame
import os
from random import randint


def get_var():
    songs = get_songs()
    if (songs == None):
        return "ERROR!"
    else:
        print("Guess the song!\nVarients: \n")
        for key in (list(map("\n".__add__, songs))):
            print(key)
        num = input("Song? ")
        return songs[int(num)]


def get_songs():
    files = os.listdir("./")
    songs = list(filter(lambda x: x.endswith('.mp3'), files))
    return songs


def get_random_song():
    songs = get_songs()
    length = len(songs)
    random_number = randint(0, length - 1)
    return songs[random_number]


def start_game():
    pygame.init()
    random_song = get_random_song()
    song = pygame.mixer.Sound(random_song)
    clock = pygame.time.Clock()
    song.play()
    while True:
        result = get_var()
        clock.tick(20)
        if (result == random_song):
            print("Success!")
            pygame.quit()
            return "Good"

        else:
            print("Failure!")
            pygame.quit()
            return "Bad"


def menu():
    num = str(input())
    print("You choosed: " + num)
    if (num == "1"):
        start_game()
        return "0"
    if (num == "2"):
        return "1"


print("Welcome to guess the melody game!\nChoose one of the options below!\n(1) - start the game, (2) - quit the game")
menu()
