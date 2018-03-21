#!/usr/bin/env python3
# encoding: utf-8
import sys
import re

# command line utility that removes regex patterns from text
RGX_LIST = ['\(.+\)', '\[.+\]', '\*', '\+']


def clean_text(rgx_list, text):
  new_text = text
  #TODO: remove this pattern, add to RGX_LIST, make sure it works
  new_text = re.sub(r'\d.+\(.+\)', '', new_text)
  for rgx_match in rgx_list:
      new_text = re.sub(rgx_match, '', new_text)
  return new_text

def open_input(filename):
  f = open(filename, 'r')
  text = f.read()
  f.close()
  return text

def write_output(output):
  file = open('output.txt', 'w')
  file.write(output)
  file.close()

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Wrong number of arguments")
    sys.exit(1)

  text = open_input(sys.argv[1])
  cleaned_text = clean_text(RGX_LIST, text)
  write_output(cleaned_text)
  print("We did it bois")
  sys.exit(0)
