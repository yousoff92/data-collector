
# Introduction

This is a program to extract list of posted properties from Mudah.my. Use it wisely.

P/s : I did this because Mudah.my doesn't have export feature...

# Prequisite

This program used these libraries
- pandas==0.22.0
- MechanicalSoup==0.10.0
- beautifulsoup4==4.6.0

Please install these libraries and some other required libraries if any.

# Getting Started

First, edit config.py PAGE_THRESHOLD to parse X number of pages that you want.
Edit other configuration if required.

Execute these commands, depends on your current directory.

```
from mudah.config import General, Region, PropertyCategory
from mudah.MudahExtractor import PropertyExtractor
prop = PropertyExtractor()
df = prop.find_properties(region=Region.SELANGOR)
```

# Sample

See `sample` folder.
