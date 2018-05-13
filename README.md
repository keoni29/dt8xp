# Detokenize 8xp
Detokenize 8xp program files for ti8x calculators. Instructions for git integration are included in this readme.

## Dependencies
**ti83f** : Python package for encoding and decoding TI83F files. https://bitbucket.org/keoni29/ti83f

## Installing
```
git clone https://bitbucket.org/keoni29/dt8xp
cd dt8xp
pip install .
```

## How to use
```
dt-8xp -h
usage: dt-8xp [-h] [--xml XML] [-l {basic,axe,grammer,ti84pcse,ti82,ti73}]
              filename

Detokenize calculator programs

positional arguments:
  filename              Input .8xp file.

optional arguments:
  -h, --help            show this help message and exit
  --xml XML             Custom XML file containing tokens.
  -l {basic,axe,grammer,ti84pcse,ti82,ti73}, --lib {basic,axe,grammer,ti84pcse,ti82,ti73}
                        Select a library.
```

## GIT Integration
Use git attribute textconv to show binary 8xp files as text. This works with git log type commands (e.g. show) and git diff. Add the following 
lines to .git/config. 
```
[diff "8xp"]
    textconv = dt-8xp --lib axe
```

Add the following lines to .gitattributes
```
*.8xp	diff=8xp
```

Read more about git attributes: https://git-scm.com/docs/gitattributes

