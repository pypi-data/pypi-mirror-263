from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
  name='pyaiolava',
  version='0.1.0',
  author='kesevone',
  author_email='kesevone@gmail.com',
  description='Asynchronous library for working with Business Lava API. Creating invoices, checking balances and more.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/kesevone/aiolava',
  packages=find_packages(),
  install_requires=['aiohttp>=3.9.3', "pydantic>=2.6.4"],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='lava aiolava lavaapi businesslava pyaiolava',
  project_urls={
    'Official documentation': 'https://dev.lava.ru/business',
  },
  python_requires='>=3.10'
)