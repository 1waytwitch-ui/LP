import streamlit as st
import requests

st.set_page_config(page_title="Stratégie Krystal", layout="wide")

st.title("Positions d'une stratégie Krystal")

strategy_id = st.text_input("Numéro de stratégie", value="51464556")

API_KEY = st.secrets["KRYSTAL_API_KEY"]

if st.button("Récupérer la stratégie"):

    if not strategy_id.isdigit():
        st.error("Le numéro de stratégie doit être un nombre.")
    else:
        url = f"https://cloud-api.krystal.app/v1/strategies/{strategy_id}/positions"

        headers = {
            "accept": "application/json",
            "x-api-key": API_KEY
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            st.success("Données récupérées avec succès")
            st.dataframe(data, use_container_width=True)
        else:
            st.error(f"Erreur API : {response.status_code}")
            st.text(response.text)
