# Detokenize 8xp
Detokenize 8xp AXE program files for ti8x calculators. Instructions for git integration are included in this Readme.

Read more about the AXE parser project: https://www.omnimaga.org/the-axe-parser-project/

## Installing
```
git clone https://bitbucket.org/keoni29/dt8xp
cd dt8xp
pip install .
```

## Dependencies
**ti83f** :
Python package for encoding and decoding TI83F files.
https://bitbucket.org/keoni29/ti83f

## GIT Integration
Use git attribute textconv to show binary 8xp files as text. This works with git log type commands (e.g. show) and git diff. Add the following 
lines to .git/config. 
```
[diff "8xp"]
    textconv = dt-axe
```

Add the following lines to .gitattributes
```
*.8xp	diff=8xp
```

Read more about git attributes: https://git-scm.com/docs/gitattributes



## Using stand alone
Detokenize an AXE program
```
dt-axe FILE
```

Compare two AXE programs
```
diff-axe FILE
```

Detokenize a BASIC program

```
dt8xp --xml /usr/share/dt8xp/tokens/NoLib.xml FILE
```
