
# Introduction

This is a program to extract list of posted jobs from Jobstreet.my. Use it wisely.

P/s : I did this because Jobstreet.my doesn't have export feature...

# Getting Started

Execute these commands, depends on your current directory.

```
from jobstreet.config import Location
from jobstreet.JobStreetExtractor import JobStreetExtractor
extractor = JobStreetExtractor()
df = extractor.find_jobs(keyword="Software", location=Location.KUALA_LUMPUR)
```
