from NeoLang.interpreter.operator import Operator
from NeoLang.interpreter.tokenizer import str_to_type

class Parser:
	def __init__(self, packages = [], tokens = []) -> None:
		self.packages = packages
		self.tokens = tokens
	def parse_expr(self,token):
		#* Parse expression and return output of expression'
		pattern = token['pattern']
		for package in self.packages:
			for expression in package.expressions:
				if pattern in expression.patterns:
					args = []
					for arg in token['args']:
						args.append(self.parse_args(arg))
					
					result = str_to_type(expression.parser(args))
					return result	
		#! NO EXPRESSION FOUND - THROW ERROR
		print('no expr')

	def parse_args(self,args):
		#* Parse arguments and return result of arguments
		
		clean_args = [] #? List containing args where expressions have been parsed

		for arg in args:
			if arg['type'] == 'EXPRESSION':
				clean_args.append(self.parse_expr(arg))
			else:
				clean_args.append(arg)
		
		stripped_args = [] #? List containing args where the datatypes is clarified (dict -> str/int/etc)

		for arg in clean_args:
			match arg['type']:
				case 'TEXT':
					stripped_args.append(str(arg['value']))
				case 'NUMBER':
					stripped_args.append(float(arg['value']))
				case 'OPERATOR':
					stripped_args.append(Operator(arg['value']))
				case _:
					pass #! NOT VALID DATATYPE - PRINT ERROR
		
		pattern = [] #? List containing datatypes excluding operators to figure out how to handle merging args (['hello', Operator('+'), 21] -> [str,float])
		operators = [] #? List containing all operators
		values = [] #? List containing all values

		for arg in stripped_args:
			if isinstance(arg,str):
				pattern.append(str)
				values.append(arg)
			elif isinstance(arg,float):
				pattern.append(float)
				values.append(arg)
			elif isinstance(arg,Operator):
				operators.append(arg)

		if len(pattern) == 1:
			return values[0]
		
		i = 1
		result = values[0]

		while i <= len(pattern) - 1:
			if float and str in (pattern[0], pattern[i]):
				result = str(result) + str(values[i])
			elif float and float in (pattern[0], pattern[i]):
				result = eval(f'{result} {operators[0]} {values[i]}')
			elif str and str in (pattern[0], pattern[i]):
				result = result + values[i]
			operators.pop(0)
			i += 1
		return result

	def parse_effect(self, token):
		'Parse and run effect'
		pattern = token['pattern']
		for package in self.packages:
			for effect in package.effects:
				if pattern in effect.patterns:
					args = []
					for arg in token['args']:
						args.append(self.parse_args(arg))
					return effect.parser(args)
		#! NO EFFECT FOUND - THROW ERROR
		print('no effect')


	def parse(self):
		for token in self.tokens:
			if token['type'] == 'EFFECT':
				self.parse_effect(token)

	def load_packages(self, packages):
		self.packages.extend(packages)
	
	def add_tokens(self, tokens):
		self.tokens.extend(tokens)