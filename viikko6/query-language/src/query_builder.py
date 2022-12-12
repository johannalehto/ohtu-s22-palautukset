from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, type):
        return QueryBuilder(And(self.query, HasAtLeast(value, type)))
    
    def hasFewerThan(self, value, type):
        return QueryBuilder(And(self.query, HasFewerThan(value, type)))
    

    def build(self):
            return self.query

    