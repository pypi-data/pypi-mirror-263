from re import match

def extract_pattern(tokens):
	pattern = ''

	for token in tokens:
		if isinstance(token,str):
			pattern += token
		else:
			pattern += '$'

	return pattern

def extract_args(tokens):
	args = []

	for token in tokens:
		if isinstance(token,list):
			args.append(token)

	return args

def clean_arr(arr):
	cleaned_arr = []
	for item in arr:
		if isinstance(item,list):
			cleaned_arr.append(clean_arr(item))
		elif not item == '': # and not item == ' '
			cleaned_arr.append(item)
	
	return cleaned_arr

def str_to_type(string):
	type = ''
	value = ''

	if string.startswith('"'):
		if string.endswith('"'):
			type = 'TEXT'
			value = string.removeprefix('"').removesuffix('"')
		else:
			print('ERROR - TEXT IS MISSING END QUOTE')
	elif string in '+-*/':
		type = 'OPERATOR'
		value = string
	elif match(r'[\d+.]+',string) or match(r'-[\d+.]+',string): #? Could also be r'[0-9.]+'?
		type = 'NUMBER'
		value = string
	elif match(r'[a-zA-Z ]+',string):
		type = 'NAME'
		value = string
	else:
		print('ERROR: COULDT NOT DETECT ANY TYPE FROM STRING')
	return { 'type': type, 'value': value}

def str_to_type_from_arr(arr):
	result = []
	for item in arr:
		if isinstance(item,str):
			result.append(str_to_type(item))
		else:
			result.append(str_to_type_from_arr(item))
	return result

def extract_simple_tokens(dicted_tokens):
	simple_tokens = []

	for token in dicted_tokens:
		if isinstance(token,dict):
			simple_tokens.append(token['value'])
		else:
			simple_tokens.append(token)
	
	return simple_tokens

def get_expression(content):
	simple_token = extract_simple_tokens(content)

	pattern = extract_pattern(simple_token)
	args = extract_args(simple_token)

	return {'type':'EXPRESSION', 'pattern': pattern, 'args': args}


def define_expressions(tokens):
	result = []
	in_expr = False

	temp_list = []
	temp_str = ''

	for token in tokens:
		if isinstance(token,dict):
			if token['type'] == 'NAME':
				if not in_expr:
					in_expr = True
				temp_str += token['value'] + ' '
			else:
				if in_expr:
					temp_list.append(temp_str)
					result.append(temp_list)
					temp_str = ''
					temp_list = []
				result.append(token)

		elif isinstance(token,list):
			if in_expr:
				temp_list.append(temp_str)
				temp_str = ''
			else:
				in_expr = True
			temp_list.append(define_expressions(token))

	temp_list.append(temp_str.removesuffix(' '))
	result.append(temp_list)

	result = clean_arr(result)


	# Make strings names (idk)
	for item in result:
		item_index = result.index(item)
		if isinstance(item,list):
			for value in item:
				if isinstance(value,str):
					index = result[item_index].index(value)
					result[item_index].pop(index)
					result[item_index].insert(index,{'type':'NAME', 'value':value})

	# Convert lists (not yet defined expressions ig) to formatted expressions
	for token in result:
		if isinstance(token,list):
			index = result.index(token)
			result.pop(index)
			result.insert(index,get_expression(token))

	#* Finally, clear result for expression(s) with emtpy patterns 
	for token in result:
		if token['type'] == 'EXPRESSION' and token['pattern'] == '':
			result.pop(result.index(token))

	return result

def tokenize(content):
	chars = list(content)
	result = "['"

	quotes = 0
	in_par = 0

	for char in chars:
		if char == '"':
			quotes += 1
		if quotes % 2:
			in_quotes = True
		else:
			in_quotes = False
		
		if char == '(' and not in_quotes:
			result += "',['"
			in_par += 1
		
		elif char == ')' and not in_quotes:
			result += "'],'"
			in_par -= 1

		elif char == ' ' and not in_quotes and in_par >= 1:
			result += "','"

		else:
			result += char

	result += "']"
	result = eval(result)

	# Clean the list for empty strings ('')

	result = clean_arr(result)

	pattern = extract_pattern(result)
	args = extract_args(result)

	# Tokenizing args

	args = str_to_type_from_arr(args)

	# Merging names into expressions

	temp = []
	for arg in args:
		temp.append(define_expressions(arg))
	args = temp

	result = {'type': 'EFFECT', 'pattern': pattern, 'args': args}

	# Return tokenized content
	return result

def tokenize_content(content):
	tokens = []
	for line in content.split('\n'):
		tokens.append(tokenize(line))
	return tokens