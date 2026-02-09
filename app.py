import streamlit as st
from PIL import Image

st.set_page_config(page_title="P.A.D.O.V.A. – Urban Platform", layout="wide")

import streamlit as st
from PIL import Image

st.set_page_config(page_title="P.A.D.O.V.A. – Urban Platform", layout="wide")


st.title("P.A.D.O.V.A. – Urban Platform (LIGHT)")
st.markdown("Where Technology Meets Sustainability")

st.markdown("""
<style>
/* Caption custom: leggibile su desktop, ok su mobile */
.cap{
  font-size: 1.05rem;
  color: #6b7280;
  line-height: 1.45;
  margin-top: -0.2rem;
  margin-bottom: 1.2rem;
  max-width: 1000px;
}

/* Desktop/proiettore */
@media (min-width: 900px){
  .cap{ font-size: 1.35rem; }
}
@media (min-width: 1400px){
  .cap{ font-size: 1.55rem; }
}
</style>
""", unsafe_allow_html=True)



section = st.selectbox(
    "Sezione",
    [
        "Home",
        "Raingardens and water tanks",
        "Energy saving retrofit",
        "Roof thermography",
        "Waste management",
        "Smart poles"
    ]
)

def show_img(path, title=None, caption=None):
    if title:
        st.subheader(title)
    img = Image.open(path)
    st.image(img, use_container_width=True)  # IMMAGINI GRANDI
    if caption:
        st.markdown(f"<div class='cap'>{caption}</div>", unsafe_allow_html=True)


if section == "Home":
    show_img("sfondo_dashboard.png")

elif section == "Raingardens and water tanks":
    st.header("Raingardens and water tanks")
    show_img("raingardenscisterne.jpg", title= "One of the areas where rain gardens and corresponding tanks have been installed" , caption= "Due to the need to increase permeable surfaces and reduce the high hydraulic risk, the intervention proposes the installation of rain gardens and cisterns for water collection.")
    show_img("raingardenportello.png", title="Nature-Based water collection and filtration gardens at Porta Portello", caption="In addition to the mitigation of the hydraulic risk, the use of Hemerocallis hybrida has generated an estimated evaporative cooling ecosystem service of 17.86 kW of thermal power substracted from the environment during peak hours, acting as a zero-impact natural air conditioning system")
    show_img("Daily_rainfall_nov.png", "Daily precipitation in November")
    show_img("volume_tank_20m3.png", "Tank volume (20 m³)")
    show_img("Overflow_tank_20m3.png","Overflow", caption= "In the month of November with a 20 m³ tank the total overflow was 4.57 m³.")
    show_img("recupero_acqua_piovana.png", "SMART Scenario", caption= "In the event of periods of rainwater shortage, a smart scenario is proposed by adding catchment surfaces such as roofs and grey water collection.")

elif section == "Energy saving retrofit":
    st.header("Energy saving retrofit")
    show_img(path="pre_post_retrofit.jpg", title= "Energy savings calculation")
    show_img("tabella_prepost_retrofit.jpg", caption= "The proposed retrofit includes internal thermal insulation of walls, roof insulation, and the replacement of existing windows with high-performance low-emissivity glazing, while preserving architectural constraints.")
    show_img("mappa_retrofit.jpg", title= "Map of energy savings in historic city center buildings", caption= "A simplified essessment shows that these measures can achieve energy savings exceeding 60% across the historic city center.")

elif section == "Roof thermography":
    st.header("Roof thermography")
    show_img("drone.jpeg", title= "Drone for thermographic analysis", caption= "By using drones equipped with thermal sensors, it is possible to detect areas of heat loss across buildings and identify where interventions are needed to improve energy efficiency.")
    show_img("1.jpeg", title= "Thermographic images of roofs", caption= "Using specialized software, starting from the image captured by the drone, we calculate the area of heat loss. In this case, it is 16,7%.")
    show_img("2.jpeg", caption= "Heat loss area: 9,4%")
    show_img("3.jpeg", caption= "Heat loss area: 37,4%")
    show_img("4.jpeg", caption= "Heat loss area: 4,1%")
    show_img("5.jpeg", caption= "Heat loss area: 4,5%")

elif section == "Waste management":
    st.header("Waste management")
    show_img("rifiuti.png", title= "Waste data", caption="Smart sensors installed in waste collection trucks record location, waste type and collected quantities along its path.")
    show_img("waste_heatmap.png", caption="The heatmap enables the analysis and subsequent management of waste in the city.")
    show_img("bufferwaste.png", title="Buffer analysis", caption="The area within which the collection service is easily accessible to citizens.")
    show_img("rifiuti_padova.jpeg", "Percentage of waste in Padua")

elif section == "Smart poles":
    st.header("Smart poles")
    show_img("led_vs_hps.png", title="Confronto HPS vs LED", caption= "The transition to LED lighting systems has guaranteed a 150% increase in ground luminance, ensuring superior safety standards even in persistent fog conditions. A significant economic milestone is added to the performance benefit, with an annual saving of 74€ per light point and an estimated return on investment in just 5-6 years.")



