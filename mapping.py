from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.embed import components
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.tile_providers import STAMEN_TERRAIN_RETINA

import pickle

geoDataFrame = pickle.load(open('./data/output/CountyPoverty.pickle', 'rb'))

def get_list_of_states():
    return list(geoDataFrame.state.unique())

def add_hover_tool(my_plot):
    hover = my_plot.select_one(HoverTool)
    hover.point_policy = 'follow_mouse'
    hover.tooltips = [
        ("Name", "@name"),
        ("Percent poor", "@percent_poor%"),
        ("Median income", "$@median_income")
    ]

def get_map_div(state_name, field_to_plot='MEDHHINC_2016', add_tiles=False):
    df_filtered = geoDataFrame[geoDataFrame.state == state_name]

    colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

    if add_tiles:
        x_values = list(df_filtered.x_wm.values)
        y_values = list(df_filtered.y_wm.values)
    else:
        x_values = list(df_filtered.lons.values)
        y_values = list(df_filtered.lats.values)

    source = ColumnDataSource(dict(
        x=x_values,
        y=y_values,
        name=df_filtered.name,
        state=list(df_filtered.state),
        median_income=df_filtered.MEDHHINC_2016,
        percent_poor=df_filtered.PCTPOVALL_2016,
        income_color_county=[colors[min(int(data/15000.0), len(colors) - 1)] for data in df_filtered.MEDHHINC_2016],
        percent_poor_color_county=[colors[min(int(percent/5.0), len(colors)-1)] for percent in df_filtered.PCTPOVALL_2016]
    ))

    TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

    title = '{}: map of {}'.format(state_name, field_to_plot)

    if field_to_plot == 'MEDHHINC_2016':
        name_of_color_field = 'income_color_county'
    else:
        name_of_color_field = 'percent_poor_color_county'

    f = figure(title=title, tools=TOOLS,
               plot_width=450, plot_height=350,
               background_fill_color='#C1DEE2')

    f.patches(xs='x', ys='y', fill_color=name_of_color_field,
              line_color='white', line_width=0.5, line_alpha=0.7,
              fill_alpha=0.7, source=source)

    if (add_tiles):
        f.add_tile(STAMEN_TERRAIN_RETINA)

    add_hover_tool(f)
    print(df_filtered.PCTPOVALL_2016)
    javascript, div = components(f)

    return (javascript, div)
