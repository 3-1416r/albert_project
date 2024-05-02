# Like Prediction

## Overview
The goal of our project is to be able to predict the amount of likes on an Instagram publication. We gathered data via scrapping then applied our model to predict likes.

## Dataset
This dataset has infomations (date, number of like, description, URL) about all the publications from [Instagram's Instagram acount](https://www.instagram.com/instagram/) between 2023 and 2024.
Those informartion were collected using selenium in the [get_data.ipynb](https://github.com/3-1416r/albert_project/blob/main/get_data.ipynb) notebook. We cleaned and did some feature engineering in the [clean_data.ipynb](https://github.com/3-1416r/albert_project/blob/main/clean_data.ipynb) notebook.
All the data we used can be found on this [drive](https://drive.google.com/drive/folders/1KKpLS07tiZiVGEmfxpXyybQwfPcuWEzD?usp=sharing).

## Data cleaning
La préparation des données est une étape cruciale pour assurer l'efficacité des analyses ultérieures. Dans cette phase de notre projet, nous avons effectué les transformations et nettoyages suivants pour garantir que nos données soient prêtes pour l'analyse :

#Transformation des Données Numériques
Conversion des Likes : Les likes, initialement présents sous forme textuelle, ont été convertis en entiers. Cette transformation est essentielle pour permettre les analyses numériques et statistiques, rendant les données compatibles avec divers outils et méthodes d'analyse.
#Extraction et Transformation des Dates
Décomposition de la Date : Afin de faciliter les analyses temporelles, nous avons décomposé les informations de date en plusieurs colonnes distinctes (jour, heure, mois, année). Cela nous permet d'effectuer des analyses plus détaillées et ciblées en fonction des périodes.
Calcul du Temps Écoulé : Nous avons calculé le nombre de jours écoulés depuis la publication de chaque post pour suivre l'évolution temporelle des interactions. Cette métrique aide à analyser les tendances au fil du temps et à évaluer l'impact de la temporalité sur l'engagement des utilisateurs.
Jour de la Semaine : L'extraction du jour de la semaine à partir de la date de publication permet d'analyser les tendances hebdomadaires. Comprendre quel jour de la semaine reçoit le plus d'interactions peut s'avérer utile pour optimiser les stratégies de publication.

## Presentation
Here is a link to the presentation: Canva (https://www.canva.com/design/DAGDySTTzq8/0N8qlMnIeo6OPQECwa0TRA/edit?utm_content=DAGDySTTzq8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## Group members
Margaux, Chania, Evaluna, Meni & Pierre

## Installation
We don't know yet cause the project is not finished


```bash
git clone https://github.com/3-1416r/albert_project.git
cd albert_project
pip install -r requirements.txt
