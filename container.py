from animal import Animal

class Container:
    'Animal container'
    game = False
    rootNode = None

    def __init__(self):
        self.game = True

    def getRootNode(self):
        return self.rootNode

    def setRootNode(self, rootNode):
        self.rootNode = rootNode

    def initRoot(self):
        #newAnimalName = raw_input('New animal type: ')
        newAnimal = Animal('hund')
        #newQuestion = raw_input('New question: ')
        newAnimal.setQuestion('har den hale')
        self.rootNode = newAnimal

        
