import utils
import read_csv
import charts
import pandas as pd

def run():

  ## Solucion graficar el % de poblacion en pie
  # filtrar que solo muestre latinoamerica

  '''

  data= list(filter(lambda item: item['Continent']== 'South America',data))
  countries = list(map(lambda x:x['Country/Territory'],data))
  percentajes = list(map(lambda x:x['World Population Percentage'],data))
  charts.generate_pie_chart(countries,percentajes)
  '''
  #Codigo en pandas
  df = pd.read_csv("data.csv")  # Nos ahorramos el método creado read_csv.py
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentajes = df['World Population Percentage'].values

  charts.generate_pie_chart(countries,percentajes)

  ## Solucion Poblacion por pais y año
  

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  
  result = utils.population_by_country(data,country)

  if len(result) >0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)
  
  
  

if __name__ == '__main__':
  run()