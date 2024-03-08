from setuptools import setup, find_packages

setup(
    name='transform-csv',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'transform-csv = transform_csv.transform_csv:transform_csv'
        ]
    },
    author='timofruehwirth',
    author_email='timo.fruehwirth@oeaw.ac.at',
    description='https://github.com/timofruehwirth/py-codespace',
    url='https://github.com/timofruehwirth/py-codespace/blob/main/transform-csv/transform-csv.py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)