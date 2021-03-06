#!/usr/bin/env python3

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
import common
import re

volumes = {'1': Volume('1', 1, 19),
           '2': Volume('2', 20, 37),
           '3': Volume('3', 38, 57),
           '4': Volume('4', 58, 78),
           '5': Volume('5', 79, 89),
           '6': Volume('6', 90, 104),
           '7': Volume('7', 105, 128),
           '8': Volume('8', 129, 150),
           '9': Volume('9', 151, 174),
           '10': Volume('10', 175, 205),
           '11': Volume('11', 206, 225),
           '12': Volume('12', 226, 250),
           '13': Volume('13', 251, 272),
           '14': Volume('14', 273, 292),
           '15': Volume('15', 293, 324),
           '16': Volume('16', 325, 352),
           '17': Volume('17', 353, 379),
           '18': Volume('18', 380, 403),
           '19': Volume('19', 404, 435),
           '20': Volume('20', 436, 475),
           '21': Volume('21', 476, 502),
           '22': Volume('22', 503, 523),
           '23': Volume('23', 524, 551),
           '24': Volume('24', 552, 584),
           '25': Volume('25', 585, 613),
           '26': Volume('26', 614, 656),
           '27': Volume('27', 657, 681),
           '28': Volume('28', 682, 709),
           '29': Volume('29', 710, 758),
           '30': Volume('30', 759, 789),
           '31': Volume('31', 790, 810),
           '32': Volume('32', 811, 841),
           '33': Volume('33', 842, 874),
           '34': Volume('34', 875, 899),
           '35': Volume('35', 900, 961),
           '36': Volume('36', 962, 996),
           '37': Volume('37', 997, 1020),
           '38': Volume('38', 1021, 1049),
           '39': Volume('39', 1050, 1098),
           '40': Volume('40', 1099, 1172),
           '41': Volume('41', 1173, 1223),
           '42': Volume('42', 1224, 1251),
           '43': Volume('43', 1252, 1278),
           '44': Volume('44', 1279, 1319),
           '45': Volume('45', 1320, 1354),
           '46': Volume('46', 1355, 1387),
           '47': Volume('47', 1388, 1424),
           '48': Volume('48', 1425, 1466),
           '49': Volume('49', 1467, 1507),
           '50': Volume('50', 1508, 1556),
           '51': Volume('51', 1557, 1591),
           '52': Volume('52', 1592, 1619),
           '53': Volume('53', 1620, 1646),
           '54': Volume('54', 1647, 1719),
           '55': Volume('55', 1720, 1771),
           '56': Volume('56', 1772, 1790),
           '57': Volume('57', 1791, 1855),
           '58': Volume('58', 1856, 1898),
           '59': Volume('59', 1899, 1976),
           '60': Volume('60', 1977, 2015),
           # The original novel ends at chapter 2012 of volume 60, but for some
           # reason the translation does not. Maybe some chapteres were split
           # in two parts or something like that.
           }

origin = 'http://www.wuxiaworld.co/Castle-of-Black-Iron/'
author = 'Drunken Tiger'
cover_file = 'Covers/castle-of-black-iron.jpg'
title = 'Castle of Black Iron - Vol'

synopsis_text = """
After the Catastrophe, every rule in the world was rewritten.</p>

<p>In the Age of Black Iron, steel, iron, steam engines and fighting force
became the crux in which human beings depended on to survive.</p>

<p>A commoner boy by the name Zhang Tie was selected by the gods of fortune and
was gifted a small tree which could constantly produce various marvelous
fruits. At the same time, Zhang Tie was thrown into the flames of war, a
three-hundred-year war between humans and demons on the vacant continent. Using
crystals to tap into the potentials of the human body, one must cultivate to
become stronger.</p>

<p>The thrilling legends of mysterious clans, secrets of Oriental fantasies,
numerous treasures and legacies in the underground world — All in the Castle of
Black Iron!
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = '^' + str(i) + ' .*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        print('    Credline')
        i.replaceWith('')
    spam1 = re.compile(r'Find authorized.*Webnovel.*webnovel.*')
    for i in content.find_all(text=spam1):
        print('    Spam')
        istring = re.sub(spam1, '', i)
        i.replaceWith(istring)
    return content
