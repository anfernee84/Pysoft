from setuptools import setup, find_namespace_packages


setup(name='CLI_bot',
      version='1',
      description='Personal assistant',
      url='https://github.com/rostykpython/Python_Project_CLI',
      author='Rostyslav Lytvynets\nLesya Fedorenko\nEd Rogulin\nIvan Grigoriev',
      author_email='rostislavlitvinets@gmail.com',
      packages=find_namespace_packages(),
      install_requires=['click', 'pathlib', 'fuzzywuzzy', 'datetime', 'pathlib'],
      entry_points={'console_scripts': ['bot = CLI_project.main:main']}
      )
