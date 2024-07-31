# relational plots
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
tips=sns.load_dataset('tips')
print(tips.to_string())
print(tips.head(15))
print(tips.info)
# its an axes level function
sns.scatterplot(data=tips,x='total_bill',y='tip',hue='sex',style='time',size='size')
# you can also use the relplot ->figure level function -> square in the shape mainly
# at both places you have benefits and alos drawbacks
sns.relplot(data=tips,x='total_bill',y='tip',kind='line',hue='sex',style='time',size='size')
gap=px.data.gapminder()
temp_df = gap[gap['country'].isin(['India','Brazil','Germany'])]

sns.relplot(kind='line',data=temp_df,x='year',y='lifeExp',hue='country',style='continent',size='iso_num')
sns.relplot(kind='scatter',data=temp_df,x='year',y='lifeExp',hue='country',style='continent',size='iso_num')

print(temp_df)

# facet plot
# work only will figure level function onlyyy
# facet plot are very informative ->side by side plots we can say;
sns.relplot(data=tips,kind='scatter',x='total_bill',y='tip',hue='sex',size='size', col='sex')
sns.relplot(data=tips,kind='scatter',x='total_bill',y='tip',hue='sex',size='size', row='sex')
sns.relplot(data=tips,kind='scatter',x='total_bill',y='tip',hue='sex',size='size', col='smoker',row='sex')
sns.relplot(data=tips,kind='scatter',x='total_bill',y='tip',hue='sex',size='size', col='smoker',row='day')
sns.relplot(data=tips,kind='scatter',x='total_bill',y='tip',hue='sex',size='size', col='sex',row='day')
sns.relplot(data=gap,kind='line',x='lifeExp',y='gdpPercap',col='year',col_wrap=3)

# these col and row are only work in the relplot not in scatter plot and not in line plot
plt.legend()
plt.show()

