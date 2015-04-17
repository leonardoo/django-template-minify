import os
from setuptools import setup, find_packages

template_min = __import__('template_minify')

install_requires = ['html_minifier']

setup(
      name='django-template-minify',
      version=template_min.get_version(),
      description='A Template render for minify templates',
      author='Leonardo Orozco',
      url='https://github.com/leonardoo/django-engine-minify/',
      packages = find_packages(),
      install_requires=install_requires,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
     )