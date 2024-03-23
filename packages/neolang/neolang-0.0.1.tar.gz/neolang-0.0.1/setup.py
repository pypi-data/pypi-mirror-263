from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.read().splitlines()

with open('README.md') as f:
	description = f.read()

setup(
	name='neolang',
	version='0.0.1',
	packages=find_packages(),
	install_requires=requirements,
	author='Sv3ks',
	author_email='snorre@silkjaer.dk',
	description='The Interpreter for the Neo Programming Language',
	long_description=description,
	long_description_content_type='text/markdown',
	url='https://https://github.com/NeoLangTeam/NeoLang',
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Education',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python',
		'Topic :: Software Development',
		'Operating System :: OS Independent'
	],
	license='GPLv3',
	keywords='programming-language language interpreter scripting syntax', #* totally not made by chatgpt ;)
	project_urls={
		'Documentation': 'https://your-package-name.readthedocs.io/',
		'Source': 'https://github.com/NeoLangTeam/NeoLang',
		'Tracker': 'https://github.com/NeoLangTeam/NeoLang/issues',
	},
	python_requires='>=3.10',
	platforms=['any'],
	include_package_data=True,
	zip_safe=False,
	entry_points={
		'console_scripts': [
			'neo = NeoLang:Main',
		],
	},
)