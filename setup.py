from setuptools import setup, find_packages

setup(
    name="loberia-identity-shield",
    version="1.0.0",
    author="XL0b3r14X",
    description="Universal metadata purger and system trace cleaner by Loberia Tactical Group",
    packages=find_packages(),
    install_requires=[
        'Pillow>=10.0.0',
    ],
    entry_points={
        'console_scripts': [
            'loberia-shield=core.sentinel:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
