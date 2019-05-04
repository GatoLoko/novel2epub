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
Created on 24/01/17

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - Divine strength awakens, mystery of Qing '
                       'Shui\'s birth',
                       1, 115),
           '2': Volume('2 - Legend of Hundred Miles city, peerless and '
                       'independent',
                       116, 160),
           '3': Volume('3 - The resplendent fireworks, the Mountains and '
                       'Rivers like painting',
                       161, 243),
           '4': Volume('4 - Tears of a beauty destroying the kingdom, the '
                       'twelve Portraits of Beauty',
                       244, 350),
           '5': Volume('5 - Greencloud continen of the Nine Continents, '
                       'stepping into the Yan Clan',
                       351, 443),
           '6': Volume('6 - Aura of a King, sword pointing at the Dome of '
                       'Heavens',
                       444, 508),
           '7': Volume('7 - Path of Martial Saint, heart of the strong',
                       509, 594),
           '8': Volume('8 - Through the flourishing Central Continent',
                       595, 744),
           '9': Volume('9 - Southern Vieweing Continent, hatred of the former'
                       ' years',
                       745, 825),
           '10': Volume('10 - Eastern Victory Divine continent, exquisite'
                        ' bell spirit',
                        826, 935),
           '11': Volume('11 - Storm in the Fifth Continent, the northern'
                        ' Sacred Lu Continent',
                        936, 1060),
           '12': Volume('12 - Stepping on Lion King Ridge, trampling with such'
                        ' force until the mountains and rivers crumble',
                        1061, 1133),
           '13': Volume('13 - Arriving at the Four Continents, Hundred'
                        ' Dynasties, Hundred States. The path of a state'
                        ' master',
                        1134, 1313),
           '14': Volume('14 - Soaring Dragon, dancing Phoenix, Haohan'
                        ' continent',
                        1314, 1593),
           '15': Volume('15 - Demons & monsters dancing in riotous revelry,'
                        ' beautiful women are like poetry',
                        1594, 1794),
           '16': Volume('16 - Oceanic Grand World, Legend of the Nine'
                        ' Continents',
                        1795, 2216)
           # 1795, 2492)
           }

origin = 'http://www.wuxiaworld.com/novel/ancient-strengthening-technique/'
author = 'I Am Superfluous (我是多余人)'
cover_file = 'Covers/ancient-strengthening-technique.jpg'
title = 'Ancient Strengthening Technique - Vol'

synopsis_text = """
A human warrior cultivating the Ancient Strengthening Technique has
transcended dimensions and arrived on Kyushu. Together with twelve ravishing
beauties with looks that were unmatched in their generation, will he be able
to stand on the summit of this world?</p>

<p>This novel is about the main character, named Qing Shui, who transcended
dimensions and arrived in the Kyushu continent. Storms of blood and wind,
resulting in corpses and bones strewn about are extremely common here. The
young warrior Qing Shui forged ahead in his path to cultivate, using 10
years to train himself, only to seek vengeance for the one who had forsaken
his mother! On the road, he had a chance encounter with the cold beauty (ice
princess) Shi Qing Zhuang, incurring hatred and vengeance from her fiancée
– Situ Bu Fan. After entering the Hundred Miles City, Qing Shui got
acquainted with a dignified and beautiful lady named Yu He and other Xian
Tian Realm cultivators – After which, he willingly invited tribulation on
himself, after killing the young master of the Gong Yang Clan because of
Yu He, and was forced into a corner. Luckily for Qing Shui, a lady as
beautiful as a celestial maiden named Yi Ye Jian Ge rushed back to save him
from afar, following which a bloody battle ensued. Can Qing Shui turn danger
into safety, averting disaster? And his relationships with the various
beautiful ladies, what will it develop into?</p>

<p><b>Note from Author: I Am Superfluous</b><br />
To put it simply, this is a story about the rising up in ranks, and getting
hot chicks along his journey to stand at the summit of this world.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i not in [29, 1183]:
            url = origin + "ast-chapter-" + str(i)
            if i == 28 or i in range(1697, 1952):
                url = origin + "ast-chapter-" + str(i) + "-1"
                if i == 1951:
                    chapterlist.append(url)
                    url = origin + "ast-chapter-" + str(i) + "-2"
            elif i == 232:
                url = origin + "ast-chapter-232-part-1000"
            elif i in [246, 248]:
                url = origin + "ast-chapter-" + str(i) + "-part-1"
            elif i == 329:
                url = origin + "ast-chapter-329-part-4"
            elif i == 1421:
                url = origin + "chapter-1421"
            elif i == 1661:
                url = origin + "ast-chapter-16611"
            chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
