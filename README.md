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

## Rule Index

The rule definition index is [here](docs/README.md).

## Change Management

We actively accept, and encourage, pull requests for code changes.  An explanation of what the change is for, and why, is required, and the request will be reviewed by the technical leads of the project.  If the request is accepted, it will be merged into the master branch.  If it is found to be missing something, or incomplete, commments will be noted regarding the missing or incomplete pieces.

To propose new rules, you can submit requests through the [Data Quality Committee](Link Here).