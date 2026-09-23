# ============================================================
# Lesson 030 - Dictionary
# ============================================================

# Dictionary:
# بنستخدم الـ Dictionary لتخزين البيانات في شكل:
# Key : Value
#
# مثال:
# "name": "Osama"
#
# Key   = "name"
# Value = "Osama"


# ============================================================
# Dictionary Properties
# ============================================================

# [1] Dictionary items are enclosed in Curly Braces {}
#
# [2] Dictionary items contain Key : Value
#
# [3] Dictionary Key must be Immutable
#     يعني الـ Key مينفعش يكون نوع بيانات قابل للتغيير.
#
#     Allowed:
#     - String
#     - Number
#     - Tuple
#
#     Not Allowed:
#     - List
#
# [4] Dictionary Value can have ANY data type.
#     String, Integer, Float, List, Dictionary... etc.
#
# [5] Dictionary Keys must be UNIQUE.
#    key لو كررت نفس الـ 
#    آخر Value 
#    هي اللي هتتحفظ.
# [6] We access Dictionary elements using the Key.
#     مش باستخدام Index زي الـ List.


# ============================================================
# Create Dictionary
# ============================================================

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}

print(user)

# Output:
# {
#   'name': 'Osama',
#   'age': 36,
#   'country': 'Egypt',
#   'skills': ['Html', 'Css', 'JS'],
#   'rating': 10.5
# }


# ============================================================
# Dictionary Key Must Be Immutable
# ============================================================

# ❌ List cannot be used as a Dictionary Key

# user = {
#     [1, 2, 3, 4]: "Test"
# }

# Output:
# TypeError: unhashable type: 'list'


# السبب:
# List = Mutable
# يعني ممكن تتغير، لذلك مينفعش نستخدمها كـ Dictionary Key.

# لكن Tuple ممكن لأنها Immutable.

example = {
    (1, 2, 3, 4): "Test"
}

print(example)

# Output:
# {(1, 2, 3, 4): 'Test'}


# ============================================================
# Dictionary Keys Must Be Unique
# ============================================================

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5,
    "name": "Ahmed"
}

print(user)

# Output:
# {'name': 'Ahmed', 'age': 36, 'country': 'Egypt',
#  'skills': ['Html', 'Css', 'JS'], 'rating': 10.5}

# لأن "name" اتكرر.
# Python احتفظ بآخر Value:
#
# "name": "Ahmed"


# ============================================================
# Access Dictionary Items
# ============================================================

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}


# الطريقة الأولى:
# Access using the Key مباشرة

print(user["country"])

# Output:
# Egypt


# الطريقة الثانية:
# باستخدام get()

print(user.get("country"))

# Output:
# Egypt


# الاتنين هنا بيرجعوا نفس النتيجة:
#
# user["country"]
# user.get("country")
#
# => Egypt


# ============================================================
# keys()
# ============================================================

# keys() ترجع كل الـ Keys الموجودة في الـ Dictionary.

print(user.keys())

# Output:
# dict_keys(['name', 'age', 'country', 'skills', 'rating'])


# ============================================================
# values()
# ============================================================

# values() ترجع كل الـ Values الموجودة في الـ Dictionary.

print(user.values())

# Output:
# dict_values(['Osama', 36, 'Egypt', ['Html', 'Css', 'JS'], 10.5])


# ============================================================
# Two-Dimensional / Nested Dictionary
# ============================================================

# Dictionary ممكن يكون الـ Value داخله Dictionary تاني.
#
# يعني:
#
# Dictionary
#     |
#     └── Dictionary
#
# وده اسمه Nested Dictionary.


languages = {

    "One": {
        "name": "Html",
        "progress": "80%"
    },

    "Two": {
        "name": "Css",
        "progress": "90%"
    },

    "Three": {
        "name": "Js",
        "progress": "90%"
    }

}


# ============================================================
# Print Entire Nested Dictionary
# ============================================================

print(languages)

# Output تقريباً:
#
# {
#   'One': {'name': 'Html', 'progress': '80%'},
#   'Two': {'name': 'Css', 'progress': '90%'},
#   'Three': {'name': 'Js', 'progress': '90%'}
# }


# ============================================================
# Access Dictionary Inside Dictionary
# ============================================================

print(languages["One"])

# Output:
# {'name': 'Html', 'progress': '80%'}


print(languages["Three"])

# Output:
# {'name': 'Js', 'progress': '90%'}


# لو عايز Value معينة جوه الـ Nested Dictionary:
#
# الأول نحدد الـ Key الخارجي:
# ["Three"]
#
# وبعد كده الـ Key الداخلي:
# ["progress"]

print(languages["Three"]["progress"])

# Output:
# 90%


print(languages["Three"]["name"])

# Output:
# Js


# الفكرة:
#
# languages
#    |
#    └── "Three"
#           |
#           ├── "name"     -> "Js"
#           └── "progress" -> "90%"
#
# لذلك:
#
# languages["Three"]["progress"]
#
# Output:
# 90%


# ============================================================
# Dictionary Length
# ============================================================

# len() بتحسب عدد الـ Keys في الـ Dictionary.

print(len(languages))

# Output:
# 3

# لأن عندنا:
# One
# Two
# Three


# ممكن كمان نحسب عدد العناصر داخل Dictionary معين.

print(len(languages["Two"]))

# Output:
# 2

# لأن Dictionary "Two" يحتوي على:
#
# name
# progress


# ============================================================
# Create Dictionary From Variables
# ============================================================

# ممكن نعمل Dictionaries منفصلة الأول،
# وبعد كده نجمعهم داخل Dictionary أكبر.


frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}


# نجمع الـ Dictionaries الثلاثة داخل Dictionary واحد.

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree
}

print(allFramework)

# Output تقريباً:
#
# {
#   'one': {'name': 'Vuejs', 'progress': '80%'},
#   'two': {'name': 'ReactJs', 'progress': '80%'},
#   'three': {'name': 'Angular', 'progress': '80%'}
# }


# ============================================================
# Important Difference
# ============================================================

# List:
#
# devices = ["Router", "Switch", "Firewall"]
#
# Access باستخدام Index:
# devices[0]
#
# Output:
# Router


# Dictionary:
#
# device = {
#     "hostname": "FGT-01",
#     "vendor": "Fortinet"
# }
#
# Access باستخدام Key:
# device["hostname"]
#
# Output:
# FGT-01


# ============================================================
# Network Automation Example
# ============================================================

# الـ Dictionary مهم جداً في Network Automation.
# لأننا ممكن نمثل كل Device ومعلوماته بالشكل ده:

device = {
    "hostname": "FGT-01",
    "vendor": "Fortinet",
    "ip": "10.0.0.1",
    "model": "FortiGate",
    "interfaces": ["wan1", "wan2", "port1"]
}

print(device["hostname"])
# Output:
# FGT-01

print(device["ip"])
# Output:
# 10.0.0.1

print(device["interfaces"])
# Output:
# ['wan1', 'wan2', 'port1']


# وممكن نعمل Nested Dictionary لأكتر من Device:

network_devices = {

    "device1": {
        "hostname": "FGT-01",
        "vendor": "Fortinet",
        "ip": "10.0.0.1"
    },

    "device2": {
        "hostname": "F5-01",
        "vendor": "F5",
        "ip": "10.0.0.2"
    }

}

print(network_devices["device1"]["vendor"])

# Output:
# Fortinet


# ============================================================
# Quick Summary
# ============================================================

# Dictionary Syntax:
# {Key: Value}


# Example:
# user = {
#     "name": "Osama",
#     "age": 36
# }


# Access Value:
# user["name"]
# -> Osama


# Another Access Method:
# user.get("name")
# -> Osama


# Get All Keys:
# user.keys()


# Get All Values:
# user.values()


# Dictionary Key:
# Must be Immutable
#
# ✅ String
# ✅ Number
# ✅ Tuple
# ❌ List


# Dictionary Value:
# Can be ANY data type.


# Keys:
# Must be Unique.


# Nested Dictionary:
# languages["Three"]["progress"]
# -> 90%


# Dictionary Length:
# len(languages)
# -> 3


# Nested Dictionary Length:
# len(languages["Two"])
# -> 2


# أهم فكرة:
#
# List       -> Access by Index
# Dictionary -> Access by Key
#
# List:
# devices[0]
#
# Dictionary:
# device["hostname"]
#
# الـ Dictionary من أهم الـ Data Structures اللي هنستخدمها
# بعد كده في Python و Network Automation.