# PYTEST framework sample

## Installation

make sure you how python3 and installed browser and driver in your machine before executing the tests  
To get started, open terminal and execute this command

```bash
pip install -r requirements.txt -U
```

## Execute tests

This is a BDD pytest framework which is using BDD Gherkin style as an interface

```bash
rm -rf allure-report
allure generate
pytest --alluredir=allure-report/
```

## Alure report

Execute the following commands to show report in browser

```bash
allure serve allure-report/
```

## Code Quality

Black

```bash
black --check .
black **/*.py
```

Flake8

```bash
flake8
```
