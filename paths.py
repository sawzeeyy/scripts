#!/usr/bin/env python3
# Extract PATHs from a list of URLs
# Exactly what @TomNomNom's Unfurl does
# But I needed a different result and coded this anyway
# PS: This was for a specific use case.

import argparse
import os
import sys
from urllib.parse import urlparse

parser = argparse.ArgumentParser(
    description='This extract PATHs from a list of URLs'
)
parser.add_argument(
    '-i', '--input', required=True,
    help='Text file containing a list of URLs'
)
parser.add_argument(
    '-r', '--reversed', required=False, action='store_true',
    help='Reverse the output'
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
  lines_output = []

  for line in lines:
    if urlparse(line).query:
      lines_output.append('`{}?{}`'.format(
        urlparse(line).path, urlparse(line).query)
      )
    else:
      lines_output.append("'{}'".format(urlparse(line).path))

  if args.reversed:
    lines_output = lines_output[::-1]

  with open(output, 'w') as other_lines:
    other_lines.write(',\n'.join(lines_output))
  print('[!] Success! Output saved to {}'.format(output))
