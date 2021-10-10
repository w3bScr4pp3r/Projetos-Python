import pandas as pd

confirmados = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
mortos = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

date = '10/9/21'  # Data no padrão m/d/aa

df_confirmados = pd.DataFrame(
    confirmados[["Country/Region", date]].groupby("Country/Region").sum())
df_confirmados = df_confirmados.sort_values(by=date, ascending=False)
df_confirmados.columns = ['Confirmados']

df_mortos = pd.DataFrame(
    mortos[["Country/Region", date]].groupby("Country/Region").sum())
df_mortos = df_mortos.sort_values(by=date, ascending=False)
df_mortos.columns = ['Mortes']

tl = ((df_mortos['Mortes'] / df_confirmados['Confirmados'])*100).to_frame()
tl = tl.rename(columns={0: 'Taxa Let'})

resultado = pd.concat([df_confirmados, df_mortos],
                   axis=1, join="inner").join(tl)

top20 = resultado.head(20)

print(top20)

analise = resultado.head(193).describe()

analise = analise.rename({'count':'contador','mean':'média','std':'mediana','min':'minimo','25%':'Q1','50%':'Q2','75%':'Q3','max':'máximo'})

print(analise)
