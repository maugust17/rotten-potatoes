from mongodb import db

class Pelicula(db.Document):


    titulo = db.StringField()
    resumen = db.StringField()
    duracion = db.StringField()
    lanzamiento = db.StringField()
    categoria = db.StringField()
    elenco = db.StringField()
    direccion = db.StringField()
    reviews = db.ListField()
    slide = db.StringField()
    thumb = db.StringField()

    def add_review(self, review):
        self.reviews.append(review)