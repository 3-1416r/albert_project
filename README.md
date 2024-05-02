# Like Prediction

## Overview
The goal of our project is to be able to predict the amount of likes on an Instagram publication. We gathered data via scrapping then applied our model to predict likes.

## Dataset
This dataset has infomations (date, number of like, description, URL) about all the publications from [Instagram's Instagram acount](https://www.instagram.com/instagram/) between 2023 and 2024.
Those informartion were collected using selenium in the [get_data.ipynb](https://github.com/3-1416r/albert_project/blob/main/get_data.ipynb) notebook. We cleaned and did some feature engineering in the [clean_data.ipynb](https://github.com/3-1416r/albert_project/blob/main/clean_data.ipynb) notebook.
All the data we used can be found on this [drive](https://drive.google.com/drive/folders/1KKpLS07tiZiVGEmfxpXyybQwfPcuWEzD?usp=sharing).

## Data cleaning
Data preparation is a crucial step in ensuring the effectiveness of subsequent analyses. In this phase of our project, we carried out the following transformations and clean-ups to ensure that our data was ready for analysis:

#Digital Data Transformation
Likes conversion: Likes, initially present in text form, were converted to integers. This transformation is essential to enable numerical and statistical analysis, making the data compatible with various analysis tools and methods.

#Date extraction and transformation
Date decomposition: To facilitate temporal analyses, we have decomposed date information into several distinct columns (day, hour, month, year). This allows us to perform more detailed and targeted analyses according to time periods.
Time Elapsed Calculation: We have calculated the number of days elapsed since the publication of each post to track the temporal evolution of interactions. This metric helps analyze trends over time and assess the impact of temporality on user engagement.
Day of the Week: Extracting the day of the week from the date of publication enables analysis of weekly trends. Understanding which day of the week receives the most interactions can be useful for optimizing publication strategies.

## Feature engineering
This part transforms the raw data into a format better suited to machine learning algorithms. Here are the key methods we used:

#Text analysis
- Symbol Counting: We calculated the number of hashtags (#) and mentions (@) in post captions to assess the engagement and reach of each post. This simple yet powerful metric helps quantify popularity and user interaction with content.
#Dimensionality reduction
- TF-IDF (Term Frequency-Inverse Document Frequency): This technique was used to analyze the relative importance of words in captions compared to the corpus as a whole. It extracts the most significant terms and reduces the noise associated with frequent but uninformative words.
- Principal Component Analysis (PCA): To reduce the dimensionality of textual data while preserving essential information, we applied PCA. This method is crucial for simplifying machine learning models by reducing the number of input variables without losing critical information.
#Post Type Classification
- URL analysis: We have developed a system to identify the type of publication (Reel or photo) from the URL. This classification helps differentiate content strategies and analyze their relative effectiveness according to media type.


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
