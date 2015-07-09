from paver.easy import task, sh, needs
from paver.setuputils import setup

setup(
    name = 'scdr',
    packages=['scdr'],
    license='GNU GPL 2.0',
    install_requires=['lxml', 'colorama'],
    requires=['lxml', 'colorama'],
    scripts=['bin/define']
)

@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    pass
