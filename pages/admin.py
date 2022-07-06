import dash
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output, State
from datetime import date
from dash.exceptions import PreventUpdate
import DB_SQL as db


@app.callback(
    Output('url', 'pathname'),
    Input('adminLoginButton', 'n_clicks'),
    Input('adminUsername', 'value'),
    Input('adminPassword', 'value'),
    Input('adminManageEDB', 'n_clicks')
)
def adminLogin(adminLoginButton, username, password, manage_btn):
    if(adminLoginButton and username == 'admin' and password == 'password'):
         return "/admin/panel"
    if(manage_btn):
        return "/admin/panel/Employee-Directory"

    raise PreventUpdate


layout = html.Div(
    id="adminLayout",
    children=[
        html.Div(
            id="adminLogin",
            children=[
                html.H2('Admin Control Panel'),
                html.Div(
                    id="userPassInputDiv",
                    children=[
                        dcc.Input(
                            id="adminUsername",
                            type="text",
                            placeholder="Username"),
                        html.Br(),
                        dcc.Input(
                            id="adminPassword",
                            type="password",
                            placeholder="Password"
                        ),
                        html.Br(),
                        html.Button("Login", id="adminLoginButton")
                    ]
                )
            ]
        ),
        html.Div(
            id="adminManageEDB"
        )
    ]
)

layout_panel_selection = html.Div(
    id="adminControlPanel",
    children=[
        html.Button("Manage Employee Database", id="adminManageEDB")
    ]
), html.Div(
    id="dummyDiv", #Dump fake Divs, allow multioutputs, one page
    children=[
        html.Div(
            id="adminLoginButton"
        ),
        html.Div(
            id="adminUsername"
        ),
        html.Div(
            id="adminPassword"
        ),
    ]
)

layout_panel_EDB = html.Div(
    
)