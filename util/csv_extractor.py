#!/usr/bin/env python3
# encoding: utf-8
import sys
import csv
import re


def parse_file(filename):
  with open(filename, 'rU') as infile:
    # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
      for header, value in row.items():
        try:
          data[header].append(value)
        except KeyError:
          data[header] = [value]

  # extract the variables you want
  return data['text']


def write_output(output):
  file = open('../data/csv_output.txt', 'w')
  file.write(output)
  file.close()

def clean_list(list_to_be_parsed):
  new_text = []
  for string_fragment in list_to_be_parsed:
    if not re.match('^RT', string_fragment) and not re.match(r'^http[s]?:\/\/.*[\W]*', string_fragment):
      new_text.append(string_fragment)
  return "\n".join(new_text)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Wrong number of arguments")
    sys.exit(1)
  raw_list = parse_file(sys.argv[1])
  write_output(clean_list(raw_list))
  print("csv_output.txt saved in ../data")
  sys.exit(0)
  # cleaned_string = clean_list(raw_list, RGX_LIST)
  # write_output(cleaned_string)
