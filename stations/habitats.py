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
import os
import pandas as pd


################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

def write(**kwargs):

    st.title(f"Habitats")
    df_tortues = pd.read_excel ('data/econature_tortues_bd.xlsx')
    Especes_selectbox = st.sidebar.selectbox("Quelle espèce souhaitez-vous analyser?",("Bourdon à tache rousse", "Carmantine d'Amérique", "Chauve-souris nordique","Chevalier cuivré","Chevalier de rivière","Couleuvre tachetée","Dard de sable","Fouille-roche gris","Martinet ramoneur","Mané d'herbe","Engoulevent d'Amérique","Faucon pèlerin","Tortue géographique","Moucherolle à côtés olive","Paruline du Canada", "Petit blongios","Petit-chauve-souris brune","Pipistrelle de l'Est","Tortue serpentine","Hirondelle rustique"))
    #choix selon le secbox du df    df=df-Espesces_selecbox
    st.map(df_tortues)
    st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',initial_view_state=pdk.ViewState(latitude=45.77,longitude=-73.32,zoom=8,pitch=20),layers=pdk.Layer("HeatmapLayer",df_tortues,opacity=0.9,get_position=["lat", "long"],get_weight="Nombre d'individus")))


################################################################################
### X. END OF CODE                                                           ###
################################################################################