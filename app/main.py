import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda item:item["Continent"]=="South America",data))
  countries = list(map(lambda x:x["Country"], data))
  percentages = list(map(lambda x:x["World Population Percentage"], data))
  charts.generat_pie_chart(countries, percentages)
  
  country = input("Type country =>")

  result = utils.population_by_country(data, country)
  if len(result)>0:
    country = result[0]
    k, v = utils.get_population(country)
    charts.generat_bar_chart(country["Country"], k, v)

if __name__ == "__main__":
  run()