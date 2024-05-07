# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:13:03 2024

@author: 90539
"""

import pandas as pd

dset=pd.read_csv("country_vaccination_stats.csv")
print(dset)
countries = dset['country'].unique()
mean_vaccination = {}
for country in countries:
   country_row = dset[dset['country'] == country]
   dailymean_vaccinations = country_row['daily_vaccinations'].mean()
   mean_vaccination[country]=dailymean_vaccinations
   top3 = sorted(mean_vaccination.items(), key=lambda x: x[1], reverse=True)[:4]
   
for country, mean in top3:
    if not pd.isnull(mean):
        print(country, ":", mean)