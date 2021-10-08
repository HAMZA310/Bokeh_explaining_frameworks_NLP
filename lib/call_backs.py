from bokeh.models import CustomJS

# handle the currently selected article
def selected_code():
    code = """
            var titles = [];
            cb_data.source.selected.indices.forEach(index => titles.push(source.data['titles'][index]));
            title = "<h4>" + titles[0].toString().replace(/<br>/g, ' ') + "</h4>";
            current_selection.text = title
            current_selection.change.emit();
    """
    return code

# handle the keywords and search
def input_callback(plot, source, out_text, topics): 

    # slider call back for cluster selection
    callback = CustomJS(args=dict(p=plot, source=source, out_text=out_text, topics=topics), code="""
				var key = text.value;
				key = key.toLowerCase();
				var cluster = slider.value;
                var data = source.data; 
                
                
                x = data['x'];
                y = data['y'];
                x_backup = data['x_backup'];
                y_backup = data['y_backup'];
                labels = data['desc'];
                passage = data['passage'],
                titles = data['title']
                if (cluster == '7') {
                    for (i = 0; i < x.length; i++) {
						if(passage[i].includes(key) || 
						titles[i].includes(key)) {
							x[i] = x_backup[i];
							y[i] = y_backup[i];
						} else {
							x[i] = undefined;
							y[i] = undefined;
						}
                    }
                }
                else {
                    for (i = 0; i < x.length; i++) {
                        if(labels[i] == cluster) {
							if(passage[i].includes(key) || 
							titles[i].includes(key)) {
								x[i] = x_backup[i];
								y[i] = y_backup[i];
							} else {
								x[i] = undefined;
								y[i] = undefined;
							}
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }
            source.change.emit();
            """)
    return callback
