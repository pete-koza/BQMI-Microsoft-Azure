import dash
import flask


app = dash.Dash(
    __name__,
    # use_pages=True,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
