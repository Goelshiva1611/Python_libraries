# distributions plots 
#  histplot
# kdeplot
# rugplot
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips=sns.load_dataset('tips')
print(tips)

sns.displot(kind='hist',data=tips,x='tip',element='step',hue='sex')#histogram plot

titanic=sns.load_dataset('titanic')
# matrix plot
# we also have here a heatmap
# we also have a clustermap

plt.show()