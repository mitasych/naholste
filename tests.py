#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import os
from PIL import Image
from math import floor

a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(2)
print a
"""
t = ' &nbsp;1&nbsp;2256.89&nbsp;  &nbsp; &nbsp; '
t = float(t.strip().replace('&nbsp;', '').replace(' ', ''))
#print t

a = 2
b = 5
c = a > b and a or b

class ChoiseAdmin(object):

	start = 0
	
	def new(self, row):
		self.start = self.start + 1
		###
		return (self.start, u"%sx%s см" % (row[0], row[1]))

ca = ChoiseAdmin()

SIZE_CHOISES = (
	(12, 12,),
	(20, 20,),
	(30, 30,),
	(36, 36,),
	(16, 12,),
	(20, 16,),
	(30, 24,),
	(35, 28,),
	(12, 16,),
	(16, 20,),
	(24, 30,),
	(28, 35,),
)

t = tuple(ca.new(v) for v in SIZE_CHOISES)

print t
"""

#http://blog.swlogic.eu/2010/09/19/pishem-rasshirenie-prilozheniya-dlya-django/
"""
class Test(object):
	f_0 = 1
	f_1 = 2
	f_2 = 3
	f_3 = 4
	f_4 = 5

t = Test()
for i in xrange(5):
	print getattr(t, 'f_%s' % (i,))

aa = int(floor(float(88)/3))

print aa
"""
"""l = [
	'111',
	'222',
	'333',
	'444',
]

l.remove('222')
print l

n = datetime.datetime.now()

print n.year
print '%02d%02d' % (n.month, n.day)

try:
	img = Image.open('__init__.pyfd')
except IOError, e:
	print IOError, e
"""
#class Test(object):

#	def __init__(self, obj=None):
#		return None

#t = Test()

#print t
#f = 'sfdsdfasdfasdfasdfsadfsadfasdf.tiff'

#print os.path.splitext(f)

#a = 0.22

#print type(a).__name__
