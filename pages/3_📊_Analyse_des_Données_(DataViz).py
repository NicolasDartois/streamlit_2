import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.io import to_html
from bokeh.plotting import figure
from bokeh.models import HoverTool
from include.css_and_credit import css_and_credit

st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

col1, col2, col3 = st.columns([3, 3, 3])
with col2:
            st.header("📊 Analyse des Données (DataViz)")

st.markdown("<br><br><br>", unsafe_allow_html=True)
allocine = pd.read_csv('data/allocine.csv')
allocine_budget = pd.read_csv('data/Allocine_v2_8.csv')

#---------------#
col1, col2, col3, col4, col5 = st.columns([2, 8, 1, 8, 2])

with col2:
            distrib = {
                2000: 532,
                2001: 504,
                2002: 487,
                2003: 509,
                2004: 559,
                2005: 550,
                2006: 589,
                2007: 573,
                2008: 555,
                2009: 558,
                2010: 579,
                2011: 588,
                2012: 614,
                2013: 654,
                2014: 663,
                2015: 652,
                2016: 716,
                2017: 693,
                2018: 683,
                2019: 746,
                2020: 364,
                2021: 454,
                2022: 681,
                2023: 712
            }
            annees = list(distrib.keys())
            valeurs = list(distrib.values())
            colorscale = [[0, 'blue'], [1, 'orange']]
            fig3 = go.Figure(data=[go.Bar(x=annees, y=valeurs, marker=dict(color=valeurs, colorscale='Viridis', cmin=0, cmax=max(valeurs)))])
            fig3.update_layout(width=750, height=400)
            fig3.update_layout(title='🎞️ Nombre de films sortis par année en France (après 2000)', xaxis_title='Année de sortie', yaxis_title='Nombre de films')
            st.plotly_chart(fig3)
            
            st.markdown('<div class="box"><p>On remarque une augmentation progressive du nombre de films sortis chaque année, le pic étant atteint en 2019 avec 746 films sortis au cours de l’année. Les effets de la pandémie mondiale en 2020 et 2021 sont également visibles sur ce graphique. L’année dernière, 712 films sont sortis sur les écrans français, soit une moyenne de 13,7 films par semaine.</p></div>', unsafe_allow_html=True)

with col4: 
            fig2 = px.box(allocine, x="premiere_semaine_france",
                        hover_data=['titre_original'],
                        title='🎫 Analyse de la distribution de notre target: première semaine en France',
                        labels={'premiere_semaine_france': 'Première semaine en France'})
            fig2.update_layout(width=750, height=400)
            fig2.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey'))
            st.plotly_chart(fig2)
            
            st.markdown('<div class="box"><p>Ces données suggèrent une forte asymétrie dans la distribution des performances des films. La présence de quelques films avec des résultats exceptionnels lors de la première semaine indique que ces films peuvent être des moteurs significatifs pour l’industrie, tandis que la majorité des films affichent des performances beaucoup plus modestes.</p></div>', unsafe_allow_html=True)

#---------------#

with col2:
            fig4 = px.scatter(
                        allocine, 
                        x='cumul_france', 
                        y='premiere_semaine_france',
                        hover_data=['titre_original'],
                        title=f'📈 Corrélation entre le cumul en France et la première semaine en France: 0.92',
                        labels={'cumul_france': 'Cumul en France', 'premiere_semaine_france': 'Première semaine en France'},
                        opacity=0.5,
                        trendline='ols'
                        )
            fig4.data[1].line.color = 'red'
            fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
            fig4.update_xaxes(showgrid=True, title='Cumul en France')
            fig4.update_yaxes(showgrid=True, title='Première semaine en France')
            st.plotly_chart(fig4)
            
            st.markdown('<div class="box"><p>En calculant la corrélation entre la première semaine et le cumul en France, on obtient un score de 0.92. La corrélation est donc positive et très élevée. Ainsi, si un film réalise de bonnes performances en première semaine en termes d’entrées, il a des chances de connaître le succès pendant toute son exploitation cinématographique. Cela suppose donc que le nombre d’entrées de la première semaine peuvent être utilisées pour estimer le nombre total d’entrées.</p></div>', unsafe_allow_html=True)

with col4:
            actors_columns = ['acteur_1', 'acteur_2', 'acteur_3', 'acteur_4']
            melted_actors = pd.melt(allocine, id_vars=['premiere_semaine_france'], value_vars=actors_columns, value_name='actor').dropna().drop(columns='variable', axis=1)
            
            top_10_actors = melted_actors.groupby('actor')['premiere_semaine_france'].sum().nlargest(10)
            
            fig6 = px.bar(top_10_actors, x=top_10_actors.values, y=top_10_actors.index, orientation='h',
            text=top_10_actors.values,
            labels={'y': 'Acteurs', 'x': 'Nombre total d’entrées première semaine France'},
            color_discrete_sequence=['green'],
            title='🧑 Top 10 des acteurs avec le plus grand nombre d’entrées en première semaine France')
            
            fig6.update_traces(texttemplate='%{text:.3s}', textposition='inside', hovertemplate='<b>%{y}</b><br>Nombre total d’entrées première semaine: %{x}<extra></extra>')
            fig6.update_layout(
                xaxis_title='Nombre total d’entrées première semaine France',
                yaxis_title='Acteurs',
                uniformtext_minsize=8, uniformtext_mode='hide',
                height=400, width=800, yaxis_autorange='reversed'
            )
            st.plotly_chart(fig6)
            
            st.markdown('<div class="box"><p>C’est le quatuor des films Harry Potter (8 films) qui cumule le plus de spectateurs en première semaine. Dans le reste du classement, on trouve deux acteurs français : Jean Dujardin et Gérard Depardieu, tous deux très populaires et dont certains films ont dépassé les frontières de la France. Ils ont également eu des rôles à l’international. Entre la 4e et la 10e position, on trouve des acteurs américains ayant tous participé à des franchises : Pirates des Caraïbes pour Johnny Depp, Avengers et Iron Man pour Robert Downey Jr., Mission : Impossible pour Tom Cruise.</p></div>', unsafe_allow_html=True)
 
#---------------#

with col2:
            fig4 = px.scatter(
                        allocine_budget, 
                        x='budget_euro', 
                        y='premiere_semaine_france',
                        hover_data=['titre_original'],
                        title='📈 Corrélation entre le budget du film et la première semaine en France. Pearson : 0.62',
                        labels={'budget_euro': 'Budget', 'premiere_semaine_france': 'Première semaine en France'},
                        opacity=0.5,
                        trendline='ols'
                        )
            fig4.data[1].line.color = 'red'
            fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
            fig4.update_xaxes(showgrid=True, title='Budget')
            fig4.update_yaxes(showgrid=True, title='Première semaine en France')
            st.plotly_chart(fig4)

            st.markdown('<div class="box"><p>Ces graphiques illustrent la corrélation entre le budget d’un film et le nombre d’entrées en première semaine en France. On remarque une corrélation positive avec un coefficient de Pearson de 0,62.</p></div>', unsafe_allow_html=True)

            
with col4:            
            pays_counts = allocine['pays'].value_counts()
            top_pays = pays_counts[:8]
            autres = pays_counts[8:].sum()
            top_pays['Autres'] = autres    
            fig1 = go.Figure(data=[go.Pie(labels=top_pays.index, values=top_pays.values, hole=.3)])
            fig1.update_traces(textposition='inside', textinfo='percent+label')
            fig1.update_layout(
                        title_text='🌎 Répartition des films par pays',
                        annotations=[dict(text='Pays', x=0.5, y=0.5, font_size=20, showarrow=False)],
                        legend_title="Pays"
                        )
            st.plotly_chart(fig1)
            
            st.markdown('<div class="box"><p>La France (38,9%) et les U.S.A (30,7%) se partagent une importante part du marché cinématographique français. On remarque l’incroyable exportabilité des films américains qui égalise presque le volume de films produits par le pays d’où sont issues les données.</p></div>', unsafe_allow_html=True)

#---------------#
col1, col2, col3, col4, col5 = st.columns([2, 6, 1, 10, 2])

with col2:
            genres_to_include = ['Drame', 'Comédie', 'Action', 'Comédie dramatique', 'Aventure', 
                    'Documentaire', 'Biopic', 'Animation', 'Policier', 'Epouvante-horreur', 
                    'Thriller', 'Fantastique']
            
            genres_color = {'Drame' : 'blue', 'Comédie' : 'red', 'Action' : 'orange', 'Comédie dramatique' : 'purple', 'Aventure' : 'yellow', 
                    'Documentaire' : 'grey', 'Biopic' : 'green', 'Animation' : 'pink', 'Policier' : 'brown', 'Epouvante-horreur' : 'black', 
                    'Thriller' : 'coral', 'Fantastique' : 'turquoise'}
            
            allocine['genre'] = allocine['genre'].str.split(', ')
            allocine = allocine.explode('genre')
            
            allocine['genre'] = allocine['genre'].str.strip()
            allocine['genre'] = allocine['genre'].str.capitalize()
            filtered_data = allocine[allocine['genre'].isin(genres_to_include)].copy()
            filtered_data['premiere_semaine_france'] = pd.to_numeric(filtered_data['premiere_semaine_france'], errors='coerce')
            filtered_data.dropna(subset=['premiere_semaine_france', 'genre'], inplace=True)
            
            median_data = filtered_data.groupby('genre')['premiere_semaine_france'].median().reset_index()
            
            fig5 = px.bar(median_data, x='genre', y='premiere_semaine_france',
            labels={'genre': 'Genre', 'premiere_semaine_france': 'Médiane des entrées en première semaine'},
            title='🎞️ Médiane des entrées en première semaine en France par genre',
            color='genre',
            color_discrete_map=genres_color)
            
            fig5.update_layout(
                        xaxis_title='Genre',
                        yaxis_title='Médiane des entrées en première semaine',
                        xaxis={'categoryorder':'total descending'},
                        width=600,
                        height=800
                        )
            fig5.update_xaxes(tickangle=45)
            st.plotly_chart(fig5)
            
            st.markdown('<div class="box"><p>On remarque qu’en France, en première semaine, ce sont les films d’action qui génèrent le plus de spectateurs, suivis de près par les films d’aventures. Le drame, genre très représenté chaque année, est loin d’attirer le plus de spectateurs. Ainsi, le lien entre un genre et le succès d’un film est à nuancer notamment par la surreprésentation de certains genres ou encore la perception que nous pouvons en avoir.</p></div>', unsafe_allow_html=True)
            
            
with col4:
            allocine['genre'] = allocine['genre'].str.split(', ')
            allocine = allocine.explode('genre')
            
            genres_to_include = ['Drame', 'Comédie', 'Action', 'Comédie dramatique', 'Aventure', 
                    'Documentaire', 'Biopic', 'Animation', 'Policier', 'Epouvante-horreur', 
                    'Thriller', 'Fantastique']
            
            genres_color = {'Drame': 'blue', 'Comédie': 'red', 'Action': 'orange', 'Comédie dramatique': 'purple', 'Aventure': 'yellow', 
            'Documentaire': 'grey', 'Biopic': 'green', 'Animation': 'pink', 'Policier': 'brown', 'Epouvante-horreur': 'black', 
            'Thriller': 'coral', 'Fantastique': 'turquoise'}
            
            allocine = allocine[allocine['genre'].isin(genres_to_include)]
            
            grouped_data = allocine.groupby(['genre', 'mois', 'mois_nom']).size().reset_index(name='counts')
            
            rows, cols = 3, 4
            fig5 = make_subplots(rows=rows, cols=cols, subplot_titles=genres_to_include)
            
            positions = [(i, j) for i in range(1, rows+1) for j in range(1, cols+1)]
            
            for genre, pos in zip(genres_to_include, positions):
                        data = grouped_data[grouped_data['genre'] == genre]
                        trace = go.Bar(x=data['mois'], y=data['counts'], name=genre, marker_color=genres_color[genre])
                        fig5.add_trace(trace, row=pos[0], col=pos[1])
            fig5.update_xaxes(tickvals=allocine['mois'], ticktext=allocine['mois_nom'])
            fig5.update_layout(height=800, width=1000, title_text="🎞️ Occurrences de films par mois et par genre", showlegend=False)
            fig5.update_xaxes(tickangle=45)
            
            st.plotly_chart(fig5)
            
            st.markdown('<div class="box"><p>Ici, nous n’avons représenté que les 12 genres ayant le plus d’occurrences. On remarque des pics de certains genres à des périodes clé. Notamment les films d’horreurs sont plus représentés en octobre (Halloween). Les films d’animation sont plus représentés pendant la période des fêtes de fin d’année (en décembre) et connaissent également des pics en février et octobre qui peuvent correspondre aux vacances scolaires. Il y a un pic de films d’action pendant l’été (traditionnellement période où sortent les blockbusters).</p></div>', unsafe_allow_html=True)

#---------------#

allocine_notes = allocine[['note_presse', 'note_spectateurs']].apply(lambda x: x.str.replace(',', '.').astype(float))

press_histogram, press_edges = np.histogram(allocine_notes['note_presse'], bins=np.linspace(1, 5, 9))
spect_histogram, spect_edges = np.histogram(allocine_notes['note_spectateurs'], bins=np.linspace(1, 5, 9))

press_percentage = (press_histogram / press_histogram.sum())*100
spect_percentage = (spect_histogram / spect_histogram.sum())*100

p1 = figure(plot_height=400, plot_width=800, title="✍️ Distribution des notes de la presse", tools="", x_range=(1, 5), y_range=(0, 35))
p2 = figure(plot_height=400, plot_width=800, title="✍️ Distribution des notes des spectateurs", tools="", x_range=(1, 5), y_range=(0, 35))
p3 = figure(plot_height=400, plot_width=800, title="✍️ Comparaison de la distribution", tools="", x_range=(1, 5), y_range=(0, 35))

for p in [p1, p2, p3]:
    p.xaxis.axis_label = "Notes"
    p.yaxis.axis_label = "Pourcentage de Films (%)"
    p.grid.grid_line_color = "whitesmoke"

p1.vbar(x=press_edges+0.25, top=press_percentage, width=0.5, fill_color='cornflowerblue', line_color='white')
p2.vbar(x=spect_edges+0.25, top=spect_percentage, width=0.5, fill_color='burlywood', line_color='white')

p3.vbar(x=press_edges+0.25, top=press_percentage, width=0.5, fill_color=None, line_color='cornflowerblue', line_width=3)
p3.vbar(x=spect_edges+0.25, top=spect_percentage, width=0.5, fill_color=None, line_color='burlywood', line_width=3)

hover_p1 = HoverTool(tooltips=[("Pourcentage de Films", "@top{0.2f} %")])
hover_p2 = HoverTool(tooltips=[("Pourcentage de Films", "@top{0.2f} %")])
p1.add_tools(hover_p1)
p2.add_tools(hover_p2)

p3.legend.location = "top_right"

col1, col2, col3, col4, col5 = st.columns([6, 17, 17, 17, 6])

with col2:
            st.bokeh_chart(p1, use_container_width=True)
with col3:
            st.bokeh_chart(p2, use_container_width=True)
with col4:
            st.bokeh_chart(p3, use_container_width=True)
            
col1, col2, col3 = st.columns([2, 17, 2])

with col2:
            st.markdown('<div class="box"><p>En examinant attentivement le graphique comparatif des notes attribuées par les spectateurs et la presse pour des films sortis au cinéma, on remarque que les deux distributions présentent des similitudes notables. Les spectateurs semblent attribuer moins facilement des bonnes notes que la presse, car ils ne donnent quasiment pas de notes au-delà de 4,5. </p></div>', unsafe_allow_html=True)

#---------------#
