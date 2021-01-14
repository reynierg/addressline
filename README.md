Address line parser

- [DESCRIPTION](#description)
- [SOLUTION](#solution)
- [DEV-DEPENDENCIES](#dev-dependencies)  
- [RUN](#run)
- [OPTIONS](#options)
- [EXAMPLES](#examples)
- [RUN-TESTS](#run-tests)

# DESCRIPTION

An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for the street name and street number.

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

1. Write a simple program that does the task for the simplest cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

# SOLUTION

It requires the Python interpreter, version 3.6+, and is not platform specific. It should work on Unix, 
on Windows or on macOS.\
The solution being used tries to extract the Street name and house number using regular expressions.\
Are being used 3 different regular expressions to try to extract the corresponding address components.\
They are evaluated one at a tame, and when one regex matches against the input address line, it's not necessary 
continue evaluating the ones that have not been used yet:

## Regex I

`^(?P<street>[a-zA-ZäöüÄÖÜẞß]+(?:(?:\s|-)[a-zA-ZäöüÄÖÜẞß]+)*\.?)\,?\s(?P<number>(?:(?:\d)+\s?[a-zA-Z]{0,1})|(?:\d+\s?-\s?\d+))$`

It will match addresses with the following format between others:
- Winterallee 3
- Musterstrasse 45
- Blaufeldweg 123B
- Am Bächle 23
- Auf der Vogelwiese 23 b
- Lange Str. 8
- Königsbrücker Str. 21 - 29
- Karl-Weysser-Str. 9
- Calle Aduana, 29

## Regex II

`^(?P<number>[\d]+),?\s(?P<street>[a-zA-Z]+(?:\s[a-zA-Z]+)*)$`

It will match addresses with the following format between others:
- 4, rue de la revolution
- 200 Broadway Av

## Regex III

`^(?P<street>.+\d+)\s(?P<number>(?:No|no|nr|Nr)\.?\s\d+\s?[a-zA-Z]?)$`

It will match addresses with the following format between others:
- Calle 39 No 1540
- Calle 39 Nr. 1540  

# DEV-DEPENDENCIES

For development purpose, source code quality analysis, detection of error and for running tests, 
the following dependencies are required:

- tox
- flake8
- pylint
- mypy
- pydev

# RUN
Clone the project executing the following command in a terminal:\
`git clone https://github.com/reynierg/addressline.git`

Move to the project directory using:\
`cd addressline`

Execute the following:\
`python3 bin/addressline.py [OPTIONS] ADDRESS_LINE`

# OPTIONS
    -h, --help                  Print this help text and exit
    -v, --verbose               Display verbose information about the proram execution

# EXAMPLES
I- Parse the address "Königsbrücker Str. 21 - 29":\
`python bin/addressline.py 'Königsbrücker Str. 21 - 29'`
  
Output:
```
A regular expression matched the specified address line
Output: {'street': 'Königsbrücker Str.', 'housenumber': '21 - 29'}
```

II- Parse the address "4, rue de la revolution":\
`python bin/addressline.py '4, rue de la revolution'`
  
Output:
```
A regular expression matched the specified address line
Output: {'street': 'rue de la revolution', 'housenumber': '4'}
```

# RUN-TESTS

For run the tests, first will be needed to install the development requirements:
## Create and activate a virtual environment
Being in the project directory, execute the following commands:
```
python3 -m venv venv
. venv/bin/activate
```

## Install the development dependencies
`pip install -r dev-requirements.txt`

## Run the tests
Once installed the dependencies, is only necessary to execute "tox", and it will take care of run 
"flake8", "pylint", "mypy" and the tests using "pytest":\
`tox`
