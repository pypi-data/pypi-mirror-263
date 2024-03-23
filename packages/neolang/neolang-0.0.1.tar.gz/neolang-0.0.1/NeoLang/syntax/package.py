from json import loads
from sys import path as syspath
from NeoLang.syntax.parser import Parser

class Package:
	def __init__(self, path):
		infof = ''
		try:
			infof = open(f'{path}/package-info.json').read()
		except:
			print(f'ERROR LOADING PACKAGE - NO PACKAGE INFO FOUND: {path}')
			return
		
		info = loads(infof) # info = json loaded package-info.json
		
		self.name = info['name']
		self.description = info['description']	
		self.requirements = info['requirements']
		
		syspath.append(path)

		#* Turn effects from dict to Parser and put into list
		effects = []
		for effect in info['effects']:
			parser = effect['parser']
			exec(f'from {effect["filePath"]} import {parser}')
			effects.append(Parser(
				parser = eval(parser),
				patterns = effect['patterns']
			))
		self.effects = effects

		#* The same with expressions
		expressions = []
		for expression in info['expressions']:
			parser = expression['parser']
			exec(f'from {expression["filePath"]} import {parser}')
			expressions.append(Parser(
				parser = eval(parser),
				patterns = expression['patterns'])
			)
		self.expressions = expressions