#import numpy as np
import pandas as pd
import plotly as py
import plotly.express as pex

df = pd.read_csv(r'C:\Users\prakash.pandey\Downloads\Covid-19.csv')

print(df.head())

df=pd.melt(df,id_vars=['Province/State','Country/Region','Lat','Long'],var_name = 'Date',value_name='Cases')

df=df.rename(columns = {'Country/Region':'Country'})
df_countries = df.groupby(['Country','Date']).sum().reset_index().sort_values('Date',ascending='False')
df_countries = df_countries[df_countries['Cases']>0].drop_duplicates(subset = ['Country'])
df_countries = df_countries.replace({'Date':})
print(df_countries)
#print(df_countries[df_countries['Date'] =='3/3/20'])

Choropleth_data = py.graph_objs.Choropleth(locations = df_countries['Country']
                                            ,locationmode='country names'
                                            ,z=df_countries['Cases']
                                            ,colorscale='Bluered'
                                            ,marker_line_color = 'Black'
                                            ,marker_line_width = 0.25
                                            )
fig = py.graph_objs.Figure(data = Choropleth_data)

fig.update_layout(title_text = 'Confirmed_cases as of {}'.format(df_countries['Date'].max())
                                     ,title_x = 0.5
                                     ,geo=dict(showframe = False
                                               ,showcoastlines = False
                                               ,projection_type = 'equirectangular'
                                             )
                                    )

df_countrydate = df[df['Cases']>0]
df_countrydate = df_countrydate.groupby(['Date','Country']).sum().reset_index()

fig=pex.choropleth(df_countrydate
                      ,locations='Country'
                      ,locationmode='country names'
                      ,color='Cases'
                      ,color_continuous_scale='Viridis'
                      ,hover_name='Country'
                      ,animation_frame='Date'
                      )
fig.update_layout(title_text='Global Spread Covid-19'
                  ,title_x=0.5
                  ,geo=dict(showframe=False,showcoastlines=False)
                )
fig.show()