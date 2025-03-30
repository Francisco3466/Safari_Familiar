import streamlit as st
import datetime

st.set_page_config(page_title="Planificador Safari Familiar", layout="centered")

st.title("🦁 Planificador de Safari Familiar")
st.markdown("Organiza tu safari desde Madrid o Cancún de forma colaborativa")

# --- Paso 1: Selección de usuario ---
st.header("1. Datos del Viajero")

nombre = st.text_input("Nombre del miembro de la familia")
aeropuerto = st.selectbox("Aeropuerto de salida", ["Madrid (MAD)", "Cancún (CUN)"])
fecha_inicio = st.date_input("Fecha disponible de salida", datetime.date.today())
fecha_fin = st.date_input("Fecha de regreso aproximada", datetime.date.today() + datetime.timedelta(days=7))

# --- Paso 2: Preferencias ---
st.header("2. Preferencias de viaje")
tipo_viaje = st.radio("¿Qué tipo de experiencia prefieres?", ["Comodidad", "Aventura", "Naturaleza intacta", "Ver animales específicos"]) 
presupuesto = st.select_slider("Presupuesto estimado por persona (USD)", options=["<1000", "1000-2000", "2000-3000", ">3000"])
animales = st.multiselect("¿Qué animales te gustaría ver?", ["León", "Elefante", "Leopardo", "Rinoceronte", "Jirafa", "Gorilas", "Hipopótamos"])

# --- Paso 3: Resultado sugerido ---
st.header("3. Recomendación inicial")

if aeropuerto and tipo_viaje:
    if tipo_viaje == "Comodidad":
        pais = "Sudáfrica"
    elif tipo_viaje == "Aventura":
        pais = "Tanzania"
    elif tipo_viaje == "Naturaleza intacta":
        pais = "Botsuana"
    else:
        pais = "Kenia"

    st.success(f"{nombre}, te recomendamos considerar un safari en **{pais}** 🇿🇦🇰🇪🇹🇿🇧🇼")

    st.markdown(f"- Salida desde: **{aeropuerto}**")
    st.markdown(f"- Fechas: del **{fecha_inicio}** al **{fecha_fin}**")
    st.markdown(f"- Presupuesto estimado: **{presupuesto} USD**")
    if animales:
        st.markdown(f"- Animales favoritos: {', '.join(animales)}")

    st.info("En futuras versiones, esta app te mostrará vuelos, visados y safaris disponibles automáticamente.")

else:
    st.warning("Por favor, completa los datos para recibir una recomendación personalizada.")

st.markdown("---")
st.caption("Versión inicial de prueba. Pronto podrás ver vuelos, safaris y más conectados a tiempo real.")
