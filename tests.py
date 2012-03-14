#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import os
from PIL import Image
from math import floor

t = tuple((k, 'name - %s'% k) for k in xrange(10))

print t


www = [
	'1',
	'2',
	'3',
	'4',
]

print www

d1 = {'a1':1, 'a2':2, 'a3':3,}
d2 = {'a1':4, 'a5':5, 'a6':7,}

print d1
print 
print d2

d1.update(d2)
print d1
print
print d2
"""
ee = ['a1', 'a2', 'a3']

if 'a4' not in ee:
	print 'Yep'

d = {
	'k1':10,
	'k2':20,
}

print d.get('k3', None)

letterst = 'qwertyuiop'
signst = 'uiop'

print letterst[0:-len(signst)]

TYPE_SIZE_2 = (
	(288, 192,),
	(192, 144,),
	(144, 192,),
	(144, 192,),
	(96, 96,),
	(96, 96,),
	(192, 144,),
)

for i in xrange(7):
	print TYPE_SIZE_2[i][0]

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

SIZE_CHOISES = (
	(1, u'30x20 см',),
	(2, u'40x30 см',),
	(3, u'50x40 см',),
	(4, u'60x40 см',),
	(5, u'70x50 см',),
	(6, u'90x60 см',),
	(7, u'30x30 см',),
	(8, u'40x40 см',),
	(9, u'50x50 см',),
	(10, u'60x60 см',),
	(11, u'70x70 см',),
	(12, u'90x90 см',),
)

print '%(price).2f' % {'price': 10}
"""
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
