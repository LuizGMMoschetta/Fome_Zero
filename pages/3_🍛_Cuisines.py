#--------------------------------------------------
# Import das bibliotecas
#--------------------------------------------------
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium as fl
from haversine import haversine
from streamlit_folium import folium_static
import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'City', page_icon='🍛',layout='wide')

#--------------------------------------------------
# Funções
#--------------------------------------------------

def melhores_restaurantes(df):
    df = df.rename(columns={'Country Code': 'Country'})
    cols = ['Restaurant ID','Restaurant Name','Country','City','Cuisines','Average Cost for two','Aggregate rating','Votes']

    df_aux = df.loc[:,cols].sort_values('Aggregate rating',ascending=False).head(10)
    
    return df_aux

def tipos_culinarias(df,asc):
    cols = ['Cuisines','Aggregate rating']

    df_aux = round(df.loc[:,cols].groupby('Cuisines').mean().sort_values('Aggregate rating',ascending=asc).reset_index().head(10),2)

    fig = (px.bar(df_aux,x='Cuisines',y='Aggregate rating',text_auto = True,
             labels = {'Curisines':'Culinarias','Aggregate rating':'Média da Avaliação Média'}))
    
    return fig

def avaliação(df,n):
    
    cols = ['Restaurant Name','Aggregate rating']

    df_aux = (df.loc[df['Cuisines'] == 'Italian',cols].groupby('Restaurant Name').mean().sort_values('Aggregate rating',ascending=False).reset_index())

    avl = df_aux.iloc[n,1]
    
    return avl

def restaurant(df,n):
    
    cols = ['Restaurant Name','Aggregate rating']

    df_aux = (df.loc[df['Cuisines'] == 'Italian',cols].groupby('Restaurant Name').mean().sort_values('Aggregate rating',ascending=False).reset_index())

    rest = df_aux.iloc[n,0]
    
    return rest

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

st.title('🍛Visão Tipos de Culinaria')

with st.container():
    st.header('Melhores Restaurantes dos Principais tipos Culinárias Italiana')
        
    col1, col2, col3, col4, col5 = st.columns( 5 )
    with col1:
        aval = avaliação(df,n=0)
        rest = restaurant(df,n=0)
        col1.metric(rest, aval)
    with col2:
        aval = avaliação(df,n=1)
        rest = restaurant(df,n=1)
        col2.metric(rest, aval)
    with col3:
        aval = avaliação(df,n=2)
        rest = restaurant(df,n=2)
        col3.metric(rest, aval)
    with col4:
        aval = avaliação(df,n=3)
        rest = restaurant(df,n=3)
        col4.metric(rest, aval)
    with col5:
        aval = avaliação(df,n=4)
        rest = restaurant(df,n=4)
        col5.metric(rest, aval)

with st.container():
    Dataframe = melhores_restaurantes(df)
    st.markdown('Top 10 Melhores Restaurantes')
    
    st.dataframe(Dataframe)

with st.container():
    
    col1, col2 = st.columns( 2 )
    
    with col1:
        fig = tipos_culinarias(df,asc=False)
        st.markdown('Top 10 Melhores Culinarias')
            
        st.plotly_chart(fig ,use_container_width=True)
        
    with col2:
        fig = tipos_culinarias(df,asc=True)
        st.markdown('Top 10 Piores Culinarias')
            
        st.plotly_chart(fig ,use_container_width=True)