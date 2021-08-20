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
  <li>Turn each document instance di into a feature vector Xi by embedding a paragraph using sentence-transformer.</li>
  <li>Apply Dimensionality Reduction to each feature vector Xi using t-Distributed Stochastic Neighbor Embedding (t-SNE) to cluster similar research articles in the two dimensional plane X embedding Y1.</li>
  <li>Use Principal Component Analysis (PCA) to project down the dimensions of X to a number of dimensions that will keep .95 variance while removing noise and outliers in embedding Y2.</li>
  <li>Apply k-means clustering on Y2, where k is 7, to label each cluster on Y1.</li>
  <li>Apply Topic Modeling on X using Latent Dirichlet Allocation (LDA) to discover keywords from each cluster.</li>
  <li>Investigate the clusters visually on the plot, zooming down to specific articles as needed, and via classification using Stochastic Gradient Descent (SGD).</li>  
</ul>
""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search titles and passages both.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 7 to show all.</p1>""")

description_keyword = Div(text="""<h3>Keywords:</h3>""")

description_current = Div(text="""<h3>Selected:</h3>""")
