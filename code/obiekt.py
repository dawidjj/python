class Test:
    def __init__(self):
        self._variable = 5

    @property
    def variable(self):
        print('sssss')
        return self._variable

    @variable.setter
    def variable(self, data):
        print('ustawiam')
        self._variable = data

    @variable.deleter
    def variable(self):
        print('usuwam')
        del self._variable

    def hello(self):
        Test.statyczna()
        print('siema')

    @staticmethod
    def statyczna():
        print('statyczna')

    # dla developerów
    def __repr__(self):
        return f'Test(_variable: {self.variable})'

    # dla użytkowników przy zrobieniu print
    def __str__(self):
        return f'Test(_variable: {self.variable})'