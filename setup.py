
from setuptools import setup

setup(
    name="barkcli",
    version="1.0.0",
    py_modules=["barkcli"],
    install_requires=["BarkNotificator"],
    entry_points={
        'console_scripts': [
            'bark = barkcli:main',
        ],
    },
)
