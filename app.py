from dash import Dash, html, dcc, Input, Output
from data_loader import load_data

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# Shared dropdown styling
dropdown_style = {
    'width': '100%',
    'margin': '0 auto',
    'color': 'black',
    'backgroundColor': 'white'
}

########################################################################################

app = Dash(__name__)

data = load_data()

app.layout = html.Div([

    # Header
    html.Div([
        html.A(html.Img(src="/assets/ENERGY-NEXUS-LOGO.png", className="logo"), href="/"),
        html.A(html.Div([
            html.Div(className="burger-line"),
            html.Div(className="burger-line"),
            html.Div(className="burger-line")
        ], className="burger-menu", id="burger-menu"),
            href="#menu-section",
            className="scroll-link")
    ], className="header-bar"),

    # Intro Section
    html.Div([
        html.Div([
            html.H1("ENERGY NEXUS"),
            html.H2("MAPPING THE RENEWABLE FUTURE")
        ], style={'textAlign': 'center'})
    ], className="intro section"),

    # Project Members
    html.Div([
        html.Div([
            html.A([
                "A project by:",
                html.Br(), html.Br(),
                "Lim Shui Hong, Josie", html.Br(),
                "Chezhian Kowsika", html.Br(),
                "Nurul Qamaryna Binte Sulaiman", html.Br(),
                "Syeda Zainab Fathimay", html.Br(), html.Br(),
            ], className="paragraph-text"),
            html.A(html.Img(src="/assets/MU-LOGO.png", className="logo2")),
        ], style={'textAlign': 'center'})
    ], className="section"),

    # Introduction
    html.Div([
        html.P([
            "In the 21st century, energy is more than a utility — it's the heartbeat of global development, "
            "economic resilience, and environmental survival. Yet, over 80% of the world’s energy still "
            "comes from fossil fuels, driving the climate crisis, polluting ecosystems, and exacerbating inequality.",
            html.Br(), html.Br(),
            "Every year, rising global temperatures lead to more extreme weather, water scarcity, and displacement "
            "of communities. Meanwhile, fossil fuel reserves are finite and geopolitically volatile, leaving "
            "nations vulnerable to price shocks and supply disruptions.",
            html.Br(),html.Br(),
            "Renewable energy — solar, wind, hydro, and more — offers a different path:",
            html.Br(),
            "    It's clean, drastically reducing greenhouse gas emissions.",
            html.Br(),
            "    It’s sustainable, tapping into natural, replenishable sources.",
            html.Br(),
            "    It’s becoming cheaper than fossil fuels, even in developing economies.",
            html.Br(), html.Br(),
            "Despite its promise, adoption remains uneven. Infrastructure gaps, policy inertia, and misinformation slow "
            "progress. But with the right investments and informed decisions, renewable energy can be the "
            "foundation for a more resilient, just, and sustainable future.",
            html.Br(), html.Br(),
            "This project explores the data behind the transition—where we are now, where we’re heading, and what it "
            "will take to get there. Through clear, compelling visualizations and insights, we aim to both "
            "educate and empower."

        ], className="paragraph-text", style={'margin': 0, 'fontSize': '1.3rem'})
    ], className="section"),

    # Menu Section
    html.Div([
        html.A(["Nations with higher renewable", html.Br(),
                "energy adoption rely less", html.Br(),
                "on imported fossil fuels."], className="menu-box hypo-1", href="#hypo1-section"),

        html.A(["The Cost of Renewable", html.Br(),
                "Energy Continues to Decline", html.Br(),
                "- Is It The Most ", html.Br(),
                "Cost-Effective Energy Source?"], className="menu-box hypo-2", href="#hypo2-section"),

        html.A(["Technological advancements", html.Br(),
                "and cost reductions", html.Br(),
                "drive growth adoptions", html.Br(),
                "- but are we adopting it?"], className="menu-box hypo-3", href="#hypo3-section"),

        html.A(["Solar Power is the future", html.Br(),
                "– Will we embrace it", html.Br(),
                "or fall behind?"], className="menu-box hypo-4", href="#hypo4-section"),

        html.A(["Renewable diversification strategies", html.Br(),
                " reduce reliance on volatile" ,html.Br(),
                " global energy markets - " ,html.Br(),
                "so why is it overlooked?"], className="menu-box hypo-5", href="#hypo5-section"),

        html.A(["Environmental activism and ", html.Br(),
               "citizen engagement accelerate ", html.Br(),
               "renewable energy policy and", html.Br(),
               " infrastructure deployment"], className="menu-box hypo-6", href="#hypo6-section"),
    ], className="menu-grid section", id="menu-section"),

    # Hypothesis 1 Section
    html.Div([
        html.Div([
            html.H4("Nations with Higher Renewable Energy Adoption Rely Less On Imported Fossil Fuels."),
            html.P([
                "As global energy demand rises, energy independence becomes more than a goal — it becomes a necessity."
                " Countries investing in renewable energy aren’t just decarbonizing; they’re reducing their"
                " vulnerability to volatile international fossil fuel markets.",
                html.Br(),
                "This interactive choropleth map illustrates the percentage share of renewables in each country's "
                "energy mix from 2000 to 2023. The pattern is striking: the greener a nation’s power generation, "
                "the more resilient it is to price shocks, geopolitical disruptions, and supply chain uncertainty. ",
                html.Br(),html.Br(),
                "Energy security today is about more than oil reserves — it’s about renewable readiness.",
                html.Br(), html.Br(),
                "This animated choropleth map allows you to see how each country’s renewable share has evolved over the "
                "past two decades, observe regional disparities and policy impacts over time, and understand which "
                "countries have become more self-sufficient — and which remain dependent."

            ], className='paragraph-text'),

            html.Div([
                dcc.Graph(id="renewable-map")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data source: Energy Institute - Statistical Review of World Energy (2024) – ",
                html.A("Learn more", href="https://ourworldindata.org/grapher/renewable-share-energy",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• Nordic countries immediately stand out. Sweden, Norway, and Finland have maintained high renewable "
                "shares throughout the time series, largely thanks to robust hydropower, wind, and early "
                "government investments.",
                html.Br(), html.Br(),
                "• South America, especially Brazil, has consistently high renewable energy due to its massive "
                "hydropower infrastructure — a legacy advantage that still gives it a lead in energy self-sufficiency.",
                html.Br(), html.Br(),
                "• The United States and Western Europe show slower but steady growth. Their renewable shares rise "
                "mostly post-2010, reflecting policy changes and technology cost drops — but they still trail the"
                " top-tier leaders.",
                html.Br(), html.Br(),
                "• Large parts of Asia and Africa remain relatively unchanged until the mid-2010s. While there's some "
                "pickup, it remains modest and uneven — often reflecting infrastructural or financial barriers.",
                html.Br(), html.Br(),
                "• Fossil fuel exporters like Saudi Arabia, Russia, and others tend to have low domestic renewable "
                "shares — highlighting potential vulnerabilities as global demand shifts.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "This map sets the foundation: countries with higher renewable shares today are not "
                "randomly distributed — they tend to be those who either invested early or had existing clean "
                "infrastructure (like hydro). It’s clear that national policy, geography, and long-term planning "
                "are major differentiators. It also hints at energy import reliance: if a country produces more of "
                "its energy renewably and domestically, it has less reason to depend on foreign fossil fuels. "
                "But to really understand that dynamic, we need to look at how much energy countries are actually importing.",
                html.Br(), html.Br(),
                "This horizontal bar chart shows net energy imports as a percentage of total energy use, over time, "
                "for a curated list of countries. Positive values mean net importers. Negative values mean exporters.",
            ], className='paragraph-text'),

            html.Div([
                html.Div([
                    html.Label("Select Country/Countries:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='import-country-dropdown',
                        multi=True,
                        value=[
                            'Belarus', 'Spain', 'Senegal', 'Finland', 'United Kingdom', 'Sweden',
                            'Zimbabwe', 'Denmark', 'Vietnam', 'Nigeria', 'Turkmenistan'
                        ],
                        placeholder='Select countries',
                        options=[
                            {'label': country, 'value': country}
                            for country in sorted(data["energy_im_and_exports_df"]['Entity'].dropna().unique())
                        ],
                        style=dropdown_style
                    ),
                    html.Br(),

                    dcc.Graph(id="import-dependency-graph")
                ], style={'width': '1000px', 'margin': '0 auto'}),

                html.P([
                    "Data source: International Energy Agency (2025) - Energy imports and exports - ",
                    html.A("Learn more",
                           href="https://ourworldindata.org/grapher/energy-imports-and-exports-energy-use",
                           target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
                ], style={'fontSize': '0.8rem'}),
            ]),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• Sweden, Denmark, Finland — all leaders in renewable energy — show consistently low net imports, "
                "with Sweden and Denmark even approaching energy neutrality. Their ability to generate electricity "
                "locally (especially from wind and hydro) directly reduces their need to import.",
                html.Br(), html.Br(),
                "• Spain and Belarus, though more developed, remain heavily reliant on energy imports — aligning with "
                "their slower renewable transition. These countries have made gains in wind and solar but still "
                "depend heavily on imported natural gas and oil.",
                html.Br(), html.Br(),
                "• Senegal, Zimbabwe, and other lower-income countries show moderate to high import percentages."
                " These nations often lack the infrastructure to harness domestic renewables — despite high solar "
                "potential — leading to persistent import reliance.",
                html.Br(), html.Br(),
                "• Vietnam and the UK appear in the middle — both with declining imports over time, "
                "mirroring rising domestic renewable production.",
                html.Br(), html.Br(),
                "• Nigeria and Turkmenistan are outliers with negative import values. But here’s the key: that’s not "
                "because of renewables. These are fossil fuel exporters. They produce oil and gas in abundance — "
                "which skews their import metrics but doesn’t mean they’re energy-diverse or sustainable.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "There’s a visible trend: in countries without fossil fuel reserves, high renewable adoption "
                "correlates with lower energy import dependency.",
                html.Br(),
                "Renewable energy doesn't just clean the grid — it also anchors energy security. But to really test "
                "that idea, we need to see the correlation across a broader dataset.",
                html.Br(), html.Br(),
                "The bubble chart below maps every country’s fossil fuel energy consumption (%) on the x-axis against their "
                "net energy imports (%) on the y-axis. Each bubble’s size represents total energy use.",
            ], className='paragraph-text'),

            html.Div([
                html.Div([
                    dcc.Graph(id="fossil-vs-import-bubble")
                ], style={'width': '1000px', 'margin': '0 auto'}),

                html.P([
                    "Data Source: Merged dataset – ",
                    html.Br(),
                    "IEA Statistics © OECD/IEA 2014 - Fossil fuel energy consumption (% of total) - ",
                    html.A("Learn more",
                           href="https://data.worldbank.org/indicator/EG.USE.COMM.FO.ZS",
                           target="_blank",
                           style={'color': 'white', 'textDecoration': 'underline'}),
                    html.Br(),
                    "World Bank national accounts data, and OECD National Accounts data files. - GDP (current US$) - ",
                    html.A("Learn more",
                           href="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD",
                           target="_blank",
                           style={'color': 'white', 'textDecoration': 'underline'}),
                    html.Br(),
                    "International Energy Agency (2025) – Energy imports and exports - ",
                    html.A("Learn more",
                           href="https://ourworldindata.org/grapher/energy-imports-and-exports-energy-use?tab=table&time=earliest..latest#explore-the-data",
                           target="_blank",
                           style={'color': 'white', 'textDecoration': 'underline'})
                ], style={'fontSize': '0.8rem'}),
            ]),
            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• In the top right, we see countries that both heavily depend on fossil fuels and also import large "
                "portions of their energy. These are double-exposed: vulnerable to supply disruptions and emissions "
                "penalties.",
                html.Br(), html.Br(),
                "• The bottom left is sparse, but powerful: countries with low fossil dependency and low import needs — "
                "the renewables winners. Brazil, Norway, and some other hydro-rich nations sit here.",
                html.Br(), html.Br(),
                "• The top left includes some countries with moderate fossil use but high imports — often reflecting "
                "a slow renewables ramp-up or limited domestic production.",
                html.Br(), html.Br(),
                "• Then there are the bottom right outliers — fossil fuel producers like Russia and Saudi Arabia — "
                "who show low or negative imports because they’re exporting energy. But they’re highly exposed to "
                "fossil volatility and lack long-term sustainability.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "This chart confirms the pattern:",
                html.Br(),
                "Countries that rely heavily on fossil fuels — especially those that don’t produce them — "
                "are consistently more import-dependent.",
                html.Br(),
                "Meanwhile, countries that have adopted renewable energy in a serious, sustained way benefit from "
                "lower net imports, more stable energy prices, and enhanced national autonomy.",
                html.Br(), html.Br(),
                "Together, these visualizations tell a clear story: Renewable energy adoption reduces the need for "
                "imported fossil fuels, especially in nations without oil or gas reserves. But even more importantly, "
                "they highlight that renewables are not just a climate tool — they’re a geopolitical one.",
                html.Br(),
                "Investing in domestic clean energy is a strategy to safeguard national interests, hedge against global "
                "instability, and redefine what energy security means in the 21st century."
            ], className='paragraph-text'),
        ])
    ], className="scroll-page", id="hypo1-section"),

    html.Br(),

    html.P([
        "If renewable energy offers nations a path to greater independence, the next logical question is: Can they afford it?",
        html.Br(),html.Br(),
        "Historically, one of the biggest barriers to adoption wasn’t political will or public support — it was cost. "
        "Fossil fuels were cheaper, easier to scale, and deeply embedded in national economies. But that dynamic has changed. Fast.",
        html.Br(),html.Br(),
        "In the next section, we explore the economic turning point of the global energy transition — where innovation, "
        "market forces, and scale have begun tipping the balance. The data doesn’t just suggest that renewables "
        "are cleaner and more secure — it may now be true that they are also the most cost-effective energy option "
        "on the table."
    ], className='paragraph-text'),

    # Hypothesis 2 Section
    html.Div([
        html.Div([
            html.H4([" The Cost of Renewable Energy Continues to Decline", html.Br(),
            "– Is It The Most Cost-Effective Energy Source?"]),
            html.P([
                "If renewable energy is getting cheaper and more widely adopted, we’d expect to see countries not just "
                "adopting it — but using it to replace fossil fuel imports.",
                html.Br(),
                "To truly understand the economic case for renewable energy, we must zoom out and "
                "compare it to the price volatility of traditional energy sources. Fossil "
                "fuels — particularly oil and coal — are notorious for sharp, unpredictable "
                "swings driven by geopolitics, supply shocks, and market speculation.",
                html.Br(), html.Br(),
                "In contrast, solar and wind have followed a different path: a steady, engineered decline in cost.",
                html.Br(), html.Br(),
                "This line chart tracks the Global Energy Price Indices over time, normalized to 2019. It allows us "
                "to compare long-term trends in Coal, Oil, Solar and Wind."
            ], className='paragraph-text'),

            # Model 2.1
            html.Div([
                dcc.Graph(id="global-energy-price-index-trend")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: IRENA (2024) – Levelized cost of energy for renewables - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "IRENA (2024) – Fossil fuel price index – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/fossil-fuel-price-index",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
            ], style={'fontSize': '0.8rem'})

        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Oil prices show the sharpest volatility, peaking pre-2010, dropping significantly, and spiking "
            "again around 2022 — largely due to geopolitical shocks.",
            html.Br(),
            "• Coal follows a similar path, with significant fluctuations that make energy planning"
            " difficult and import costs unpredictable.",
            html.Br(),
            "• Solar and wind, on the other hand, show a steady decline in price index — with solar showing the "
            "most dramatic reduction, especially after 2010.",
            html.Br(),
            "• By 2020, solar and wind achieved price parity — and stability — even as fossil prices "
            "surged again post-pandemic.",
            html.Br(),html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Fossil fuels remain highly exposed to global shocks. Price spikes aren’t rare "
            "events — they’re expected. In contrast, renewables offer not just affordability,"
            " but price stability — a critical advantage for governments, businesses, and "
            "utilities trying to plan for the long term.",
            html.Br(), html.Br(),
            "Cost declines in renewables didn’t happen by chance — they were driven by intentional investment in R&D, "
            "infrastructure, and deployment. But how strong is the link between financial "
            "commitment and technological innovation?",
            html.Br(), html.Br(),
            "This next scatter plot tracks total investment in renewable energy against the number of patent "
            "filings per year, from 2004 onward."

        ], className='paragraph-text'),

        html.Div([
            # Model 2.2
            html.Div([
                dcc.Graph(id="investment-vs-patents-graph")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: Frankfurt School-UNEP Centre/BNEF (2020)  – Investment in renewable energy - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/investment-in-renewable-energy-by-technology",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),

                "IRENA - INSPIRE Platform (2022)  – Annual patents filed for renewable energy technologies - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/patents-filed-for-renewables",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
            ], style={'fontSize': '0.8rem'}),

        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• From 2004 to 2010, investment was modest — and so was innovation.",
            html.Br(),
            "• Around 2012–2014, we see a sharp jump: investment surges above $150B and patents follow in lockstep.",
            html.Br(),
            "• By 2018–2020, both values plateau at all-time highs, with over 70,000 patents and nearly $350B "
            "invested annually.",
            html.Br(), html.Br(),
            "This strong correlation is no accident. Increased funding into solar, wind, battery storage, and smart "
            "grids has fueled a feedback loop: better tech → lower costs → more adoption → more investment.",
            html.Br(),html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Cost reduction in renewables hasn’t been accidental — it’s been engineered. Through innovation and scale, "
            "renewables have crossed a critical threshold: they’re not just viable — they’re economically competitive.",
            html.Br(), html.Br(),
            "Zooming into Southeast Asia, we see the competition play out on the grid.",
            html.Br(),
            "This dual-line chart tracks electricity generation (% share) from: Renewables (green), and Fossil fuels (red).",
            html.Br(),
            "From 2000 to 2023, ASEAN countries — facing fast-growing populations and energy demand — had a choice: "
            "stick with cheap coal and oil, or start transitioning."
        ], className='paragraph-text'),


        html.Div([
            # Model 2.3
            html.Label("Toggle Lines:", style={'fontWeight': 'bold'}),
            dcc.Checklist(
                id='asean-line-toggle',
                options=[
                    {'label': 'Show Renewables Line', 'value': 'renewables'},
                    {'label': 'Show Fossil Fuels Line', 'value': 'fossil'}
                ],
                value=['renewables', 'fossil'],  # both lines shown by default
                inline=True,
                style={'color': 'white', 'marginBottom': '10px'}
            ),

            html.Div([
                dcc.Graph(id="asean-electricity-trend")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.Br(),

            html.Label("Select Year Range:", style={'fontWeight': 'bold', 'textAlign': 'center'}),
            dcc.RangeSlider(
                id='asean-year-slider',
                min=data["asean_energy_df"]["Year"].min(),
                max=data["asean_energy_df"]["Year"].max(),
                step=1,
                value=[2000, 2023],  # or most recent 20 years
                marks={year: str(year) for year in range(2000, 2024, 2)},
                tooltip={"placement": "bottom", "always_visible": False},
                allowCross=False,
                className="custom-slider"
            ),

            html.P([
                "Data Source: Ember (2024); Energy Institute - Statistical Review of World Energy (2024) – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/electricity-fossil-renewables-nuclear-line",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
            ], style={'fontSize': '0.8rem'}),
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Fossil fuels dominated until around 2015, peaking at over 85% of total generation.",
            html.Br(),
            "• Post-2016, fossil use starts falling, while renewables start rising rapidly — jumping from ~18% "
            "to nearly 28% by 2022.",
            html.Br(),
            "• The crossover gap between 2018–2022 marks the most aggressive growth in renewables.",
            html.Br(), html.Br(),
            "This chart doesn’t just show preference — it shows momentum.",
            html.Br(),html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Even in regions traditionally seen as fossil-reliant, renewables are now cost-competitive enough "
            "to take market share. This is a major turning point for price parity — and for emerging markets "
            "that were once priced out of clean energy.",
            html.Br(), html.Br(),
            "Despite national-level growth, what does the average household experience?",
            html.Br(),
            "This donut chart answers that by showing the global share of renewable electricity in household energy for 2023:",
            html.Br(),
            "It’s a reality check. While industrial and utility-scale transitions are underway, household-level "
            "access remains limited, especially in lower-income countries and fossil-dependent grids."
        ], className='paragraph-text'),

        html.Div([
            # Model 2.4
            html.Label("Select Country:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='model2-4-country-dropdown',
                options=[{'label': c, 'value': c} for c in data["valid_consumption_countries"]],
                value='World',
                style=dropdown_style
            ),

            html.Br(),

            html.Div([
                dcc.Graph(id='model2-4-renewable-share-pie')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.Label("Select Year:", style={'fontWeight': 'bold', 'color': 'white', 'textAlign': 'center'}),
            html.Div([
                dcc.Slider(
                    id='model2-4-year-slider',
                    min=data["consumption_df"]["Year"].min(),
                    max=data["consumption_df"]["Year"].max(),
                    step=1,
                    value=2023,
                    marks={
                        year: str(year) for year in range(
                            data["consumption_df"]["Year"].min(),
                            data["consumption_df"]["Year"].max() + 1, 5
                        )
                    },
                    tooltip={"placement": "bottom", "always_visible": False},
                    included=False,
                    className="custom-slider"
                )
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source:  Energy Institute - Statistical Review of World Energy (2024) – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/energy-consumption-by-source-and-country",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "IRENA (2024) – Levelized cost of energy for renewables - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Energy Institute based on S&P Global Platts - Fossil fuel price index – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/fossil-fuel-price-index",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Even as renewables become cost-effective at scale, the infrastructure, incentives, and access "
            "for residential consumers still lag.",
            html.Br(),
            "• Price drops haven’t fully translated into equity — particularly where subsidies and legacy "
            "systems favor fossil fuels.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "The transition is happening — but not evenly. Without targeted investment in household electrification, "
            "the benefits of cost declines won’t reach the most vulnerable users.",
            html.Br(), html.Br(),
            "We end this section with a close-up on the U.S., comparing the relative affordability of "
            "renewables vs. coal, year by year.",
            html.Br(),
            "In this bar chart: Blue = Renewables (higher = more affordable), Red = Coal (higher = more affordable)",
        ], className='paragraph-text'),

        html.Div([
            html.Label("Select Country:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='affordability-country-dropdown',
                options=[{'label': c, 'value': c} for c in data["common_afford_countries"]],
                value='United States',
                style=dropdown_style
            ),

            html.Br(),

            html.Div([
                dcc.Graph(id='energy-affordability-chart')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data source: Energy Institute - Statistical Review of World Energy (2024) - Fossil Fuel Price Index Dataset - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/fossil-fuel-price-index",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),

                "IEA - Renewables 2024 - ",
                html.A("Learn More",
                       href="https://www.iea.org/data-and-statistics/data-product/renewables-2024-dataset",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),
        ], style={'marginTop': '40px'}),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• From 2010–2017, coal dominated in affordability. Renewables trailed due to high installation and storage costs.",
            html.Br(),
            "• Around 2018, renewables caught up — and since 2020, they’ve become consistently more affordable than coal.",
            html.Br(),
            "By 2022, renewables reached peak affordability, even as coal prices spiked — likely due to fuel market "
            "volatility and carbon pricing trends.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "The U.S. is a case study in the larger trend: renewables have not just caught up — they’ve overtaken fossil"
            " fuels on price in competitive markets. This shift is no longer theoretical — it’s real, and it’s happening now.",
            html.Br(), html.Br(),
            "So, is renewable energy now the most cost-effective option? The answer is yes! The data strongly"
            " supports this. From global innovation patterns to real-time grid economics, the evidence is clear: "
            "renewables are now more affordable, scalable, and resilient than fossil fuels in many regions. "
            "The barriers today aren’t cost — they’re policy inertia, legacy systems, and uneven access.",
            html.Br(),
            "The world isn’t asking “Can we afford renewable energy?” anymore. It’s asking: “Can we afford to delay it any longer?”",
        ], className='paragraph-text'),

    ], className="scroll-page", id="hypo2-section"),

    html.Br(),

    html.P([
        "Renewable energy is no longer new. It’s proven, scalable, and — as we’ve seen — increasingly affordable. "
        "But affordability doesn’t automatically mean adoption. The question now becomes:",
        html.Br(),html.Br(),
        "Are countries actually making the switch — or just admiring the price drop from a distance?",
        html.Br(),html.Br(),
        "This section explores whether advances in cost and technology are translating into real-world "
        "energy system transformation — or if economic opportunity is being left on the table."
    ], className='paragraph-text'),

    # Hypothesis 3 Section
    html.Div([
        html.H4("Technological Advancements & Cost Reductions – But Are We Adopting It?"),
        html.P([
            "As we’ve seen, the affordability argument for renewables is no longer up for debate. "
            "The question now is whether countries are translating falling costs into actual on-the-ground "
            "adoption. Are we acting on opportunity — or missing it?",
            html.Br(), html.Br(),
            "This line chart compares total electricity generation from renewables, fossil fuels, and nuclear with "
            "the capital costs of renewable technologies over time."
        ], className='paragraph-text'),

        html.Div([
            # 3.1
            html.Label("Select Technology Category:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='tech-category-dropdown',
                options=[{'label': 'All Renewables', 'value': 'All Renewables'}] +
                        [{'label': cat, 'value': cat} for cat in sorted(data["lcoe_df"]["Plant category"].dropna().unique())],
                value='All Renewables',
                clearable=False,
                style=dropdown_style
            ),
            html.Br(),

            html.Div([
                dcc.Graph(id='tech-cost-vs-renewables-graph')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Sources: IEA – Levelised Cost of Electricity - ",
                html.A("Learn More",
                       href="https://www.iea.org/data-and-statistics/data-tools/levelised-cost-of-electricity-calculator",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Ember (2024); Energy Institute - Electricity generation from fossil fuels, nuclear and renewables - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/elec-mix-bar",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

        ]),

        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Fossil fuel generation peaked around 2019, followed by a slight decline — signaling the start of a plateau.",
            html.Br(),
            "• In contrast, renewable energy generation (green line) shows steady and sustained growth, "
            "especially after 2010 — a period marked by rapid cost reductions.",
            html.Br(),
            "• Nuclear, by comparison, remains largely stagnant, reflecting policy hesitance and high regulatory barriers.",
            html.Br(), html.Br(),
            "This trend is not random — it coincides with a clear downward movement in capital costs for renewables "
            "across the same timeframe.",
            html.Br(),html.Br(),
            " 💡 Insight:",
            html.Br(),
            "There’s a visible inflection: as renewable costs fall, adoption rises. But fossil fuel use hasn’t dropped"
            " proportionately — suggesting renewables are supplementing, not fully replacing legacy "
            "sources in many regions.",
            html.Br(), html.Br(),
            "These scatter plots explore how technology-specific costs correlate with total renewable electricity "
            "generation across countries. Toggle between onshore wind and solar photovoltaic."
        ], className='paragraph-text'),

        # 3.2
        html.Div([
            html.Label("Select Technology Cost:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='correlation-tech-dropdown',
                options=[
                    {'label': 'Onshore Wind Cost ($/MWh)', 'value': 'onshore_wind'},
                    {'label': 'Solar PV Cost ($/MWh)', 'value': 'solar_photovoltaic'}
                ],
                value='onshore_wind',
                multi=False,
                style=dropdown_style
            ),

            html.Br(),

            html.Div([
                dcc.Graph(id='correlation-scatter')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Sources: IRENA (2024) – Levelized cost of energy for renewables – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'})
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Both charts show a negative correlation: lower costs tend to be associated with higher generation.",
            html.Br(),
            "• But the relationship isn’t steep. Some countries still have low adoption even at low cost "
            "thresholds — pointing to barriers beyond economics: grid limitations, regulatory delays, "
            "or political inertia.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Cost is a driver — but not the only one. Even with falling prices, countries need "
            "supportive infrastructure, policy certainty, and investment pipelines to convert "
            "potential into production.",
            html.Br(), html.Br(),
            " This bar chart breaks down the cost trajectory of each renewable technology from 2000 to today."
        ], className='paragraph-text'),

        # 3.3
        html.Div([
            html.Label("Select Country:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='tech-cost-country-dropdown',
                options=[{'label': c, 'value': c} for c in sorted(data["cost_merged_df"]["Entity"].dropna().unique())],
                value='World',
                style=dropdown_style
            ),
            html.Br(),

            html.Label("Select Technologies:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='tech-cost-tech-dropdown',
                options=[{'label': t, 'value': t} for t in
                         sorted(data["cost_merged_df"]["Technology"].dropna().unique())],
                value=sorted(data["cost_merged_df"]["Technology"].dropna().unique()),  # ✅ Select all by default
                multi=True,
                style=dropdown_style
            ),

            html.Br(),

            html.Div([
                dcc.Graph(id='tech-cost-grouped-bar-chart')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: IRENA (2024) – Levelized cost of energy for renewables – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Ember (2024); Energy Institute – Electricity production by source – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/electricity-production-by-source",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'})
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Solar PV and onshore wind have seen the most dramatic declines — over 80% in many cases.",
            html.Br(),
            "• Hydropower remains stable, while offshore wind and concentrated solar have higher costs but are falling.",
            html.Br(),
            "• Bioenergy and geothermal have relatively flat costs — often due to niche use cases or \
            smaller deployment scales.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "We’re witnessing a technology maturing curve in real time. Wind and solar are rapidly "
            "approaching — and often undercutting — the costs of fossil fuel alternatives.",
            html.Br(), html.Br(),
            "This dual-axis chart tracks global investment in renewables against the cost of solar PV — "
            "perhaps the clearest example of the feedback loop."
        ], className='paragraph-text'),

        # 3.4
        html.Div([
            html.Label("Select Country:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id="lineplot-country-dropdown",
                options=[{"label": country, "value": country} for country in data["heatmap_entities"]],
                value="World",
                style=dropdown_style
            ),

            html.Br(),

            html.Label("Select Cost Technology:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id="lineplot-tech-dropdown",
                options=[
                    {"label": t, "value": t}
                    for t in data["heatmap_long_df"]["Technology"].unique()
                    if not "energy" in t.lower()
                ],
                value="solar_photovoltaic",
                style=dropdown_style
            ),

            html.Br(),

            html.Div([
                dcc.Graph(id="investment-vs-cost-lineplot")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: IRENA (2024) – Levelized cost of energy for renewables – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Frankfurt School-UNEP Centre/BNEF (2020) - Investment in renewable energy, by technology - ",
                html.A("Learn More", href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'})
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• From 2004 to 2011, investments surged alongside high costs — funding research and development.",
            html.Br(),
            "• Post-2012, costs plummeted, even as investment remained strong — a sign that early funding "
            "successfully unlocked scale and efficiency.",
            html.Br(),
            "• The blue line (cost) shows exponential decline — a direct result of learning curves, "
            "mass manufacturing (especially in China), and tech breakthroughs.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Cost reduction is not passive — it’s engineered. The more we invest, the cheaper renewables "
            "become — and the more viable they are for widespread adoption.",
            html.Br(), html.Br(),
            "The final chart for this section shows the global build-out of installed capacity — "
            "the infrastructure that actually "
            "delivers renewable energy to homes, cities, and industries."
        ], className='paragraph-text'),

        # 3.5
        html.Div([
            html.Label("Chart Style:", style={'fontWeight': 'bold'}),
            dcc.RadioItems(
                id='slope-chart-mode',
                options=[
                    {'label': 'Line Chart', 'value': 'line'},
                    {'label': 'Area Chart', 'value': 'area'}
                ],
                value='line',
                inline=True,
                style={'color': 'white', 'marginBottom': '10px'}
            ),
            html.Label("Select Technologies:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='slope-tech-dropdown',
                options=[{'label': tech, 'value': tech} for tech in sorted(data["global_capacity_df"]["Entity"].unique())],
                value=['Hydropower (total)', 'Solar (total)', 'Hydropower (total)', 'Geothermal',
                       'Marine', 'Wind (total)', 'Bioenergy (total)'],  # Default selection
                multi=True,
                placeholder='Select renewable technologies to display',
                style=dropdown_style
            ),
            html.Br(),

            html.Div([
                dcc.Graph(id="slope-renewable-capacity")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: IRENA (2024) – Levelized cost of energy for renewables – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/levelized-cost-of-energy",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Data Source: IRENA (2024) – Installed capacity for different renewable technologies – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/installed-global-renewable-energy-capacity-by-technology",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
            ], style={'fontSize': '0.8rem'}),

        ], className="scroll-page", id="global-slope-section"),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Solar and wind show explosive growth, especially post-2015 — a lagging but powerful "
            "response to the cost reductions we’ve seen.",
            html.Br(),
            "• Hydropower, though still the largest, is leveling off due to site saturation and "
            "environmental constraints.",
            html.Br(),
            "• Bioenergy and marine grow modestly, playing niche roles in specific markets.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "Technology maturity is now translating into infrastructure. The build-out is real — but uneven. "
            "Some technologies (like solar) are surging; others (like marine) remain underutilized.",
            html.Br(), html.Br(),
            "This section answers the core question: Are we adopting renewables in response "
            "to falling costs and better technology? Yes, but not fast enough.",
            html.Br(),
            "There is momentum, especially post-2015, but the adoption rate still lags behind the urgency of "
            "climate targets and the pace of cost reduction. Investment alone isn’t enough — deployment "
            "speed and grid integration must catch up.",
            html.Br(),html.Br(),
            "As we move forward, the data suggests a key shift: from proving renewables can work, "
            "to making sure they do work — everywhere."
        ], className='paragraph-text'),

    ], className="scroll-page", id="hypo3-section"),

    html.Br(),

    html.P([
            "If technological innovation and falling costs have laid the foundation, then adoption is "
            "the structure we’re building. And while global deployment is underway, it's clear "
            "that not all renewables are growing equally.",
            html.Br(),html.Br(),
            "Some technologies — like marine and geothermal — remain small-scale. Others — like hydropower — "
            "are mature but reaching physical and environmental limits. But one stands out above "
            "the rest in both momentum and potential: Solar power.",
            html.Br(),html.Br(),
            "Solar isn’t just another clean energy option — it’s the centerpiece of the global energy "
            "transition. But with its rapid rise comes a challenge: Are we keeping pace with "
            "the opportunity? Are countries embracing solar aggressively — or falling behind "
            "just as it reaches prime time?"
        ], className='paragraph-text'),

    # Hypothesis 4 Section
    html.Div([
        html.Div([
            html.H4("Solar Power is the Future - Will We Embrace It Or Fall Behind?"),
            html.P([
                "Despite being the most abundant and accessible source of energy on Earth, solar power "
                "still represents a small slice of the global energy mix. However, the momentum is "
                "shifting fast — and the data makes it clear: the question is no longer can we "
                "transition, but will we transition fast enough?",
                html.Br(),
                "Let’s explore the trends shaping this turning point.",
                html.Br(),html.Br(),
                "Before we look to the future, we need to understand where solar adoption stands today — "
                "and who’s leading the way. This graph compares installed solar photovoltaic (PV) "
                "capacity over time, grouped by national income levels: high, upper-middle, "
                "lower-middle, and low-income countries."

            ], className='paragraph-text'),

            # Model 4.1
            html.Div([
                html.Label("Select Country/Countries:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='solar-country-dropdown',
                    multi=True,
                    value=['High-income countries', 'Upper-middle-income countries', 'Lower-middle-income countries', 'Low-income countries'],
                    placeholder='Select countries',
                    options=[
                        {'label': country, 'value': country}
                        for country in data["available_countries"]
                    ],
                    style=dropdown_style
                ),

                html.Br(),
                dcc.Graph(id="solar-capacity-growth-graph")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data source: Energy Institute - Statistical Review of World Energy (2024) - Installed Solar PV Capacity Dataset - ",
                html.A("Learn More",
                       href="https://www.kaggle.com/datasets/amirhoseinmousavian/renewable-energy-share?select=installed-solar-pv-capacity.csv",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• High-income countries dominate in installed capacity, with growth sharply accelerating around 2010, "
                "and reaching nearly 500 GW by 2022. This reflects strong government incentives, mature infrastructure, "
                "and private sector innovation.",
                html.Br(),html.Br(),
                "• Upper-middle-income countries are not far behind — their growth curve is steeper post-2015, showing "
                "how emerging economies (like China, Africa, and Vietnam) are rapidly catching up, driven by "
                "falling costs and energy security needs.",
                html.Br(),html.Br(),
                "• Lower-middle-income countries show some traction, but adoption remains modest — under 100 GW total "
                "by 2022. This suggests room for scalable investment, but also hints at infrastructure and "
                "financing barriers.",
                html.Br(),html.Br(),
                "• Low-income countries are nearly flatlined on the graph. Despite massive solar potential "
                ", lack of financing, grid infrastructure, and policy support have left these regions behind.",
                html.Br(),html.Br(),
                " 💡 Insight:",
                html.Br(),
                "The global solar race is underway — but it’s not a level playing field. Without targeted intervention, "
                "low- and lower-middle-income nations risk being left out of the clean energy transition, "
                "widening the global energy divide."
            ], className='paragraph-text')

        ]),

        html.Div([
            html.P([
                "Now that we’ve seen solar capacity accelerating across income groups, the next question is: Which "
                "renewable technologies are actually driving electricity generation? This stacked area chart "
                "tracks how solar, wind, hydro, and bioenergy have evolved as a share of total renewable "
                "electricity production from 2003 to 2022."
            ], className='paragraph-text'),

            # Model 4.2
            dcc.Checklist(
                id='renewable-source-selector',
                options=[
                    {'label': 'Solar', 'value': 'Solar'},
                    {'label': 'Wind', 'value': 'Wind'},
                    {'label': 'Hydro', 'value': 'Hydro'},
                    {'label': 'Bioenergy', 'value': 'Bioenergy'}
                ],
                value=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
                inline=True,
                style={'color': 'white', 'textAlign': 'center'}
            ),
            html.Br(),


            html.Div([
                dcc.Graph(id="renewable-share-area-graph")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.Label("Select Year Range:", style={'fontWeight': 'bold', 'textAlign': 'center'}),
            html.Div([
                dcc.RangeSlider(
                    id='renewable-area-year-slider',
                    min=data["renewable_melted"]["Year"].min(),
                    max=data["renewable_melted"]["Year"].max(),
                    step=1,
                    value=[data["renewable_melted"]["Year"].max() - 19, data["renewable_melted"]["Year"].max()],
                    marks={year: str(year) for year in range(data["renewable_melted"]["Year"].min(), data["renewable_melted"]["Year"].max()+1, 5)},
                    tooltip={"placement": "bottom", "always_visible": False},
                    allowCross=False,
                    className="custom-slider"
                )
            ], style={'width': '1000px', 'margin': '0 auto'}),
            html.Br(),


            html.P([
                "Data source: Energy Institute - Statistical Review of World Energy (2024) – Modern Renewable Energy Prod Dataset - ",
                html.A("Learn More",
                       href="https://www.kaggle.com/datasets/amirhoseinmousavian/renewable-energy-share?select=modern-renewable-prod.csv",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• Hydropower has long been the dominant player, making up the vast majority of renewable electricity "
                "until the mid-2010s. Its share is now declining in relative terms as new technologies emerge.",
                html.Br(), html.Br(),
                "• Wind power began rising steadily post-2005 and now commands a substantial share — a strong complement"
                " to solar in many regions.",
                html.Br(), html.Br(),
                "• Solar power, while starting from a tiny base (~1–2% in the early 2000s), has shown the most dramatic "
                "rise in recent years. By 2022, it makes up a clearly visible and rapidly growing portion — "
                "especially since 2015.",
                html.Br(), html.Br(),
                "• Bioenergy has maintained a relatively steady and modest role.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "While solar is still catching up in terms of total share, its growth rate is unmatched. It’s the "
                "fastest-growing renewable electricity source, and it’s poised to play a leading role in the "
                "coming decades.",
                html.Br(), html.Br(),
                "This supports the central idea — “Solar is the future.” While it’s still gaining ground on hydro "
                "and wind in terms of share, its momentum and scalability make it the standout technology of the transition.",
                html.Br(), html.Br(), html.Br(),
                "While electricity generation is a major part of the energy puzzle, primary energy consumption gives us "
                "the full picture — it includes not just electricity, but also transportation, heating, and industrial"
                " use. So, how significant is solar power when we look at total energy use worldwide?",
                html.Br(),
                "This bar chart tracks the global share of solar in primary energy consumption from 2004 to 2023.",
            ], className='paragraph-text')

        ]),

        # Model 4.3
        html.Div([
            html.Div([
                dcc.Graph(id="solar-share-bar-graph")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.Label("Select Year Range:", style={'fontWeight': 'bold', 'textAlign': 'center'}),
            html.Div([
                dcc.RangeSlider(
                    id='solar-share-year-slider',
                    min=2004,
                    max=2023,
                    step=1,
                    value=[2004, 2023],
                    marks={year: str(year) for year in range(2004, 2024, 2)},
                    tooltip={"placement": "bottom", "always_visible": False},
                    allowCross=False
                )
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.Br(),

            html.P([
                "Data Source: Energy Institute - Statistical Review of World Energy (2024) – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/solar-share-energy#explore-the-data",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

            html.P([
            "🔍 Analysis:",
                html.Br(),
                "• From 2004 to around 2010, solar's contribution was nearly negligible — barely registering on the "
                "global energy radar.",
                html.Br(), html.Br(),
                "• Around 2011, we see the beginning of a steady and then rapid increase. Each year, the bars "
                "grow taller, showing accelerating adoption.",
                html.Br(), html.Br(),
                "• By 2023, solar accounts for more than 200% growth relative to 2010 levels, marking a massive leap "
                "in less than a decade.",
                html.Br(), html.Br(),
                "• This growth correlates with declining costs, expanding policy support, and the scaling of "
                "manufacturing and deployment.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "Solar is no longer a fringe solution — it's becoming a core part of the global energy system, "
                "making real headway in total consumption, not just electricity production. But there's still "
                "a long way to go: despite the sharp rise, solar remains only a small share of total global "
                "energy, signaling both progress and untapped potential.",
                html.Br(), html.Br(),

            ], className='paragraph-text')

        ]),

        # Model 4.4
        html.Div([
            html.P([
                "So far, we’ve seen that solar capacity and share are growing globally. But where exactly is this "
                "energy being generated? Who’s producing the most — and who’s at risk of falling behind?",
                html.Br(), html.Br(),
                "This stacked bar chart shows the solar power generation in terawatt-hours (TWh) by income group over "
                "the last 20 years."

            ], className='paragraph-text'),


            html.Div([
                html.Label("Select Region:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='solar-consumption-dropdown',
                    options=[{'label': region, 'value': region} for region in data["available_solar_regions"]],
                    value=[
                        'Low-income countries',
                        'Lower-middle-income countries',
                        'Upper-middle-income countries',
                        'High-income countries'
                    ],
                    multi=True,
                    placeholder='Select regions',
                    style=dropdown_style
                ),

                html.Br(),

                dcc.Graph(id="solar-consumption-graph")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: Energy Institute - Statistical Review of World Energy (2024) – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/solar-energy-consumption",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'})
            ], style={'fontSize': '0.8rem'}),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• High-income countries (green) lead in total generation, reflecting early investment, stable policy "
                "environments, and established infrastructure. Their share remains dominant, but growth is "
                "now steady rather than explosive.",
                html.Br(), html.Br(),
                "• Upper-middle-income countries (pink) show the most dynamic growth. Their generation has skyrocketed "
                "since ~2012, overtaking others and showing that emerging economies are scaling solar "
                "aggressively.",
                html.Br(), html.Br(),
                "• Lower-middle-income countries (light blue) are growing — but not fast enough to close the gap. While "
                "they’ve made progress post-2015, structural and financial constraints remain evident.",
                html.Br(), html.Br(),
                "• Low-income countries (yellow) remain almost invisible in terms of output, despite abundant solar "
                "potential. This underlines the global equity challenge in the clean energy transition.",
                html.Br(), html.Br(),
                " 💡 Insight:",
                html.Br(),
                "Solar generation is expanding fast, but unevenly. The future of solar is global — but only if we make "
                "it accessible. Without targeted policies, investments, and partnerships, entire regions "
                "could be locked out of the clean energy future.",
                html.Br(), html.Br(),html.Br(),
                "Across all four visuals, the data speaks loud and clear:",
                html.Br(),
                "• Solar is no longer niche — it’s scalable, affordable, and accelerating.",
                html.Br(),
                "• The technology is ready, the economics make sense, and the urgency is undeniable",
                html.Br(),
                "•  But adoption and benefits are uneven, and we risk leaving the most vulnerable regions behind.",

            ], className='paragraph-text')
        ]),

    ], className="scroll-page", id="hypo4-section"),

    html.Br(),

    html.P([
        "Solar power shows us what’s possible when innovation, investment, "
        "and political will align. But no single energy source — no matter how efficient — "
        "can meet the complex demands of a global energy system alone..",
        html.Br(),html.Br(),
        "As the world races to decarbonize, reliance on just one or two technologies creates "
        "new vulnerabilities — whether that’s solar’s dependency on daylight, "
        "wind’s intermittency, or hydropower’s exposure to drought.",
        html.Br(),html.Br(),
        "That’s why the next frontier in energy security and resilience isn’t just renewables "
        "— it’s renewable diversification.",
        html.Br(),html.Br(),
        "Building a balanced, multi-source clean energy mix is key to: Shielding economies from "
        "single-source disruptions, matching supply with variable demand profiles, reducing dependence "
        "on volatile fossil fuel markets and foreign imports.",
        html.Br(), html.Br(),
        "Yet despite clear advantages, diversification strategies remain overlooked or "
        "underdeveloped in many national energy plans. Why?"
    ], className='paragraph-text'),

    # Hypothesis 5 Section
    html.Div([
        html.Div([
            html.H4(["Renewable diversification strategies reduce reliance on volatile", html.Br(),
                "global energy markets - so why is it overlooked?"]),
            html.P([
                "Countries that lean heavily on a single energy source — even if it’s clean — risk exposure"
                " to weather patterns, seasonal variability, or price shifts. Diversifying the energy "
                "mix within the renewable sector provides resilience — a safeguard against instability "
                "and a hedge against the volatility of global fossil fuel markets.",
                html.Br(),
                "But the global energy transition reveals an uncomfortable truth: many countries are failing to "
                "diversify. Solar-heavy nations may neglect wind; hydro-dominant economies may resist solar "
                "scale-up. This imbalance not only limits flexibility but also exposes grids to unnecessary risk.",
                html.Br(), html.Br(),
                "This multi-panel radar chart visualizes the renewable energy mix across all continents —"
                " comparing the share of solar, wind, hydro, biofuels, and other renewables. Each region’s"
                " “shape” reveals how balanced — or imbalanced — its energy portfolio is."
            ], className='paragraph-text'),

            # 5.1
            html.Div([
                dcc.RadioItems(
                    id='radar-toggle-mode',
                    options=[
                        {'label': 'Single Continent View', 'value': 'single'},
                        {'label': 'Compare All Continents', 'value': 'compare'}
                    ],
                    value='single',
                    inline=True,
                    style={'color': 'white', 'textAlign': 'center'}
                ),
                html.Br(),

                html.Label("Select Continent:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='continent-dropdown',
                    options=[{"label": k, "value": k} for k in ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]],
                    value='Europe',
                    clearable=False,
                    style=dropdown_style
                ),
                html.Br(),
                dcc.Graph(id='radar-chart')
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source:  Energy Institute - Energy consumption by source – ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/energy-consumption-by-source-and-country",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                " Ember (2024); Energy Institute - Share of electricity generated by renewables - ",
                html.A("Learn More",
                       href="https://ourworldindata.org/grapher/share-electricity-renewables",
                       target="_blank",
                       style={'color': 'white', 'textDecoration': 'underline'}),
            ], style={'fontSize': '0.8rem'}),

        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Africa is dominated by hydropower, with wind as a distant second. Solar, despite the continent’s "
            "vast potential, remains underutilized — a sign of infrastructural and investment barriers.",
            html.Br(), html.Br(),
            "• Asia presents a more evenly spread mix, with moderate contributions from hydro, solar, "
            "and biofuels, and some wind. A continent of contrasts — from solar giants like China "
            "to hydro-heavy regions in Southeast Asia.",
            html.Br(), html.Br(),
            "• Europe leads in wind power, supported by hydro and solar. It's the most balanced "
            "portfolio, reflecting decades of policy-driven diversification and market liberalization.",
            html.Br(), html.Br(),
            "• North America leans heavily on hydropower and wind, with less contribution from solar "
            "and minimal use of biofuels.",
            html.Br(), html.Br(),
            "• South America is overwhelmingly hydro-reliant, especially in Brazil and the Andes — "
            "showcasing legacy infrastructure but also potential over dependence on rainfall.",
            html.Br(), html.Br(),
            "• Oceania, particularly Australia, shows growing wind and solar, but limited use of "
            "other sources, likely due to geography and grid constraints.",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "The radar plots expose a clear truth: renewable energy strategy is still regionally siloed. "
            "While Europe demonstrates high diversification, other regions — especially Africa and "
            "South America — rely on just one or two dominant technologies.",
            html.Br(),
            "This lack of diversification isn’t just a missed opportunity — it’s a risk. Hydro-heavy countries "
            "face climate vulnerability (droughts). Solar-dependent systems can strain without storage."
            " Without a broad portfolio, nations are more likely to turn to fossil fuels when one source falters.",
            html.Br(), html.Br(),
            "The dynamic scatter plot below maps countries based on % of fossil fuel imports "
            "(exposure to volatile markets) and % of renewable energy in the energy mix (domestic clean production)."
        ], className='paragraph-text'),

        # 5.2
        html.Div([
            html.Div([
                html.Div([
                    html.Div("🟢 High Renewables, Low Fossil Imports", className="quadrant-box", style={"backgroundColor": "rgba(0,255,0,0.15)"}),
                    html.Div("🟡  High Renewables, High Fossil Imports", className="quadrant-box", style={"backgroundColor": "rgba(255,255,0,0.15)"})
                ], style={"display": "flex", "justifyContent": "center", "gap": "20px", "marginBottom": "10px"}),

                html.Div([
                    html.Div("🔵 Low Renewables, Low Fossil Imports", className="quadrant-box", style={"backgroundColor": "rgba(0,191,255,0.15)"}),
                    html.Div("🔴 Low Renewables, High Fossil Imports", className="quadrant-box", style={"backgroundColor": "rgba(255,0,0,0.15)"})
                ], style={"display": "flex", "justifyContent": "center", "gap": "20px"})
            ], style={"textAlign": "center", "marginTop": "10px", "color": "white", "fontSize": "0.9rem"}),

            html.Br(),

            dcc.Graph(id="renewable-vs-fossil-scatter"),
        ], style={'width': '1000px', 'margin': '0 auto'}),

        html.P([
            "Data source: Energy Institute - Share of primary energy consumption from renewable sources - ",
            html.A("Learn More",
                   href="https://ourworldindata.org/grapher/renewable-share-energy",
                   target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
            html.Br(),
            "IEA Statistics © OECD/IEA 2014 - Energy imports, net (% of energy use) - ",
            html.A("Learn More",
                   href="https://data.worldbank.org/indicator/EG.IMP.CONS.ZS",
                   target="_blank", style={'color': 'white', 'textDecoration': 'underline'})
        ], style={'fontSize': '0.8rem'}),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• The top-left quadrant (green) represents the ideal: high renewables, low imports. These "
            "countries are energy resilient and largely self-sufficient — think Norway or Brazil.",
            html.Br(), html.Br(),
            "• The bottom-right (red) is the danger zone: high imports, low renewables — a risky, costly combination.",
            html.Br(), html.Br(),
            "• The top-right (yellow) quadrant highlights nations actively deploying renewables, yet still "
            "dependent on imports — often due to lagging infrastructure or legacy fossil contracts.",
            html.Br(), html.Br(),
            "• The bottom-left (blue) contains countries that import little fossil fuel, but haven’t scaled "
            "renewables — likely fossil producers exporting energy (e.g., Russia, Saudi Arabia).",
            html.Br(), html.Br(),
            " 💡 Insight:",
            html.Br(),
            "The strategic payoff of renewable diversification is clear: countries with broader, more balanced "
            "clean energy mixes trend toward lower fossil fuel import dependence. They control more"
            " of their energy destiny and are better shielded from market shocks.",
            html.Br(),
            "Yet, many nations remain stuck in the bottom-right — despite having the potential to diversify. "
            "Why? Inertia, lack of infrastructure, political complexity, or simply a failure to "
            "prioritize resilience over short-term cost logic."
        ], className='paragraph-text'),

    ], className="scroll-page", id="hypo5-section"),

    html.Br(),

    html.P([
        "If diversification is a strategic necessity, what's stopping us from achieving it?",
        html.Br(),html.Br(),
        "Government policies, market incentives, and infrastructure funding are often cited as the missing pieces"
        " — and they are. But behind all of them, there’s another force that too often goes "
        "under-acknowledged: People.",
        html.Br(), html.Br(),
        "From climate protests and grassroots campaigns to digital activism and NGO lobbying, "
        "citizen engagement is shaping energy policy more than ever before. The shift to "
        "renewables isn’t just happening in boardrooms or parliaments — it’s being pushed "
        "forward from the ground up.",
        html.Br(), html.Br(),
        "That brings us to the final section."
    ], className='paragraph-text'),

    # Hypothesis 6 Section
    html.Div([
        html.Div([
            html.H4([
                "Environmental Activism & Citizen Engagement Accelerate",html.Br(),
                " Renewable Energy Policy and Infrastructure Deployment"]),
            html.P([
                "Renewable adoption is not only a matter of economic logic or technical feasibility —"
                " it’s also about political will. And political will is often forged through public pressure.",
                html.Br(),html.Br(),
                "The following Sankey diagram visualizes the influence flow: from public actors "
                "like NGOs, protest movements, and social media campaigns — to policy adoption, "
                "public investment, and ultimately, real infrastructure change."
            ], className='paragraph-text'),

            html.Div([
                dcc.Graph(id="activism-policy-sankey")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data Source: Conceptual representation derived from multiple qualitative analyses of "
                "environmental policy formation and NGO reports."
            ], style={'fontSize': '0.8rem'}),

            html.Br(),

            html.P([
                "🔍 Analysis:",
                html.Br(),
                "• Environmental NGOs are key drivers of formal policy adoption. Their structured lobbying, "
                "research, and legal interventions play a direct role in shaping regulations.",
                html.Br(), html.Br(),
                "• Climate protests — often seen as symbolic — also push governments toward policy shifts and "
                "stimulate public investment by keeping pressure on institutions and political agendas.",
                html.Br(), html.Br(),
                "• Social media activism, while more diffuse, is increasingly influential. It builds awareness, "
                "mobilizes younger demographics, and amplifies urgency — especially when tied to viral"
                " events or campaigns.",
                html.Br(), html.Br(),
                "💡 Insight:",
                html.Br(),
                "This makes one thing clear: public pressure is not peripheral — it’s catalytic.",
                html.Br(),html.Br(),
                "In countries where political will lags behind economic or technological readiness, grassroots "
                "engagement can bridge the gap. Civil society becomes the engine that turns potential into action.",
                html.Br(),html.Br(),
                "More than ever, citizens are shaping the energy landscape — not just as consumers, but"
                " as advocates, watchdogs, and co-creators of the renewable future.  But that influence"
                " doesn’t arise equally in every country. Some nations see high levels of climate protests, "
                "NGO action, and online advocacy — while others remain quiet, constrained by political, cultural, "
                "or economic limitations.",
                html.Br(), html.Br(),
                "To understand how public engagement varies across the globe, we created an Engagement Index — a "
                "composite metric drawing from climate protest frequency, NGO activity, and social media "
                "activism per country. This choropleth map visualizes those results."
            ], className='paragraph-text'),
        ]),
        html.Br(),

        # 6.2
        html.Div([
            html.Div([
                dcc.Graph(id="engagement-map")
            ], style={'width': '1000px', 'margin': '0 auto'}),

            html.P([
                "Data source: Carnegie Endowment - Climate Protest Tracker - ",
                html.A("Learn More",
                       href="https://carnegieendowment.org/features/climate-protest-tracker?lang=en",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "Carneiro & Tucci - Climate security dialogues on Twitter - ",
                html.A("Learn More",
                       href="https://www.sciencedirect.com/science/article/pii/S235234092400595X",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
                html.Br(),
                "EEB - Membership - ",
                html.A("Learn More",
                       href="https://eeb.org/membership/our-members/",
                       target="_blank", style={'color': 'white', 'textDecoration': 'underline'}),
            ], style={'fontSize': '0.8rem'}),
        ]),
        html.Br(),

        html.P([
            "🔍 Analysis:",
            html.Br(),
            "• Western Europe is a hotspot. Countries like the UK, Germany, France, and Italy show the "
            "highest engagement scores — reflecting frequent climate protests, well-funded environmental "
            "NGOs, and strong digital activism.",
            html.Br(), html.Br(),
            "• Eastern Europe shows growing engagement, especially in countries like Poland and Slovenia"
            " — a newer wave of climate consciousness fueled by youth movements and energy policy shifts.",
            html.Br(), html.Br(),
            "• North America tells a mixed story: Canada scores higher than the United States, likely due "
            "to more centralized climate action efforts and stronger NGO-government ties.",
            html.Br(), html.Br(),
            "• South America has isolated pockets of engagement — particularly in Colombia and Chile — "
            "but overall remains below average.",
            html.Br(), html.Br(),
            "• Africa and large parts of Asia remain on the lower end of the spectrum. This likely "
            "reflects not apathy, but capacity limitations: lower internet access, fewer organized "
            "movements, or political barriers to protest.",
            html.Br(), html.Br(),
            "💡 Insight:",
            html.Br(),
            "Public engagement is a force multiplier — but it’s also unevenly distributed.",
            html.Br(),html.Br(),
            "In high-engagement nations, citizens help shape policy and demand action — often "
            "accelerating investment and reform.",
            html.Br(),html.Br(),
            "In lower-engagement contexts, the risk is that renewables remain top-down — pursued only when convenient "
            "or profitable, not because of societal demand.",
            html.Br(), html.Br(),
            "For a truly global transition, activism, awareness, and access to influence must be scaled — especially "
            "in countries that are most vulnerable to climate change."
        ], className='paragraph-text'),

    ], className="scroll-page", id="hypo6-section"),
    html.Br(),

    # Conclusion

    html.Div([
        html.H4("Conclusion: The Future is Renewable, But the Window is Narrow"),
        html.P([
            "The data is clear: renewable energy adoption is accelerating across many parts of the world, "
            "but progress is uneven. Countries with favorable policies, low costs, and high climate "
            "engagement are surging ahead — while others lag behind, constrained by economic, infrastructural, "
            "or political challenges.",
            html.Br(), html.Br(),
            "Through Energy Nexus, we’ve highlighted five critical points that demonstrate how variables "
            "like cost, policy support, GDP, and civic engagement influence renewable energy "
            "outcomes. The global view reveals a mosaic of ambition, hesitation, and potential.",
            html.Br(),html.Br(),
            "Key Takeaways:",
            html.Br(),
            "Cost still matters — but declining prices are unlocking adoption even in emerging markets.",
            html.Br(),
            "Policy is a game-changer — subsidies, tax breaks, and mandates significantly shape the "
            "trajectory of clean energy.",
            html.Br(),
            "Engagement drives momentum — from NGO activity to public protests and climate-related discourse "
            "online, civic pressure is a measurable force.",
            html.Br(),
            "There’s no one-size-fits-all — local context matters. Adoption strategies must be tailored to "
            "economic realities and energy needs.",
            html.Br(),
            html.H4("🚀 Call to Action: Build the Nexus — Act Now for a Renewable Tomorrow!"),
            html.Br(),
            "This app is more than a dashboard — it's a call for strategic intervention, targeted investment, "
            "and collective action.",
            html.Br(), html.Br(),
            " For Policymakers: Use the insights to fine-tune policy instruments. Where adoption is lagging, "
            "incentivize transitions and build infrastructure. Align national plans "
            "with international climate goals and SDGs.",
            html.Br(), html.Br(),
            " For Businesses: Spot opportunity in the data. Invest in regions ripe for innovation."
            " Partner with governments and communities to deploy solutions where they’re needed most.",
            html.Br(), html.Br(),
            " For Students and Researchers: Let this be a launchpad. Analyze the gaps, ask bold questions, "
            "and develop new models to drive progress further and faster.",
            html.Br(), html.Br(),
            " For Everyone: The energy future is ours to shape. Civic engagement — whether through activism, "
            "education, or voting — continues to influence the direction of national and global priorities.",
            html.Br(), html.Br(), html.Br(), html.Br(),
            html.H4('"The energy choices we make today will define the stability, equity, and livability of our world tomorrow."'),
            html.Br(), html.Br(), html.Br(), html.Br(),


        ], className="paragraph-text", style={'margin': 0, 'fontSize': '1.3rem'}),

    ], className="scroll-page"),



])



################################ CALLBACKS ##############################################

# Hypothesis 1.1
@app.callback(
    Output("renewable-map", "figure"),
    Input("renewable-map", "id")
)
def display_renewable_map(_):
    df = data["renewable_share_energy_df"][
        (data["renewable_share_energy_df"]["Year"] >= 2000) &
        (data["renewable_share_energy_df"]["Year"] <= 2023) &
        data["renewable_share_energy_df"]["Code"].notna()
    ]

    fig = px.choropleth(
        df,
        locations="Code",
        color="Renewables (% equivalent primary energy)",
        hover_name="Entity",
        animation_frame="Year",
        color_continuous_scale="Viridis",
        labels={"Renewables (% equivalent primary energy)": "Renewable Share (%)"},
        title="Global Renewable Energy Adoption (2000–2023): Share of Renewables in National Energy Mix"
    )

    fig.update_geos(
        showcountries=True,
        projection_type="natural earth",
        showframe=False,
        showcoastlines=False
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin={"r": 0, "t": 60, "l": 0, "b": 100},
        geo=dict(
            bgcolor='#0e1111',
            center={"lat": 27.8206, "lon": 25.8025},
            projection_scale=1.3,
        ),
        coloraxis_colorbar=dict(
            len=0.7,
            thickness=75,
            title="Renewables (%)"
        ),
        plot_bgcolor='#0e1111',
        paper_bgcolor='#0e1111',
        font=dict(color='white'),
    )
    return fig

# Hypothesis 1.2
@app.callback(
    Output('import-dependency-graph', 'figure'),
    Input('import-country-dropdown', 'value')
)
def update_import_dependency_chart(selected_countries):
    df = data["energy_im_and_exports_df"].rename(columns={
        'Energy imports, net (% of energy use)': 'Net_Energy_Imports'
    }).dropna(subset=['Year', 'Net_Energy_Imports'])
    df['Year'] = df['Year'].astype(int)

    # Filter last 20 years
    max_year = df['Year'].max()
    df = df[df['Year'] >= (max_year - 19)]

    if not selected_countries:
        return px.bar(title="Please select at least one country.")

    df = df[df['Entity'].isin(selected_countries)]

    # Fill missing year-entity combos for animation
    all_years = sorted(df['Year'].unique())
    full_index = pd.MultiIndex.from_product([all_years, selected_countries], names=["Year", "Entity"])
    df = df.set_index(['Year', 'Entity']).reindex(full_index).reset_index()

    # Add sort rank per frame
    df['sort_order'] = df.groupby('Year')['Net_Energy_Imports'].rank(ascending=True, method='first')

    # Sort by year and rank for plotly to honor the y-axis order per frame
    df = df.sort_values(by=['Year', 'sort_order'])

    # Convert sort_order into a pseudo-category (Entity + Rank) to enforce order
    df['Entity_Sorted'] = df['Entity'] + ' '

    fig = px.bar(
        df,
        x='Net_Energy_Imports',
        y='Entity',
        orientation='h',
        animation_frame='Year',
        color='Net_Energy_Imports',
        color_continuous_scale='RdBu',
        labels={
            'Entity': 'Country',
            'Net_Energy_Imports': 'Net Energy Imports (%)'
        },
        title='Net Energy Imports Over Time (Selected Countries)'
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0.0)',
        font=dict(color='white'),
        xaxis_title='Net Energy Imports (% of total energy use)',
        yaxis_title='',
        xaxis_range=[-100, 100],
        transition={'duration': 500}
    )

    return fig

# Hypothesis 1.3
@app.callback(
    Output("fossil-vs-import-bubble", "figure"),
    Input("fossil-vs-import-bubble", "id")
)
def update_fossil_import_bubble(_):
    df = data["bubble_2013_df"].copy()
    df = df.dropna(subset=["Fossil_Fuel_%", "Energy imports, net (% of energy use)", "Energy_Import_Bill_%GDP"])

    fig = px.scatter(
        df,
        x='Fossil_Fuel_%',
        y='Energy imports, net (% of energy use)',
        size='Energy_Import_Bill_%GDP',
        color='Country',
        hover_name='Country',
        size_max=40,
        title='Fossil Fuel Dependency vs Net Energy Imports (2013)',
        labels={
            'Fossil_Fuel_%': 'Fossil Fuel Energy Consumption (%)',
            'Energy imports, net (% of energy use)': 'Net Energy Imports (%)',
            'Energy_Import_Bill_%GDP': 'Import Bill as % of GDP'
        }
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis_title='Fossil Fuel Energy Consumption (%)',
        yaxis_title='Net Energy Imports (%)',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)'
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)'
        )
    )

    return fig


# Hypothesis 2.1
@app.callback(
    Output("global-energy-price-index-trend", "figure"),
    Input("global-energy-price-index-trend", "id")
)
def update_energy_price_index_trend(_):
    fossil_avg = data["fossil_avg_index"]
    renewable_avg = data["renewable_avg_index"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=fossil_avg["Year"],
        y=fossil_avg["Coal price index"],
        mode="lines+markers",
        name="Coal Price Index",
        line=dict(color="#9b5de5", dash="dash")
    ))

    fig.add_trace(go.Scatter(
        x=fossil_avg["Year"],
        y=fossil_avg["Oil spot crude price index"],
        mode="lines+markers",
        name="Oil Spot Crude Price Index",
        line=dict(color="#3a86ff", dash="dash")
    ))

    fig.add_trace(go.Scatter(
        x=renewable_avg["Year"],
        y=renewable_avg["Solar energy index"],
        mode="lines+markers",
        name="Solar Energy Index",
        line=dict(color="#ff4d6d")
    ))

    fig.add_trace(go.Scatter(
        x=renewable_avg["Year"],
        y=renewable_avg["Wind energy index"],
        mode="lines+markers",
        name="Wind Energy Index",
        line=dict(color="#2ec4b6")
    ))

    fig.update_layout(
        title="Global Average Energy Price Indices Over Time",
        xaxis_title="Year",
        yaxis_title="Energy Price Index (Normalized to 2019 = 100)",
        autosize=False,
        width=1000,
        height=600,
        plot_bgcolor='rgba(255,255,255,0)',
        paper_bgcolor='rgba(255,255,255,0.1)',
        font=dict(color='white'),
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.15)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.15)'),
        legend=dict(orientation='h', yanchor='bottom', y=-0.25, xanchor='center', x=0.5)
    )

    return fig


# Hypothesis 2.2
@app.callback(
    Output("investment-vs-patents-graph", "figure"),
    Input("investment-vs-patents-graph", "id")
)
def update_investment_vs_patents(_):
    df = data["investment_patent_df"].copy()

    fig = px.scatter(
        df,
        x="Total Investment",
        y="Total Patents",
        color="Year",
        color_continuous_scale="Turbo",
        title="Global Renewable Investment vs Patent Filings",
        labels={
            "Total Investment": "Total Investment in Renewables (USD)",
            "Total Patents": "Total Renewable Energy Patents Filed"
        }
    )

    fig.update_traces(marker=dict(
        size=12,
        symbol='diamond',
        line=dict(width=1, color='black')
    ))

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0.0)',
        font=dict(color='white'),
        xaxis_title='Total Investment in Renewables (USD)',
        yaxis_title='Total Patents Filed',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        coloraxis_colorbar=dict(title="Year")
    )

    return fig

# Hypothesis 2.3
@app.callback(
    Output("asean-electricity-trend", "figure"),
    Input("asean-year-slider", "value"),
    Input("asean-line-toggle", "value")
)
def update_asean_trend(year_range, toggle_options):
    df = data["asean_energy_df"].copy()
    df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

    fig = go.Figure()

    if 'renewables' in toggle_options:
        fig.add_trace(go.Scatter(
            x=df["Year"],
            y=df["Renewables - % electricity"],
            name="Renewables",
            mode="lines+markers",
            line=dict(color="#7ce38b", width=3)
        ))

    if 'fossil' in toggle_options:
        fig.add_trace(go.Scatter(
            x=df["Year"],
            y=df["Fossil fuels - % electricity"],
            name="Fossil Fuels",
            mode="lines+markers",
            line=dict(color="#fa7970", width=3, dash="dash"),
            yaxis="y2"
        ))

    fig.update_layout(
        title="ASEAN Electricity Generation: Renewables vs Fossil Fuels Over Time",
        xaxis=dict(title=dict(text="Year", font=dict(color='white'))),
        yaxis=dict(title=dict(text="Renewables (% of Electricity)", font=dict(color="#7ce38b"))),
        yaxis2=dict(title=dict(text="Fossil Fuels (% of Electricity)", font=dict(color="#fa7970")),
                    overlaying='y', side='right'),
        legend=dict(x=0.5, y=-0.25, orientation='h', xanchor='center'),
        autosize=False,
        width=1000,
        height=600,
        margin=dict(r=0, t=40, l=0, b=60),
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
    )

    return fig

# Hypothesis 2.4
@app.callback(
    Output('model2-4-renewable-share-pie', 'figure'),
    Input('model2-4-country-dropdown', 'value'),
    Input('model2-4-year-slider', 'value')
)
def update_model_2_4_pie(country, year):
    df = data["consumption_df"][(data["consumption_df"]["Entity"] == country) & (data["consumption_df"]["Year"] == year)]

    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            title=f"No data available for {country} in {year}",
            autosize=False,
            width=1000,
            height=600,
            paper_bgcolor='rgba(255,255,255,0.1)',
            plot_bgcolor='rgba(255,255,255,0)',
            font=dict(color='white')
        )
        return fig

    renewable_total = df[data["renewable_sources"]].sum(axis=1).values[0]
    total_consumption = df[data["total_sources"]].sum(axis=1).values[0]
    other_total = total_consumption - renewable_total

    fig = go.Figure(data=[
        go.Pie(
            labels=["Renewable Electricity", "Fossil & Other Electricity"],
            values=[renewable_total, other_total],
            hole=0.45,
            marker=dict(colors=["#00cc96", "#ef553b"]),
            textinfo='label+percent',
            insidetextorientation='radial'
        )
    ])

    fig.update_layout(
        title={
            'text': f"{country} – Share of Renewable Electricity in Household Energy ({year})",
            'x': 0.5,
            'xanchor': 'center'
        },
        autosize=False,
        width=1000,
        height=600,
        margin=dict(l=0, r=0, t=60, b=40),
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=-0.2,
            xanchor='center',
            x=0.5
        )
    )

    return fig

# Hypothesis 2.5
@app.callback(
    Output('energy-affordability-chart', 'figure'),
    Input('affordability-country-dropdown', 'value')
)
def update_energy_affordability_chart(country):
    fossil = data["fossil_df"][data["fossil_df"]["Entity"] == country].set_index("Year")
    renewable = data["renewable_df"][data["renewable_df"]["Entity"] == country].set_index("Year")
    renewable = renewable.drop(columns=["Entity"], errors='ignore')

    combined = fossil.join(renewable, how="inner")
    combined = combined.rename(columns={
        "Coal price index": "Coal",
        "Solar energy index": "Solar",
        "Wind energy index": "Wind"
    })
    combined = combined[["Coal", "Solar", "Wind"]].dropna()

    if combined.empty:
        fig = go.Figure()
        fig.update_layout(
            title=f"No data available for {country}",
            autosize=False,
            width=1000,
            height=600,
            paper_bgcolor='rgba(255,255,255,0.1)',
            plot_bgcolor='rgba(255,255,255,0)',
            font=dict(color='white')
        )
        return fig

    combined["Renewables (Avg)"] = 100 - combined[["Solar", "Wind"]].mean(axis=1)
    combined["Fossil Fuel (Coal)"] = combined["Coal"]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=combined.index.astype(str),
        y=combined["Renewables (Avg)"],
        name="Renewables (Avg)",
        marker_color="#6366f1",
    ))
    fig.add_trace(go.Bar(
        x=combined.index.astype(str),
        y=combined["Fossil Fuel (Coal)"],
        name="Coal Price Index",
        marker_color="#ff6e6c",
    ))

    fig.update_layout(
        barmode='group',
        title=f"{country}: Renewables vs Coal Affordability Index Over Time",
        xaxis_title="Year",
        yaxis_title="Affordability Index (Higher = More Affordable)",
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.08)',
            tickangle=45,
            linecolor='rgba(255,255,255,0.15)'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.08)',
            linecolor='rgba(255,255,255,0.15)',
            zerolinecolor='rgba(255,255,255,0.2)'
        ),
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        legend = dict(
            orientation='h',
            yanchor='bottom',
            y=-0.25,
            xanchor='center',
            x=0.5
        )
    )

    return fig

# Hypothesis 3.1
@app.callback(
    Output('tech-cost-vs-renewables-graph', 'figure'),
    Input('tech-category-dropdown', 'value')
)
def update_tech_cost_vs_renewables(selected_category):
    lcoe_df = data["lcoe_df"]
    elec_mix_df = data["elec_mix_df"]

    fig = go.Figure()

    # Add energy adoption trends
    fig.add_trace(go.Scatter(
        x=elec_mix_df['Year'],
        y=elec_mix_df['renewable_generation__twh_chart_elec_mix_bar'],
        mode='lines',
        name='Total Renewable Generation (TWh)',
        line=dict(color='limegreen', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=elec_mix_df['Year'],
        y=elec_mix_df['fossil_generation__twh_chart_elec_mix_bar'],
        mode='lines',
        name='Fossil Fuel Generation (TWh)',
        line=dict(color='tomato', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=elec_mix_df['Year'],
        y=elec_mix_df['nuclear_generation__twh_chart_elec_mix_bar'],
        mode='lines',
        name='Nuclear Generation (TWh)',
        line=dict(color='skyblue', width=2)
    ))

    # Filter and plot LCOE data
    if selected_category == 'All Renewables':
        filtered_lcoe = lcoe_df[lcoe_df["Plant category"].str.contains("renewable", case=False, na=False)]
    else:
        filtered_lcoe = lcoe_df[lcoe_df["Plant category"] == selected_category]

    for plant_type in filtered_lcoe["Plant type"].unique():
        subset = filtered_lcoe[filtered_lcoe["Plant type"] == plant_type]
        fig.add_trace(go.Scatter(
            x=subset['Country'],
            y=subset['Total capital costs (USD/MWh)'],
            mode='markers+lines',
            name=f"{plant_type} Cost",
            line=dict(dash='dash')
        ))

    fig.update_layout(
        title="Renewable Adoption vs Technology Capital Costs",
        xaxis_title="Year / Country",
        yaxis_title="Value (TWh or USD/MWh)",
        autosize=False,
        width=1000,
        height=600,
        plot_bgcolor='rgba(255,255,255,0.0)',
        paper_bgcolor='rgba(255,255,255,0.1)',
        font=dict(color='white'),
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        legend=dict(orientation='h', yanchor='bottom', y=-0.25, xanchor='center', x=0.5)
    )

    return fig

# Hypothesis 3.2
@app.callback(
    Output('correlation-scatter', 'figure'),
    Input('correlation-tech-dropdown', 'value')
)
def update_corr_scatter(selected_tech):
    df = data["corr_df"]
    y_col = "renewable_generation__twh_chart_elec_mix_bar"

    # Create scatter plot with enhancements
    fig = px.scatter(
        df,
        x=selected_tech,
        y=y_col,
        hover_data=['Year'],
        trendline="ols",
        opacity=0.6,  # Add transparency to handle overplotting
        labels={
            selected_tech: "Cost ($/MWh)",
            y_col: "Renewable Generation (TWh)"
        },
        title=f"Correlation Between {selected_tech.replace('_', ' ').title()} Cost and Renewable Adoption"
    )

    # Optional: log scale for better distribution visibility
    fig.update_yaxes(type="log")  # Comment this out if log isn't appropriate

    # Optional: Trendline emphasis
    fig.update_traces(marker=dict(size=7), selector=dict(mode='markers'))

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)',
            title_standoff=10
        ),
        margin=dict(t=40, b=60, l=60, r=10)
    )

    return fig


# Hypothesis 3.3
@app.callback(
    Output('tech-cost-grouped-bar-chart', 'figure'),
    Input('tech-cost-country-dropdown', 'value'),
    Input('tech-cost-tech-dropdown', 'value')
)
def update_tech_cost_grouped_bar(selected_country, selected_techs):
    df = data["cost_merged_df"]

    filtered = df[
        (df["Entity"] == selected_country) &
        (df["Technology"].isin(selected_techs)) &
        (df["Year"] >= 2000)  # ✅ Filter for year 2000 onwards
        ]

    if filtered.empty:
        fig = go.Figure()
        fig.update_layout(
            title=f"No data available for {selected_country} with selected technologies",
            autosize=False,
            width=1000,
            height=650,
            paper_bgcolor='rgba(255,255,255,0.1)',
            plot_bgcolor='rgba(255,255,255,0)',
            font=dict(color='white')
        )
        return fig

    fig = px.bar(
        filtered,
        x="Year",
        y="Cost (USD/MWh)",
        color="Technology",
        barmode='group',
        title=f"Cost of Renewable Technologies Over Time – {selected_country}"
    )

    fig.update_traces(marker_line_width=0.5)
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        bargap=0.1,  # Smaller gap between groups (default ~0.2)
        bargroupgap=0.05,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis_title='',
        yaxis_title='Cost (USD/MWh)',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        xaxis=dict(tickangle=45),
        legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5)
    )

    return fig

# Hypothesis 3.4
@app.callback(
    Output("investment-vs-cost-lineplot", "figure"),
    Input("lineplot-country-dropdown", "value"),
    Input("lineplot-tech-dropdown", "value")
)
def update_lineplot(country, tech):
    df = data["heatmap_long_df"]

    inv_df = df[
        (df["Entity"] == country) &
        (df["Technology"].str.lower().str.contains("energy"))
    ].groupby("Year")["Value"].sum().reset_index(name="Total Investment")

    cost_df = df[
        (df["Entity"] == country) &
        (df["Technology"] == tech)
    ][["Year", "Value"]].rename(columns={"Value": "Cost (USD/MWh)"})

    fig = go.Figure()

    # Investment line (left Y-axis)
    fig.add_trace(go.Scatter(
        x=inv_df["Year"],
        y=inv_df["Total Investment"] / 1e9,  # convert to billion USD
        name="Total Investment (Billion USD)",
        mode="lines+markers",
        line=dict(color="gold")
    ))

    # Cost line (right Y-axis)
    fig.add_trace(go.Scatter(
        x=cost_df["Year"],
        y=cost_df["Cost (USD/MWh)"],
        name=f"{tech.replace('_', ' ').title()} Cost ($/MWh)",
        mode="lines+markers",
        line=dict(color="deepskyblue"),
        yaxis="y2"
    ))

    fig.update_layout(
        title=f"{country} – Investment vs {tech.replace('_', ' ').title()} Cost",
        xaxis=dict(title="Year"),
        yaxis=dict(
            title=dict(text="Investment (Billion USD)", font=dict(color="orange")),
            tickfont=dict(color="orange")
        ),
        yaxis2=dict(
            title=dict(text="Cost ($/MWh)", font=dict(color="skyblue")),
            tickfont=dict(color="skyblue"),
            overlaying="y",
            side="right"
        ),
        legend=dict(orientation='h', x=0.5, xanchor='center', y=-0.25),
        autosize=False,
        width=1000,
        height=600,
        plot_bgcolor='rgba(255,255,255,0)',
        paper_bgcolor='rgba(255,255,255,0.1)',
        font=dict(color='white'),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    return fig



# Hypothesis 3.5
@app.callback(
    Output("slope-renewable-capacity", "figure"),
    Input("slope-chart-mode", "value"),
    Input("slope-tech-dropdown", "value")
)
def update_slope_chart(chart_mode, selected_techs):
    df = data["global_capacity_df"].copy()
    df = df.dropna(subset=["Year", "capacity", "Entity"])
    df["Year"] = df["Year"].astype(int)

    # Filter by selected technologies
    if selected_techs:
        df = df[df["Entity"].isin(selected_techs)]
    else:
        return go.Figure().update_layout(
            title="No technologies selected.",
            paper_bgcolor='rgba(255,255,255,0.1)',
            plot_bgcolor='rgba(255,255,255,0)',
            font=dict(color='white'),
            width=1000,
            height=600
        )

    fig = go.Figure()

    for entity in df["Entity"].unique():
        entity_data = df[df["Entity"] == entity]
        if len(entity_data["Year"].unique()) > 1:
            if chart_mode == 'line':
                fig.add_trace(go.Scatter(
                    x=entity_data["Year"],
                    y=entity_data["capacity"],
                    mode='lines+markers',
                    name=entity,
                    marker=dict(size=6),
                    line=dict(width=2)
                ))
            elif chart_mode == 'area':
                fig.add_trace(go.Scatter(
                    x=entity_data["Year"],
                    y=entity_data["capacity"],
                    mode='lines',
                    name=entity,
                    fill='tozeroy',
                    line=dict(width=0.5),
                    hoverinfo='x+y+name'
                ))

    fig.update_layout(
        title="Installed Renewable Energy Capacity by Technology",
        xaxis=dict(
            title="Year",
            tickangle=30,
            tickmode='linear',
            dtick=2,
            ticklabelposition="outside bottom",
            automargin=True,
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(
            title="Installed Capacity (GW)",
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)'
        ),
        margin=dict(t=40, b=80, l=0, r=0),
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        legend=dict(orientation='h', yanchor='bottom', y=-0.25, xanchor='center', x=0.5)
    )

    return fig



# Hypothesis 4.1
@app.callback(
    Output("solar-capacity-growth-graph", "figure"),
    Input("solar-country-dropdown", "value")
)
def update_solar_capacity_graph(selected_countries):
    df = data["solar_capacity_df"].rename(columns={"Solar energy capacity": "Installed Capacity (GW)"})
    if selected_countries:
        df = df[df['Entity'].isin(selected_countries)]
    else:
        df = df[df['Entity'] == 'World']

    df = df[df['Year'].notna()]
    df['Year'] = df['Year'].astype(int)

    fig = px.line(
        df,
        x="Year",
        y="Installed Capacity (GW)",
        color="Entity",
        markers=True,
        hover_data={"Installed Capacity (GW)": ':.2f', "Year": True, "Entity": True},
        title="Installed Solar PV Capacity Over Time",
        color_discrete_sequence=[
            "#ff5722", "#ff7043", "#ff8a65", "#f44336",
            "#e53935", "#d32f2f", "#ff9800", "#ffa726"
        ]
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0.)',
        font=dict(color='white'),
        xaxis_title='Year',
        yaxis_title='Installed Capacity (GW)',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
    )

    return fig


# Hypothesis 4.2
@app.callback(
    Output("renewable-share-area-graph", "figure"),
    Input("renewable-area-year-slider", "value"),
    Input("renewable-source-selector", "value")
)
def update_renewable_area_chart(year_range, selected_sources):
    df = data["renewable_melted"].copy()

    # Filter by year range
    df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

    # Filter by selected sources
    if selected_sources:
        df = df[df["Source"].isin(selected_sources)]
    else:
        df = df[df["Source"] == "Solar"]  # Fallback

    fig = px.area(
        df,
        x="Year",
        y="Share",
        color="Source",
        groupnorm='percent',
        labels={"Share": "Share of Renewable Electricity (%)", "Year": "Year", "Source": "Energy Source"},
        title="Share of Electricity Production from Solar and Other Renewables",
        color_discrete_map={
            "Solar": "gold",
            "Wind": "deepskyblue",
            "Hydro": "royalblue",
            "Bioenergy": "forestgreen"
        }
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        plot_bgcolor='rgba(255,255,255,0)',
        paper_bgcolor='rgba(255,255,255,0.1)',
        font=dict(color='white'),
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        legend=dict(title="Source")
    )

    return fig


#Hypothesis 4.3
@app.callback(
    Output("solar-share-bar-graph", "figure"),
    Input("solar-share-year-slider", "value")
)
def update_solar_share_bar_chart(selected_year_range):
    df = data["solar_share_energy_df"].copy()
    df = df.dropna(subset=["Solar Share (%)"])
    df["Year"] = df["Year"].astype(int)

    # Filter to selected range
    start_year, end_year = selected_year_range
    df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

    fig = px.bar(
        df,
        x="Year",
        y="Solar Share (%)",
        title="Solar Energy’s Share in Primary Energy Consumption",
        color_discrete_sequence=["gold"]
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis_title='Year',
        yaxis_title='Share of Primary Energy from Solar (%)',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        xaxis=dict(tickangle=45),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
    )

    return fig


# Hypothesis 4.4
@app.callback(
    Output("solar-consumption-graph", "figure"),
    Input("solar-consumption-dropdown", "value")
)
def update_solar_consumption_chart(selected_regions):
    df = data["solar_consumption_df"].copy()

    # Filter for last 20 years
    latest_year = df["Year"].max()
    df = df[df["Year"] >= (latest_year - 19)]

    # Filter for selected regions
    if selected_regions:
        df = df[df["Entity"].isin(selected_regions)]
    else:
        df = df[df["Entity"] == "World"]

    df = df.sort_values(by=["Entity", "Year"])

    fig = px.bar(
        df,
        x="Year",
        y="solar_generation__twh",
        color="Entity",
        barmode="stack",
        title="Solar Power Generation by Region (Last 20 Years)",
        labels={
            "Year": "Year",
            "solar_generation__twh": "Solar Power Generation (TWh)",
            "Entity": "Region"
        },
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis_title='Year',
        yaxis_title='Solar Generation (TWh)',
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        xaxis=dict(tickangle=45),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
    )

    return fig


# Hypothesis 5.1
@app.callback(
    Output('radar-chart', 'figure'),
    Input('radar-toggle-mode', 'value'),
    Input('continent-dropdown', 'value')
)
def update_radar_chart(mode, continent):
    continent_countries = {
        "Africa": ["Nigeria", "South Africa", "Egypt", "Morocco", "Kenya"],
        "Asia": ["India", "China", "Japan", "Indonesia", "South Korea"],
        "Europe": ["Germany", "France", "United Kingdom", "Italy", "Spain"],
        "North America": ["United States", "Canada", "Mexico"],
        "South America": ["Brazil", "Argentina", "Chile"],
        "Oceania": ["Australia", "New Zealand"]
    }

    renewable_cols = ['Solar', 'Wind', 'Hydro', 'Biofuels', 'Other RE']

    if mode == 'single':
        countries = continent_countries[continent]
        radar_df = data["consumption_df"][
            (data["consumption_df"]['Entity'].isin(countries)) &
            (data["consumption_df"]['Year'] == 2020)
        ].copy()

        radar_df = radar_df.rename(columns={
            'Solar consumption - TWh': 'Solar',
            'Wind consumption - TWh': 'Wind',
            'Hydro consumption - TWh': 'Hydro',
            'Biofuels consumption - TWh': 'Biofuels',
            'Other renewables (including geothermal and biomass) - TWh': 'Other RE'
        })
        radar_df[renewable_cols] = radar_df[renewable_cols].fillna(0)
        radar_df['Total RE'] = radar_df[renewable_cols].sum(axis=1)
        for col in renewable_cols:
            radar_df[f'{col} %'] = (radar_df[col] / radar_df['Total RE']) * 100

        fig = go.Figure()
        for _, row in radar_df.iterrows():
            values = [row[f'{col} %'] for col in renewable_cols]
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=renewable_cols,
                fill='toself',
                name=row['Entity']
            ))

        # Calculate dynamic radial axis max
        max_value = radar_df[[f'{col} %' for col in renewable_cols]].max().max()
        radial_max = min(100, (max_value + 10))  # Add buffer, cap at 100

        fig.update_layout(
            title=f"Renewable Energy Diversification – {continent} (2020)",
            polar=dict(
                radialaxis=dict(visible=True, range=[0, radial_max], color='white'),
                bgcolor='rgba(255,255,255,0.05)'
            ),
            font=dict(color='white'),
            paper_bgcolor='rgba(255,255,255,0.1)',
            plot_bgcolor='rgba(255,255,255,0)',
            width=1000,
            height=600,
            margin={"r": 0, "t": 40, "l": 0, "b": 40},
            legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5)
        )
        return fig

    else:
        from plotly.subplots import make_subplots
        rows, cols = 2, 3
        fig = make_subplots(
            rows=rows, cols=cols,
            subplot_titles=list(continent_countries.keys()),
            specs=[[{'type': 'polar'}]*cols]*rows
        )

        for idx, (cont, countries) in enumerate(continent_countries.items()):
            radar_df = data["consumption_df"][
                (data["consumption_df"]['Entity'].isin(countries)) &
                (data["consumption_df"]['Year'] == 2020)
            ].copy()

            radar_df = radar_df.rename(columns={
                'Solar consumption - TWh': 'Solar',
                'Wind consumption - TWh': 'Wind',
                'Hydro consumption - TWh': 'Hydro',
                'Biofuels consumption - TWh': 'Biofuels',
                'Other renewables (including geothermal and biomass) - TWh': 'Other RE'
            })
            radar_df[renewable_cols] = radar_df[renewable_cols].fillna(0)
            radar_df['Total RE'] = radar_df[renewable_cols].sum(axis=1)
            for col in renewable_cols:
                radar_df[f'{col} %'] = (radar_df[col] / radar_df['Total RE']) * 100

            r = (idx // cols) + 1
            c = (idx % cols) + 1

            for _, row in radar_df.iterrows():
                values = [row[f'{col} %'] for col in renewable_cols]
                fig.add_trace(
                    go.Scatterpolar(
                        r=values,
                        theta=renewable_cols,
                        fill='toself',
                        name=row['Entity'],
                        showlegend=False
                    ),
                    row=r, col=c
                )

            # Calculate dynamic radial axis max
            max_value = radar_df[[f'{col} %' for col in renewable_cols]].max().max()
            radial_max = min(100, (max_value + 10))  # Add buffer, cap at 100

            fig.update_layout(
                height=850,
                width=1200,
                title_text="Renewable Energy Diversification by Continent (2020)",
                font=dict(color='white'),
                paper_bgcolor='rgba(255,255,255,0.1)',
                plot_bgcolor='rgba(255,255,255,0)',
                margin={"r": 20, "t": 50, "l": 20, "b": 40},
            )

            # Manually update each polar subplot’s layout
            for i in range(1, 7):  # You have 6 subplots (2 rows x 3 columns)
                fig.update_layout({
                    f'polar{i}': dict(
                        radialaxis=dict(visible=True, range=[0, radial_max], color='white'),
                        bgcolor='rgba(255,255,255,0.05)'
                    )
                })

        return fig

# Hypothesis 5.2
@app.callback(
    Output("renewable-vs-fossil-scatter", "figure"),
    Input("renewable-vs-fossil-scatter", "id")
)
def update_renewable_vs_fossil_scatter(_):
    df = data["renewable_vs_fossil_df"].copy()

    fig = px.scatter(
        df,
        x="Fossil Import Share (%)",
        y="Renewable Share (%)",
        animation_frame="Year",
        animation_group="Country",
        color="Country",
        hover_name="Country",
        title="Renewable Energy vs Fossil Fuel Imports (2000–2023)",
        labels={
            "Fossil Import Share (%)": "% Fossil Fuel Imports",
            "Renewable Share (%)": "% Renewable Energy"
        },
        size_max=55
    )

    quadrant_shapes = [
        dict(x0=-20, x1=50, y0=40, y1=80, type="rect", fillcolor="rgba(0,255,0,0.08)", line_width=0, layer="below"),
        dict(x0=50, x1=100, y0=40, y1=80, type="rect", fillcolor="rgba(255,255,0,0.08)", line_width=0, layer="below"),
        dict(x0=-20, x1=50, y0=0, y1=40, type="rect", fillcolor="rgba(0,191,255,0.08)", line_width=0, layer="below"),
        dict(x0=50, x1=100, y0=0, y1=40, type="rect", fillcolor="rgba(255,0,0,0.08)", line_width=0, layer="below"),
    ]

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(255,255,255,0.1)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='white'),
        xaxis=dict(title="% Fossil Fuel Imports", range=[-20, 100], fixedrange=True),
        yaxis=dict(title="% Renewable Energy", range=[0, 80], fixedrange=True),
        margin={"r": 0, "t": 40, "l": 0, "b": 40},
        shapes=quadrant_shapes
    )

    for frame in fig.frames:
        frame.layout = go.Layout(
            yaxis=dict(range=[0, 80]),
            shapes=quadrant_shapes
        )

    return fig

# Hypothesis 6.1
@app.callback(
    Output("activism-policy-sankey", "figure"),
    Input("activism-policy-sankey", "id")
)
def update_sankey_diagram(_):
    sankey = data["sankey_data"]

    # Use a gradient color palette for nodes
    node_colors = [
        "#636EFA",  # Blue
        "#EF553B",  # Red-orange
        "#00CC96",  # Green
        "#AB63FA",  # Purple
        "#FFA15A",  # Orange
        "#19D3F3"   # Cyan
    ]

    # Match links to source node colors with transparency
    link_colors = [
        "rgba(99, 110, 250, 0.4)",   # Blue semi-transparent
        "rgba(239, 85, 59, 0.4)",    # Red-orange
        "rgba(0, 204, 150, 0.4)",    # Green
        "rgba(171, 99, 250, 0.4)",   # Purple
        "rgba(255, 161, 90, 0.4)",   # Orange
        "rgba(25, 211, 243, 0.4)"    # Cyan
    ]

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=0.8),
            label=sankey["nodes"],
            color=node_colors
        ),
        link=dict(
            source=sankey["links"]["source"],
            target=sankey["links"]["target"],
            value=sankey["links"]["value"],
            label=sankey["links"]["label"],
            color=link_colors
        )
    ))

    fig.update_layout(
        title_text="Public Influence on Renewable Energy Policy & Infrastructure",
        font_size=14,
        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',  # transparent background
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        margin=dict(l=0, r=0, t=40, b=20),
    )

    return fig


# Hypothesis 6.2
@app.callback(
    Output("engagement-map", "figure"),
    Input("engagement-map", "id")
)
def update_engagement_map(_):
    from sklearn.preprocessing import MinMaxScaler
    import plotly.express as px

    ngo_df = data["ngo_df"]
    protest_df = data["protest_df"]
    tweet_df = data["tweet_df"]

    # Count per country
    ngo_counts = ngo_df['Country'].value_counts().reset_index()
    ngo_counts.columns = ['Country', 'NGO_Count']

    protest_counts = protest_df['Location'].value_counts().reset_index()
    protest_counts.columns = ['Country', 'Protest_Count']

    tweet_mentions = tweet_df['dataset_CS$countries_mentioned'].dropna().str.split(", ")
    tweet_flat = tweet_mentions.explode()
    tweet_country_counts = tweet_flat.value_counts().reset_index()
    tweet_country_counts.columns = ['Country', 'Tweet_Count']

    # Merge and scale
    df = pd.merge(ngo_counts, protest_counts, on='Country', how='outer')
    df = pd.merge(df, tweet_country_counts, on='Country', how='outer')
    df[['NGO_Count', 'Protest_Count', 'Tweet_Count']] = df[['NGO_Count', 'Protest_Count', 'Tweet_Count']].fillna(0)

    scaler = MinMaxScaler()
    df[['NGO_Scaled', 'Protest_Scaled', 'Tweet_Scaled']] = scaler.fit_transform(
        df[['NGO_Count', 'Protest_Count', 'Tweet_Count']]
    )
    df['Engagement_Index'] = df[['NGO_Scaled', 'Protest_Scaled', 'Tweet_Scaled']].mean(axis=1)

    # Create choropleth map using px
    fig = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Engagement_Index",
        hover_name="Country",
        hover_data={
            "Country": False,
            "Engagement_Index": ':.2f',
            "NGO_Count": True,
            "Protest_Count": True,
            "Tweet_Count": True
        },
        color_continuous_scale="Turbo",
        title = "Global Civic Engagement in Climate Action"
    )

    fig.update_geos(
        showcountries=True,
        projection_type="natural earth",
        showframe=False,
        showcoastlines=False
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin={"r": 0, "t": 60, "l": 0, "b": 100},
        geo=dict(
            bgcolor='#0e1111',
            center={"lat": 43.132328, "lon": -39.589356},
            projection_scale=1.5,
        ),
        coloraxis_colorbar=dict(
            len=0.7,
            thickness=75,
            title="Engagement<br>Index"
        ),
        plot_bgcolor='#0e1111',
        paper_bgcolor='#0e1111',
        font=dict(color='white'),
    )

    return fig


# Run app
if __name__ == '__main__':
    app.run(debug=True)
