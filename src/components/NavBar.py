from dash import html
import dash_bootstrap_components as dbc
# SIDEBAR_STYLE = {
#     "position": "relative",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
#     "transition": "width 0.3s ease-in-out"
# }

sidebar = html.Div(
    [
        
        html.Div(
            [

                html.Img(src="./assets/images/premierleaguelogo.jpg", style={"width": "3rem"}),
                dbc.NavLink([
                html.H6("PremierLeague", className="me-2",style={"font-size": "12px"})],href="/"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="tf-icons bx bx-trophy fas fa-home"), html.Span("22/23 Season" , className="me-2")],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-football"),
                        html.Span("22/23 Teams"),
                    ],
                    href="/team-analysis",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-stats"),
                        html.Span("Predictions"),
                    ],
                    href="/predictions",
                    active="exact",
                    className="pe-3",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)

