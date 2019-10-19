# rtb
This tool **r**emoves **t**exts **b**efore a specified breakpoint in a given file.


# Installation
```
git clone https://github.com/sawzeeyy/scripts.git
cd rtb
```

# Usage
```
usage: rtb.py [-h] -i INPUT -b BREAKPOINT [-s] [-o OUTPUT]

This tool removes texts before a specified breakpoint in a given file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Text file to be worked on
  -b BREAKPOINT, --breakpoint BREAKPOINT
                        Specify the deletion point
  -s, --inclusive       Specify if the breakpoint should be included
  -o OUTPUT, --output OUTPUT
                        Optional output text file
```