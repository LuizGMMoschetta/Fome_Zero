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

st.set_page_config(page_title = 'City', page_icon='🌇',layout='wide')

#--------------------------------------------------
# Funções
#--------------------------------------------------

def top_city_mais_r(df):
    cols = ['City','Restaurant Name','Country Code']

    df_aux = df.loc[:,cols].groupby(['City','Country Code']).count().sort_values('Restaurant Name',ascending=False).reset_index().head(10)

    fig = px.bar(df_aux, x='City', y='Restaurant Name',text_auto = True, color = 'Country Code',
             labels = {'Restaurant Name':'Quantidade de Restaurantes','City':'Cidades'})
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def top_city_acima_4(df):
    cols = ['Restaurant Name','City','Country Code']

    df_aux = (df.loc[df['Aggregate rating'] >= 4,cols].groupby(['City','Country Code']).count().sort_values('Restaurant Name',ascending=False).reset_index().head(7))

    fig = (px.bar(df_aux,x='City',y='Restaurant Name',text_auto = True,color='Country Code',
             labels = {'Restaurant Name':'Quantidade de Restaurantes','City':'Cidades'}))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def top_city_menor_2(df):
    cols = ['Restaurant Name','City','Country Code']

    df_aux = (df.loc[df['Aggregate rating'] <= 2.5,cols].groupby(['City','Country Code']).count().sort_values('Restaurant Name',ascending=False).reset_index().head(7))

    fig = px.bar(df_aux,x='City',y='Restaurant Name',text_auto = True,color='Country Code',
             labels = {'Restaurant Name':'Quantidade de Restaurantes','City':'Cidades'})
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    
    return fig

def top_city_tipos_c(df):
    cols = ['City','Cuisines','Country Code']

    df_aux = df.loc[:,cols].groupby(['City','Country Code']).nunique().sort_values('Cuisines', ascending=False).reset_index().head(10)

    fig = px.bar(df_aux, x='City', y='Cuisines',text_auto = True,color='Country Code',
             labels = {'Curisines':'Quantidade de Culinarias distintas','City':'Cidades'})
    
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

st.title('🌇Visão Cidades')

with st.container():
    fig = top_city_mais_r(df)
    st.markdown('Top 10 Cidades com mais Restaurantes')
    
    st.plotly_chart(fig ,use_container_width=True)

st.markdown("""---""")

with st.container():
    
    col1, col2 = st.columns( 2 )
    
    with col1:
        fig = top_city_acima_4(df)
        st.markdown('Top 7 Cidades que tem Avaliação acima de 4')
            
        st.plotly_chart(fig ,use_container_width=True)
        
    with col2:
        fig = top_city_menor_2(df)
        st.markdown('Top 7 Cidades que tem Avaliação menor de 2.5')
            
        st.plotly_chart(fig ,use_container_width=True)

with st.container():
    fig = top_city_tipos_c(df)
    st.markdown('Top 10 Cidades com mais Restaurantes')
    
    st.plotly_chart(fig ,use_container_width=True)