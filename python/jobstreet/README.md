
# Introduction

This is a program to extract list of posted jobs from Jobstreet.my. Use it wisely.

P/s : I did this because Jobstreet.my doesn't have export feature...

# Prequisite

This program using these libraries
- pandas==0.22.0
- MechanicalSoup==0.10.0
- beautifulsoup4==4.6.0

Please install these libraries and some other required libraries if any.

# Getting Started

First, edit config.py with your Jobstreet username and password.
Then, execute these commands, depends on your current directory.

```
from jobstreet.config import Location
from jobstreet.JobStreetExtractor import JobStreetExtractor
extractor = JobStreetExtractor()
df = extractor.find_jobs(keyword="Software", location=Location.KUALA_LUMPUR)
```
