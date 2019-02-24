#!/usr/bin/env python3

# Copyright (C) 2016 GatoLoko
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
Created on 28/12/16

@author: GatoLoko
"""

import string
import urllib.request
import urllib.error
import urllib.parse
import socket
import gzip
from io import BytesIO
import re
import platform
from bs4 import BeautifulSoup

novel_module = ""
# timeout in seconds
TIMEOUT = 10
socket.setdefaulttimeout(TIMEOUT)

# Limit chapter file names to characters that wont cause problems.
VALID_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)

# Create our own User-Agent strings. We may need to fake this if a server tryes
# to mess with us.
USER_AGENT = 'Mozilla/5.0 compatible (' + platform.system() + ' ' + \
    platform.machine() + '; Novel-Indexer-Bot)'

# Woxter QX95
# Mozilla/5.0 (Linux; Android 4.4.2; Woxter QX95 Build/KOT49H)
#     AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0
#     Safari/537.36

# Webview (KitKat & Lolipop)
# Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36
#     (KHTML, like Gecko) Version 4.0 Chrome/30.0.0.0 Mobile Safari/537.36

# Nexus 5 WebView (nuevo):
# Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv)
#     AppleWebKit/537.36 (KHTML, like Gecko) Version 4.0 Chrome/43.0.2357.65
#     Mobile Safari/537.36


class Volume():
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last


def get_html(url):
    tryes = 5
    # Build our request
    req = urllib.request.Request(url)
    # Accept gziped content
    req.add_header('Accepting-encoding', 'gzip')
    # Fake user aggent
    req.add_header('User-Agent', USER_AGENT)
    while tryes > 0:
        try:
            request = urllib.request.urlopen(req)
            break
        except socket.timeout:
            tryes -= 1
        except urllib.error.URLError as error:
            if isinstance(error.reason, socket.timeout):
                tryes -= 1
            else:
                print("URL error: " + error.reason)
                quit()
    if request.info().get('Content-Encoding') == 'gzip':
        buffer = BytesIO(request.read())
        uncompressed_buffer = gzip.GzipFile(fileobj=buffer)
        html = BeautifulSoup(uncompressed_buffer.read(), 'lxml')
    else:
        html = BeautifulSoup(request.read(), "lxml")
    request.close()
    return html


def get_wuxiaworld_com(html):
    html_title = html.find('title').text
    title_parts = html_title.split(' - ')
    chapter_title = ' - '.join(title_parts[1:-1])
    if len(title_parts) == 3:
        chapter_title = title_parts[1]
    # Extract the main text DIV content and turn it into a string
    contents = html.find('div', 'panel-default').find('div', 'fr-view')
    # Site dependant cleanup
    # Remove links to previous and next chapter
    nav_links = re.compile(r'[\s]*(Previous|Next) Chapter[\s]*')
    for link in contents.find_all('a', text=nav_links):
        link.decompose()
    for link in contents.find_all('p', text=nav_links):
        link.decompose()
    return(chapter_title, contents)


def get_wuxiaworld_co(html):
    html_title = html.find('title').text
    title_parts = html_title.split(' - ')
    chapter_title = ' - '.join(title_parts[1:-1])
    if len(title_parts) == 3:
        chapter_title = title_parts[1]
    # Site dependant cleanup
    # Extract the main text DIV content and turn it into a string
    contents = html.find('div', {'id': 'content'})
    credline = re.compile(r'Translator:.*Editor:.*')
    if contents.find(text=credline):
        contents.find(text=credline).replaceWith('')
    for script in contents.find_all('script'):
        script.decompose()
    return(chapter_title, contents)


def get_gravitytales(html):
    html_title = html.find('title').text
    chapter_title = html_title.split(' - ', 1)[1].rsplit(' - ', 1)[0]
    # Extract the main text DIV content and turn it into a string
    contents = html.find('div', 'innerContent')
    # Site dependant cleanup
    for i in contents.find_all('p', {'style': 'text-align: center;'}):
        i.decompose()
    return(chapter_title, contents)


def clean_chapter_name(chapter_title):
    # Replace spaces with underscore
    chapter_file = chapter_title.replace(' ', '_') + '.xhtml'
    # Also replace non ascii "–" with "-"
    chapter_file = chapter_file.replace("–", "-")
    # Remove any remaining non-ascii character to avoid problems
    chapter_file = ''.join(c for c in chapter_file if c in VALID_CHARS)
    return chapter_file


def get_chapter(url):
    print("Processing: " + url)
    html = get_html(url)
    if 'wuxiaworld.com' in url:
        chapter_title, contents = get_wuxiaworld_com(html)
    elif 'wuxiaworld.co' in url:
        chapter_title, contents = get_wuxiaworld_co(html)
    elif 'gravitytales' in url:
        chapter_title, contents = get_gravitytales(html)
    else:
        print('Something went wrong! Unsuported server!')
        exit()
    # Novel dependant cleanup
    try:
        novel = __import__(novel_module)
        contents = novel.clean(contents)
    except ImportError:
        pass
    soup_str = "".join(map(str, contents))
    # Before turning the html into a soup, replace all weird chinese spaces
    # with actual spaces.
    soup_str = soup_str.replace('　', ' ')
    # And replace double br tags with a paragraph break
    soup_str = re.sub(r'<br/>[\t\n\r\f\v\s　]*<br/>', '</p>\n<p>', soup_str)

    print(chapter_title)
    chapter_file = clean_chapter_name(chapter_title)
    print(chapter_file)
    # Then turn the string back into a soup
    soup_text = BeautifulSoup(soup_str, 'lxml')
    # Remove all atributes from all tags
    for tag in soup_text.findAll(True):
        tag.attrs = {}
    # Remove empty paragrafs, including those which only contain br tags or the
    # weird space character (why the &·$% do you have a paragraf with nothing?)
    for paragraf in soup_text.findAll(['span', 'p']):
        if len(paragraf.text) == 0 or paragraf.text in [' ', '。']:
            paragraf.decompose()
    # Remove stray br tags
    for br_tag in soup_text.findAll('br'):
        br_tag.decompose()
    # Turn the soup into text
    # text = str(soup_text)
    text = soup_text.prettify()

    # Undo some ridiculous censoring
    # text = damnit.sub('damn it', text)
    # text = damned.sub('damned', text)
    # text = fuck.sub('fuck', text)

    return chapter_title, chapter_file, text
