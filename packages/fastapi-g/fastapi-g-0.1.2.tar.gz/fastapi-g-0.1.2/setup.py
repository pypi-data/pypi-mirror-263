from setuptools import setup, find_packages
from setuptools.command.install import install
import sys
from pathlib import Path

class CustomInstall(install):
    user_options = install.user_options + [
        ('project_name=', None, 'Name of the project'),
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.project_name = None

    def finalize_options(self):
        install.finalize_options(self)

    def run(self):
        install.run(self)

def get_project_name():
    for arg in sys.argv:
        if arg.startswith('--project_name='):
            return arg.split('=')[1]
    return 'fastapi-g'

# read the contents of your README file

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=get_project_name(),
    version='0.1.2',
    author='Ashary Gartanto',
    author_email='ashary.gartanto@gmail.com',
    # description='CLI generator tool for FastAPI Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fastapi-g = fastapi_g.main:main'
        ]
    },
    install_requires=[
        'pydantic',
        'fastapi',
        'tqdm'
    ],
    cmdclass={'install': CustomInstall},
)
