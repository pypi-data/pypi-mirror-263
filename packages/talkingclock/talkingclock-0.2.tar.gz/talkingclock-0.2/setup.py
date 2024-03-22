from setuptools import setup, find_packages

setup(
    name='talkingclock',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'talkingclock': ['mp3/*'],
    },
    install_requires=[
        'playsound',
    ],
)
