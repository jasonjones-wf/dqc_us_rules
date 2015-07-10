# XBRL US Data Quality Committee Rules

dqc_us_rules is a plugin for Arelle that contains the agreed upon set of rules for the XBRL US Data Quality Committee

## dqc_us_rules contains:

* The agreed upon rules as set forth by the members of the XBRL US Data Quality Committee
* Reference implementation of the agreed upon rules, using Arelle as an XBRL processor.
* Unit tests for the reference implementation
* A [rule definition index](docs/README.md)

## Contributions and Feedback

The [Data Quality Committee](http://xbrl.us/home/data-quality/committee/) encourages contributions and feedback to this ruleset.

If you have feedback about the rules themselves, please use the [Data Quality Committee public review site](http://publicreview.xbrl.us) to comment.

The implementation of these rules is an iterative process.  The [master branch](https://github.com/DataQualityCommittee/dqc_us_rules) represents the current state, but we expect to improve the implementation via incremental changes.  This repo contains a [history](https://github.com/DataQualityCommittee/dqc_us_rules/commits/master) of all changes made.

If you have feedback or contributions to the implementation of the rules we encourage code contributions via [pull request](https://github.com/DataQualityCommittee/dqc_us_rules/pulls) or you can submit a github [issue](https://github.com/DataQualityCommittee/dqc_us_rules/issues) to this repo. 

Please provide an explanation of the purpose and need of the change in your PR or Issue.  [@andrewperkins-wf](https://github.com/andrewperkins-wf) and [@hermfischer-wf](https://github.com/hermfischer-wf) will review pull requests for code improvements and fixes on github.  However, substantive rule changes and new rules must be routed to the [Committee](http://xbrl.us/home/data-quality/committee/) for approval before any code can be incorporated into the ruleset.

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
