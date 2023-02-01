from datetime import datetime as dt


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def validate_title(title: int):
    if title < 0:
        raise NegativeTitlesError("titles cannot be negative")


def validate_first_cup(first_cup: str):
    year = dt.strptime(first_cup, "%Y-%m-%d").year
    if not (year >= 1930 and ((year % 1930) % 4) == 0):
        raise InvalidYearCupError("there was no world cup this year")


def validate_title_first_cup(title: int, first_cup: str):
    year = dt.strptime(first_cup, "%Y-%m-%d").year
    present = (2022 % 1930) / 4
    cup = (year % 1930) / 4
    if (present - cup) < title:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


def data_processing(**data):
    try:
        validate_title(data["titles"])
        validate_first_cup(data["first_cup"])
        validate_title_first_cup(data["titles"], data["first_cup"])
    except NegativeTitlesError as err:
        print(err.message)
    except InvalidYearCupError as err:
        print(err.message)
    except ImpossibleTitlesError as err:
        print(err.message)


data = {
    "name": "França",
    "titles": -3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2000-10-18",
}

data1 = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1911-10-18",
}

data2 = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1932-10-18",
}

data3 = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}

print(data_processing(**data))
print(data_processing(**data1))
print(data_processing(**data2))
print(data_processing(**data3))
