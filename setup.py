from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in qp_invoice_observation/__init__.py
from qp_invoice_observation import __version__ as version

setup(
	name='qp_invoice_observation',
	version=version,
	description='Add observations field in invoice creation opening tool',
	author='MENTUM',
	author_email='aryrosa.fuentes@MENTUM.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
