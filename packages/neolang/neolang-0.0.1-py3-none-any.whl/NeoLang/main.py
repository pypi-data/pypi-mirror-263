# Get rid of pycache
import sys
sys.dont_write_bytecode = True

# Utils 
from json import dumps
from os import path, getcwd

# Internal
from NeoLang.syntax import *
from NeoLang.interpreter import *

def Main():
	content = open(f'{path.abspath(getcwd())}/{sys.argv[1]}').read()

	parser = Parser()

	#* Load and feed packages to Parser
	packages = get_packages()
	parser.load_packages(packages)

	#* Tokenize file and feed tokens to Parser
	tokens = tokenize_content(content)
	parser.add_tokens(tokens)

	#? Logging
	#f = open('output.json','w')
	#f.write(dumps(tokens,sort_keys=False, indent=4))

	#* Parse everything
	parser.parse()