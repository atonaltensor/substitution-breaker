from collections import defaultdict
import re

class substitution_breaker():
	def __init__(self):
		self.version = 0.1
	#make lowercase and strip out all non-alpha characters
	def strip(self, plaintext):
		return re.sub(r'[^a-zA-Z]','',plaintext.lower())
	
	#provide key = 'qwertyu...'
	def generate_keydict(self, key):
		self.encode_dict = defaultdict()
		i = 0
		for each in key:
			self.encode_dict[i] = each
			i += 1
		#encode_dict = {0: x, 1: h, ...}
			
		self.decode_dict = {v: k for k, v in self.encode_dict.items()}
		#decode_dict = {x: 0, ...}

	def decode(self, ciphertext, key):
		self.generate_keydict(key)
		plaintext = ''
		for each in ciphertext:
			plaintext += chr(self.decode_dict[each]+97) #unicode a <--> 0
		return plaintext

	def encode(self, plaintext, key):
		self.generate_keydict(key)
		plaintext = self.strip(plaintext)
		ciphertext = ''
		for each in plaintext:
			ciphertext += self.encode_dict[ord(each)-97] #unicode a <--> 0
		return ciphertext

	def attack(self):
		return