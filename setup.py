from setuptools import setup

setup(
    name='python-json',
    version='1.0',
    py_modulesa=['python_json'],
    install_requires=[
        'Click',
        'jsonschema'
    ],
    entry_points='''
        [console_scripts]
        python_json=python_json:parse_json
    '''
)
