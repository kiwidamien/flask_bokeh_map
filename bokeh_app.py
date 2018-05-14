from flask import Flask, render_template
from mapping import get_map_div, get_list_of_states

app=Flask('bokeh demo')

@app.route('/<state>')
def get_state_page(state):
    javascript, div = get_map_div(state, add_tiles=True)
    state_list = get_list_of_states()

    return render_template('map_of_state.html', javascript=javascript, div=div,
                            state_abbr=state, state_list=state_list)

app.run(port=5000, debug=True)
