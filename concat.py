#!/usr/bin/env python3
# Add a text to a list of URLs

import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description='This tool adds a text to a specified \
      position in a given file.'
)
parser.add_argument(
    '-i', '--input', required=True,
    help='Text file to be worked on'
)
parser.add_argument(
    '-t', '--text', required=True,
    help='Specify the text to be added'
)
parser.add_argument(
    '-f', '--front', required=False, action='store_true',
    help='Add text to the front of the text'
)
parser.add_argument(
    '-b', '--back', required=False, action='store_true',
    help='Add text to the back of the text'
)
parser.add_argument(
    '-o', '--output', required=False,
    help='Optional output text file'
)

args = parser.parse_args()
output = args.input if args.output is None else args.output
output = output if '/' in output else os.getcwd() + '/' + output

with open(args.input) as lines:
  lines = [i.strip() for i in lines.readlines()]

  if args.front and args.back:
    lines = [args.text+i+args.text for i in lines]
  elif args.back:
    lines = [i+args.text for i in lines]
  else:
    lines = [args.text+i for i in lines]

  with open(output, 'w') as other_lines:
    other_lines.write('\n'.join(lines))
  print('[!] Success! Output saved to {}'.format(output))
