from distutils.core import setup
from Emailer.__init__ import __version__

setup(
name = 'Emailer',
version = __version__,
packages = ['Emailer'],
author_name = 'Jacob Renn',
author_email = 'jwrenn4@outlook.com',
description = 'Single Python object for sending emails',
long_description = open('README.md','r').read()
)
