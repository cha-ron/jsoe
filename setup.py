from setuptools import setup

setup(
    name='jsoe',
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
