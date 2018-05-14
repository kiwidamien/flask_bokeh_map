# Flask and Bokeh mapping

The Bokeh project shows how to add unemployment data at the county level in its documentation. The county data included in Bokeh is in a strange format; the goal of this project is to show
1. How to integrate your own FIPS data with Bokeh, and
2. How to use the Bokeh geoplots with Flask.

## Parts of the project -- setup

We preprocess the data in `data/input` and put a pickled file in `data/output`

In the iPython notebook, `map of states.ipynb`, we read in our own `PovertyData.csv` with FIPs data. This data is joined with the `us_counties` that can be imported as part of Bokeh. The `map of states.ipynb` also exports a picked file to `data/output` to be used in the Flask app.

If you want to use your own data, you would replace the `pd.merge` of the Poverty Data dataset and `us_counties` with your own dataset, and export to the `data/output` directory.

This notebook also includes some plotting, but this is just to help us write the flask part of the project.

## Parts of the project -- Flask

The `static`, `templates`, and `bokeh_app.py` are all part of the Flask application. You don't need the `map of states.ipynb` file once it has generated our pickle file.

To use the app, run
```
python3 bokeh_app.py
```

To load in your browser, visit [http://127.0.0.1/il] (for the state of Illinois)
