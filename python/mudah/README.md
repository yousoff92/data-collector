
# Introduction

This is a program to extract list of posted properties from Mudah.my. Use it wisely.

# Getting Started

Execute these commands, depends on your current directory.

from mudah.config import General, Region, PropertyCategory
from mudah.MudahExtractor import PropertyExtractor
prop = PropertyExtractor()
df = prop.find_properties(region=Region.SELANGOR)
