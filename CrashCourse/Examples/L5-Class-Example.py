class BakedGood:
    name: str
    fattening: int

    def __init__(self, name: str, fattening: int):
        self.name = name
        self.fattening = fattening


class Consumer:
    weight: int

    def __init__(self):
        self.weight = 160

    def eat(self, food: BakedGood):
        self.weight = self.weight + food.fattening

    def currentWeight(self):
        return self.weight


class Person(Consumer):
    name: str
    gender: str

    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

        super().__init__()

    def sayName(self):
        print("Hi I am " + self.name + " and I am " + self.gender)

    def talk(self):
        if self.currentWeight() < 200:
            print("I am quite thin")
        elif self.currentWeight() < 300:
            print("I am getting chubby")
        elif self.currentWeight() < 400:
            print("Oh man I am getting fat")
        elif self.currentWeight() < 500:
            print("I am so fat I can barely stand")
        else:
            print("I am so fat I can not move anymore!")


def feedTheFeedee(feedee: Consumer, bakedGoods: list) -> Consumer:
    for food in bakedGoods:
        feedee.eat(food)

    return feedee

if __name__ == '__main__':
    cookies: BakedGood = BakedGood('Cookies', 50)
    cupcakes: BakedGood = BakedGood('Cupcakes', 100)
    pie: BakedGood = BakedGood('Pie', 150)
    calorieBomb: BakedGood = BakedGood('Calorie Bomb', 500)

    melanie: Person = Person("Melanie", "Feedee")
    bob: Person = Person("Bob", "Feedee")

    buffet: list = [cookies, cupcakes]
    melanie.sayName()
    melanie.talk()
    melanie = feedTheFeedee(melanie, buffet)
    melanie.talk()

    bobsBurgers: list = [calorieBomb, calorieBomb, cookies]
    bob.sayName()
    bob.talk()
    bob = feedTheFeedee(bob, bobsBurgers)
    bob.talk()
