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
from PIL import Image
import plotly.graph_objects as go
#import plotly.express as go

sp_dict= {
  "Sélectionner": [],
  "Pipistrelle de l'est": [2,2,3,2,2,2,2,5,3,0],
  "Chauve-souris nordique": [2,2,3,2,2,2,2,5,3,0],
  "Chauve-souris brune": [2,2,4,2,2,2,2,5,3,0],
  "Bourdon à tache rousse": [4,4,0,4,0,0,2,5,5,5]
}

################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

def write(**kwargs):
    st.title(f"Menaces")
    st.write("Espèces ciblées par Éco-nature")

    categories = ['Développement résidentiel et commercial','Agriculture et aquaculture',"Production d'énergie et exploitation minière",\
                "Corridors de transport et de service", "Utilisation des ressources biologiques","Intrusions et perturbations humaines",\
                "Modifications des systèmes naturels","Espèces et gènes envahissants ou autrement problématiques","Pollution",\
                "Changements climatiques et phénomènes météorologiques violents"]
    
    fig = go.Figure()
    sp=st.selectbox("sélectionnez l'espèce",list(sp_dict.keys()))
    if sp != "Sélectionner":
        sp2=st.selectbox("sélectionnez la deuxière espèce",list(sp_dict.keys()))
    if sp!= "Sélectionner" and sp2 != "Sélectionner":
        sp3=st.selectbox("sélectionnez la troisième espèce",list(sp_dict.keys()))
    st.subheader("Impact des menaces sur l'expèce")
    if sp != []:
        fig.add_trace(go.Scatterpolar(
            r=sp_dict[sp],
            theta=categories,
            fill='toself',
            name=sp
            ))
    if sp!= "Sélectionner" and sp2 != "Sélectionner":
        fig.add_trace(go.Scatterpolar(
            r=sp_dict[sp2],
            theta=categories,
            fill='toself',
            name=sp2
        ))
    if sp!= "Sélectionner" and sp2 != "Sélectionner" and sp3 != "Sélectionner":
        fig.add_trace(go.Scatterpolar(
            r=sp_dict[sp3],
            theta=categories,
            fill='toself',
            name=sp3
        ))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 5])),showlegend=True,\
        legend=dict(yanchor="top",y=0.79,xanchor="left",x=0.99))

    st.plotly_chart(fig,use_container_width=True)
    st.write("L'impact de la menace considère la portée et la gravité de la menace. Les valeurs attribuées correspondent au déclin potentiel de la population ou de la superficie en fonction des menaces")
    
    st.subheader("Sources de l'information")
    if st.checkbox("Bourdon à tache rousse"):
        bourdon_rousse_1=Image.open("data/Bourdon_rousse_p1.png")
        bourdon_rousse_2=Image.open("data/Bourdon_rousse_p2.png")
        st.image(bourdon_rousse_1)
        st.image(bourdon_rousse_2, caption='Menaces pour le bourdon à tâche rousse')
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/registre-public-especes-peril/programmes-retablissement/bourdon-tache-rousse-propose-2016.html")
        st.text("Source 2: https://www.sararegistry.gc.ca/virtual_sara/files/plans/rs_rusty_patched_bumble_bee_f_proposed.pdf")
    if st.checkbox("Tortue géographique"):
        tortue_geo_1=Image.open("data/tortue_geo_p1.png")
        tortue_geo_2=Image.open("data/tortue_geo_p2.png")
        st.image(tortue_geo_1)
        st.image(tortue_geo_2, caption='Menaces pour la tortue géographique')
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/registre-public-especes-peril/plans-gestion/tortue-geographique-2019.html#toc10")
        st.text("Source 2: https://www3.mffp.gouv.qc.ca/faune/especes/menacees/fiche.asp?noEsp=72")
        st.text("Source 3: https://mffp.gouv.qc.ca/documents/faune/especes/plan_retablissement_tortue-geographique_2020-2030.pdf")

    if st.checkbox("Chevalier cuivré"):
        chevalier_cuivre_1=Image.open("data/chevalier_cuivre_p1.png")
        st.image(chevalier_cuivre_1,caption='Menaces pour le chevalier cuivré')
        st.text("Source 1: https://www.registrelep-sararegistry.gc.ca/document/doc1565p/p1_f.cfm#_1.5")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/PL_intervention_survie_chevalier_cuivre.pdf")
        st.text("Source 3: https://mffp.gouv.qc.ca/documents/faune/plan-retablissement-chevalier.pdf")
        st.text("Source 4: https://www.sararegistry.gc.ca/default.asp?lang=Fr&n=56437564-1&offset=10&toc=show")
        st.text("Source 5: https://www3.mffp.gouv.qc.ca/faune/especes/menacees/fiche.asp?noEsp=5")

    if st.checkbox("Dard de sable"):
        dard_sable_1=Image.open("data/dard_sable.png")
        st.image(dard_sable_1, caption='Menaces pour le dard de sable')
        st.text("Source 1: https://www.sararegistry.gc.ca/virtual_sara/files/plans/rs_dard_sable_esd_qc_0414_f.pdf")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/plan_retablissement_dard-de-sable_2020-2030.pdf")
        st.text("Source 3: https://www3.mffp.gouv.qc.ca/faune/especes/menacees/fiche.asp?noEsp=77")
    
    if st.checkbox("Carmantine d'Amérique"):
        carmantine_1=Image.open("data/carmantine_p1.png")
        carmantine_2=Image.open("data/carmantine_p2.png")
        carmantine_3=Image.open("data/carmantine_p3.png")
        carmantine_4=Image.open("data/carmantine_p4.png")
        carmantine_5=Image.open("data/carmantine_p5.png")
        st.image(carmantine_1)
        st.image(carmantine_2)
        st.image(carmantine_3)
        st.image(carmantine_4)
        st.image(carmantine_5, caption="Menaces pour la Carmantine d'Amérique")
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/registre-public-especes-peril/programmes-retablissement/carmantine-amerique/chapitre-2.html#tab2")
        st.text("Source 2: https://faune-especes.canada.ca/registre-especes-peril/species/speciesDetails_f.cfm?sid=206#limits")

    if st.checkbox("Chauve-souris brune"):
        chauvesouris_brune_1=Image.open("data/Chauve-souris_brune_p1.png")
        chauvesouris_brune_2=Image.open("data/Chauve-souris_brune_p2.png")
        chauvesouris_brune_3=Image.open("data/Chauve-souris_brune_p3.png")
        st.image(chauvesouris_brune_1)
        st.image(chauvesouris_brune_2)
        st.image(chauvesouris_brune_3, caption="Menaces pour la chauve-souris brune")
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/Rs-TroisChauveSourisThreeBats-v01-2019Nov-Fra.pdf")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/plan_retablissement_chauves-souris_2019-2029.pdf")

    if st.checkbox("Chauve-souris nordique"):
        chauvesouris_nordique_1=Image.open("data/Chauve-souris_nordique_p1.png")
        chauvesouris_nordique_2=Image.open("data/Chauve-souris_nordique_p2.png")
        chauvesouris_nordique_3=Image.open("data/Chauve-souris_nordique_p3.png")
        st.image(chauvesouris_nordique_1)
        st.image(chauvesouris_nordique_2)
        st.image(chauvesouris_nordique_3, caption="Menaces pour la chauve-souris nordique")
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/Rs-TroisChauveSourisThreeBats-v01-2019Nov-Fra.pdf")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/plan_retablissement_chauves-souris_2019-2029.pdf")

    if st.checkbox("Pipistrelle de l'Est"):
        pipistrelle_est_1=Image.open("data/pipistrelle_est_p1.png")
        pipistrelle_est_2=Image.open("data/pipistrelle_est_p2.png")
        pipistrelle_est_3=Image.open("data/pipistrelle_est_p3.png")
        st.image(pipistrelle_est_1)
        st.image(pipistrelle_est_2)
        st.image(pipistrelle_est_3, caption="Menaces pour la Pipistrelle de l'Est")
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/Rs-TroisChauveSourisThreeBats-v01-2019Nov-Fra.pdf")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/plan_retablissement_chauves-souris_2019-2029.pdf")
    
    if st.checkbox("Chevalier de rivière"):
        chevalier_riviere_1=Image.open("data/chevalier_riviere_p1.png")
        st.image(chevalier_riviere_1,caption='Menaces pour le chevalier de rivière')
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/Mp-Redhorse-v00-2018Jul-Fra.pdf")
        st.text("Source 2: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/cosewic/River%20Redhorse_Status_Appraisal_Summary_2015_f.pdf")
        st.text("Source 3: https://mffp.gouv.qc.ca/documents/faune/rapport-situation-chevalier.pdf")
        st.text("Source 4: https://registre-especes.canada.ca/index-fr.html#/especes/111-413#cosewic_assessment")
    if st.checkbox("Méné d'herbe"):
        mene_herbe_1=Image.open("data/menee_herbe_p1.png")
        st.image(mene_herbe_1,caption="Menaces pour le méné d'herbe")
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/mp_bridle_shiner_0611_f.pdf")
    if st.checkbox("Couleuvre tachetée"):
        couleuvre_tachetee_1=Image.open("data/couleuvre_tachetee_p1.png")
        st.image(couleuvre_tachetee_1,caption="Menaces pour la couleuvre tachetée")
        st.text("Source 1: https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/mp_milksnake_f_final.pdf")
    if st.checkbox("Fouille-roche gris"):
        fouille_roche_1=Image.open("data/fouille_roche_p1.png")
        st.image(fouille_roche_1,caption="Menaces pour le fouille-roche gris")
        st.text("Source 1: https://dfo-mpo.gc.ca/species-especes/publications/sara-lep/channeldarter-fouilleroche/index-fra.html")
        st.text("Source 2: https://mffp.gouv.qc.ca/documents/faune/plan_retablissement_fouille-roche-gris_2020-2030.pdf")
    if st.checkbox("Martinet ramoneur"):
        martinet_1=Image.open("data/martinet_p1.png")
        st.image(martinet_1,caption="Menaces pour le martinet ramoneur")
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/registre-public-especes-peril/evaluations-rapports-situations-cosepac/martinet-ramoneur-2018.html")
    if st.checkbox("Monarque"):
        monarque_1=Image.open("data/monarque_p1.png")
        monarque_2=Image.open("data/monarque_p2.png")
        st.image(monarque_1,caption="Menaces pour le monarque")
        st.image(monarque_2,caption="Solution pour le monarque")
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/especes-peril-centre-education/fiches-information/papillon-monarque.html") 
    if st.checkbox("Engoulement d'Amérique"):
        engoulement_1=Image.open("data/engoulement_p1.png")
        st.image(engoulement_1,caption="Menaces pour l'Engoulement d'Amérique'")
        st.text("Source 1: https://www.canada.ca/fr/environnement-changement-climatique/services/registre-public-especes-peril/evaluations-rapports-situations-cosepac/engoulevent-amerique-2018.html#toc9")
        st.text("Source 2: https://faune-especes.canada.ca/registre-especes-peril/species/speciesDetails_f.cfm?sid=986#limits")
    st.write("Actions à surveiller")
    if st.checkbox("Habitat"):
        hab_1=Image.open("data/hab_p1.png")
        hab_2=Image.open("data/hab_p2.png")
        hab_3=Image.open("data/hab_p3.png")
        st.image(hab_1)
        st.image(hab_2)
        st.image(hab_3)
        st.text("https://wildlife-species.canada.ca/species-risk-registry/virtual_sara/files/plans/Ap-TinpFinal-v00-2016Mar24-Fra.pdf")

################################################################################
### X. END OF CODE                                                           ###
################################################################################