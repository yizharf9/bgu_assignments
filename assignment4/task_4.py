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
    coors : tuple[float,float]

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
        # print(f"total:{self.space_left},volume:{bird.volume}")
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
        return l_cage

    def __str__(self):
        res = f"Cage ID: {self.ID}\nSize: {self.length,self.depth,self.height}\nColor: {self.color}\nNum of Birds: {self.get_num_of_birds()}\nBirds type: {self.btype}\n"
        return res

    def show_cage(self):
        for line in self.get_cage():
            for j in line:
                print(j,end=" ")
            print()

    def make_id(self):
        rand = random.randint(0, 1000)
        return str(rand)


class Birdroom:
    length: int
    width: int
    height: int
    cages: list[Cage] = []
    blueprint: list[list[str]] = [[]]

    def __init__(self, length: float, width: float, height: float):
        if 2 <= length <= 10 and 2 <= width <= 6 and 2 <= height <= 3:
            self.length = int(length * 100)
            self.width = int(width * 100)
            self.height = int(height * 100)
            # initiating a 2 dim list of the current room measurements
            l = int((self.length) / 10 + 2)
            h = int((self.height) / 10 + 2)
            self.blueprint = [
                [self.set_def_bound(i, j, l, h) for j in range(l)]
                for i in range(int(h))
            ]
        else:
            raise ValueError(
                "invalid cage measurements!\nmake sure the of the following requirements:\n2 <= length <= 10\n2 <= width <= 6\n2 <= height <= 3"
            )

    def get_cages(self):
        return self.cages

    def add_cage(self, cage: Cage, x: float, y: float):
        if (
            self.length < x * 100 + cage.length
            or self.height < y * 100 + cage.height
            or self.width < cage.depth
        ):
            raise ValueError("invalid placement for cage!\nexceeds room boundries")
        if self.check_cage_overlap(cage, x, y):
            self.place_cage(cage, x, y)
        else:
            raise ValueError("invalid placement for cage!\noverlaping an existing cage")

    def place_cage(self, cage: Cage, x: float, y: float):
        _cage = cage.get_cage()
        for i, row in enumerate(_cage):
            x_coor = i + int(x * 10) + 1
            for j, char in enumerate(row):
                y_coor = j + int(y * 10) + 1
                self.blueprint[x_coor][y_coor] = char
        self.cages.append(cage)

        cage.coors = (x , y )

    # a method that returns if a new cage can be placed in a given x,y coordinates within the room
    # by checking overlaping coors with all cages in the room
    def check_cage_overlap(self, added_cage: Cage, a: float, b: float):
        # adjusting measurments to match cage coordinates
        l, h = int(added_cage.length / 10)-1, int(added_cage.height / 10)-1
        a, b = int(a * 10), int(b * 10)
        # setting mores coors for the other corners of the added cage
        _a = a + l
        _b = b + h
        for existing_cage in self.cages:
            # adjusting measurments to match cage coordinates
            _l, _h = int(existing_cage.length / 10)-1, int(existing_cage.height / 10)-1
            x, y = existing_cage.coors
            x, y = int(x * 10), int(y * 10)
            # setting mores coors for the other corners of the existing cage
            _x = x + _l
            _y = y + _h

            cond1 = x <= a <= _x
            cond2 = x <= _a <= _x
            cond3 = y <= b <= _y
            cond4 = y <= _b <= _y
            
            # if at least 2 of the conds return True it means that 
            # at least one of the cages corners is within the current existing cage
            # in other words - the added cage is overlapping with at least one cage
            if (cond1 or cond2) and (cond3 or cond4):
                return False
        return True
    
    def show_room(self):
        for line in self.get_birdroom():
            for j in line:
                print(j, end=" ")
            print()

    def __str__(self):
        return f"{self.length}x{self.width}x{self.height} [cm^3]"
    
    def get_birds(self):
        res = []
        for cage in self.cages:
            res += cage.birds
        return res

    def get_birdroom(self):
        return self.blueprint
    
    def get_most_colorful(self):
        all_birds = self.get_birds()
        most_colorful = all_birds[0]
        for bird in all_birds:
            if len(bird.colors) > len(most_colorful.colors):
                most_colorful = bird
        return most_colorful

    def get_strength(self):
        res = 0
        for bird in self.get_birds():
            if type(bird) == Gouldianfinch:
                res += bird.singing_strength
            elif type(bird) == Budgerigar:
                res += bird.tweet_strength
        return res
    
    # a method that is used in the init func to set boundries of the room
    def set_def_bound(self, i, j, l, h):
        if i == 0 or i == l - 1:
            return "-"
        elif j == 0 or j == h - 1:
            return "|"
        else:
            return "•"
            #! change before submision
            return " "

