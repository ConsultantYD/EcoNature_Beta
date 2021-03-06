################################################################################
### 1. HEADER 																 ###
################################################################################
# -*- coding: utf-8 -*-

"""
@authors: Phil Scalabrini & Ysael Desage
"""

################################################################################
### 2. IMPORTS 																 ###
################################################################################

# GENERAL
import streamlit as st
import os


# STATIONS
from stations import accueil as station_accueil
from stations import menaces as station_menaces
from stations import data_lake as station_data_lake
from stations import visualisation as station_visualisation
from stations import analysis as station_analysis
from stations import ai_analysis as station_ai_analysis
from stations import gantt as station_gantt
from stations import text_summarize as station_text_summarize


@st.cache(allow_output_mutation=True)
def initialize_data():
    return {}


class NotAvailable():

    def write(self, *args, **kwargs):
        st.info("Cette ressource n'est pas disponible dans la version d'essai.")


################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

# Stations dictionary
STATIONS = {
    "Accueil": station_accueil,
    # "Documentation": None,
    "Gestion de Projet": station_gantt,
    "Menaces": station_menaces,
    "Littérature": station_text_summarize,
    "Lac de Données": station_data_lake,
    "Visualisation": station_visualisation,
    # "Analyse": station_analysis,
    # "Intelligence Artificielle": station_ai_analysis,
    "Analyse": NotAvailable(),
    "IA - Analyse automatique": NotAvailable(),
    "IA - Vision par Ordinateur": NotAvailable(),
}

#------------------------------------#
#- MAIN STREAMLIT LAUNCHER FUNCTION -#
#------------------------------------#


def main():

    """Main function of the App"""
    st.sidebar.title("Client: Éco Nature")

    selection = st.sidebar.radio("Aller à", list(STATIONS.keys()))


    # Authentification
    try:
        authentified
    except:
        authentified = {'auth':False}

    if not authentified['auth']:
        block1 = st.empty()
        password = block1.text_input("Mot de Passe",value="")

    if password == 'EcoNature2021':
        authentified['auth'] = True
        block1.empty()
    elif password == '':
        pass
    else:
        st.error('Mot de passe incorrect !')


    # Important authentified code
    if authentified['auth']:
        page = STATIONS[selection]

        data_dict = initialize_data()

        with st.spinner(f"Chargement ..."):
            page.write(data_dict=data_dict)

        st.sidebar.title("Important")
        # st.sidebar.info(
        #     "[Site Web](https://github.com/YsaelDesage/OverOneThousand)\n\n"
        #     "[Répertoire GitHub](https://github.com/YsaelDesage/OverOneThousand)"
        # )
        st.sidebar.info(
            "Ceci est une version préliminaire d'essai. Toute utilisation commerciale ou redistribution est strictement interdite. \n\n Merci de transmettre vos questions et commentaires à ysael.desage@me.com ou à pscalabrini@hotmail.ca."
        )
        st.sidebar.title("Auteurs")
        st.sidebar.info(
            "Ysael Desage et Philippe Scalabrini."
        )
        #-------------------#
        #- END OF FUNCTION -#
    #-------------------#

################################################################################
### 4. MAIN EXECUTION CODE                                                   ###
################################################################################


if __name__ == "__main__":

    st.set_page_config(layout='wide')
    main()

################################################################################
### X. END OF CODE                                                           ###
################################################################################
