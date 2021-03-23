from setuptools import setup

setup(
    name='dokimi',
    version='0.1',
    py_modules=['dokimi'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dokimi=dokimi:cli
    ''',
)
