from setuptools import setup

setup(name='dt8xp',
      version='0.2',
      description='Detokenize 8xp calculator program files',
      url='',
      author='Koen van Vliet',
      author_email='8by8mail@gmail.com',
      license='MIT',
      packages=['dt8xp'],
      install_requires=['ti83f<=0.9'],
      include_package_data=True,
      entry_points={
            'console_scripts': ['dt-8xp=dt8xp.dt8xp:main']},
      scripts=[
            'bin/dt-axe',
            'bin/diff-axe'],
      zip_safe=False,
      )