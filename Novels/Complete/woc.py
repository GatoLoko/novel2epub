# Created on 19/02/2021
# Copyright (C) 2021 GatoLoko
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

import re

from libs import common

Volume = common.Volume

volumes = {
    "1": Volume("1", 1, 100),
    "2": Volume("2", 101, 200),
    "3": Volume("3", 201, 300),
    "4": Volume("4", 301, 400),
    "5": Volume("5", 401, 500),
    "6": Volume("6", 501, 600),
    "7": Volume("7", 601, 633),
}

origin = "https://www.wuxiaworld.co/While-Others-Cultivate,-I-Use-My-"
"Unique-RPG-Leveling-System-to-Cultivate-Smut-Romance-With-Their-Girlfriends!/"
author = "MotivatedSloth"
cover_file = "Covers/woc.jpg"
title = "While others cultivate, I use my unique RPG leveling system"
" to cultivate smut romance with their girlfriends - Vol"

synopsis_text = """
Did I reincarnate? Or was I transported to an Isekai cultivation world? To be
honest, I have no clue!</p>

<p>What matters is that I turned from being useless, bullied, and trash, to
fully-fledged garbage in my new cultivation world!</p>

<p>But what is this strange bleep that keeps ringing in my ears? Is this some
kind of system? Oh God! Did you gift me such a cliché, right at the start of my
journey?</p>

<p>Wait, why are you trying to kill me? Did I do something to you? Stand back
or I will be forced to use unstoppable Exhudia!</p>

<p>Tell me, what did she do for you to treat your significant other in this
way?  Let me show you how girlfriends should be taken care of!</p>

<p>Wait, everyone was always telling me that demons are bad, so why is this
demonic queen trying to seduce me? Wait! KEEP YOUR HANDS AWAY FROM MY PRECIOUS
SWORD!</p>

<p>I just came back from a mission and was promised at least a half a year of
break. Why are you bothering me again with something as silly as subjugating a
devil general?
"""


def genlist(start, end):
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end + 1):
        # print(i)
        if i in [
            605,
        ]:
            continue
        text = f"^{i} .*"
        link = list_page.find("a", text=re.compile(text))
        url = f"{origin}{link['href'].split('/')[-1]}"
        chapterlist.append(url)
    chapterlist = list(dict.fromkeys(chapterlist))
    return chapterlist


def clean(content):
    credline = re.compile(r"Translator:.*Editor:.*")
    for i in content.find_all(text=credline):
        i.replaceWith("")
    return content
