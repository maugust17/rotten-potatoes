import yaml
from mongodb import db
from models.pelicula import Pelicula
import time
import random

def llenartabla():
    n = random.randint(0,5)
    time.sleep(n/10)
    if not len(Pelicula.objects) > 0:
        with open('movies.yaml') as archivo:
            documento = yaml.full_load(archivo)

            for item, doc in documento.items():       
                for item_pelicula in doc:
                    pelicula = Pelicula(titulo=item_pelicula['titulo'],
                                resumen=item_pelicula['resumen'],
                                duracion=item_pelicula['duracion'],
                                lanzamineto=item_pelicula['lanzamiento'],
                                categoria=item_pelicula['categoria'],
                                elenco=item_pelicula['elenco'],
                                slide=item_pelicula['slide'],
                                thumb=item_pelicula['thumb'])
                    
                    pelicula.save()
                    
            archivo.close() 