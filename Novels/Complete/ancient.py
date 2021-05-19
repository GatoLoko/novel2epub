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

import re
from common import Volume
import gsweb

volumes = {'1': Volume('1 - Divine strength awakens, mystery of Qing Shui\'s '
                       'birth',
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
                        1795, 2493)
           }

origin = 'http://www.wuxiaworld.co/Ancient-Strengthening-Technique/'
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

<p><b>Note from Author: I Am Superfluous</b></p>

<p>To put it simply, this is a story about the rising up in ranks, and getting
hot chicks along his journey to stand at the summit of this world.
"""


def genlist(start, end):
    global origin
    list_page = gsweb.get_soup(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        if i in [29, 115, 342, 825, 1183, 1794]:
            continue
        elif i in range(1, 572+1):
            text = '^Chapter %s .*' % str(i)
            if i == 370:
                text = '^Chapter %s$' % str(i)
            elif i in [351, 353, 354]:
                text = '^Chapter %s - ' % str(i)
        elif i in [573, ]:
            text = '^AST: Chapter %s .*' % str(i)
        elif i in [584, 585, 586, 587, 588, 589, 605, 616]:
            text = '^AST: Chapter %s!$' % str(i)
        elif i in [590, 800, ]:
            text = '^chapter %s$' % str(i)
        elif i in [596, 598, 799, 1416] + list(range(1440, 2492+1)):
            text = '^AST %s ' % str(i)
            if i in [1797, 1957, 2281]:
                text = '^AST %s- ' % str(i)
            elif i == 2345:
                text = '^AST 2345 - Fifth .*'
            elif i == 2435:
                text = '^AST 2345 - Tyrannous .*'
            elif i in [2468, 2473]:
                text = '^Chapter %s - ' % str(i)
        elif i in [597, 600, 603, 606, 609, 610, 611, 613, 614, 615, 617,
                   619] + list(range(591, 595+1)) + list(range(623, 626+1)):
            text = '^Chapter %s$' % str(i)
        elif i in [599, 601, 602, 604, 607, 608, 621, 668, 670, 671, 672, 675,
                   676, 677, 679, 681, 682, 684, 685, 686, 687, 689, 691, ]:
            text = '^Chapter %s!' % str(i)
        elif i in [612, ]:
            text = '^Chapter %s .*' % str(i)
        elif i in [618, 620, 622, 627, 631, 633, 635, 639, 642, 645, 648, 650]:
            text = '^AST Chapter: %s!' % str(i)
        elif i in [654, 658, 661, 663, 666, 669, 674, 678, 680, 683, 688, 690,
                   693, ] + list(range(697, 798+1)) + \
                list(range(801, 1415+1)) + list(range(1417, 1436+1)):
            text = '^Chapter: %s$' % str(i)
            if i == 1184:
                text = '^1184$'
        elif i == 2493:
            text = '^Author.*'
        else:
            text = '^Chapter %s$' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split('/')[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
