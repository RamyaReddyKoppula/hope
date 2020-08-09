class home:
    def __init__(self, country, city, a, b):
        self.country = country
        self.city = city
        self.a = a
        self.b = b
    def ramya(self):
        return f"my country is {self.country} and i am from {self.city}"
    def add(self):
        return 2*(self.a+self.b)

class foreigner(home):
    def __init__(self, c, ci, h, d):
        super()._init__(country=c, city=ci, a=h, b=d)
r = home("india", "vijayawada", 2, 3)
print(r.ramya())
print(r.add())
i = home("morocco", "llb", 5, 5)
print(i.ramya())
print(i.add())
