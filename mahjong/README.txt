simple program designed to work in python editors that will display characters as you type them in the pop-up window

0-9 type honors and red 5s
q-p type man
a-; type sou
z-/ type pin
SPACE to add a space
BACKSPACE to erase one at a time
DELETE to erase quickly

Only works in programs like pycharm or spyder or whatever python editor you have; will not work when run with command line or opened with file explorer
import pygame,sys, math, glob, os
you will have to download pygame with the pip installer if you don't already have it

this program uses svg and png files from this webpage https://github.com/FluffyStuff/riichi-mahjong-tiles
the 1sou, 1pin, and 2pin svg files look a bit odd after resizing them in python, so I substituted them for pngs
this gives it a slightly bigger filesize, but at least the chicken has both legs now, and the 1pin isn't just a solid circle anymore

I might improve it by adding sideways tiles, and start a newline with enter instead of needing a bunch of spaces to get to a newline. Maybe a background?
