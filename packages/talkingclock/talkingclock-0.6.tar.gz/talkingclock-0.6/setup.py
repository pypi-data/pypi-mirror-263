from setuptools import setup, find_packages

setup(
    name='talkingclock',
    version='0.6',
    packages=find_packages(where="src"),
    include_package_data=True,
    package_dir={"":"src"}, 
    package_data={
        'talkingclock': ["*.txt","*.ics","mp3/*.mp3"],
    },
    install_requires=[
        'playsound',
    ],
)
