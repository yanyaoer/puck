from setuptools import setup, find_packages

setup(
    name='puck',
    version='0.0.1',
    author='yanyaoer',
    author_email='yanyaoer@gmail.com',
    url='http://github.com/yanyaoer/puck',
    packages=find_packages(),
    description='puck: a simple tornado package with testing',
    install_requires=[
        'tornado',
    ],
    include_package_data=True,
    entry_points={
      'console_scripts': [
        'puck= puck.main:main',
      ]
    },
    license='WTFPL',
)
