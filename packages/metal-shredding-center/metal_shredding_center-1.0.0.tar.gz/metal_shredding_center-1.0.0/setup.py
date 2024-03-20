
'''
	not sure if this works:
		[xonsh] docker run -v .:/metal_shredding_center -v /dev/sdc:/dev/sdc -it 2a1fe906ce18 /bin/bash

	pip install --upgrade setuptools

	(rm -rf dist && python3 -m build && twine upload dist/*)
'''

'''
	tags:
		#forget
'''

#
#	https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#
#	https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py
#
from setuptools import setup, find_packages

version = "1.0.0"
name = 'metal_shredding_center'
install_requires = [
	'volts',

	'shares',
	'ships',
	
	'flask',
	'jsonschema',
	'rich'
]

def scan_description ():
	try:
		with open ('structures/modules/metal_shredding_center/metal_shredding_center.s.HTML') as f:
			return f.read ()

	except Exception as E:
		pass;
		
	return '';


setup (
    version = version,

	name = name,
    install_requires = install_requires,	
	
	package_dir = { 
		'metal_shredding_center': 'structures/modules/metal_shredding_center'
	},
	scripts = [ 
		'structures/scripts/metal_shredding_center' 
	],
	
	include_package_data = True,
	package_data = {
		"": [ "*.HTML" ]
    },
	
	license = "CL",
	long_description = scan_description (),
	long_description_content_type = "text/plain",
)
