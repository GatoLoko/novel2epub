# Readme

## What is Novel2Epub

Novel2Epub downloads chinese novels and converts them into Epub files you can
use with your favorite ebook reader. This is meant for personal use only.

## Why Novel2Epub?

Most sites don't offer an option to download a story. This forces you to remain
online while reading the stories.

Having those stories in epub format allows storing them as a backup, offline
reading and self publication (for story author or copyright owners).

## Disclaimer

The generated epubs are meant for personal use ONLY. DO NOT SHARE them without
permision from their author or copyright owner.

## Requeriments

This script has the following dependencies:

 - python3
 - BeatifulSoup4
 - ebooklib

## Running it

You can run the python script doing:
`python3 novel2epub.py novel-module volume`

> `your_url_argument` should be your the name of the module for the story, for
> example, for "The book eating magician" it would be: `bem`

> `volume` should be the volume number you want to download, for example: `1`

## Output

After the script finished, you will have your epub file inside the current
folder.

