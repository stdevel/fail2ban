# This file is part of Fail2Ban.
#
# Fail2Ban is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Fail2Ban is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Fail2Ban; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# Author: Cyril Jaquier
# 
# $Revision: 321 $

__author__ = "Cyril Jaquier"
__version__ = "$Revision: 321 $"
__date__ = "$Date: 2006-09-04 21:19:58 +0200 (Mon, 04 Sep 2006) $"
__copyright__ = "Copyright (c) 2004 Cyril Jaquier"
__license__ = "GPL"

import re, time

class DateTemplate:
	
	def __init__(self):
		self.name = ""
		self.regex = ""
		self.cRegex = None
		self.pattern = ""
		self.hits = 0
	
	def setName(self, name):
		self.name = name
		
	def getName(self):
		return self.name
	
	def setRegex(self, regex):
		self.regex = regex
		self.cRegex = re.compile(regex)
		
	def getRegex(self):
		return self.regex
	
	def setPattern(self, pattern):
		self.pattern = pattern
		
	def getPattern(self):
		return self.pattern
	
	def isValid(self):
		return self.regex != "" and self.pattern != ""
	
	def incHits(self):
		self.hits = self.hits + 1
	
	def getHits(self):
		return self.hits
	
	def matchDate(self, line):
		dateMatch = self.cRegex.search(line)
		return dateMatch
	
	def getDate(self, line):
		raise Exception("matchDate() is abstract")
