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
    show_img("padova_spazi_verdi.png", "Raingardens e permeabilità urbana")
    show_img("Daily_rainfall_november.png", "Precipitazioni – Novembre")
    show_img("volume_tank_20m3.png", "Cisterna da 20 m³")
    show_img("Overflow_tank_20m3.png", "Overflow idraulico")

elif section == "Risparmio energetico":
    show_img("pre_post_retrofit.jpg", "Consumi prima e dopo il retrofit")
    show_img("mappa_retrofit.jpg", "Edifici del centro storico")

elif section == "Dispersioni di calore":
    show_img("thermo_building.jpg", "Termografia edificio")
    show_img("thermo_roof.jpg", "Tetto – dispersioni")
    show_img("thermal_building.png", "Aree critiche")

elif section == "Rifiuti":
    show_img("waste_heatmap.png", "Heatmap rifiuti urbani")

elif section == "Smart poles":
    show_img("led_vs_hps.png", "LED vs HPS")
