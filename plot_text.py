from bokeh.models import Div

#header
header = Div(text="""<h1>AUS Frameworks Clustering</h1>""")

# title for the toolbox
toolbox_header = Div(text="""<h1>Toolbox:</h1>""")

# project description
description = Div(text="""<p1>Dots of same color represent the same cluster. There are seven clusers (0-6). </p1>""")

# steps description
description2 = Div(text="""<h3>Approach:</h3>
<ul>
  <li>Parse the text from the body of each document using Natural Language Processing (NLP). </li>
  <li>Turn each document instance di into a feature vector Xi using Term Frequency–inverse Document Frequency (TF-IDF).</li>
  <li>Apply Dimensionality Reduction to each feature vector Xi using t-Distributed Stochastic Neighbor Embedding (t-SNE) to cluster similar research articles in the two dimensional plane X embedding Y1.</li>
  <li>Use Principal Component Analysis (PCA) to project down the dimensions of X to a number of dimensions that will keep .95 variance while removing noise and outliers in embedding Y2.</li>
  <li>Apply k-means clustering on Y2, where k is 20, to label each cluster on Y1.</li>
  <li>Apply Topic Modeling on X using Latent Dirichlet Allocation (LDA) to discover keywords from each cluster.</li>
  <li>Investigate the clusters visually on the plot, zooming down to specific articles as needed, and via classification using Stochastic Gradient Descent (SGD).</li>  
</ul> 
<p>Total of <b>32,651 samples</b> analysed. Articles that are not English dropped.</p1>""")

# citation
cite = Div(text="""<p1><h3>Citation:</h3><a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">COVID-19 Open Research Dataset Challenge (CORD-19) | Kaggle</a></p1>
<br><br>
<p1><a href="https://www.whitehouse.gov/briefings-statements/call-action-tech-community-new-machine-readable-covid-19-dataset/">Call to Action to the Tech Community on New Machine Readable COVID-19 Dataset | White House</a></p1>
<br><br>
<p1>Inspired by Dr. Charles Nicholas's "Mr. Shakespeare, Meet Mr. Tucker", High Performance Computing and Data Analytics Workshop, September 10-11, 2019.  Linthicum Heights, MD, USA</p1>
<br><br>
<p1>Raff, Edward and Nicholas, Charles and McLean, Mark. The Thirty-Fourth AAAI Conference on Artificial Intelligence. A New Burrows Wheeler Transform Markov Distance. 2020.</p1>""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search abstracts, 
titles, journals, and authors. Please keep in mind that only 150 words of abstracts to reduce the size. Press enter when ready. 
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 20 to show all.</p1>""")

description_keyword = Div(text="""<h3>Keywords:</h3>""")

description_current = Div(text="""<h3>Selected:</h3>""")
