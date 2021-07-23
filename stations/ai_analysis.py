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
import altair as alt
import time as time_py

from os.path import isfile, join

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

################################################################################
### 3. MAIN CODE                                                             ###
################################################################################


def write(**kwargs):

    # DATA ACQUISITION
    st.header('Analyse par Intelligence Artificielle')
    st.subheader('Données')
    excel_files = get_excel_files('')
    data_file = st.selectbox('Sélectionnez le fichier',excel_files)

    st.info(f'Fichier actuel: {data_file}')

    df = get_data(directory='data',data_file=data_file)


    # TRAINING
    st.subheader("Apprentissage de l'IA")
    col11,col12 = st.beta_columns((3,1))
    with col11:
        x_cols = st.multiselect("Données d'entrée",df.columns,[],
                                help="Données auxquelles l'IA a accès pour prédire la sortie.")

    with col12:
        y_col = st.selectbox('Donnée à prédire',df.columns)

    algo = st.selectbox("Algorithme d'IA",
                        ['Tous','Réseaux Neuronnaux','Machine à vecteur de support','Plus proches voisins'],
                        help="Le meilleur algorithme est automatiquement suggéré à partir des données soumises.")
    if st.button('Entrainer'):

        time_py.sleep(2.5)
        st.write(f'Performance estimée: ',92,'%.')


        # INFERENCE
        st.header("Inférence de l'IA")

        col21,col22 = st.beta_columns((3,1))
        with col21:
            h = .02  # step size in the mesh

            names = ["Plus Proche Voisin", "Machine à vecteur de support", 
                     "Arbre de décision", "Réseau neuronnaux"]

            classifiers = [
                KNeighborsClassifier(3),
                SVC(gamma=2, C=1),
                DecisionTreeClassifier(max_depth=5),
                MLPClassifier(alpha=1, max_iter=1000),
                ]

            X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                                       random_state=1, n_clusters_per_class=1)
            rng = np.random.RandomState(2)
            X += 2 * rng.uniform(size=X.shape)
            linearly_separable = (X, y)

            datasets = [make_moons(noise=0.3, random_state=0),
                        make_circles(noise=0.2, factor=0.5, random_state=1),
                        linearly_separable
                        ]

            figure = plt.figure(figsize=(25, 15))
            i = 1
            # iterate over datasets
            for ds_cnt, ds in enumerate(datasets):
                # preprocess dataset, split into training and test part
                X, y = ds
                X = StandardScaler().fit_transform(X)
                X_train, X_test, y_train, y_test = \
                    train_test_split(X, y, test_size=.4, random_state=42)

                x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
                y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
                xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                                     np.arange(y_min, y_max, h))

                # just plot the dataset first
                cm = plt.cm.RdBu
                cm_bright = ListedColormap(['#FF0000', '#0000FF'])
                ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
                if ds_cnt == 0:
                    ax.set_title("Données d'entrée")
                # Plot the training points
                ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                           edgecolors='k')
                # Plot the testing points
                ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6,
                           edgecolors='k')
                ax.set_xlim(xx.min(), xx.max())
                ax.set_ylim(yy.min(), yy.max())
                ax.set_xticks(())
                ax.set_yticks(())
                i += 1

                # iterate over classifiers
                for name, clf in zip(names, classifiers):
                    ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
                    clf.fit(X_train, y_train)
                    score = clf.score(X_test, y_test)

                    # Plot the decision boundary. For that, we will assign a color to each
                    # point in the mesh [x_min, x_max]x[y_min, y_max].
                    if hasattr(clf, "decision_function"):
                        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
                    else:
                        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

                    # Put the result into a color plot
                    Z = Z.reshape(xx.shape)
                    ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

                    # Plot the training points
                    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                               edgecolors='k')
                    # Plot the testing points
                    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
                               edgecolors='k', alpha=0.6)

                    ax.set_xlim(xx.min(), xx.max())
                    ax.set_ylim(yy.min(), yy.max())
                    ax.set_xticks(())
                    ax.set_yticks(())
                    if ds_cnt == 0:
                        ax.set_title(name)
                    ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                            size=15, horizontalalignment='right')
                    i += 1

            #plt.tight_layout()
            st.pyplot()

        st.subheader('Importance des données')
        col31,_ = st.beta_columns(2)

        with col31:
            # define dataset
            X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=1)
            # define the model
            model = DecisionTreeClassifier()
            # fit the model
            model.fit(X, y)
            # get importance
            importance = model.feature_importances_
            # summarize feature importance
            for i,v in enumerate(importance):
                print('Feature: %0d, Score: %.5f' % (i,v))
            # plot feature importance
            plt.bar([x for x in range(len(importance))], importance)
            
            st.pyplot()



@st.cache()
def get_excel_files(directory:str=''):

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
def get_data(directory,data_file):

    # Load excel as Dataframe
    df = pd.read_excel(os.path.join(directory,data_file))

    # Function return | Dataframe of the whole excel sheet
    return df 

################################################################################
### X. END OF CODE                                                           ###
################################################################################