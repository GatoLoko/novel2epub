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
from string import Template
import sys
sys.path.append("Novels")
try:
    import common
except ImportError:
    raise


def arguments():
    parser = argparse.ArgumentParser(
        description="Download web stories and stores them as epub.",
        epilog="This script doesn't support actualizing an existing epub" +
               " with new chapters, so it regenerates them from scratch.",
        argument_default=argparse.SUPPRESS)
    parser.add_argument('novel', metavar='novel', type=str,
                        help='Which novel you want to get')
    parser.add_argument('volume', metavar='volume', type=int,
                        help="Which volume to get")
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Print debug messages to stdout')
    parser.add_argument('labels', metavar='labels', nargs='*',
                        help='Labels to add as metadata to the epub')
    args = parser.parse_args()

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))

    return args


###############################################################################
# TODO: Remove this block when the fix is released
# Something goes wrong when adding an image as a cover, and we need to work
# around it by replacing the get_template function with our own that takes care
# of properly encoding the template as utf8.
# There is a bug reported, and this will become unnecesary once the fix gets
# into the distributions.
original_get_template = epub.EpubBook.get_template


def new_get_template(*args, **kwargs):
        return original_get_template(*args, **kwargs).encode(encoding='utf8')
epub.EpubBook.get_template = new_get_template
###############################################################################


if __name__ == "__main__":

    args = arguments()

    try:
        novel = __import__(args.novel)
        print("Loaded %s module" % args.novel)
    except ImportError:
        print("Unsuported novel")
        raise

    volume = novel.volumes[str(args.volume)]
    print("Volume start: %s" % volume.first)
    print("Volume end: %s" % volume.last)
    chapterlist = novel.genlist(volume.first, volume.last)
    fill = ''
    if args.volume < 10:
        fill = '0'
    title = novel.title + fill + volume.title
    # Remove from the file name those characters that FAT does NOT allow, so we
    # can transfer the file to a phone or tablet sdcard: \/:*?"<>|
    for i in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if i in title:
            title = title.replace(i, '')
    filename = title + ".epub"
    print("Title: " + title)
    print("Chapters: " + str(len(chapterlist)))
    print("Filename: " + filename)

    book = epub.EpubBook()
    book.set_identifier("novel2epub/%s/%s/%s" % (args.novel, novel.title,
                                                 volume.last))
    book.set_title(title)
    book.set_language('en')
    book.add_metadata('DC', 'subject', 'web2epub')
    if hasattr(args, 'labels'):
        for label in args.labels:
            book.add_metadata('DC', 'subject', label)
    # Add a cover if it's available
    book.set_cover(file_name='cover.jpg',
                   content=open(novel.cover_file, 'rb').read(),
                   create_page=True)

    allchapters = []

    for i in chapterlist:
        if args.debug:
            print(i)
        ch_title, ch_file, ch_text = common.get_chapter(i)
        chapter = epub.EpubHtml(title=ch_title, file_name=ch_file, lang='en')
        chapter.content = ch_text
        book.add_item(chapter)
        allchapters.append(chapter)

    # Define CSS style
    with open("CSS/nav.css") as style_nav:
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css",
                                media_type="text/css",
                                content=style_nav.read())
    with open("CSS/body.css") as style_body:
        body_css = epub.EpubItem(uid="style_body", file_name="style/body.css",
                                 media_type="text/css",
                                 content=style_body.read())
    # Add CSS files
    book.add_item(nav_css)
    book.add_item(body_css)

    # Introduction
    intro_ch = epub.EpubHtml(title=title, file_name='intro.xhtml')
    intro_ch.add_item(body_css)

    intro_ch = epub.EpubHtml(title='Introduction', file_name='intro.xhtml')
    intro_ch.add_item(body_css)
    with open('HTML/intro.xhtml') as infile:
        in_template = Template(infile.read())
    intro_ch.content = in_template.substitute(title=title,
                                              author=novel.author,
                                              url=novel.origin,
                                              synopsis=novel.synopsis_text)
    book.add_item(intro_ch)

    # Define Table of Contents
    book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
                (epub.Section('Chapters'), allchapters))

    # Add default NCX and Nav files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Basic spine
    # myspine = []
    # myspine.append('cover')
    # myspine.extend([intro_ch, 'nav'])
    myspine = ['cover', intro_ch, 'nav']
    myspine.extend(allchapters)
    book.spine = myspine

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))

    epub.write_epub(filename, book, {})
