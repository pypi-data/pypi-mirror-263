from setuptools import setup, find_packages

setup(
    name='nahcrofDB',
    version='1.1.2',
    py_modules=['nahcrofDB'],
    author='Tyrae Paul',
    author_email='tyraepaul@gmail.com',
    install_requires=["requests"],
    description='nahcrofDB is a simple key-value database solution allowing for fast and easy data storage',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/scuzzles/nahcrofDB/',
    python_requires='>=3.6',
)
