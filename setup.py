from setuptools import setup

setup(
    name='jsoe',
    version='1.0',
    py_modules=['jsoe'],
    install_requires=[
        'Click',
        'jsonschema'
    ],
    entry_points='''
        [console_scripts]
        jsoe=jsoe:parse_json
    '''
)
