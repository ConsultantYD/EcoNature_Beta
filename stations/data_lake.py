################################################################################
### 1. HEADER                                                                ###
################################################################################
# -*- coding: utf-8 -*-

"""
@authors: Phil Scalabrini & Ysael Desage
"""

################################################################################
### 2. IMPORTS                                                               ###
################################################################################

# GENERAL
import streamlit as st
import pandas as pd
import numpy as np
import os
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

from os.path import isfile, join

################################################################################
### 3. MAIN CODE                                                             ###
################################################################################


def write(data_dict: dict, **kwargs):

    # DATA ACQUISITION
    st.title('Lac de Données')

    st.info("Seul le fichier Observations.xlsx est disponible dans la version d'essai.")

    st.subheader('Sélection des données')
    col11, col12 = st.beta_columns((1, 2))

    with col12:
        st.image(os.path.join("stations", "images", "data_lake.png"))

    with col11:

        source = st.selectbox('Source de données', [
                              'Fichiers Locaux', 'En Ligne'])

        # Fichier locaux
        if source == 'Fichiers Locaux':
            excel_files = get_excel_files('')
            excel_files = [f for f in excel_files if f not in data_dict.keys()]
            data_file = st.selectbox('Sélectionnez le fichier', excel_files)

            if data_file is not None and st.button('Ajouter'):
                if data_file not in data_dict.keys():
                    data_dict[data_file] = get_data(directory='data',
                                                    data_file=data_file)
                    st.info(f'Fichier ajouté: {data_file}')

        # Ressources préparées en ligne
        elif source == 'En Ligne':

            if True:
                st.info("Non disponible dans la version d'essai.")

            else:
                online_sources = [
                    'Bilan de phosphore par MRC',
                    'Débordements 2017 à 2020',
                    #'Débordements de 2020',
                    #'Débordements de 2019',
                    #'Débordements de 2018',
                    #'Débordements de 2017',
                    'Effluents industriels',
                    'Météo Montréal',
                    'Refuge biologique (désigné et en projet)',
                    'Rejets eaux usées'
                    'RSMA - Données COURDO spéciales',
                    #'RSMA - Données COURDO spéciales 2017',
                    #'RSMA - Données COURDO spéciales 2014',
                    #'RSMA - Données COURDO spéciales 2013',
                    #'RSMA - Données COURDO spéciales 2012',
                    #'RSMA - Données COURDO spéciales 2011',
                    'RSMA – Point d’échantillonnage COURDO SPÉCIAL 2011-2017',
                    'Surverses Montréal',
                    'Surverses Repentigny',
                ]
            # Météo Montréal
                # if source == 'En Ligne' and online_sources == 'Météo Montréal':
                #tables_mtl = pd.read_html('https://meteo.gc.ca/forecast/hourly/qc-147_metric_f.html')
                # st.write(np.array(tables_mtl))

                for online_source in online_sources:
                    if st.checkbox(online_source):
                        if online_source not in data_dict.keys():
                            data_dict[online_source] = get_online_data(
                                online_source)

        st.subheader('Données actuelles')
        f = st.selectbox('Données disponibles: ', list(data_dict.keys()))
        if f is not None:
            ln, cols = data_dict[f].shape
            st.write(f"Nombre d'entrées: {ln}")
            st.write(f"Nombre de colonnes: {cols}")

    # if f is not None and st.checkbox('Visualiser les statistiques descriptives'):
    #     df = data_dict[f]
    #     desc = df.describe().T
    #     desc_df = pd.DataFrame(index= [col for col in df.columns if df[col].dtype != 'O'],
    #                        columns= df.describe().T.columns.tolist(),data= desc )

    #     f,ax = plt.subplots(figsize=(12,8))
    #     sns.heatmap(desc_df, annot=True,cmap = "Purples", fmt= '.0f',
    #                 ax=ax,linewidths = 5, cbar = False,
    #                 annot_kws={"size": 16})

    #     plt.xticks(size = 18)
    #     plt.yticks(size = 14, rotation = 0)
    #     plt.title("Descriptive Statistics", size = 16)
    #     st.pyplot(f,clear_figure=True)

    if f is not None and st.checkbox('Visualiser les données brutes'):
        st.write(data_dict[f])


def get_online_data(data):

    # Météo Montréal
    if data == 'Météo Montréal':
        url = 'https://meteo.gc.ca/forecast/hourly/qc-147_metric_f.html'
        df = pd.read_html(url, encoding="ISO-8859-1")[0]

    # Surverses Montréal
    if data == 'Surverses Montréal':
        url = 'https://www.donneesquebec.ca/recherche/dataset/60acd1db-0adb-4388-8c94-f9671f622110/resource/18a63ea6-c36f-415d-8ae8-cb09246973e9/download/surverses.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA - Données COURDO spéciales 2017
    if data == 'RSMA - Données COURDO spéciales 2017':
        url = 'https://data.montreal.ca/dataset/243f731a-0c30-4e31-a15b-bd388cb7c91d/resource/4d506fe3-853e-4982-962c-cad2bec5da03/download/courdo_special_2017.csv '
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA - Données COURDO spéciales 2014
    if data == 'RSMA - Données COURDO spéciales 2014':
        url = 'https://data.montreal.ca/dataset/243f731a-0c30-4e31-a15b-bd388cb7c91d/resource/0e6ae430-f166-4f7c-b5ea-ba9ab2a70118/download/courdo_special_2014.csv '
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA - Données COURDO spéciales 2013
    if data == 'RSMA - Données COURDO spéciales 2013':
        url = 'https://data.montreal.ca/dataset/243f731a-0c30-4e31-a15b-bd388cb7c91d/resource/16a9657c-eeab-4a21-87a8-467f6f50ea4e/download/courdo_special_2013.csv '
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA - Données COURDO spéciales 2012
    if data == 'RSMA - Données COURDO spéciales 2012':
        url = 'https://data.montreal.ca/dataset/243f731a-0c30-4e31-a15b-bd388cb7c91d/resource/989d8cfc-81ee-48ae-a657-6259e5a90881/download/courdo_special_2012.csv '
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA - Données COURDO spéciales 2011
    if data == 'RSMA - Données COURDO spéciales 2011':
        url = 'https://data.montreal.ca/dataset/243f731a-0c30-4e31-a15b-bd388cb7c91d/resource/dcc19f2e-f7ff-4d14-8143-80e5199c1409/download/courdo_special_2011.csv '
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Surverses Repentigny
    if data == 'Surverses Repentigny':
        url = 'https://www.donneesquebec.ca/recherche/dataset/60acd1db-0adb-4388-8c94-f9671f622110/resource/18a63ea6-c36f-415d-8ae8-cb09246973e9/download/surverses.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Rejets eaux usées
    if data == 'Rejets eaux usées':
        url = 'https://www.donneesquebec.ca/recherche/dataset/64372248-d60b-4a2b-a326-bf34c721e568/resource/ae0509d7-466f-4bfc-90aa-b4d4fd82018a/download/stations-depurations-rejets-deaux-usees-2021-02-12.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Effluents industriels
    if data == 'Effluents industriels':
        url = 'https://www.donneesquebec.ca/recherche/dataset/2b945a95-e65e-4cf4-8792-b73e291c0919/resource/b1da0299-709c-4b28-bd66-70858f900af4/download/effluents_industriels.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Bilan de phosphore par MRC
    if data == 'Bilan de phosphore par MRC':
        url = 'https://www.donneesquebec.ca/recherche/dataset/943bf975-e796-4236-a5b0-c46bc1afd6b1/resource/b9dd903d-38d8-4018-b3fb-4b9a204af4be/download/pressions-agricoles-2019-10-18.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Milieux humides Laval
    if data == 'Milieux humides Laval':
        url = 'https://www.donneesquebec.ca/recherche/dataset/8113b9bd-bd08-4182-b9d4-b527323410b2/resource/de33b456-8fd4-4847-b6a2-f875604e591d/download/milieux-humides-interet.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # RSMA – Point d’échantillonnage COURDO SPÉCIAL 2011-2017
    if data == 'RSMA – Point d’échantillonnage COURDO SPÉCIAL 2011-2017':
        url = 'https://data.montreal.ca/dataset/0ef85f14-fd79-49e4-af85-bfc0c589ad79/resource/297d841e-5ab5-4119-aa66-ebcbcd2ad021/download/stations_courdo_speciales_2011-2017.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Refuge biologique (désigné et en projet)
    if data == 'Refuge biologique (désigné et en projet)':
        url = 'https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/CONSERVATION_PROTECTION/Refuges_biologiques/LISTE_REFUGE.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Débordements de 2020
    if data == 'Débordements de 2020':
        url = 'https://data.montreal.ca/dataset/17ec5343-6d39-45b8-9ce1-e76843daaaa4/resource/7c70ca85-5223-4db3-91ca-82fcce464f41/download/debordements2020.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Débordements de 2019
    if data == 'Débordements de 2019':
        url = 'https://data.montreal.ca/dataset/17ec5343-6d39-45b8-9ce1-e76843daaaa4/resource/674d0872-6327-48c7-9648-85a83d96bc36/download/debordement2019.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Débordements de 2018
    if data == 'Débordements de 2018':
        url = 'https://data.montreal.ca/dataset/17ec5343-6d39-45b8-9ce1-e76843daaaa4/resource/48aada2a-5dd0-4460-b253-cd88209cc434/download/debordements2018.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Débordements de 2017
    if data == 'Débordements de 2017':
        url = 'https://data.montreal.ca/dataset/17ec5343-6d39-45b8-9ce1-e76843daaaa4/resource/fed0ee5a-4d8f-46d5-bc08-b66c3c6c0d53/download/debordements2017.csv'
        df = pd.read_csv(url, encoding="ISO-8859-1")

    # Function return | Dataframe of desired online data
    return df


@st.cache()
def get_excel_files(directory: str = ''):

    # Use local directory if none specified
    if directory == '':
        #directory = os.getcwd()
        directory = 'data'

    # List of all files in directory
    files = [f for f in os.listdir(directory) if isfile(join(directory, f))]

    # Excel files
    excel_files = [f for f in files if ('xlsx' in f or 'xls' in f)]

    # Function return | List of excel files
    return excel_files


@st.cache()
def get_data(directory: str, data_file: str):

    # LOAD FILE BASED ON FORMAT
    # Excel
    if data_file.endswith('.xlsx') or data_file.endswith('.xls'):
        df = pd.read_excel(
            os.path.join(directory, data_file),
            parse_dates={"date": ["DATE_ANNEE", "DATE_MOIS", "DATE_JOUR"]},
            na_values=['-'])
    elif data_file.endswith('.csv'):
        df = pd.read_excel(
            os.path.join(directory, data_file),
            parse_dates={"date": ["DATE_ANNEE", "DATE_MOIS", "DATE_JOUR"]},
            na_values=['-'])

    # Time series index standardization
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(
            df['date'], errors='coerce', format='%Y/%m/%d')
        df = df.set_index('date')

        df = df[df.index > dt.datetime(year=1900, month=1, day=1)]

    # Specific Econature treatment
    eco_nature_int_cols = ['NOMBRE']
    for c in eco_nature_int_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Function return | Dataframe of the whole excel sheet
    return df


################################################################################
### X. END OF CODE                                                           ###
################################################################################
