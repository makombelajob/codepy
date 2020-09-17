# coding: utf-8

import re

x = 'Form: Job Makombela: character'
y = re.findall('^F.+:', x)
print(y)

# second code with the non_deegry '+?'
x = 'Form: Job Makombela: character'
y = re.findall('^F.+?:', x)
print(y)