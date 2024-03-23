

from setuptools import setup, find_packages

def readme():
  with open('README.md',  encoding='utf-8', mode ='r') as f:
    return f.read()

setup(
  name='postfixcalc_advanced',
  version='0.1',
  author='wolkolak1',
  author_email='e.a.z.y.machining@gmail.com',
  description='Tokeniztion, posfixing and postfix calculation',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/wolkolak/postfixcalc',
  packages=find_packages(),#['token_posfix_calculation'],
  install_requires=['requests>=0.0'],
  classifiers=[
	'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Build Tools',
    'Operating System :: OS Independent'
  ],
  keywords='python algorithm postfix calculation',
  project_urls={
    #'Documentation': 'link'
  },
)