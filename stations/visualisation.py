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
import datetime as dt
import pandas as pd
import numpy as np
import os
import io 
import requests
import pydeck as pdk
import seaborn as sns
import uuid
import plotly.graph_objects as go
import plotly.express as px


################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

def write(**kwargs):

    st.title("Visualisation")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Create columns
    c01,_ = st.beta_columns(2)
    with c01:
        data_key = st.selectbox('Choisissez la source de données',list(kwargs["data_dict"].keys()))

    if data_key is not None:

        df = kwargs["data_dict"][data_key]
        df = df.rename(columns={'LAT_DD':'lat','LONG_DD' : 'lon'})

        chosen_ligns = pd.DataFrame([[0,0]],columns=['lat','lon'])


        ###- VIZUALIATION 1 -###
        st.header("Visualisation 1")
        st.subheader('Filtres')


        # FILTER DATAFRAME
        c11,c12,c13,_,_,_ = st.beta_columns(6)
        # Openable filters
        f1 = add_filter(df.copy(), c11, c12, c13, 1)
        f2,f3,f4 = False,False,False
        if f1 is not False:
            f2 = add_filter(df.copy(), c11, c12, c13, 2)
            if f2 is not False:
               f3 = add_filter(df.copy(), c11, c12, c13, 3)
               if f3 is not False:
                   f4 = add_filter(df.copy(), c11, c12, c13, 4) 
        df1 = df.copy()
        if f1 is False:
            f1 = df1 == df1
        df1 = df1[f1 | f2 | f3 | f4]

        # Date 
        start = df1.index.min().date()
        end = dt.datetime.today().date()
        date_list = pd.date_range(start=start,end=end,periods=(end-start).days).to_pydatetime().tolist()
        date_list = [i.date() for i in date_list]

        temp_c1,_ = st.beta_columns((3,3))
        with temp_c1:
            date_start,date_end = st.select_slider('Dates',options=date_list,value=(date_list[0],date_list[-1]))

        # Apply df filters
        df1 = df1[(df1.index.date >= date_start) & (df1.index.date <= date_end)]
        df1 = df1.sort_index()
        st.subheader("Ressources")

        if st.checkbox('Voir tableau de données'):
            st.write(df1)
        
        df1[['lat','lon']] = df1[['lat','lon']].apply(pd.to_numeric, errors='coerce',axis=1)
        df1_map = df1[['lat','lon']].dropna()

        if st.checkbox('Voir carte géographique'):
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(
                latitude=45.68,         
                    longitude=-73.68,
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'HexagonLayer',
                        data=df1_map,
                        get_position='[lon, lat]',
                        radius=200,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                     ),
                     # pdk.Layer(
                     #     'ScatterplotLayer',
                     #     data=df,
                     #     get_position='[lon, lat]',
                     #     get_color='[200, 30, 0, 160]',
                     #     get_radius=200,
                     # ),
                 ],
             ))

        if st.checkbox('Voir graphique temporel'):

            st.subheader('Variation dans le temps')
            fig11 = px.line(x=df1.index,y=df1['NOMBRE'])
            st.plotly_chart(fig11,use_container_width=True)

            st.subheader('Somme cumulative')
            fig12 = px.line(x=df1.index,y=df1['NOMBRE'].cumsum())
            st.plotly_chart(fig12,use_container_width=True)


        ###- VISUALISATION 2 -###
        st.header("Visualisation 2")
        st.subheader('Filtres')


        # FILTER DATAFRAME
        c21,c22,c23,_,_,_ = st.beta_columns(6)
        # Openable filters
        f21 = add_filter(df.copy(), c21, c22, c23, 5)
        f22,f23,f24 = False,False,False
        if f21 is not False:
            f22 = add_filter(df.copy(), c21, c22, c23, 6)
            if f22 is not False:
               f23 = add_filter(df.copy(), c21, c22, c23, 7)
               if f23 is not False:
                   f24 = add_filter(df.copy(), c21, c22, c23, 8) 
        df2 = df.copy()
        if f21 is False:
            f21 = df2 == df2
        df2 = df2[f21 | f22 | f23 | f24]

        # Date 
        start2 = df2.index.min().date()
        end2 = dt.datetime.today().date()
        date_list2 = pd.date_range(start=start2,end=end2,periods=(end2-start2).days).to_pydatetime().tolist()
        date_list2 = [i.date() for i in date_list2]

        temp_c2,_ = st.beta_columns((3,3))
        with temp_c2:
            date_start2,date_end2 = st.select_slider('Date',options=date_list2,value=(date_list2[0],date_list2[-1]),key='2')

        # Apply df filters
        df2 = df2[(df2.index.date >= date_start2) & (df2.index.date <= date_end2)]
        df2 = df2.sort_index()
        st.subheader("Ressources")

        if st.checkbox('Voir tableau de données',key='1'):
            st.write(df2)
        
        df2[['lat','lon']] = df2[['lat','lon']].apply(pd.to_numeric, errors='coerce',axis=1)
        df2_map = df2[['lat','lon']].dropna()

        if st.checkbox('Voir carte géographique',key='3'):
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(
                latitude=45.68,         
                    longitude=-73.68,
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'HexagonLayer',
                        data=df2_map,
                        get_position='[lon, lat]',
                        radius=200,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                     ),
                     # pdk.Layer(
                     #     'ScatterplotLayer',
                     #     data=df,
                     #     get_position='[lon, lat]',
                     #     get_color='[200, 30, 0, 160]',
                     #     get_radius=200,
                     # ),
                 ],
             ))

        if st.checkbox('Voir graphique temporel',key='4'):
            st.subheader('Variation dans le temps')
            fig21 = px.line(x=df2.index,y=df2['NOMBRE'])
            st.plotly_chart(fig21,use_container_width=True)

            st.subheader('Somme cumulative')
            fig22 = px.line(x=df2.index,y=df2['NOMBRE'].cumsum())
            st.plotly_chart(fig22,use_container_width=True)




def add_filter(df,c11,c12,c13,nbiter):
    with c11:
        col = st.selectbox('Colonne',['']+list(df.columns),key='col'+str(nbiter))
    with c12:
        opr = st.selectbox('Opérateur',['=='],key='opr'+str(nbiter))
    with c13:
        poss_vals = np.unique(df[col].values).tolist() if col != '' else ['']
        val = st.selectbox('Valeur', poss_vals,key='val'+str(nbiter))

    if col == '' or val == '':
        output = False
    else:
        output = df[col] == val
    return output

################################################################################
### X. END OF CODE                                                           ###
################################################################################