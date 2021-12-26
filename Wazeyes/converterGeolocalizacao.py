from geopy.geocoders import Nominatim
from Funções.funcoesJSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")  #nome do app
dicionario=ler_arquivo("entradaJSON")
lista=dicionario["endereco"]
endereco=lista[0] + "," + lista[1] + "," + lista[2] + "," + lista[3]
location = geolocator.geocode(endereco)
saida={"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida, "saidaJSON")