#!/usr/bin/env python3
# Copyright (C) 2016 GatoLoko

"""
Crated on Sat Nov 12 16:41:00 2016
@author: GatoLoko
"""

import os
import argparse
import psutil
from ebooklib import epub
import urllib.request
import socket
from bs4 import BeautifulSoup
import re
from string import Template
import common

# Regex for HTML cleanup
# WARNING: The "space" character between p tags isn't really an space character
cleanup = re.compile('<div class="innerContent" ng-class="fontClass">|</div>'
                     '|<span style="font-weight: 400">|</span>|<p> </p>')
# Regex for uncensoring
damnit = re.compile('d\*m\*t|d\*mn\*t|d\*mmit')
damned = re.compile('d\*mn\*d')
fuck = re.compile('fxck')


def arguments():
    parser = argparse.ArgumentParser(
        description="Download web stories and stores them as epub.",
        epilog="This script doesn't support actualizing an existing epub with" +
               "new chapters, so it regenerates them from scratch.",
        argument_default=argparse.SUPPRESS)
    parser.add_argument('start', metavar='start', type=int,
                        help='First chapter in the series')
    parser.add_argument('end', metavar='end', type=int,
                        help='Last chapter in the series')
    parser.add_argument('-t', '--title', metavar='title', type=str,
                        help='Especify a title for the epub')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Print debug messages to stdout')
    parser.add_argument('labels', metavar='labels', nargs='*',
                        help='Labels to add as metadata to the epub')
    args = parser.parse_args()

    if not hasattr(args, "title"):
        args.title = 'untitled'

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))
    return args


def genlist(start, end):
    baseurl = 'http://gravitytales.com/novel/Zhan-Long/zl-chapter-'
    chapterlist = []
    # end = end + 1
    for i in range(start, end+1):
        url = baseurl + str(i)
        if i in [12, 30, 31, 32, 33, 34, 35, 236, 237, 238, 472]:
            url = url + "-2"
        elif i is 11:
            url = url + "-3"
        chapterlist.append(url)
    return chapterlist


def get_chapter(url):
    print("Processing: " + url)
    html = common.get_html(url)
    html_title = html.find('title').text
    chapter_title = html_title.split(' - ', 1)[1].rsplit(' - ', 1)[0]
    print(chapter_title)
    chapter_file = chapter_title.replace(' ', '_').replace(':', '') + '.xhtml'
    print(chapter_file)
    # Extract the main text DIV content and join all strings into a single one
    soup_str = "".join(map(str, html.find('div', 'innerContent').contents))
    # Turns the string back into a soup
    soup_text = BeautifulSoup(soup_str, 'lxml')
    for i in soup_text.find_all('p', {'style': 'text-align: center;'}):
        i.decompose()
    text = str(soup_text)

    # HTML cleanup
    text = cleanup.sub('', text)

    # Fixing common typos

    # Undo some ridiculous censoring
    text = damnit.sub('damn it', text)
    text = damned.sub('damned', text)
    text = fuck.sub('fuck', text)

    # Turn it into a chapter
    chapter = epub.EpubHtml(title=chapter_title, file_name=chapter_file,
                            lang='en')
    chapter.content = text
    # print(text)
    return chapter


if __name__ == "__main__":
    args = arguments()
    chapterlist = genlist(args.start, args.end)
    filename = args.title + ".epub"
    print("Title: " + args.title)
    print("Chapters: " + str(len(chapterlist)))
    print("Filename: " + filename)

    book = epub.EpubBook()
    book.set_title(args.title)
    book.set_language('en')
    book.add_metadata('DC', 'subject', 'web2epub')
    if hasattr(args, 'labels'):
        for label in args.labels:
            book.add_metadata('DC', 'subject', label)

    allchapters = []

    for i in chapterlist:
        if args.debug:
            print(i)
        chapter = get_chapter(i)
        book.add_item(chapter)
        allchapters.append(chapter)

    # Define CSS style
    with open("CSS/nav.css") as style_nav:
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css",
                                media_type="text/css", content=style_nav.read())
    with open("CSS/body.css") as style_body:
        body_css = epub.EpubItem(uid="style_body", file_name="style/body.css",
                                 media_type="text/css",
                                 content=style_body.read())
    # Add CSS files
    book.add_item(nav_css)
    book.add_item(body_css)

    # Introduction
    intro_ch = epub.EpubHtml(title=args.title, file_name='intro.xhtml')
    intro_ch.add_item(body_css)
    # TODO: Extract this variables
    origin = "http://gravitytales.com/novel/Zhan-Long"
    author = 'Shi Luo Ye'
    intro_ch = epub.EpubHtml(title='Introduction', file_name='intro.xhtml')
    intro_ch.add_item(body_css)
    with open('HTML/intro.xhtml') as infile:
        in_template = Template(infile.read())
    intro_ch.content = in_template.substitute(title=args.title, author=author,
                                              url=origin,
                                              synopsis="Synopsis placeholder")
    book.add_item(intro_ch)

    # Define Table of Contents
    book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
                (epub.Section('Chapters'), allchapters))

    # Add default NCX and Nav files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Basic spine
    myspine = [intro_ch, 'nav']
    for i in allchapters:
        myspine.append(i)
    book.spine = myspine

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))

    epub.write_epub(filename, book, {})
