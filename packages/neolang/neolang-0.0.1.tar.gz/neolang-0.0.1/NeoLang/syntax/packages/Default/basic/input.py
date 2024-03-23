def Input(args):
	#? Expressions needs to return actual type like a neo argument ->
	#? hello -> "hello", 21 -> 21, example-expr -> example-expr
	return f'"{input()}"'

def PrefixedInput(args):
	return input(args[0])