from setuptools import setup, find_packages
from MIRACLEpy.units import default_general

setup(
	name=default_general["name"],
	version=default_general["version"],
	author=default_general["author"],
	author_email=default_general["contact"],
	description=default_general['description'],
	url='https://github.com/JinWookArgon/MIRACLEpy',
        package_data={'MIRACLEpy': ['Data/Lengthlist_Reference_normal.txt', 'Data/Training_data.txt', 'Data/Invariable_Microsatellite_information.bed']},
	keyword='MSI, RNA-seq, Length variation',
	license='MIT License',
	packages=find_packages(),
	install_requires=['pandas>=0.25', 'pysam>=0.15', 'scikit-learn>=0.21'],
	python_requires='>=3.6',
	entry_points={'console_scripts': ['MIRACLE = MIRACLEpy.main:main']},
)
