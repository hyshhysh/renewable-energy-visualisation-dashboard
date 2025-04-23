import pandas as pd

def load_data():
    data = {}

    # Hypothesis 1
    data["renewable_share_energy_df"] = pd.read_csv('data/renewable-share-energy.csv')
    data["energy_im_and_exports_df"] = pd.read_csv('data/energy-imports-and-exports-energy-use.csv')
    data["bubble_2013_df"] = pd.read_csv("data/merged_energy_data_2013.csv")

    # Hypothesis 2
    renewable_vs_fossil_df = pd.read_excel("data/renewable_vs_fossil_imports_2000_2023.xlsx")
    data["renewable_vs_fossil_df"] = renewable_vs_fossil_df[
        (renewable_vs_fossil_df['Year'] >= 2000) & (renewable_vs_fossil_df['Year'] <= 2023)
    ]

    investment_df = pd.read_csv("data/investment-in-renewable-energy-by-technology.csv")
    patents_df = pd.read_csv("data/patents-filed-for-renewables.csv")
    investment_by_year = investment_df.groupby("Year").sum(numeric_only=True)
    investment_by_year["Total Investment"] = investment_by_year.sum(axis=1)
    patents_world = patents_df[patents_df["Entity"] == "World"]
    patents_by_year = patents_world.groupby("Year").sum(numeric_only=True)
    patents_by_year["Total Patents"] = patents_by_year.sum(axis=1)
    data["investment_patent_df"] = pd.merge(
        investment_by_year[["Total Investment"]],
        patents_by_year[["Total Patents"]],
        left_index=True,
        right_index=True,
        how="inner"
    ).reset_index()

    asean_df = pd.read_csv("data/electricity-fossil-renewables-nuclear-line.csv")
    asean_df = asean_df[asean_df["Entity"] == "ASEAN (Ember)"]
    data["asean_energy_df"] = asean_df[["Year", "Renewables - % electricity", "Fossil fuels - % electricity"]].dropna()

    consumption_df = pd.read_csv("data/energy-consumption-by-source-and-country.csv")
    data["consumption_df"] = consumption_df

    renewable_sources = [
        "Solar consumption - TWh",
        "Wind consumption - TWh",
        "Hydro consumption - TWh",
        "Other renewables (including geothermal and biomass) - TWh"
    ]
    total_sources = renewable_sources + [
        "Coal consumption - TWh",
        "Gas consumption - TWh",
        "Oil consumption - TWh",
        "Nuclear consumption - TWh"
    ]
    valid_countries = sorted(consumption_df.dropna(subset=total_sources)["Entity"].unique())
    data["renewable_sources"] = renewable_sources
    data["total_sources"] = total_sources
    data["valid_consumption_countries"] = valid_countries

    fossil_df = pd.read_csv("data/cleaned_fossil_fuels_energy_index.csv")
    renewable_df = pd.read_csv("data/cleaned_renewable_energy_index.csv")
    available_fossil = fossil_df.dropna(subset=["Coal price index"])
    available_renew = renewable_df.dropna(subset=["Solar energy index", "Wind energy index"])
    data["fossil_df"] = fossil_df
    data["renewable_df"] = renewable_df
    data["common_afford_countries"] = sorted(set(available_fossil["Entity"]).intersection(available_renew["Entity"]))

    # Hypothesis 4
    solar_df = pd.read_csv("data/installed-solar-pv-capacity.csv")
    solar_df = solar_df.dropna(subset=["Solar energy capacity", "Year", "Entity"])
    solar_df["Year"] = solar_df["Year"].astype(int)
    data["solar_capacity_df"] = solar_df
    data["available_countries"] = sorted(solar_df["Entity"].unique())

    renewable_prod_df = pd.read_csv("data/modern-renewable-prod.csv")
    renewable_global = renewable_prod_df.groupby("Year").sum()
    renewable_global["Total Renewable"] = (
        renewable_global["Electricity from wind (TWh)"] +
        renewable_global["Electricity from hydro (TWh)"] +
        renewable_global["Electricity from solar (TWh)"] +
        renewable_global["Other renewables including bioenergy (TWh)"]
    )
    renewable_global["Solar"] = (renewable_global["Electricity from solar (TWh)"] / renewable_global["Total Renewable"]) * 100
    renewable_global["Wind"] = (renewable_global["Electricity from wind (TWh)"] / renewable_global["Total Renewable"]) * 100
    renewable_global["Hydro"] = (renewable_global["Electricity from hydro (TWh)"] / renewable_global["Total Renewable"]) * 100
    renewable_global["Bioenergy"] = (renewable_global["Other renewables including bioenergy (TWh)"] / renewable_global["Total Renewable"]) * 100
    data["renewable_melted"] = renewable_global[["Solar", "Wind", "Hydro", "Bioenergy"]].reset_index().melt(
        id_vars=["Year"], var_name="Source", value_name="Share"
    )

    solar_share_df = pd.read_csv("data/solar-share-energy.csv")
    solar_share_df = solar_share_df.sort_values(by="Year")
    solar_share_df.rename(columns={"solar__pct_equivalent_primary_energy": "Solar Share (%)"}, inplace=True)
    data["solar_share_energy_df"] = solar_share_df

    solar_consumption_df = pd.read_csv("data/solar-energy-consumption.csv")
    solar_consumption_df = solar_consumption_df[solar_consumption_df["Year"] >= 2000]
    solar_consumption_df = solar_consumption_df.dropna(subset=["solar_generation__twh"])
    solar_consumption_df["Year"] = solar_consumption_df["Year"].astype(int)
    data["solar_consumption_df"] = solar_consumption_df
    data["available_solar_regions"] = sorted(solar_consumption_df["Entity"].unique())

    lcoe_df = pd.read_csv("data/LCOE All - IEA.csv")
    elec_mix_df = pd.read_csv("data/elec-mix-bar.csv")

    numeric_cols = lcoe_df.select_dtypes(include=['number']).columns
    lcoe_df = lcoe_df.groupby(["Country", "Plant category", "Plant type"])[numeric_cols].mean().reset_index()
    elec_mix_df = elec_mix_df.groupby("Year").sum().reset_index()

    data["lcoe_df"] = lcoe_df
    data["elec_mix_df"] = elec_mix_df

    cost_df = pd.read_csv("data/levelized-cost-of-energy.csv")
    elec_mix_bar_df = pd.read_csv("data/elec-mix-bar.csv")

    cost_melted = cost_df.melt(id_vars=["Entity", "Code", "Year"],
                               var_name="Technology",
                               value_name="Cost (USD/MWh)")
    cost_merged = pd.merge(cost_melted, elec_mix_bar_df, on=["Entity", "Code", "Year"], how="inner")
    data["cost_merged_df"] = cost_merged

    capacity_df = pd.read_csv("data/installed-global-renewable-energy-capacity-by-technology.csv")
    data["global_capacity_df"] = capacity_df

    elec_mix_corr_df = pd.read_csv("data/elec-mix-bar.csv")
    cost_corr_df = pd.read_csv("data/levelized-cost-of-energy.csv")

    # Clean & merge
    elec_mix_corr_df["Year"] = pd.to_numeric(elec_mix_corr_df["Year"], errors="coerce")
    cost_corr_df["Year"] = pd.to_numeric(cost_corr_df["Year"], errors="coerce")

    elec_mix_corr_df = elec_mix_corr_df.dropna(subset=["Year"])
    cost_corr_df = cost_corr_df.dropna(subset=["Year"])

    merged_corr_df = elec_mix_corr_df.merge(cost_corr_df, on="Year", how="inner")
    merged_corr_df.dropna(inplace=True)

    data["corr_df"] = merged_corr_df

    heat_investment_df = pd.read_csv("data/investment-in-renewable-energy-by-technology.csv")
    heat_cost_df = pd.read_csv("data/levelized-cost-of-energy.csv")

    heat_merged_df = pd.merge(heat_investment_df, heat_cost_df, on=["Entity", "Code", "Year"], suffixes=("_investment", "_cost"))
    heat_merged_df.drop(columns=["Code"], inplace=True)
    heat_long_df = heat_merged_df.melt(id_vars=["Entity", "Year"], var_name="Technology", value_name="Value")

    data["heatmap_long_df"] = heat_long_df
    data["heatmap_entities"] = sorted(heat_merged_df["Entity"].dropna().unique())

    fossil_avg = fossil_df.groupby("Year")[["Coal price index", "Oil spot crude price index"]].mean().reset_index()
    renewable_avg = renewable_df.groupby("Year")[["Solar energy index", "Wind energy index"]].mean().reset_index()
    data["fossil_avg_index"] = fossil_avg
    data["renewable_avg_index"] = renewable_avg

    # Sankey Diagram data for Hypothesis 6
    data["sankey_data"] = {
        "nodes": [
            "Climate Protests",
            "Social Media Activism",
            "Environmental NGOs",
            "Policy Adoption",
            "Renewable Infrastructure",
            "Public Investment",
        ],
        "links": {
            "source": [0, 1, 2, 2, 3, 5],
            "target": [3, 3, 3, 5, 4, 4],
            "value": [50, 30, 40, 20, 60, 40],
            "label": [
                "Protests push policies",
                "Online campaigns shape opinion",
                "NGO lobbying efforts",
                "NGO-backed funding",
                "Policy enables infrastructure",
                "Investment funds infrastructure"
            ]
        }
    }

    # Causal Loop Diagram data for Hypothesis 6
    data["cld_data"] = {
        "nodes": [
            "Social Media Activism",
            "Climate Protests",
            "Environmental NGOs",
            "Policy Adoption",
            "Public Investment",
            "Infrastructure Projects",
            "Public Satisfaction"
        ],
        "edges": [
            ("Social Media Activism", "Climate Protests", "+"),
            ("Climate Protests", "Policy Adoption", "+"),
            ("Environmental NGOs", "Policy Adoption", "+"),
            ("Policy Adoption", "Public Investment", "+"),
            ("Public Investment", "Infrastructure Projects", "+"),
            ("Infrastructure Projects", "Public Satisfaction", "+"),
            ("Public Satisfaction", "Climate Protests", "-"),
            ("Public Satisfaction", "Social Media Activism", "+")
        ]
    }

    # Hypothesis 6.3 - Civic Engagement Map
    data["ngo_df"] = pd.read_csv("data/EEB_Member_Organizations_Complete.csv")
    data["protest_df"] = pd.read_excel("data/Global Climate Protest Tracker.xlsx")
    data["tweet_df"] = pd.read_csv("data/cs_tweets_annotated.csv", low_memory=False)

    return data


