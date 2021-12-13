class Book():
    listPersons = list()

    def add_person(self, person):
        self.listPersons.append(person)

    def show_all(self):
        for i in range(len(self.listPersons)):
            print(self.listPersons[i].__dict__)
            print('\n')

    def del_all(self):
        del self.listPersons[i]