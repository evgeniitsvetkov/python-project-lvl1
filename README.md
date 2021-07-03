# Brain Games

[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Python package](https://github.com/evgeniitsvetkov/python-project-lvl1/actions/workflows/python-package.yml/badge.svg)](https://github.com/evgeniitsvetkov/python-project-lvl1/actions/workflows/python-package.yml)


## Five games to make your brain work

1. Brain Even. Find odd or even number
2. Brain Calc. Are you good at calculus?
3. Brain GCD. Do you know Euclidean algorithm?
4. Brain Progression. Find the missing number
5. Brain Prime. Prime numbers and where to find them

[![asciicast](https://asciinema.org/a/iMkymRTilwuba7wPXaGCXGacb.svg)](https://asciinema.org/a/iMkymRTilwuba7wPXaGCXGacb)


## Usage

Install the dependencies using Make and Poetry

```bash
make install
```

Run a game

```bash
make brain-even (brain-calc, brain-gcd, brain-progression, brain-prime)
```

Make a python package

```bash
make build
```

Install Brain Games package on your OS

```bash
make package-install
```

Run a game from your OS

```bash
brain-even (brain-calc, brain-gcd, brain-progression, brain-prime)
```


## Contribution

Check your style using Flake8

```bash
make lint
```

Publish package in PyPi (Dry run)

```bash
make publish
```
