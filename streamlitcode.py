import random
import pandas as pd
import streamlit as st

def filter_data(data, choices):
    pattern = r'^\w+([- ])(' + '|'.join(choices) + r')\1\w+$'
    filtered_column = data[data.str.contains(pattern, regex=True, na=False)]
    return filtered_column


file_path = "villes_dinteret.csv"
filtered_df = pd.read_csv(file_path)
st.title("Nos villages ont du talent")
st.write("Sélectionnez les options pour filtrer les données et obtenir un nom aléatoire.")

options = st.multiselect(
    "Choisissez les options pour la selection de ville:",
    ['le', 'la', 'l\'', 'l', 'les']
)

# Bouton pour lancer le filtrage et la sélection
if st.button("Lancer"):
    if not options:
        st.write("Veuillez sélectionner au moins une option.")
    else:
        filtered_data = filter_data(filtered_df.iloc[:, 0], options)
        if filtered_data.empty:
            st.write("Aucun résultat ne correspond aux critères.")
        else:
            random_choice = random.choice(filtered_data.tolist())
            st.markdown(f'<div class="result">Se {random_choice} !</div>', unsafe_allow_html=True)




    # CSS personnalisé pour centrer et agrandir le texte
    st.markdown(
        """
        <style>
        .result {
            font-size: 50px;
            text-align: center;
            color: gold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )