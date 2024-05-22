import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from bokeh.plotting import figure
from bokeh.models import HoverTool

background_image = '''
    <style>
    .stApp {
        background-color: white;
        background-image: url("https://github.com/NicolasDartois/streamlit_2/blob/main/images/background.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        text-align: left;
    }
    </style>
    '''
st.markdown(background_image, unsafe_allow_html=True)

allocine = pd.read_csv('data/allocine.csv')


#---------------#
st.markdown('<div class="box"><p>', unsafe_allow_html=True)
            
pays_counts = allocine['pays'].value_counts()
top_pays = pays_counts[:8]
autres = pays_counts[8:].sum()
top_pays['Autres'] = autres    
fig1 = go.Figure(data=[go.Pie(labels=top_pays.index, values=top_pays.values, hole=.3)])
fig1.update_traces(textposition='inside', textinfo='percent+label')
fig1.update_layout(
            width=800,
            height=600,
            title_text='Répartition des films par pays',
            annotations=[dict(text='Pays', x=0.5, y=0.5, font_size=20, showarrow=False)],
            legend_title="Pays"
            )
st.plotly_chart(fig1)

st.markdown('</p></div>', unsafe_allow_html=True)
#---------------#

fig2 = px.box(allocine, x="premiere_semaine_france",
            hover_data=['titre_original'],
            title='Analyse de la distribution de notre target: première semaine en France',
            labels={'premiere_semaine_france': 'Première semaine en France'})
fig2.update_layout(width=800, height=400)
fig2.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey'))
st.plotly_chart(fig2)

#---------------#

filtered_data = allocine[(allocine['annee'] > 2000) & (allocine['annee'] <= 2023)]
film_counts = filtered_data['annee'].value_counts().sort_index()
colorscale = [[0, 'blue'], [1, 'orange']]
fig3 = go.Figure(data=[go.Bar(x=film_counts.index, y=film_counts, marker=dict(color=film_counts, colorscale=colorscale, cmin=0, cmax=film_counts.max()))])
fig3.update_layout(width=800, height=400)
fig3.update_layout(title='Nombre de films sortis par année en France (après 2000)', xaxis_title='Année de sortie', yaxis_title='Nombre de films')
st.plotly_chart(fig3)

#---------------#
correlation = allocine['cumul_france'].corr(allocine['premiere_semaine_france'])
fig4 = px.scatter(
            allocine, 
            x='cumul_france', 
            y='premiere_semaine_france',
            hover_data=['titre_original'],
            title=f'Corrélation entre le cumul en France et la première semaine en France: {correlation:.2f}',
            labels={'cumul_france': 'Cumul en France', 'premiere_semaine_france': 'Première semaine en France'},
            opacity=0.5,
            trendline='ols'
            )
fig4.data[1].line.color = 'red'
fig4.update_layout(width=800, height=400)
fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
fig4.update_xaxes(showgrid=True, title='Cumul en France')
fig4.update_yaxes(showgrid=True, title='Première semaine en France')
st.plotly_chart(fig4)

#---------------#
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
title='Médiane des entrées en première semaine en France par genre',
color='genre',
color_discrete_map=genres_color)

fig5.update_layout(
xaxis_title='Genre',
yaxis_title='Médiane des entrées en première semaine',
xaxis={'categoryorder':'total descending'},
height=800
)
fig5.update_xaxes(tickangle=45)
fig5.update_layout(width=800, height=600)
st.plotly_chart(fig5)

#---------------#

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

rows, cols = 6, 2
fig5 = make_subplots(rows=rows, cols=cols, subplot_titles=genres_to_include)

positions = [(i, j) for i in range(1, rows+1) for j in range(1, cols+1)]

for genre, pos in zip(genres_to_include, positions):
            data = grouped_data[grouped_data['genre'] == genre]
            trace = go.Bar(x=data['mois'], y=data['counts'], name=genre, marker_color=genres_color[genre])
            fig5.add_trace(trace, row=pos[0], col=pos[1])
fig5.update_xaxes(tickvals=allocine['mois'], ticktext=allocine['mois_nom'])
fig5.update_layout(height=1600, width=800, title_text="Occurrences de films par mois et par genre", showlegend=False)
fig5.update_xaxes(tickangle=45)

st.plotly_chart(fig5)

#---------------#

actors_columns = ['acteur_1', 'acteur_2', 'acteur_3', 'acteur_4']
melted_actors = pd.melt(allocine, id_vars=['premiere_semaine_france'], value_vars=actors_columns, value_name='actor').dropna().drop(columns='variable', axis=1)

top_10_actors = melted_actors.groupby('actor')['premiere_semaine_france'].sum().nlargest(10)

fig6 = px.bar(top_10_actors, x=top_10_actors.values, y=top_10_actors.index, orientation='h',
text=top_10_actors.values,
labels={'y': 'Acteurs', 'x': 'Nombre total d\'entrées première semaine France'},
color_discrete_sequence=['green'],
title='Top 10 des acteurs avec le plus grand nombre d\'entrées en première semaine France')

fig6.update_traces(texttemplate='%{text:.3s}', textposition='inside', hovertemplate='<b>%{y}</b><br>Nombre total d\'entrées première semaine: %{x}<extra></extra>')
fig6.update_layout(
    xaxis_title='Nombre total d\'entrées première semaine France',
    yaxis_title='Acteurs',
    uniformtext_minsize=8, uniformtext_mode='hide',
    height=400, width=800, yaxis_autorange='reversed'
)
st.plotly_chart(fig6)

#---------------#

allocine_notes = allocine[['note_presse', 'note_spectateurs']].apply(lambda x: x.str.replace(',', '.').astype(float))

press_histogram, press_edges = np.histogram(allocine_notes['note_presse'], bins=np.linspace(1, 5, 9))
spect_histogram, spect_edges = np.histogram(allocine_notes['note_spectateurs'], bins=np.linspace(1, 5, 9))

press_percentage = (press_histogram / press_histogram.sum())*100
spect_percentage = (spect_histogram / spect_histogram.sum())*100

p1 = figure(plot_height=250, plot_width=800, title="Distribution des notes de la presse", tools="", x_range=(1, 5), y_range=(0, 35))
p2 = figure(plot_height=250, plot_width=800, title="Distribution des notes des spectateurs", tools="", x_range=(1, 5), y_range=(0, 35))
p3 = figure(plot_height=250, plot_width=800, title="Comparaison de la distribution", tools="", x_range=(1, 5), y_range=(0, 35))

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
st.bokeh_chart(p1, use_container_width=True)
st.bokeh_chart(p2, use_container_width=True)
st.bokeh_chart(p3, use_container_width=True)

#---------------#
allocine_budget = pd.read_csv('data/Allocine_v2_8.csv')
correlation = allocine_budget['premiere_semaine_france'].corr(allocine_budget['budget_euro'])

def millions_formatter(x, pos):
    return f'{x / 1e6}M'
formatter = FuncFormatter(millions_formatter)

plt.figure(figsize=(20, 10))

sns.regplot(x='budget_euro', y='premiere_semaine_france', data=allocine_budget)
plt.xlabel('Budget du film')
plt.ylabel('Première semaine en France (nombre de spectateurs)')
plt.title(f'Corrélation entre le budget du film et la première semaine en France. Pearson : {round(correlation, 3)}')
plt.gca().yaxis.set_major_formatter(formatter)
plt.gca().xaxis.set_major_formatter(formatter)
st.pyplot(plt)
#---------------#
