from dash import html, dcc
from dash.dependencies import Input, Output
from pages import Request_Form as rf, Form_Submitted as fs, admin as admin

from app import app

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return rf.content
    elif pathname == '/Form-Submitted' or pathname == '/Form-Submitted/':
        return fs.layout
    elif pathname == '/admin' or pathname == '/admin/':
        return admin.layout
    else:
        return "404"


if __name__ == '__main__':
    app.run_server(debug=False)