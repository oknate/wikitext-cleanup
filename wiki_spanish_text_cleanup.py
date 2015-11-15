#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from AppKit import NSPasteboard,NSObject,NSStringPboardType

def sendToClipBoard(string):
    pasteboard = NSPasteboard.generalPasteboard()
    emptyOwner = NSObject.alloc().init()
    pasteboard.declareTypes_owner_([NSStringPboardType], emptyOwner)
    pasteboard.setString_forType_(string, NSStringPboardType)


filename = '/Users/oknate2/Downloads/sample.txt'

searchreplace  = { 
 
  '[...]' : ', ',
  '–' : ',',
  '…' : ', ',
  ' -' : ', ',
  '- ' : ', ',
  '-.' : '.',
  "’" : "'",
  "‘" : "'",
  '“' : '"',
  '”' : '"',
  "—" : ', ',
  ' - ' : ', ',
  ' - ' : ', ',
  '-,' : ', ',
  ' -' : ', ',
  "…" : ', ',
}

clipboard = '';
f1 = open(filename, 'r')
for line in f1:
    newline = line
    for i, v in searchreplace.items():
        newline = newline.replace(str(i), str(v))
    newline = re.sub('\[\d+\]', '', newline);
    newline = re.sub('\[note\s[0-9]+\]', '', newline);
    newline = re.sub('([A-Z])\.([A-Z])\.', r'\1 \2 ', newline); # remove spaces after initials
    newline = re.sub('([A-Z])\.\s([A-Z])\.\s', r'\1 \2 ', newline); # remove spaces after initials
    newline = re.sub('([A-Z]\w+)\s([A-Z])\.\s([A-Z]\w+)', r'\1 \2 \3', newline); # get rid of dot in Names such as William H. Seward 
    #newline = re.sub('([A-Z]\w+)\s\(([A-Z]\w+(\s)?)+\)', r'\1', newline); # gets rid of actor names with first and last name
    newline = re.sub('\n','; ; \n', newline);
    clipboard = clipboard + newline;
f1.close()
sendToClipBoard(clipboard)
