#Make a script that plays a sound file.

import pygame
pygame.init()
pygame.mixer.music.load('PATH TO AUDIO FILE')
pygame.mixer.music.play()
pygame.event.wait()# Wait the end of the music to close the program