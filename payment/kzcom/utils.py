# -*- coding: utf-8 -*-

import os
import base64
import M2Crypto
import OpenSSL.crypto as pki
from xml.etree import ElementTree
from settings import *

class ProcessXML(object):

	def process_XML(self, f='', request={}):
		c = False
		###
		with open(f) as wf:
			c = wf.read()
			###
			for k in request:
				c = c.replace(''.join(['[', k, ']']), str(request[k]))
		###
		return c

class ParserXml(object):

	def parseString(self, s):
		parsed = ElementTree.XML(s)
		###
		data = {}
		###
		for elem in parsed.getiterator():
			t = elem.tag.upper()
			data['_'.join(['TAG', t])] = t
			###
			if elem.text is not None and elem.text.strip():
				data['_'.join([t, 'CHARDATA'])] = elem.text
			###
			if elem.tail is not None and elem.tail.strip():
				data['_'.join([t, 'TAIL'])] = elem.tail
			###
			for name, value in sorted(elem.attrib.items()):
				data['_'.join([t, name.upper()])] = value
			###
		return data

class SplitSign(object):

	def split_sign(self, xml, tag):
		data = {};
		###
		letterst = ''
		fnd = xml.find(''.join(['<', tag]))
		if fnd >= 0: letterst = xml[fnd:]
		###
		signst = ''
		fnd = xml.find(''.join(['<', tag, '_sign']))
		if fnd >= 0: signst = xml[fnd:]
		###
		signed = ''
		fnd = xml.find(''.join(['</', tag, '_sign']))
		if fnd >= 0: signed = xml[fnd:]
		###
		doced = ''
		fnd = signed.find('>')
		if fnd >= 0: doced = signed[fnd:]
		###
		data['LETTER'] = letterst[0:-len(signst)]
		data['SIGN'] = signst[0:-len(doced)+1]
		###
		rawsignst = ''
		fnd = data['SIGN'].find('>')
		if fnd >= 0: rawsignst = data['SIGN'][fnd:]
		###
		rawsigned = ''
		fnd = rawsignst.find('</')
		if fnd >= 0: rawsigned = rawsignst[fnd:]
		###
		data['RAWSIGN'] = rawsignst[1:-len(rawsigned)]
		###
		return data

class KKBsign(object):

	invert = 0
	ecode = 0
	estatus = None
	private_key = None

	def load_private_key(self, f='', p=None):
		ret = False
		###
		self.ecode = 0
		###
		if os.path.isfile(f):
			with open(f) as wf:
				c = wf.read()
				###
				try:
					ca_key = pki.load_privatekey(pki.FILETYPE_PEM, c, p)
				except Exception, ex:
					self.parse_errors(ex)
					###
					return False
				###
				self.private_key = ca_key
				###
				ret = c
		else:
			self.ecode = 4
			###
			self.estatus = '[KEY_FILE_NOT_FOUND]'
		###
		return ret

	def set_invert(self):
		self.invert = 1

	def parse_errors(self, ex):
		if len(ex.args[0]) > 0:
			if ex[0][2] == 'bad decrypt':
				self.ecode = 3
				self.estatus = 'Bad password read. Maybe empty password.'
			elif ex[0][2] == 'wrong tag':
				self.ecode = 2
				self.estatus = 'Bad decrypt. Verify your Cert password or Cert type.'
			else:
				self.ecode = 255
				self.estatus = ex[0][2][2]
		else:
			self.ecode = 255
			self.estatus = 'Error reading Certificate. Verify Cert type.'

	def reverse(self, s):
		return s[::-1]

	def sign(self, s):
		sign = pki.sign(self.private_key, s, 'sha1')
		###
		if self.invert == 1:
			sign = self.reverse(sign)
		###
		return sign

	def sign64(self, s=''):
		return self.encode64(self.sign(s))

	def encode64(self, s):
		return base64.encodestring(s).replace("\n", '').replace("\r", '').replace("\t", '')

	def decode64(self, s):
		return s.decode('base64')

	def check_sign(self, data, s, f):
		self.ecode = 0
		###
		if self.invert == 1:
			s = self.reverse(s)
		###
		if os.path.isfile(f):
			with open(f) as wf:
				c = wf.read()
				###
				cert = M2Crypto.X509.load_cert_string(c)
				pubkey = cert.get_pubkey()
				pubkey.reset_context(md='sha1')
				pubkey.verify_init()
				pubkey.verify_update(data)
				###
				return M2Crypto.m2.verify_final(pubkey.ctx, s, pubkey.pkey)
			###
			return 0
		else:
			self.ecode = 4
			###
			self.estatus = '[KEY_FILE_NOT_FOUND]'
			###
			return 2
		###
		return 3

	def check_sign64(self, data, s, f):
		return self.check_sign(data, self.decode64(s), f)

class ProcessRequest(KKBsign, ProcessXML):

	def get(self, order_id=0, currency_code='398', amount=0, b64=True):
		if order_id > 0:
			if amount > 0:
				order_id = '%06d' % order_id
				###
				request = {
					'MERCHANT_CERTIFICATE_ID':MERCHANT_CERTIFICATE_ID,
					'MERCHANT_NAME':MERCHANT_NAME,
					'ORDER_ID':order_id,
					'CURRENCY':currency_code,
					'MERCHANT_ID':MERCHANT_ID,
					'AMOUNT':amount,
				}
				###
				self.set_invert()
				###
				if not self.load_private_key(PRIVATE_KEY_FN, PRIVATE_KEY_PASS):
					if self.ecode > 0:
						return self.estatus
				###
				result = self.process_XML(XML_TEMPLATE_FN, request)
				###
				if result:
					result_sign = ''.join(['<merchant_sign type="RSA">', self.sign64(result), '</merchant_sign>'])
					###
					xml = ''.join(['<document>', result, result_sign, '</document>'])
					###
					if (b64):
						return self.encode64(xml)
					else:
						return xml
				else:
					self.estatus = 'Error reading XML template.';
			else:
				self.estatus = 'Nothing to charge'
		else:
			self.estatus = 'Null Order ID'
		###
		return self.estatus

class ProcessResponse(KKBsign, SplitSign, ParserXml):

	def get(self, response):
		result = self.parseString(response)
		###
		if result.get('TAG_ERROR', None) is not None:
			return result
		###
		if result.get('TAG_DOCUMENT', None) is None:
			return '[XML_DOCUMENT_UNKNOWN_TYPE]'
		else:
			self.set_invert()
			###
			data = self.split_sign(response, 'bank')
			###
			check = self.check_sign64(data['LETTER'], data['RAWSIGN'], PUBLIC_KEY_FN);
			###
			if (check == 1):
				data['CHECKRESULT'] = "[SIGN_GOOD]"
			elif (check == 0):
				data['CHECKRESULT'] = "[SIGN_BAD]"
			else:
				data['CHECKRESULT'] = ''.join(["[SIGN_CHECK_ERROR]: ", self.estatus])
		###
		ret = {}
		ret.update(result)
		ret.update(data)
		###
		return ret
