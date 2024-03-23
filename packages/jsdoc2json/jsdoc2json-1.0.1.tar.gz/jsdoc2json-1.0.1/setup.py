from setuptools import setup, find_packages

setup(
    name='jsdoc2json',
    version='1.0.1',
    description='A Python tool for Game Maker developers to convert JSDoc comments from GML files to JSON.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Nicolas Dejean',
    author_email='nicolasdejean@laposte.net',
    url='https://github.com/Cooleure/jsdoc2json',
    license='MIT',
    packages=find_packages(),
    package_data={'jsdoc2json': ['*.md'], 'jsdoc2json.modules': ['*.py']},
    entry_points={
        'console_scripts': [
            'jsdoc2json = jsdoc2json.main:convert_command_line',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
