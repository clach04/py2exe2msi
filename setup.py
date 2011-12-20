import os, re

from setuptools import setup

from py2exe2msi import __version__ as VERSION

PACKAGE_NAME='py2exe2msi'

setup(
	name 		= PACKAGE_NAME,
	version 	= '.'.join(map(str, VERSION)),
	description	= 'An easy way to create Windows standalone applications in Python',
	author		= 'Artem Andreev',
	author_email = 'just.wow@gmail.com',
	url			= 'http://code.google.com/p/py2exe2msi/',
	packages	= ['py2exe2msi'],
	long_description = '''py2exe2msi is an extension to distutils which creates 
	MSI packages for py2exe-compiled applications''',
	classifiers = [
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Programming Language :: Python',
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Operating System :: Microsoft :: Windows',
	],
	keywords	= 'windows installer msi py2exe executable',
	license		= 'Proprietary License',
	install_requires = [
		'py2exe', 'msilib'
	],
)
#
