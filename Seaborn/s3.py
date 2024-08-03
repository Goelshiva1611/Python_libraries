import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')

print(tips.to_string())
print(iris.to_string())
# categorical scatter plots
# *strip plot
    # axes level
    # figure level
# *swarm plots
# categorical distribution plots

sns.stripplot(data=tips,x='day',y='total_bill',jitter=False)
sns.catplot(data=tips,x='day',y='total_bill',jitter=False,kind='strip')
sns.catplot(data=tips,x='day',y='total_bill',jitter=False,kind='swarm')

plt.legend()
plt.show()