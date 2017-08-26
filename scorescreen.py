#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Stick Hero
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com

import os
from gi.repository import Gtk
import pickle
import pygame
import sys
from gettext import gettext as _

from math import *

from random import *


class scorescreen:

    def make(self, gameDisplay, back, score, fruitscore):

        pygame.init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        crashed = False
        disp_width = 600
        disp_height = 600

        press = 0

        info = pygame.display.Info()
        gameDisplay = pygame.display.get_surface()

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

        replay = pygame.image.load("images/scorescreen/replay.png")
        replay = pygame.transform.scale(replay, (104, 102))
        scoreplate = pygame.image.load("images/scorescreen/scoreplate.png")
        scoreplate = pygame.transform.scale(scoreplate, (230 + 130, 140 + 80))

        plate = pygame.image.load("images/scoreplate.png").convert()
        plate = pygame.transform.scale(plate, (340, 90))
        plate.set_alpha(220)

        home = pygame.image.load("images/scorescreen/home.png")
        # back=pygame.image.load("screenshot/screenshot.png")

        back.convert()
        back.set_alpha(225)

        font_path = "fonts/Arimo.ttf"
        font_size = 55
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", 30)
        font3 = pygame.font.Font("fonts/Arimo.ttf", 40)
        font4 = pygame.font.Font("fonts/Arimo.ttf", 20)

        down = 1
        bounce = 0
        i = 0

        keypressflag = 0

        maxscore = 0
        fruitmaxscore = 0

        with open('score.pkl', 'rb') as input:  # REading
            maxscore = pickle.load(input)
            fruitmaxscore = pickle.load(input)

        if(fruitscore > fruitmaxscore):
            fruitmaxscore = fruitscore
            with open('score.pkl', 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fruitmaxscore, output, pickle.HIGHEST_PROTOCOL)

        if(score > maxscore):
            maxscore = score
            with open('score.pkl', 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fruitmaxscore, output, pickle.HIGHEST_PROTOCOL)

        # GAME LOOP BEGINS !!!

        while not crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.KEYDOWN:
                    # jump.play(0)

                    return 1
                if event.type == pygame.QUIT:
                    crashed = True

                # event=pygame.event.poll()

            mos_x, mos_y = pygame.mouse.get_pos()

            # print event

            i += 1

            if(i > 20):
                i = 0

            if(i % 3 == 0):
                if(down == 1):
                    bounce += 1
                    if(bounce > 8):
                        down = 0
                if(down == 0):
                    bounce -= 1
                    if(bounce < 0):
                        down = 1

            gameDisplay.fill(white)
            gameDisplay.blit(back, (350, 0))

            gameDisplay.blit(plate, (430, 40))

            head1 = font1.render(_("GAME OVER!"), 1, (white))
            gameDisplay.blit(head1, (440, 40))

            gameDisplay.blit(scoreplate, (420, 200))

            gameDisplay.blit(home, (380 + 60 + 25, 400 + 50))

            gameDisplay.blit(replay, (600 + 60 - 25, 400 + 50))

            # score check

            scores = font2.render(_(str(score)), 1, black)
            gameDisplay.blit(scores, (575, 250))

            maxscores = font2.render(_(str(maxscore)), 1, black)
            gameDisplay.blit(maxscores, (575, 350))

            # GAME START

            if home.get_rect(center=(380 + 60 + 52 + 25, 400 + 50 + 51)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    home, (108, 106)), (380 + 60 + 25 - 2, 400 + 50 - 2))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 0

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            # Help menu

            if replay.get_rect(center=(600 + 60 + 52 - 25, 400 + 50 + 51)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    replay, (108, 106)), (600 + 60 - 25 - 2, 400 + 50 - 2))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 1

            pygame.draw.rect(gameDisplay, black, (0, 0, 350, 768))

            pygame.draw.rect(gameDisplay, black, (840, 0, 693, 768))

            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()
