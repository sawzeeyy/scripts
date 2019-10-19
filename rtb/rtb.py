#!/usr/bin/env python3
import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description='This tool removes texts before a specified \
      breakpoint in a given file.'
)
parser.add_argument(
    '-i', '--input', required=True,
    help='Text file to be worked on'
)
parser.add_argument(
    '-b', '--breakpoint', required=True,
    help='Specify the deletion point'
)
parser.add_argument(
    '-s', '--inclusive', required=False, action='store_true',
    help='Specify if the breakpoint should be included'
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
  if args.breakpoint in lines:
    for index, i in enumerate(lines):
      if i == args.breakpoint:
        breakpoint = index if args.inclusive else index+1
  else:
    print('[!] Error! Specified breakpoint, {} not in {}'.format(
      args.breakpoint, args.input
      ))
    sys.exit()

  with open(output, 'w') as other_lines:
    other_lines.write('\n'.join(lines[breakpoint:]))
  print('[!] Success! Output saved to {}'.format(output))
