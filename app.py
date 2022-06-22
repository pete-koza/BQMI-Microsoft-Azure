import dash

appR = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)


appR.title = 'Travel & Training Request'

server = appR.server


if __name__ == '__main__':
    appR.run(debug=True)

appR.layout = dash.page_container