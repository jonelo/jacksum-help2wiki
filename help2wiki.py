#!/usr/bin/env python3

import fileinput
virgin=True
pending=0

for line in fileinput.input():
   if (line.strip()==line.rstrip() and line.isupper()):
       if (not virgin):
         print('```')
         print()
       print('## '+line.rstrip())
       print('```')
       virgin=False
       pending=0
   elif (not line.strip()):
       pending+=1
   else:
       for _ in range(pending):
           print()
       pending=0
       print(line.rstrip())
print('```')