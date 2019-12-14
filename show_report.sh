#!/bin/bash

PACKAGE_NAME=leetcode_problems
pycodestyle ${PACKAGE_NAME} tests
pylint ${PACKAGE_NAME}
mypy ${PACKAGE_NAME} tests
coverage run --source ${PACKAGE_NAME} -m unittest discover -s tests/
coverage report -m
cloc ${PACKAGE_NAME}
