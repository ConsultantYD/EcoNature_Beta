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
import io 
import requests
import seaborn as sns
from string import ascii_letters
import matplotlib.pyplot as plt
sns.set_theme(style="white")


################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

def write(data_dict,**kwargs):

    st.title("Analyse")
    df = list(data_dict.values())[0]
    col11,col12 = st.beta_columns((3,1))
    with col11:
        cols = st.multiselect("Données d'intérêt",df.columns,[],
                                help="Données auxquelles l'IA a accès pour prédire la sortie.")

    st.subheader('Distributions Statistiques')

    c31,c32 = st.beta_columns(2)

    with c31:

        # g = sns.PairGrid(df[cols])
        # g.map_upper(sns.histplot)
        # g.map_lower(sns.kdeplot, fill=True)
        # g.map_diag(sns.histplot, kde=True)

        df = df[df.NOMBRE < 250]
        g = sns.displot(df[cols], x="NOMBRE", hue="CATEGORIE", element="step")
        st.pyplot(g)


    st.subheader("Étude de corrélations")

    c21,c22 = st.beta_columns(2)

    with c21:

        # Generate a large random dataset
        rs = np.random.RandomState(33)
        d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                         columns=list(ascii_letters[26:]))

        # Compute the correlation matrix
        corr = d.corr()

        # Generate a mask for the upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize=(11, 9))

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(230, 20, as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        fig = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})
        st.pyplot()


################################################################################
### X. END OF CODE                                                           ###
################################################################################