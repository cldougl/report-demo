# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime as dt
import os
from pandas_datareader import data as web
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()
moody_logo = "https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/moody.png"

# Describe the layout, or the UI, of the app
app.layout = html.Div([

    html.Div([ # page 1

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([

            html.Div([

                html.Img(src="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/moddys-img-chart2.png",
                        style={
                            'height': '400px',
                            'float': 'center',
                            'margin-bottom': '10',
                            'margin-top': '20'
                        },
                ),
                ]),

            html.Div([

                html.Div([
                    html.H1("Moody's Analytics",
                            style={'text-align': 'center'}),
                    html.H3('Growth Report',
                             style={'color':'#7F90AC',
                                    'text-align':'center'}),
                    ]),
            ]),

            html.Div([
                html.Img(src=moody_logo,
                         style={
                                'height': '100px',
                                'float': 'right',
                                'margin-top': '240',
                                'margin-bottom': '0'
                                },
                            ),
                            ])

        ], className = "subpage" ),

    ], className = "page" ),

    html.Div([ # page 2

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([

            html.Div([

                html.Div([
                    html.H1('Gross Domestic Product',
                             style={'color':'white',
                                    'text-align':'center',
                                    'margin-top': '300',
                                    'font-weight': 'bold'}),
                    html.H3('by Industry Across Province',
                             style={'color':'white',
                                    'text-align':'center'}),
                    ]),
            ]),

            html.Div([
                html.Img(src=moody_logo,
                         style={'height': '100px',
                                'float': 'right',
                                'margin-top': '380',
                                'margin-bottom': '0'
                                }),
                            ])

        ], className = "subpage", style={'background-color': '#009BFA'} ),
    ], className = "page" ),

    html.Div([ # page 3

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([ # subpage 1

            # Row 1 (Header)

            html.Div([
                html.Iframe(src="https://plot.ly/~chelsea_lyn/15718.embed?share_key=g44NM5b1dJDe2HSSVHGEL2&modebar=false&link=false&autosize=true", \
                    seamless="seamless", style=dict(border=0), width="100%", height="900"),
                ]),

        ], className = "subpage" ),

    ], className = "page" ),


    html.Div([ # page 4

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([

            html.Div([

                html.Div([
                    html.H1("Industry Growth Rate",
                            style={'color':'white',
                                   'text-align':'center',
                                   'margin-top': '300',
                                   'font-weight': 'bold'}),
                    html.H3('2014-2019',
                             style={'color':'white',
                                    'text-align':'center'}),
                    ]),
            ]),

            html.Div([
                html.Img(src=moody_logo,
                         style={
                                'height': '100px',
                                'float': 'right',
                                'margin-top': '380',
                                'margin-bottom': '0'
                                }),
                            ])
        ], className = "subpage", style={'background-color': '#00C1B5'} ),

    ], className = "page" ),

    html.Div([ # page 5

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([ # subpage 1

            # Row 1 (Header)

                html.Iframe(src="https://plot.ly/~chelsea_lyn/15720.embed?share_key=KmGmw9bWZtvc6X4OBIL56X&modebar=false&link=false&autosize=true", \
                    seamless="seamless", style=dict(border=0), width="100%", height="800"),

            html.Div([
                html.Img(src=moody_logo,
                         style={
                                'height': '100px',
                                'float': 'right',
                                'margin-top': '0',
                                'margin-bottom': '0'
                                }),
                            ])

        ], className = "subpage"),
    ], className = "page" ),

])

if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })

external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "https://cdn.rawgit.com/cldougl/plot_images/add_r_img/moodys.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({ "external_url": css })

external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://cdn.rawgit.com/plotly/dash-app-stylesheets/a3401de132a6d0b652ba11548736b1d1e80aa10d/dash-goldman-sachs-report-js.js" ]

for js in external_js:
    app.scripts.append_script({ "external_url": js })



if __name__ == '__main__':
    app.run_server(debug=True)
