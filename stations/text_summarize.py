import streamlit as st 
from gensim.summarization import summarize
#from googletrans import Translator, constants
import os
#title 


def write(data_dict,**kwargs):
	st.title("Littérature")
	st.info("Cette ressource n'est que partiellement disponible dans la version d'essai.")

	st.header("Résumé Automatique")
	rawtext=st.text_area("Texte")
	ratio=st.slider('Taille du résumé (% taille originale)',0,100,10)

	if st.button("Résumer"):
	    summary_result=summarize(rawtext,ratio=ratio/100)
	    st.success(summary_result)
	    #language="en"
	    #output=gTTS(text=summary_result, lang=language)
	    #output.save("output.mp3")


	##### Probleme d'objet résoudre afin d'utiliser la traduction ########
	#rawtranslate=st.text_area('Translate')
	#translator = Translator()
	#if st.button("Translate"):
	    #translation = translator.translate(rawtranslate,src="en",dest="fr",)
	    #st.success(translation)

	#get number of occurrences of the substring in the string
	st.header("Analyse Lexicale")
	search=st.text_area("Mot recherché")

	if st.button("Compter"):
	    occurences=rawtext.count(search)
	    st.write('Number of occurrences of',search, occurences)