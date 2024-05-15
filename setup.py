from setuptools import setup, find_packages

setup(
    name='MusicBoard_GUI',
    version='0.1',
    packages=find_packages(),
    description='MusicBoard GUI is a way to extract MusicBoard data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='EdEquinox',
    author_email='jmarquesnox@gmail.com',
    url='https://github.com/EdEquinox/MusicboardExtract_GUI',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'time',
        'customtkinter',
        'PIL',
        'tkinter',
        'csv',
        'os',
        'threading',
    ],
)