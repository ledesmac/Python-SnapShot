from setuptools import setup

setup(
    name='snappy-3000',
    version='0.1',
    author="Alex Ledesma",
    author_email="alex.ledesma7@gmail.com",
    description="Snappy-3000 is a tool to " +
        "automate the creation of snapshots in your AWS environment",
    license="GPLv3+",
    packages=['snappy'],
    url='https://github.com/ledesmac/Python-SnapShot',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.snappy:cli
        '''
)
