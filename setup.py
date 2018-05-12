from setuptools import setup

setup(name='dt8xp',
      version='0.1',
      description='Detokenize 8xp calculator program files',
      url='',
      author='Koen van Vliet',
      author_email='8by8mail@gmail.com',
      license='MIT',
      packages=['dt8xp'],
      data_files=[
            ('/usr/share/dt8xp/tokens', ['share/tokens/AxeTokens.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/DCS8.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/GrammerTokens.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/NoLib.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/Prizm.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/TI-73.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/TI-82.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/TI-84+CSE.xml']),
            ('/usr/share/dt8xp/tokens', ['share/tokens/Tokens.xml']),
            ],
      entry_points={
            'console_scripts': ['dt-8xp=dt8xp.dt8xp:main']},
      scripts=[
            'bin/dt-axe',
            'bin/diff-axe'],
      zip_safe=False,
      )