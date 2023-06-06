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

st.set_page_config(page_title = 'Countries', page_icon='🌏',layout='wide')

#--------------------------------------------------
# Funções
#--------------------------------------------------

def Restaurant_country(df):
    
    cols = ['Country Code','Restaurant Name']

    df_aux = df.loc[:,cols].groupby('Country Code').count().reset_index()

    fig = (px.bar(df_aux,x='Country Code',y='Restaurant Name',text_auto = True,
             labels = {'Restaurant Name':'Quantidade de Restaurantes','Country Code':'Países'}))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def City_Country(df):
    cols = ['Country Code','City']

    df_aux = df.loc[:,cols].groupby('Country Code').count().reset_index()

    fig = (px.bar(df_aux, x='Country Code', y='City',text_auto = True,
             labels = {'City':'Quantidade de Cidades','Country Code':'Países'}))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def avg_avl_Country(df):
    cols = ['Votes','Country Code']

    df_aux = round(df.loc[:,cols].groupby('Country Code').mean().reset_index(),2)

    fig = (px.bar(df_aux, x='Country Code', y='Votes',text_auto = True,
             labels = {'Votes':'Média de Votos','Country Code':'Países'}))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def avg_avl_cost_for_two(df):
    cols = ['Average Cost for two','Country Code']

    df_aux = df.loc[:,cols].groupby('Country Code').mean().reset_index()

    fig = (px.bar(df_aux, x='Country Code', y='Average Cost for two',text_auto = True,
             labels = {'Average Cost for two':'Média de Prato para dois','Country Code':'Países'}))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

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

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    
    return df

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

st.title('🌏Visão Paises')

with st.container():
    fig = Restaurant_country(df)
    st.markdown('Quantidade de Restaurantes registrados por Pais')
    
    st.plotly_chart(fig ,use_container_width=True)

st.markdown("""---""")

with st.container():
    fig = City_Country(df)
    st.markdown('Quantidade de Cidade por Pais')
    
    st.plotly_chart(fig ,use_container_width=True)

st.markdown("""---""")

with st.container():
    
    col1, col2 = st.columns( 2 )
    
    with col1:
        fig = avg_avl_Country(df)
        st.markdown('Média de Avaliações feitas por País')
            
        st.plotly_chart(fig ,use_container_width=True)
        
    with col2:
        fig = avg_avl_cost_for_two(df)
        st.markdown('Média de Preço de um prato para duas pessoas por País')
            
        st.plotly_chart(fig ,use_container_width=True)