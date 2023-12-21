# coding: utf-8
pieces = []
for year in years:
    frame = pd.read_csv('pydata-book/datasets/babynames/yob%s.txt' % year, names = ['name','sex','births'])
    frame['year'] = year
    pieces.append(frame)
    
#Concatenate everything into single DataFrame 
names = pd.concat(pieces, ignore_index=True)
# As Concate glues data frame object together row wise by default. ignore_index =True because we dont want oringinal row no
names
# With this one data we can start aggregating the data at year and sec level using group_by or pivot_table.
total_births = names.pivot_table('births', index= 'year', columns= 'sex', aggfunc =sum)
total_births.tail()
total_births.plot(title = 'Total births by sex and year')
# Lets insert column 'prop' with fraction of babies given each name to total no of births. A 'prop' value of 0.02 would mean 2 
# Lets insert column 'prop' with fraction of babies given each name to total no of births. A 'prop' value of 0.02 would mean 2 out of every 100 babies were given a particular name
def add_prop(group):
    group['prop'] =
def add_prop(group):
    group['prop'] =
def add_prop(group):
    group['prop'] = group.births/group.births.sum()
    return group
    
names = names.groupby(['year','sex']).apply(add_prop)
names
# Verify that 'prop' column sums to 1 in all groups
prop_sum_check = names.groupby(['year', 'sex']).prop.sum()
# Extract the top 1000 names for each sex/year combination
top1000 = names.groupby(['year', 'sex']).apply(lambda x: x.sort_values(by='births', ascending=False)[:1000])
top1000.reset_index(inplace=True, drop=True)
top1000
# if you prefer a do-it-yourself approach, try this instead :
pieces = []
for year, group in names.groupby(['year','sex']):
    pieces.append(group.sort_values(by='births',ascending =False)[:1000])
    top1000 = pd.concat(pieces, ignore_index = True)
    
top1000
# ANALYSING  NAMING TRANDS
# Now we have top 1000 datasets, for both M and F. Now lets split the M and F. 
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', index = 'year', columns = 'name',aggfunc = sum)
#Now this can be plotted for handful for name with DataFrame plot method
subset = total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots = True, figsize =(12,10),grid = False, title = 'Number of births per year')
import matplotlib.pyplot as plt ;plt.show()
# On looking above you might think these names are vanishing after time, but reality is something else which you see
# MEASURING INCREASE IN NAMING DIVERSITY 
# one explaination to decrease in plot that fewer parents are choosing common name. one measure is proportin of the births representated by top 1000  most popular names which we aggregate and plot by year and sex 
table = top1000.pivot_table('prop',index = 'year',columns = 'sex', aggfunc = sum)
import numpy
table.plot(title='Sum of table1000.prop by year and sex', yticks = numpy.linspace(0,1.2,13), xticks=(1880,2020,10))
# As you can see in graph that there is more diveristy in name (decreasing total proportions in top 1000)
#Another interesting metrics is the number of distinct names , taken in order of popularity from highest to lowest, in
#Another interesting metrics is the number of distinct names , taken in order of popularity from highest to lowest, in¬¬
#Another interesting metrics is the number of distinct names , taken in order of popularity from highest to lowest, in top 50% of births. this number is bit tricky to compute. Lets consider just boys name from 2010
#As prviousl we defined :
boys = top1000[top1000.sex == 'M'] 
girls = top1000[top1000.sex == 'F']
df = boys[boys.year == 2010]
df
#After sorting prop in descending order, we want to know how many popular names it takes to reach 50 % 
# We use Vectorized Numpy means cumulative sum, cumsum, of 'prop' and then calling method 'searchsorted()' to position  

    ...: cumulative sum at which 0.5 would need to be inserted to keep it in order. 
# We use Vectorized Numpy means cumulative sum, cumsum, of 'prop' and then calling method 'searchsorted()' to position cumulative sum at which 0.5 would need to be inserted to keep it in order
prop_cumsum = df.sort_values(by ='prop',ascending = False).prop.cumsum()
prop_cumsum[:10]
prop_cumsum.values.searchsorted(0.5)
#Since arrys are zero-indexed, adding 1 to this result gives you a result of 117. By contrast in 1900 this number was very small
df = boys[boys['year'] == 1900]
in1900 = df.sort_values(by ='prop',ascending = False).prop.cumsum()
def get_quantile(group,q=0.5):
    group =
def get_quantile(group,q=0.5):
    group=
def get_quantile(group,q=0.5):
    group=group.sort_values(by='prop',ascending = False)
    return group.prop.cumsum().values.searchsorted(q) +1
    
diveristy =
diveristy =top1000.groupby(['year','sex']).apply(get_quantile)
diveristy = diveristy.unstack('sex')
# This resulting DataFrame diveristy now has two time series, one for each sex, indexed by year
# As you can see girl names have always been more diverse than boy names and they have only become more so over time.further analysis of what exactly is driving the diversity, like the increase of a;ternative spelllings,is left to reader
#In 2007 baby name researcher Laura Wattenberg pointed out on her website that distribution of boys names by final letter has changed significantly over last 100 years. to see this, We first aggregate all of the births in the full dataset by 'year' and 'sex' and 'last letter'
#So lets exctrat last letter from column 'name'
last_letter_get = lambda x : x[-1]
last_letters = names.name.map(last_letter_get)
#When you are applying custom function to your DataFrame Column, use .map()
names['last_letter'] = last_letters
table  = names.pivot_table('births', index = 'last_letter', columns =['sex','year'], aggfunc =sum)
# lets select three consecutive years and select the first few rows
subtable = table.reindex(columns =[1910,1960,2010], level='year')
#PS : as you see whenever you extract a few columns from the DataFrame you should use               

.reindex(columns = [] , level =): in level we write name of column
#PS : as you see whenever you extract a few columns from the DataFrame you should use .reindex(columns = [] , level =): in level we write name of column. 
# lets normalize the table by total births to compute a new table containing proportion of total births for each sex ending in the each letter
subtable.sum()
letter_prop = subtable /subtable.sum()
letter_prop.head()
# BOYS NAME THAT BECAME GIRL NAME AND VICE VERSA
#going back to top1000 names
all_names = pd.Series(top1000.name.unique())
lesley_like = all_names[all_names.str.lower().str.contains('lesl')]
# above we created new series of top1000's column's 'name' with unique name. later wewant to find all name which contain lesl. so that we passed lower to both side of name to compare our value.
lesley_like
filtered = top1000[top1000.name.isin(lesley_like)]
# As you can see to filter out from dataframe's column based on different series, pass .isin(series)
filtered
filtered.groupby(['name','sex'])['births'].sum()
