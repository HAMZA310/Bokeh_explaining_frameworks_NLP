from bokeh.models import Div

#header
header = Div(text="""<h1>AUS Frameworks Clustering</h1>""")

# title for the toolbox
toolbox_header = Div(text="""<h1>Toolbox:</h1>""")

# project description
description = Div(text="""<p1>Dots of same color represent the same cluster </p1>""")

# steps description
description2 = Div(text="""<h3>Approach:</h3>
<ul>
  <li>Investigate the clusters visually on the plot, zooming down to specific passages as needed.</li>  
  <li> Use the slider to go to a particular cluster.</li>
  <li>Use the search bar to search for a specific keyword. If your slider is set to cluster c, it'll search passages only in that cluster.</li>
  <li>Investigate the clusters visually on the plot, zooming down to specific articles as needed.</li>
  <li>By default, the slider is set to k i.e. max value. In that case it'll display all clusters. Note that the index on the slider of the first cluster is 0 (not 1).</li>
  <li> Unlike excel sheets, this plot provides insights on a different level where similairties of all passages in all frameworks are visualized at once.
    
</ul>
""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search titles and passages both. You can use 'slider' and 'search' together to search for a keyword in a particular cluster.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters/Frameworks:</h3><p1>The slider below can be used to filter the target cluster if color_by_title is set to False otherwise it filters by framework which is valid upto the number of frameworks. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to k (i.e. max) to show all.</p1>""")

description_keyword = Div(text="""<h3>Keywords:</h3>""")

description_current = Div(text="""<h3>Selected:</h3>""")
