#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Copyright (C) 2017 GatoLoko
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""
Created on 25/12/17

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - Ji Clan of Swallow Mountain',
                       1, 18),
           '2': Volume('2 - The lake in the East Mountain',
                       2, 18),
           '3': Volume('3 - Comprehending "The Way" by the pond',
                       3, 18),
           '4': Volume('4 - Underwater estate',
                       4, 20),
           '5': Volume('5 - Zifu disciple',
                       5, 26),
           '6': Volume('6 - Breaking through the cocoon, becoming a butterfly',
                       6, 38),
           '7': Volume('7 - Stillwater city',
                       7, 41),
           '8': Volume('8 - Raindragon guard',
                       8, 34),
           '9': Volume('9 - Ji Ning of Serpentwing lake',
                       9, 39),
           '10': Volume('10 - Entering the Immortal Estate',
                        10, 29),
           '11': Volume('11 - Primaltwin',
                        11, 36),
           '12': Volume('12 - Immortal destiny',
                        12, 40),
           '13': Volume('13 - Tristan Crescent Abode',
                        13, 36),
           '14': Volume('14 - Return to the Grand Xia',
                        14, 30),
           '15': Volume('15 - The sword eradicates Celestial Immortals',
                        15, 32),
           '16': Volume('16 - The Nihilum zone',
                        16, 25),
           '17': Volume('17 - Celestial immortal',
                        17, 27),
           '18': Volume('18 - Pure Yang',
                        18, 56),
           '19': Volume('19 - Empyrean God',
                        19, 55),
           '20': Volume('20 - Jindan upgrade',
                        20, 37),
           '21': Volume('21 - The Bloodlotus blooms',
                        21, 37),
           '22': Volume('22 - True God',
                        22, 29),
           '23': Volume('23 - Endwar',
                        23, 35),
           '24': Volume('24 - The Starlord of Fogstone',
                        24, 49),
           '25': Volume('25 - Novessence Thunder',
                        25, 40),
           '26': Volume('26 - World level',
                        26, 58),
           '27': Volume('27 - Twelve palaces',
                        27, 29),
           '28': Volume('28 - Archaeus region',
                        28, 48),
           '29': Volume('29 - Daolord',
                        29, 42),
           '30': Volume('30 - Ancient cultivator',
                        30, 36),
           '31': Volume('31 - Starflow river',
                        31, 24),
           '32': Volume('32 - Waveshift realm',
                        32, 28),
           '33': Volume('33 - Crimsonware temple',
                        33, 23),
           '34': Volume('34 - The stone hellephant wall',
                        34, 32),
           '35': Volume('35 - The Aeonian race',
                        35, 20),
           '36': Volume('36 - Daolord of the Fourth Step',
                        36, 30),
           '37': Volume('37 - Flamewing God',
                        37, 31),
           '38': Volume('38 - Daomerge',
                        38, 43),
           '39': Volume('39 - Nuwa',
                        39, 17),
           }

origin = 'http://www.wuxiaworld.com/desolate-era-index/'
author = 'I Eat Tomatoes （我吃西红柿）'
cover_file = 'Covers/desolate-era.jpg'
title = 'Desolate Era - Vol'

synopsis_text = """ Fate had never been kind to Ji Ning. Wracked by illnesses
and infirm his entire life on Earth, Ning knew early on that he would die as a
teenager. What he didn’t know was that there really was such a thing as life
after death, and that the universe was a far larger place than he thought. A
lucky twist of fate (one of the few in Ning’s life) meant that Ning was reborn
into a world of Immortals and monsters, of Ki Refiners and powerful Fiendgods,
a world where Dynasties lasted for millions of years. A world which is both
greater…and yet also smaller…than he ever could imagine. He would have the
opportunity to join them, and in this life, Ning swore to himself, he would
never let himself be weak again! The Era he was born into was a Desolate one,
but Ning would make it his era.  """


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(1, end+1):
        url = origin + "de-book-" + str(start) + "-chapter-" + str(i)
        chapterlist.append(url)
    return chapterlist
