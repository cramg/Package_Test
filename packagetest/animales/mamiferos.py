class Mamifero():

    def __init__(self):
        self.especies = ['gato', 'perro', 'mono']

    def listMam(self):
        print ('Estos son los animales en la clase')
        for animal in self.especies:
            print('\t%s ' % animal)
