from paver.easy import task, sh, needs
from paver.setuputils import setup

setup(
    name = 'scdr',
    packages=['scdr'],
    license='GNU GPL 2.0',
    install_requires=['lxml', 'colorama', 'autocorrect'],
    requires=['lxml', 'colorama', 'autocorrect'],
    scripts=['bin/define']
)

@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    pass

@task
def flake8():
    sh('flake8 bin/define scdr/ --max-line-length=120 --max-complexity=10')

@task
def pep8():
    sh('pycodestyle --max-line-length=120 bin/define scdr/')

@task
@needs('flake8', 'pep8')
def lint():
    pass
