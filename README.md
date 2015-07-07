# XBRL US Data Quality Committee Rules

dqc_us_rules is a plugin for Arelle that contains the agreed upon set of rules for the XBRL US Data Quality Committee

## dqc_us_rules contains:

* The agreed upon rules as set forth by the members of the XBRL US Data Quality Committee
* Reference implementation of the agreed upon rules, using Arelle as an XBRL processor.
* Unit tests for the reference implementation

## Deployment

* Deploy with Arelle
* Specify the sec directory as a plugin with Arelle

### Requirements

* Python 3.x (3.2 or greater is preferred)
* Git 1.7+
* C compiler toolchain (for LXML)
* libxml2 (also for LXML)
* Arelle

## Development

It is strongly recommended that one uses a python virtual environment, such as [virtualenv](http://www.virtualenv.org/en/latest/), to do development.  To make development and management of virtual environments easier, we recommend checking out [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).

The rest of this setup will assume you have installed [virtualenv](http://www.virtualenv.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper).

### Creating a virtual environment

To create a virtual environment, change your directory to the root of this project, and execute the following command:
    
    mkvirtualenv dqc -a $PWD -p <path_to_python3>

This will give you a virtual environment that you can then work within by inputting

    workon dqc

any time you need to work in it.

### Installing dependencies

To install the dependencies for development of only the DQC ruleset, you will use [pip](https://pip.pypa.io/en/latest/installing.html) to install the requirements.  We will install Arelle as a package first

    pip intall -r arelle-requirements.txt

When that is finished, we will then install the remainder of the development requirements

    pip install dev-requirements.txt

### Running unit tests

To run the unit tests, simply run the included shell script

    ./run-unit-tests.sh

## Rule Index

The rule definition index is [here](docs/README.md).

## Change Management

We actively accept, and encourage, pull requests for code changes.  An explanation of what the change is for, and why, is required, and the request will be reviewed by the technical leads of the project.  If the request is accepted, it will be merged into the master branch.  If it is found to be missing something, or incomplete, commments will be noted regarding the missing or incomplete pieces.

To propose new rules, you can submit requests through the [Data Quality Committee](Link Here).