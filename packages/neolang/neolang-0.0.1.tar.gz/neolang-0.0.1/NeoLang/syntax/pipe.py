 #* Pipe between packages and interpreter

from os import listdir, path
from NeoLang.syntax.package import Package

def get_packages():
	packages = []

	 #* Path thingy gets the path of the directory this file is in.
	 #? For more info, read https://stackoverflow.com/a/3430395/15400585 - it helped me out a lot!
	dir = f'{path.dirname(path.abspath(__file__))}/packages'
	for package in listdir(dir):
		packages.append(Package(f'{dir}/{package}'))
	
	return packages