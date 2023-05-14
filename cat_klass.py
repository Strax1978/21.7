cats = [
    {
     "name": "Барон",
     "gender": "мальчик",
     "age": "2",
    },
    {
      "name": "Сэм",
     "gender": "мальчик",
     "age": "2",
    },
]
class Cat:
    def __init__(self, name="", gender="", age=""):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print("\n")
    print(cat_obj.name, cat_obj.gender, cat_obj.age)