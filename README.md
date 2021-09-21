# CroydonBinScraper

## Introduction

This is a web scraper that will scrape the croydon council bin collection date site. This is effectively creating an API to retrieve the bin data for croydon councils bins.

## Usage

Grab your __CJ_AYA cookie from the croydon council bin website, the steps to obtain it are written inside of main.py. When storing your location key, make a .env file in the same folder as the python script and store it like 
LOCATION_COOKIE = 'data goes inside quotation marks'

## Credits

[robbrad's repository](https://github.com/robbrad/UKBinCollectionData) which uses python scripts to query council websites and retrieve their bin dates. I suggest looking at his repository first and then checking how your council website utilises the location data. For example, I had to instantiate a session as Croydon Councils website wont let you query the site without a JSESSIONID. Thats why this script is slower than the implementations in robbrads' repo as this script needs to wait for a JSESSIONID to be assigned by croydon councils website.

## Languages and Tools

<p align="left"> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>