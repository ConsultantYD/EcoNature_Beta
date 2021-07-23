import streamlit as st
import plotly.express as px
import pandas as pd
import openpyxl

def write(data_dict,**kwargs):
	#ouvrir les données du Gantt
	df_gantt=pd.read_excel('gantt.xlsx', engine='openpyxl')

	#Assigner les colonnes aux variables
	tache= df_gantt['Tâches']
	debut= df_gantt['Début']
	fin= df_gantt['Fin']
	suivi = st.radio("Visualiser l'avancement des étapes ou les coûts",('Complet en %', 'Coût'))

	if suivi == 'Complet en %':
	    complete = df_gantt['Complet en %']
	else:
	    complete = df_gantt['Coût']

	#Gantt chart

	fig_gantt=px.timeline(df_gantt, x_start=debut,x_end=fin,y=tache,color=complete, title='Gantt')

	fig_gantt.update_yaxes(autorange='reversed')
	fig_gantt.update_layout(title_font_size=36,font_size=14,title_font_family='Arial')

	st.write(fig_gantt)