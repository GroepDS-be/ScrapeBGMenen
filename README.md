# ScrapeBGMenen
Scrapy pagination demo

Setup
=====

Install the Python package 'virtualenv':

    sudo pip install virtualenv

Create a virtual environment for Python libraries:

    virtualenv venv

Activate the virtual environment:

    source ./venv/bin/activate

Install the Python library dependencies of this repo:

    pip install -r requirements.txt

Run the script:

    cd bgscraper
    scrapy crawl bgm -o adressen.csv
    
License:
GNU Affero GPLv3 or later.
