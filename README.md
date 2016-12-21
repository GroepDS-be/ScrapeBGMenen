# ScrapeBGMenen
Scrapy pagination demo

#About ScrapeBGMenen
Based on Scrapy, this is a small script that gets the adresses of the companies listed on the website http://www.menen.be/bedrijvengids. The "BG" stands for BedrijvenGids, translated to Company Guide, a directory of all companies in the municipality of Menin (Belgium), where I live.

It is not my intention to use the resulting data, as this could infringe privacy laws, I don't know. My intention is to learn the Scrapy web scraper framework. There is no better way to learn than to do it on real data. The specific case for this was the fact that this website used pagination.

I open sourced it so you could maybe learn from it, recieve feedback and demo my work.

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
MIT License
