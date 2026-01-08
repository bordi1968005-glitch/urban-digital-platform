import streamlit as st
from PIL import Image

st.set_page_config(page_title="P.A.D.O.V.A. – Urban Platform", layout="wide")

st.title("P.A.D.O.V.A. – Urban Platform (LIGHT)")
st.markdown("Where Technology Meets Sustainability")

section = st.selectbox(
    "Sezione",
    [
        "Home",
        "Rischio idraulico e raffrescamento climatico",
        "Risparmio energetico",
        "Dispersioni di calore",
        "Rifiuti",
        "Smart poles"
    ]
)

def show_img(path, caption=None, width=900):
    img = Image.open(path)
    st.image(img, caption=caption, width=width)

if section == "Home":
    show_img("sfondo_dashboard.png")

elif section == "Rischio idraulico e raffrescamento climatico":
    show_img("padova_spazi_verdi.png", "Porta Portello con raingardens e cisterne di raccolta acqua", width=950)
    show_img("Daily_rainfall_november.png", "Precipitazioni giornaliere di Novembre", width=950)
    show_img("volume_tank_20m3.png", "Volume cisterna (20 m³)", width=950)
    show_img("Overflow_tank_20m3.png", "Overflow della cisterna", width=950)
    show_img("daily_rainfall_july.png", "Precipitazioni giornaliere di Luglio", width=950)
    show_img("smart_scenario.png", "Scenario SMART", width=950)
    show_img("scenario_smart_deficit.png", "Deficit dello scenario SMART", width=950)


elif section == "Risparmio energetico":
    show_img("pre_post_retrofit.jpg", "Consumi pre/post retrofit degli edifici del centro storico", width=1100)
    show_img("tabella_prepost_retrofit.jpg", width=950)
    show_img("mappa_retrofit.jpg", "Mappa del centro storico di Padova con risparmi energetici", width=950)


elif section == "Dispersioni di calore":
    show_img("thermo_building.jpg", "Termografia edificio")
    show_img("thermo_roof.jpg", "Tetto – dispersioni")
    show_img("thermal_building.png", "Aree critiche")

elif section == "Rifiuti":
    show_img("waste_heatmap.png", "Heatmap rifiuti urbani")

elif section == "Smart poles":
    show_img("led_vs_hps.png", "LED vs HPS")
