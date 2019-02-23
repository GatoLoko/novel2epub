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

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 180),
           }

origin = 'http://www.wuxiaworld.co/Bringing-The-Farm-To-Live-In-Another-World/'
author = 'Ming Yu (明宇)'
cover_file = 'Covers/bringing-the-farm.jpg'
title = 'Bringing the farm to live in another world - Vol'

synopsis_text = """
“If he’s being badass, I’m gonna plant my own crops. If he messes with me, he
will not live past next year.”</p>

<p>Homebody Zhao Hai brought ‘QQ Farm’ along in his traversal to another world and
resided within the body of a fallen noble. His fief was a black land which
nothing could be planted, and more importantly, he even had a peerlessly
powerful fiancee, who was actually the successor of a duchy and future Grand
Duchess!</p>

<p>Even more importantly, he is a magical and martial cripple who could not learn
magic and martial arts. His crippling was very thorough.</p>

<p>“I can’t learn magic, but I have the farm. You dare attack me? I’ll release
bugs to eat up your rations and crops, and put pesticides and weed agents into
your water sources to make your lands grow weeds. See if you dare to attack me.
What? You wanna hire killers to assassinate me? Hehehe. I’ll hide inside the
little house in my farm and see how you can attack me. When you leave, I’m
gonna terminate your country’s crop productions, and then all of your people
will revolt. See if you dare to kill me.”</p>

<p>Watch how this somewhat black hearted hobo uses his QQ Farm in the world of
swords and magic to become a globally known nightmarish existence.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        print(i)
        text = '^%s .*' % str(i)
        # if i in range(127, 137):
        #     text = '^Chapter %s' % str(i)
        # elif i == 149:
        #     text = '^Chapter %s-.*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    return content
