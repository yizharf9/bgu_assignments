from datetime import datetime, date
from random import randrange

# todo - change dependencies
import random

random.seed()


class Bird:
    ID: str
    btype: str
    birth: str
    colors: list[str]
    foodtype: str
    volume: int

    def __init__(
        self, ID: str, btype: str, birth: str, colors: list, foodtype: str, volume: int
    ) -> None:
        self.ID = self.make_id()

        # type_list = ["Finch", "Parrot"]
        type_list = ["L", "B", "G", "Z"]
        if btype in type_list:
            self.btype = btype
        else:
            raise ValueError(
                "invalid bird type!\nmust be a string representing the bird type!"
            )

        # ? return the current datetime as birth if no alt is given
        if len(birth) != 0:
            self.birth = birth  # alt
        # todo - value checking required!!!
        else:
            # print(str(datetime.now()))
            year, month, day = str(date.today()).split("-")  # current
            self.birth = f"{day}:{month}:{year}"

        self.colors = colors
        foods = ["Corn", "Seeds"]
        if foodtype in foods:
            self.foodtype = foodtype
        else:
            raise ValueError("invalid food type!")
        if type(volume) == int:
            self.volume = volume
        else:
            raise ValueError("volume must be an integer!")

    def __str__(self) -> str:
        return f"Bird ID: {self.ID}\nBird type: {self.get_type()}\nAge: {self.get_age()}\nColors: {self.get_colors()}\nFood type: {self.get_food_type()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Bird):
            raise TypeError("comparison with non Bird objects is invalid!")
        else:
            return self.btype == other.btype

    def __gt__(self, other) -> bool:
        if not isinstance(other, Bird):
            raise TypeError("comparison with non Bird objects is invalid!")
        else:
            return len(self.colors) > len(other.colors)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Bird):
            raise TypeError("comparison with non Bird objects is invalid!")
        else:
            return len(self.colors) < len(other.colors)

    def make_id(self):
        rand = random.randint(0, 1000)
        return str(rand)

    def get_age(self):
        curr_datetime = datetime.now().date()
        day, month, year = self.birth.split(":")
        _birth = datetime(day=int(day), month=int(month), year=int(year)).date()
        # print(f"curr:{curr_datetime}\nbirth:{_birth}")
        res = curr_datetime - _birth
        Years = res.days // 365
        Months = (res.days - Years * 365) // 28
        Days = res.days - Years * 365 - Months * 28
        res = f"{Years}Y,{Months}M,{Days}D"
        # print(f"age is {res}")
        return res

    def get_type(self):
        return self.btype

    def get_colors(self):
        return self.colors

    def get_food_type(self):
        return self.foodtype

    def get_volume(self):
        return self.volume


class Finch(Bird):
    def __init__(self, ID: str, btype: str, birth: str, colors: list, volume: int):
        Bird.__init__(self, ID, btype, birth, colors, "Seeds", volume)

    def nest_building(self):
        age = self.get_age()
        i: int = age.find("Y")
        n = int(age[:i])
        res = ["|"] + n * ["_"] + ["|"]
        return res


class Parrot(Bird):
    def __init__(self, ID: str, btype: str, birth: str, colors: list, volume: int):
        Bird.__init__(self, ID, btype, birth, colors, foodtype="Corn", volume=volume)

    def find_nestbox(self):
        age = self.get_age()
        i: int = int(age.find("Y"))
        n = int(age[:i])
        if n < 3:
            return None
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(" ")
                if j == 0 or i == 0 or j == n - 1 or i == n - 1:
                    row[j] = "*"
            res.append(row)
            print(row)
        return res


class Zebrafinch(Finch):
    def __init__(self, ID: str, birth: str, colors: list):
        legal_colors = ["Brown", "Orange", "Black", "White"]
        filtered = filter(lambda color: color in legal_colors, colors)
        colors = [color for color in filtered]
        if len(colors) == 0:
            colors = ["Brown"]

        Finch.__init__(self, ID, "Z", birth, colors, volume=27000)

    def get_type(self):
        return "Zebra Finch"

    def jump(self):
        return "I like to jump"


class Gouldianfinch(Finch):
    singing_strength: int

    def __init__(self, ID: str, birth: str, colors: list):
        legal_colors = [
            "Red",
            "Green",
            "Blue",
            "Yellow",
            "Orange",
            "Black",
            "Purple",
            "White",
        ]
        filtered = filter(lambda color: color in legal_colors, colors)
        colors = [color for color in filtered]
        if len(colors) == 0:
            choice = random.choice(legal_colors)
            colors = [choice]
        self.singing_strength = random.randrange(1, 11)
        Finch.__init__(self, ID, "G", birth, colors, 96000)

    def get_type(self):
        return "Gouldian Finch"

    def sing(self):
        return "I like to sing", self.singing_strength

    def __str__(self) -> str:
        res = Finch.__str__(self)
        return res + f"\nSinging strength: {self.singing_strength}"


class Budgerigar(Parrot):
    tweet_strength: int

    def __init__(self, ID: str, birth: str, colors: list):
        legal_colors = ["Green", "Blue", "Yellow", "Gray", "Purple", "White"]

        filtered = filter(lambda color: color in legal_colors, colors)
        colors = [color for color in filtered]
        if len(colors) == 0:
            choice = random.choice(legal_colors)
            colors = [choice]

        self.tweet_strength = random.randrange(1, 11)

        Parrot.__init__(self, ID, "B", birth, colors, 96000)

    def get_type(self):
        return "Budgerigar"

    def __str__(self) -> str:
        res = Parrot.__str__(self) + f"\nTweet strength: {self.tweet_strength}"
        return res

    def tweet(self):
        return "I like to tweet", self.tweet_strength


class Lovebird(Parrot):
    def __init__(self, ID: str, birth: str, colors: list):
        legal_colors = ["Red", "Green", "Blue", "Yellow", "Black", "White"]

        filtered = filter(lambda color: color in legal_colors, colors)
        colors = [color for color in filtered]
        if len(colors) == 0:
            choice = random.choice(legal_colors)
            colors = [choice]

        Parrot.__init__(self, self.make_id(), "L", birth, colors, 120_000)

    def get_type(self):
        return "Love Bird"

    def kiss(self):
        return "I like to kiss"


class Cage:
    ID: str
    length: int
    depth: int
    height: int
    color: str
    birds: list[Bird] = []
    space_left: int
    btype: str = "#"

    def __init__(self, ID: str, length: int, depth: int, height: int, color: str):
        self.ID = self.make_id()

        if 30 <= length <= 180 and 30 <= depth <= 60 and 40 <= height <= 180:
            self.length = length
            self.depth = depth
            self.height = height
            self.space_left = length * depth * height
        else:
            raise ValueError(
                "invalid sizes for the cage!\nmake sure of the following:\n30<=length<=180\n30<=depth<=60\n40<=height<=180"
            )
        legal_colors = ["White", "Black", "Silver"]
        if color in legal_colors:
            self.color = color
        else:
            raise ValueError(
                "invalid color for cage!\ncolor can be one of the following:\nWhite,Black,Silver"
            )

    def add_bird(self, bird: Bird):
        l = self.length
        d = self.depth
        h = self.height
        print(f"total:{self.space_left},volume:{bird.volume}")
        cond = bird.volume <= self.space_left

        if self.btype != "#" and bird.btype != self.btype:
            raise TypeError(
                f"cage can only hold 1 type of bird!\nthis cage holds ({self.btype}) type birds"
            )
        elif cond and self.btype == "#":
            self.birds.append(bird)
            self.btype = bird.btype
            self.space_left -= bird.volume
        elif cond:
            self.birds.append(bird)
            self.space_left -= bird.volume
        return cond

    def get_birds(self):
        return self.birds

    def get_num_of_birds(self):
        return len(self.birds)

    def get_cage(self):
        l_cage = [
            int(self.length / 10) * self.btype for i in range(int(self.height / 10))
        ]
        # for row in l_cage:
        #     print(row)
        return l_cage

    def __str__(self):
        res = f"Cage ID: {self.ID}\nSize: {self.length,self.depth,self.height}\nColor: {self.color}\nNum of Birds: {self.get_num_of_birds()}\nBirds type: {self.btype}\n"
        return res

    def make_id(self):
        rand = random.randint(0, 1000)
        return str(rand)


 