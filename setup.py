from setuptools import setup

setup(
    name = 'scdr',
    packages=['scdr'],
    license='GNU GPL 2.0',
    install_requires=['lxml', 'colorama'],
    requires=['lxml', 'colorama'],
    scripts=['bin/define']
)
