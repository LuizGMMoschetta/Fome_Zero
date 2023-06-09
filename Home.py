#--------------------------------------------------
# Import das bibliotecas
#--------------------------------------------------
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium as fl
from haversine import haversine
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Main Paige",
    page_icon="",
    layout='wide')

#--------------------------------------------------
# Funções
#--------------------------------------------------

def Maps(df):
    
    cols = ['Restaurant Name','Rating color','Latitude','Longitude']

    df_aux = (df.loc[:, cols]
            .groupby(['Restaurant Name','Rating color'])
            .median()
            .reset_index())

    map = fl.Map()
    
    marker_cluster = MarkerCluster(
    name='Rating color',
).add_to(map)

    for index, location_info in df_aux.iterrows():
        fl.Marker([location_info['Latitude'],
                  location_info['Longitude']],
                  popup=location_info[['Restaurant Name']]).add_to(marker_cluster)
    
    #fl.LayerControl().add_to(map)
    folium_static( map )
    
    return None


COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

def clean_code(df):
    # categorizando a coluna Cuisines
    df.loc[:,'Cuisines'] = df.loc[:,'Cuisines'].astype( str )
    df['Cuisines'] = df.loc[:,'Cuisines'].apply(lambda x: x.split(',')[0])
    df['Cuisines'] = df.loc[:,'Cuisines'].apply(lambda x: "Coffee" if x == 'Restaurant Cafe' or x == 'Cafe Food' else x )

    # preenchendo o nome dos paises
    df['Country Code'] = df.loc[:,'Country Code'].apply(lambda x: country_name(x))
    # criando uma nova coluna tipos de comidAAa
    df['Price Type'] = df.loc[:,'Price range'].apply(lambda x: create_price_tye(x))
    # Criando a coluna Color Name
    df['Rating color'] = df.loc[:,'Rating color'].apply(lambda x: color_name(x))
    #retirando as informações vazias
    linhas_vazias = df['Cuisines'] != 'nan'
    df = df.loc[linhas_vazias, :]
    df = df.loc[df['Restaurant ID'].notnull(),:]
    df = df.loc[df['Restaurant Name'].notnull(),:]
    df = df.loc[df['Cuisines'].notnull(),:]
    df = df.drop_duplicates()
    df = df.dropna(axis=0,how="any",inplace=False)
    df = df.dropna(axis=1,how="any",inplace=False)
    
    return df

#----------------------------------------------------
# DATASET
#----------------------------------------------------

df = pd.read_csv('dataset/zomato.csv')

#----------------------------------------------------
# Limpeza de Dados
#----------------------------------------------------

df = clean_code(df)

df_copy = df.copy()

#----------------------------------------------------
# Barra Lateral
#----------------------------------------------------

st.sidebar.markdown('# Filtros')

Country = st.sidebar.multiselect(
    'Escolhas os paises que deseja ver os dados',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],
    default=['Brazil','Australia','Canada','England','Qatar','South Africa'])

Country_filter = df['Country Code'].isin( Country )
df = df.loc[Country_filter, :]

#----------------------------------------------------
# Graficos e edição
#----------------------------------------------------

st.title('Fome Zero!')

st.header('Melhores Lugares para encontrar seu Restaurante !')

with st.container():
    st.markdown('### Temos os Seguintos lugares em nossa plataforma:')
        
    col1, col2, col3, col4, col5 = st.columns( 5 )
    with col1:
        restaurant_unique = df_copy.loc[:,'Restaurant ID'].nunique()
        col1.metric('Restaurantes Cadastrados',restaurant_unique)
    with col2:
        country_unique = df_copy.loc[:,'Country Code'].nunique()
        col2.metric('Países Cadastrados',country_unique)
    with col3:
        city_unique = df_copy.loc[:,'City'].nunique()
        col3.metric('Cidades Cadastrados',city_unique)
    with col4:
        all_rating = int(df_copy.loc[:,'Votes'].sum())
        all_rating = f'{all_rating:,}'
        all_rating = all_rating.replace('.',',').replace(',','.')
        col4.metric('Avaliações Feitas na Plataforma',all_rating)
    with col5:
        totaly_typs = df_copy.loc[:,'Cuisines'].nunique()
        col5.metric('Tipos de Culinárias Oferecidas',totaly_typs)

with st.container():
    
    Maps(df)