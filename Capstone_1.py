# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 03:49:20 2019

@author: Bryan
"""

# This is the first part of my exploratory analysis and capstone for Springboard 
import pandas as pd

import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation 
sns.set(color_codes=True)

#due to memory size, I loaded these individually and then commented out afterwords. 
#jobs_11 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2011.xlsx')
#jobs_12 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2012.xlsx')
#jobs_13 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2013.xlsx')
#jobs_14 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2014.xlsx')
#jobs_15 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2015.xlsx')
#jobs_16 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2016.xlsx')
#jobs_17 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2017.xlsx')
#jobs_18 = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\Jobs\Jobs_2018.xlsx')

# uploading popualtion data from Us census 
pop = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\pop-est2018-alldata.xlsx')

# for 2011
filtered_cities_11 = ['Boston-Cambridge-Quincy, MA-NH','New York-Northern New Jersey-Long Island, NY-NJ-PA','Chicago-Joliet-Naperville, IL Metropolitan Division','Detroit-Warren-Livonia, MI','San Francisco-San Mateo-Redwood City, CA Metropolitan Division','Seattle-Tacoma-Bellevue, WA','Austin-Round Rock-San Marcos, TX','Nashville-Davidson--Murfreesboro--Franklin, TN','Dallas-Fort Worth-Arlington, TX','Washington-Arlington-Alexandria, DC-VA-MD-WV','Denver-Aurora-Broomfield, CO','Baltimore-Towson, MD','Charlotte-Gastonia-Rock Hill, NC-SC','Philadelphia-Camden-Wilmington, PA-NJ-DE-MD','Los Angeles-Long Beach-Santa Ana, CA','Phoenix-Mesa-Glendale, AZ','Portland-Vancouver-Hillsboro, OR-WA','Atlanta-Sandy Springs-Marietta, GA','Indianapolis-Carmel, IN','Houston-Sugar Land-Baytown, TX']
city_jobs_11 = jobs_11[jobs_11['AREA_TITLE'].isin(filtered_cities_11)]

# for 2012
city_jobs_12 = jobs_12[jobs_12['area_title'].isin(filtered_cities_11)]

# or 2013
city_jobs_13 = jobs_13[jobs_13['area_title'].isin(filtered_cities_11)]

# for 2014
filtered_cities_14 = ['Baltimore-Towson, MD','Chicago-Joliet-Naperville, IL-IN-WI','Seattle-Tacoma-Bellevue, WA','Nashville-Davidson--Murfreesboro--Franklin, TN','Dallas-Fort Worth-Arlington, TX','Washington-Arlington-Alexandria, DC-VA-MD-WV','Boston-Cambridge-Quincy, MA-NH','New York-Northern New Jersey-Long Island, NY-NJ-PA','Denver-Aurora-Broomfield, CO','Charlotte-Gastonia-Rock Hill, NC-SC','Detroit-Warren-Livonia, MI','Chicago-Joliet-Naperville, IL-IN-WI','Austin-Round Rock-San Marcos, TX','San Francisco-Oakland-Fremont, CA','Philadelphia, PA Metropolitan Division','Los Angeles-Long Beach-Santa Ana, CA','Phoenix-Mesa-Glendale, AZ','Portland-Vancouver-Hillsboro, OR-WA','Atlanta-Sandy Springs-Marietta, GA','Indianapolis-Carmel, IN','Houston-Sugar Land-Baytown, TX']
city_jobs_14 = jobs_14[jobs_14['area_title'].isin(filtered_cities_14)]

# for 2015
filtered_cities = ['Boston-Cambridge-Nashua, MA-NH','New York-Newark-Jersey City, NY-NJ-PA','Chicago-Naperville-Elgin, IL-IN-WI','Detroit-Warren-Dearborn, MI','San Francisco-Oakland-Hayward, CA','Seattle-Tacoma-Bellevue, WA','Austin-Round Rock, TX','Nashville-Davidson--Murfreesboro--Franklin, TN','Dallas-Fort Worth-Arlington, TX','Washington-Arlington-Alexandria, DC-VA-MD-WV','Denver-Aurora-Lakewood, CO','Baltimore-Columbia-Towson, MD','Charlotte-Concord-Gastonia, NC-SC','Philadelphia, PA Metropolitan Division','Los Angeles-Long Beach-Anaheim, CA','Phoenix-Mesa-Scottsdale, AZ','Portland-Vancouver-Hillsboro, OR-WA','Atlanta-Sandy Springs-Roswell, GA','Indianapolis-Carmel-Anderson, IN','Houston-The Woodlands-Sugar Land, TX']
city_jobs_15 = jobs_15[jobs_15['area_title'].isin(filtered_cities)]

# for 2016
city_jobs_16 = jobs_16[jobs_16['area_title'].isin(filtered_cities)]

# for 2017
city_jobs_17 = jobs_17[jobs_17['area_title'].isin(filtered_cities)]

# for 2018
filtered_cities_18 = ['Boston-Cambridge-Nashua, MA-NH','New York-Newark-Jersey City, NY-NJ-PA','Chicago-Naperville-Elgin, IL-IN-WI','Detroit-Warren-Dearborn, MI','San Francisco-Oakland-Hayward, CA','Seattle-Tacoma-Bellevue, WA','Austin-Round Rock, TX','Nashville-Davidson--Murfreesboro--Franklin, TN','Dallas-Fort Worth-Arlington, TX','Washington-Arlington-Alexandria, DC-VA-MD-WV','Denver-Aurora-Lakewood, CO','Baltimore-Columbia-Towson, MD','Charlotte-Concord-Gastonia, NC-SC','Philadelphia-Camden-Wilmington, PA-NJ-DE-MD','Los Angeles-Long Beach-Anaheim, CA','Phoenix-Mesa-Scottsdale, AZ','Portland-Vancouver-Hillsboro, OR-WA','Dallas-Fort Worth-Arlington, TX','Atlanta-Sandy Springs-Roswell, GA','Indianapolis-Carmel-Anderson, IN','Houston-The Woodlands-Sugar Land, TX']
city_jobs_18 = jobs_18[jobs_18['area_title'].isin(filtered_cities_18)]

# getting total jobs of all the cities 

total_jobs_11 = city_jobs_11[city_jobs_11['OCC_TITLE']=='All Occupations']

total_jobs_12 = city_jobs_12[city_jobs_12['occ_title']=='All Occupations']

total_jobs_13 = city_jobs_13[city_jobs_13['occ_title']=='All Occupations']

total_jobs_14 = city_jobs_14[city_jobs_14['occ title']=='All Occupations']

total_jobs_15 = city_jobs_15[city_jobs_15['occ title']=='All Occupations']

total_jobs_16 = city_jobs_16[city_jobs_16['occ title']=='All Occupations']

total_jobs_17 = city_jobs_17[city_jobs_17['occ_title']=='All Occupations']

total_jobs_18 = city_jobs_18[city_jobs_18['occ_title']=='All Occupations']

# adding year columns for future merger

city_jobs_11['Year'] = '2011'

city_jobs_12['Year'] = '2012'

city_jobs_13['Year'] = '2013'

city_jobs_14['Year'] = '2014'

city_jobs_15['Year'] = '2015'

city_jobs_16['Year'] = '2016'

city_jobs_17['Year'] = '2017'

city_jobs_18['Year'] = '2018'


# taking the jobs broken down by OCC Codes
job_codes = ['11-0000','13-0000','15-0000','17-000','19-0000','21-0000','23-0000','25-0000','27-0000','29-0000','31-0000','33-0000','41-0000','43-0000']

types_11 = city_jobs_11[city_jobs_11['OCC_CODE'].isin(job_codes)]

types_12 = city_jobs_12[city_jobs_12['occ_code'].isin(job_codes)]

types_13 =city_jobs_13[city_jobs_13['occ_code'].isin(job_codes)]

types_14 = city_jobs_14[city_jobs_14['occ code'].isin(job_codes)]

types_15 = city_jobs_15[city_jobs_15['occ code'].isin(job_codes)]

types_16 = city_jobs_16[city_jobs_16['occ code'].isin(job_codes)]

types_17 = city_jobs_17[city_jobs_17['occ_code'].isin(job_codes)]

types_18 = city_jobs_18[city_jobs_18['occ_code'].isin(job_codes)]

# for all years 2011 - 2018
jobs_all_years = pd.concat([types_11,types_12,types_13,types_14,types_15,types_16,types_17,types_18],axis=0)

# for visuals and exploratory analysis 
import seaborn as sns
# convertig string to numeric
types_11['A_MEAN'] = types_11['A_MEAN'].apply(pd.to_numeric,errors='coerce')
types_12['a_mean'] = types_12['a_mean'].apply(pd.to_numeric,errors='coerce')
types_13['a_mean'] = types_13['a_mean'].apply(pd.to_numeric,errors='coerce')
types_14['a_mean'] = types_14['a_mean'].apply(pd.to_numeric,errors='coerce')
types_15['a_mean'] = types_15['a_mean'].apply(pd.to_numeric,errors='coerce')
types_16['a_mean'] = types_16['a_mean'].apply(pd.to_numeric,errors='coerce')
types_17['a_mean'] = types_17['a_mean'].apply(pd.to_numeric,errors='coerce')
types_18['a_mean'] = types_18['a_mean'].apply(pd.to_numeric,errors='coerce')

#pd.concat([types_11,types_12],ignore_Index ="True")

#types_11.merge(types_12,how="left")

#boxplot for mean salaries in 2011
sns.boxplot(types_11['A_MEAN'])

#sns.boxplot(types_18['a_mean'])

#sns.boxplot(types_12['a_mean'])

# a quick corrplot test for types_11
types_11.corr(method='pearson')

#convering to excel files to combine and use in Tableau, share via excel file
#types_11.to_excel("job_types_11.xlsx")
#types_12.to_excel("job_types_12.xlsx")
#types_13.to_excel("job_types_13.xlsx")
#types_14.to_excel("job_types_14.xlsx")
#types_15.to_excel("job_types_15.xlsx")
#types_16.to_excel("job_types_16.xlsx")
#types_17.to_excel("job_types_17.xlsx")
#types_18.to_excel("job_types_18.xlsx")

#importing combined files (2011-2018)
jobs_total = pd.read_excel(r'C:\Users\Bryan\.spyder-py3\job_types_11.18.xlsx')
jobs_total['A_MEAN'] = jobs_total['A_MEAN'].apply(pd.to_numeric,errors='coerce')

sns.boxplot(jobs_total['A_MEAN'])

#ax = jobs_total.plot.bar(x = 'A_MEAN',rot=0)

# importing populations of key MSAs 
pop = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\pop-est2018-alldata.xlsx')
pop_msa = pop[pop['LSAD']=='Metropolitan Statistical Area']
MSA = ['Nashville-Davidson--Murfreesboro--Franklin, TN','Phoenix-Mesa-Scottsdale, AZ','Austin-Round Rock, TX','Indianapolis-Carmel-Anderson, IN','Philadelphia-Camden-Wilmington, PA-NJ-DE-MD','New York-Newark-Jersey City, NY-NJ-PA','Los Angeles-Long Beach-Anaheim, CA','Chicago-Naperville-Elgin, IL-IN-WI','Dallas-Fort Worth-Arlington, TX','Philadelphia-Camden-Wilmington', 'PA-NJ-DE-MD','Houston-The Woodlands-Sugar Land, TX','Washington-Arlington-Alexandria, DC-VA-MD-WV','Atlanta-Sandy Springs-Roswell, GA','Boston-Cambridge-Newton, MA-NH','San Francisco-Oakland-Hayward, CA','Detroit-Warren-Dearborn, MI','Seattle-Tacoma-Bellevue, WA','Baltimore-Columbia-Towson, MD','Denver-Aurora-Lakewood, CO','Portland-Vancouver-Hillsboro, OR-WA','Charlotte-Concord-Gastonia, NC-SC'] 
pop_20 = pop_msa[pop_msa['NAME'].isin(MSA)]

#converting to excel for tableau and visual analysis 
#pop_20.to_excel("pop_20.xlsx")
house_price = pd.read_excel(r'C:\Users\Bryan\Documents\Capstone Job Data\House_Pricing.xls')

# plotting pop/housing prices
plt.plot( 'CENSUS2010POP', data=pop_20, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'POPESTIMATE2012', data=pop_20, marker='', color='olive', linewidth=2)
plt.plot( 'POPESTIMATE2018', data=pop_20, marker='', color='olive', linewidth=2, linestyle='dashed', label="2018")
plt.legend()

plt.plot('CENSUS2010POP','POPESTIMATE2018',data=pop_20)

plt.scatter('CENSUS2010POP',data=pop_20)

# 