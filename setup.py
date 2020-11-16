from setuptools import setup, find_packages

setup(
    name='streak_cal',
    version='0.2',
    author="Kacha Mukabe",
    description="A cli calendar for keeping track of streaks",
    url="https://github.com/kachaMukabe/streak",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Click',
        'tinydb',
        'termcolor',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        streak-cal=streak.streak:cli
    ''',
)