from setuptools import setup
from relion2dynamo import __version__
setup(
    name='relion2dynamo',
    version=__version__,
    packages=['relion2dynamo'],
    url='https://github.com/EuanPyle/relion2dynamo',
    license='BSD',
    author='epyle',
    author_email='euanpyle@gmail.com',
    description='Convert data.star to Dynamo Table',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'click',
        'starfile',
        'dynamotable',
        'eulerangles'
    ],
    entry_points='''
        [console_scripts]
        relion2dynamo=relion2dynamo.relion2dynamo:cli
    ''',
)
