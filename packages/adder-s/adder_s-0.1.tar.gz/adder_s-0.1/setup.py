from setuptools import setup, find_packages
setup(
    name='adder_s',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
      [console_scripts]
      adder_s=adder_s.example:hello
      ''',
)
