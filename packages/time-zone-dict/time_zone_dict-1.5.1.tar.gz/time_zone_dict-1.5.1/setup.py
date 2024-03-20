from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='time_zone_dict',
  version='1.5.1',
  author='z1kurat',
  author_email='novorozhbitov@mail.com',
  description='Time Zone dict',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/z1kurat/Time-Zone-dict-for-python',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
      'Programming Language :: Python :: 3.11',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent'
  ],
  keywords='time time_zone zone python dict',
  project_urls={
      'Source': 'https://github.com/z1kurat/Time-Zone-dict-for-python',
      'Tracker': 'https://github.com/z1kurat/Time-Zone-dict-for-python/issues'
  },
  python_requires='>=3.7'
)
