[![Build Status](https://travis-ci.com/dcs4cop/xcube-gen-vito.svg?branch=master)](https://travis-ci.com/dcs4cop/xcube-gen-vito)


# xcube-gen-vito

This is a plugin for xcube which can be used for processing inputdata provided by RBINS. 
With xcube-gen-vito all features of xcube can be used. 
In order to use the xcube-gen-vito you need to install xcube first: 

# Installation

First install xcube
    
    $ git clone https://github.com/dcs4cop/xcube.git
    $ cd xcube
    $ conda env create
    
Then
    
    $ activate xcube
    $ python setup.py develop

Secondly, clone the xcube-gen-vito repository:

    $ git clone https://github.com/dcs4cop/xcube-gen-vito.git
    $ cd xcube-gen-vito
    $ python setup.py develop
    
Once in a while make an update of xcube and xcube-gen-vito:
    
    $ activate xcube
    $ git pull --force
    $ cd xcube
    $ python setup.py develop
    
Then change into the xcube-gen-vito directory:

    $ cd xcube-gen-vito
    $ python setup.py develop
    
    
Run tests

    $ pytest
    
with coverage

    $ pytest --cov=xcube

with [coverage report](https://pytest-cov.readthedocs.io/en/latest/reporting.html) in HTML

    $ pytest --cov-report html --cov=xcube

# Developer Guide 

...is [here](https://xcube.readthedocs.io/en/latest/devguide.html).


# User Guide

Please use the [README](https://xcube.readthedocs.io/en/latest/index.html) 
of xcube for further information. 

