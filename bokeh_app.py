from flask import Flask, render_template
from mapping import get_map_div, get_list_of_states

app=Flask('bokeh demo')

def get_state_page(state, dataset='MEDHHINC_2016'):
    javascript, div = get_map_div(state, field_to_plot=dataset, add_tiles=True)
    state_list = get_list_of_states()

    return render_template('map_of_state.html', javascript=javascript, div=div,
                            state_abbr=state, state_list=state_list,
                            dataset=dataset)

@app.route('/<state>')
def get_state_page_default(state):
    return get_state_page(state)

@app.route('/<state>/<dataset>')
def get_state_page_with_dataset(state, dataset):
    return get_state_page(state, dataset)
    
app.run(port=5000, debug=True)
