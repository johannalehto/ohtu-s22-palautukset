from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def build(self):
            return self.query

    