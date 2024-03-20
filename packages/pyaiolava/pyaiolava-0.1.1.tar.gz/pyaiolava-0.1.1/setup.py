from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
  name='pyaiolava',
  version='0.1.1',
  author='kesevone',
  author_email='kesevone@gmail.com',
  description='Simple and convenient asynchronous library for working with the Business Lava API.',
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
  keywords='lava aiolava lavaapi pyaiolava businesslava',
  project_urls={
    'Official documentation': 'https://dev.lava.ru/',
  },
  python_requires='>=3.10'
)