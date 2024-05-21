from setuptools import setup, find_packages

setup(
    name='StashExtract_GUI',
    version='0.1',
    packages=find_packages(),
    description='StashExtract_GUI is a way to extract Stash data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='EdEquinox',
    author_email='jmarquesnox@gmail.com',
    url='https://github.com/EdEquinox/StashExtract_GUI',
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