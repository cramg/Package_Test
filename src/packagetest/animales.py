class Ave():

    def __init__(self, pluma_color="gris"):
        self.especies = ['aguila', 'gallina', 'pato']
        self.pluma    = pluma_color

    def listAve(self):
        print ('Estos son los animales en la clase')
        for animal in self.especies:
            print('\t%s ' % animal)

class Mamifero():

    def __init__(self):
        self.especies = ['gato', 'perro', 'mono']

    def listMam(self):
        print ('Estos son los animales en la clase')
        for animal in self.especies:
            print('\t%s ' % animal)

class Zoo():

    def __init__(self, mamifero, ave):

        self.mamifero = mamifero
        self.ave      = ave


