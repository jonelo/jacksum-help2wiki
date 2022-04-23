#!/usr/bin/env python3

import fileinput
virgin=True

for line in fileinput.input():
   if (line.strip()==line.rstrip() and line.isupper()):
       if (not virgin):
         print('```')
         print()
       print('## '+line.rstrip())
       print('```')
       virgin=False
   else:
       print(line.rstrip())
print('```')