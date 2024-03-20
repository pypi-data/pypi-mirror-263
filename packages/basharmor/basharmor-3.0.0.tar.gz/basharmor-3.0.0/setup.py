from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import stat

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        shutil.copy('.load', '/usr/bin/.load')
        shutil.copy('basharmor', '/usr/bin/basharmor')
        os.chmod('/usr/bin/.load', stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        os.chmod('/usr/bin/basharmor', stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

setup(
    name='basharmor',
    version='3.0.0',
    description='Bash Armor is a tool to encryption bash scripts with armor',
    long_description='basharmor adalah tools untuk melakukan enkripsi pada file bash. Ini cocok digunakan pada sistem operasi Ubuntu 20.04.',
    url='https://github.com/Azigaming404',
    author='Aji permana',
    author_email='ajip51517@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    cmdclass={'install': CustomInstallCommand}
)
