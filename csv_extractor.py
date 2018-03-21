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
  file = open('csv_output.txt', 'w')
  file.write(output)
  file.close()

def clean_list(list_to_be_parsed, rgx_list):
  import pdb; pdb.set_trace()
  new_text = list_to_be_parsed
  #TODO: remove this pattern, add to RGX_LIST, make sure it works
  new_text = "\n".join(new_text)
  for rgx_match in rgx_list:
      new_text = re.sub(rgx_match, '', new_text)
  return new_text

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Wrong number of arguments")
    sys.exit(1)
  raw_list = parse_file(sys.argv[1])
  write_output("\n".join(raw_list))
  # cleaned_string = clean_list(raw_list, RGX_LIST)
  # write_output(cleaned_string)
