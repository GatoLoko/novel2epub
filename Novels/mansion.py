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
Created on 19/02/19

@author: GatoLoko
"""

from common import Volume
import common
import re

volumes = {'1': Volume('1', 1, 29),
           '2': Volume('2', 30, 85),
           '3': Volume('3', 86, 209),
           '4': Volume('4', 210, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 900),
           '10': Volume('10', 901, 1000),
           '11': Volume('11', 1001, 1100),
           '12': Volume('12', 1101, 1200),
           '13': Volume('13', 1201, 1300),
           '14': Volume('14', 1301, 1400),
           '15': Volume('15', 1401, 1500),
           '16': Volume('16', 1501, 1571),
           #
           # This novel ends in chapter 1610
           }

origin = 'http://www.wuxiaworld.co/I-Have-a-Mansion-in-the-Post-apocalyptic-World/'
author = 'Morning Star LL (晨星LL)'
cover_file = 'Covers/Mansion.jpg'
title = 'I have a mansion in the post-apocalyptic world - Vol'

synopsis_text = """
Ruins stretched across the landscape in the apocalypse after the nuclear
war.</p>

<p>If you accidentally survived on the wasteland, then you must be ready to
face the endless hunger, ceaseless dangers, the mad zombies at night, and the
peculiar mutant creatures that are the aftermaths of the constant
radiation.</p>

<p>But for Jiang Chen, this place was heaven.</p>

<p>Mansions stood tall, luxurious cars parked on the street, high tech products
and gold abandoned everywhere.</p>

<p>What? You were the president of a game development company before the war?
You were responsible for the development of the 3D virtual reality online
multiplayer game? Well, that’s great, why don’t you come work for me. The
salary is two pieces of bread a day.</p>

<p>iPhone? Ultra thin design? Don’t you see that the phone I invented are
thinner than condoms?</p>

<p>Aircraft carrier? Fighter jets? Oh, I have those things as well, but they
are designed for space combat.</p>

<p>Watch the story of Jiang Chen, who possessed the ability to travel through
space and time, as he witness the creation of an empire stretched across space
and time..
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^%s .*' % str(i)
        # if i in range(127, 137):
        #     text = '^Chapter %s' % str(i)
        # elif i in [149, 861]:
        #     text = '^Chapter %s-.*' % str(i)
        # elif i == 283:
        #     text = '^Chapter 284 – Special Requests'
        # elif i == 284:
        #     text = '^Chapter 284 – Seeing West Wonder King'
        # elif i == 311:
        #     text = '^Chapter 312 – Playing the Role of A Silkpants'
        # elif i == 312:
        #     text = '^Chapter 312 – Keeping Up Appearances'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    warpEngine = re.compile(r'wrap engine')
    for i in content.find_all(text=warpEngine):
        istring = re.sub(warpEngine, 'warp engine', i)
        i.replaceWith(istring)
    firstCorp = re.compile(r'First Crop')
    for i in content.find_all(text=firstCorp):
        istring = re.sub(firstCorp, 'First Corp', i)
        i.replaceWith(istring)
    spam = re.compile(r'Find.*authorized.*Webnovel.*click.*visiting.*')
    for i in content.find_all(text=spam):
        print('    Spam')
        istring = re.sub(spam, '', i)
        i.replaceWith(istring)
    dragoncavalry = re.compile(r'Dragon Calvary')
    for i in content.find_all(text=dragoncavalry):
        print('    Dragon Cavalry')
        istring = re.sub(dragoncavalry, 'Dragon Cavalry', i)
        i.replaceWith(istring)
    return content
