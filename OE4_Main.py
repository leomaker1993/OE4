import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions,EntitiesOptions,MetadataOptions,RelationsOptions
from watson_developer_cloud import VisualRecognitionV3
import os

from ibm_watson import ApiException


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey="GzW4AuTQzWI8mv8mwa1BX-z6dI9qPpv8I0EUB87IeV8N")


# If service instance provides API key authentication
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api',
    iam_apikey='FyJ-NE4AusDSxkfLNxVErBCLml9rLXufuDyqqDfkXANX')

# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD')
texto="El presente informe abarca un rápido análisis de lo sucedido en el primer mes luego de haber ocurrido el Terremoto de Pedernales. Toda la información presentada ha sido tomada de cada una de las Mesas Técnicas de Trabajo del COE Nacional. En cuatro semanas luego de un terremoto es muy difícil tener todo el detalle de daños, pérdidas y afectaciones, pero el esfuerzo que han hecho todas y cada una de las entidades gubernamentales que son parte del Sistema Nacional Descentralizado de Gestión de Riesgos han hecho posible el tener este acercamiento a lo sucedido ese trágico 16 de abril de 2016"
texto1='La noche del sábado 16 de abril de 2016 todo el territorio ecuatoriano fue sorprendido por un sismo muy fuerte, que alarmó a toda la población. La primera información emitida por el Instituto Geofísico mencionaba que fue un terremoto de magnitud 7.8 con epicentro en la costa ecuatoriana entre las provincias de Esmeraldas y Manabí.'
response = service.analyze(
    text=texto,
    features=Features(entities=EntitiesOptions(sentiment=True,limit=50),
                      #keywords=KeywordsOptions(),
#                        metadata=MetadataOptions(), #solo para urls y htmls
#                        relations=Reltexto='La noche del sábado 16 de abril de 2016 todo el territorio ecuatoriano fue sorprendido por un sismo muy fuerte, que alarmó a toda la población. La primera información emitida por el Instituto Geofísico mencionaba que fue un terremoto de magnitud 7.8 con epicentro en la costa ecuatoriana entre las provincias de Esmeraldas y Manabí.',ationsOptions(),
                      categories=CategoriesOptions(limit=5))).get_result()

resp_json=json.dumps(response, indent=2)
for entidad in response["entities"]:
    print (entidad["type"])
    print(entidad["text"])
    #print(entidad["disambiguation"]["subtype"])
    print("")

for categorias in response["categories"]:
    categoria=categorias["label"]
    categoria=categoria.split('/')
    #print (categoria)
    for item in categoria:
        print (item)
    print ("")

try:
    nombre_dir="O4E_Referentes_RegistroFotografico"
    for name in os.listdir(nombre_dir):
        for image in os.listdir(os.path.join(nombre_dir, name)):

            dir_image=os.path.join(nombre_dir, name,image)

            print("Archivo:     "+dir_image)
            with open(dir_image, 'rb') as images_file:
                classes = visual_recognition.classify(
                    images_file,
                    threshold='0.6',
                    owners=["IBM"]).get_result()
                for caract_image in classes['images']:
                    for carac in caract_image['classifiers']:
                        for carac1 in carac['classes']:
                            carac2= carac1['class']
                            print ("Característica:    "+carac2)
            print("")
                #print(json.dumps(classes, indent=2))
# Invoke a Visual Recognition method
except ApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)