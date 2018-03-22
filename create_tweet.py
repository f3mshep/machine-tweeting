#!/usr/bin/env python3
# encoding: utf-8
import sys
import markovify

def open_file(filename):
  with open(filename) as f:
    text = f.read()
  return markovify.Text(text)

def write_message(text_model):
  for integer in range(1):
    print(text_model.make_short_sentence(140))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit(1)
  model = open_file(sys.argv[1])
  write_message(model)
