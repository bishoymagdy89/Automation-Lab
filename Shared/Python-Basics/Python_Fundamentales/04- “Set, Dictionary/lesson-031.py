# ============================================================
# Lesson 031 - Dictionary Methods Part One
# ============================================================


# ============================================================
# clear()
# ============================================================

# clear() removes ALL items from the Dictionary.
# الـ Dictionary نفسه يفضل موجود، لكن يصبح فاضي.

user = {
    "name": "Osama"
}

print(user)

# Output:
# {'name': 'Osama'}


user.clear()

print(user)

# Output:
# {}


# ============================================================
# update()
# ============================================================

# update() is used to add new Key : Value pairs
# or update an existing Key.

member = {
    "name": "Osama"
}

print(member)

# Output:
# {'name': 'Osama'}


# الطريقة الأولى لإضافة Key جديد:
# نكتب اسم الـ Dictionary ثم الـ Key الجديد.

member["age"] = 36

print(member)

# Output:
# {'name': 'Osama', 'age': 36}


# الطريقة الثانية:
# باستخدام update()

member.update({"country": "Egypt"})

print(member)

# Output:
# {'name': 'Osama', 'age': 36, 'country': 'Egypt'}


# يعني الاتنين يقدروا يضيفوا عنصر جديد:

# member["age"] = 36
#
# member.update({"country": "Egypt"})


# update() ممكن كمان تعدل Value موجودة بالفعل.

member.update({"name": "Ahmed"})

print(member)

# Output:
# {'name': 'Ahmed', 'age': 36, 'country': 'Egypt'}


# ============================================================
# copy()
# ============================================================

# copy() creates a copy of the Dictionary.
# النسخة تبقى Dictionary منفصلة عن الأصل
# بالنسبة للعناصر البسيطة الموجودة في المثال.

main = {
    "name": "Osama"
}


b = main.copy()

print(b)

# Output:
# {'name': 'Osama'}


# دلوقتي نعدل الـ original Dictionary:

main.update({"skills": "Fighting"})

print(main)

# Output:
# {'name': 'Osama', 'skills': 'Fighting'}


# لكن b لم تتغير:

print(b)

# Output:
# {'name': 'Osama'}


# الفكرة:
#
# main
# ├── name   -> Osama
# └── skills -> Fighting
#
# b
# └── name   -> Osama
#
# لأن b اتعملت باستخدام:
#
# main.copy()


# IMPORTANT:
# copy() هنا بتعمل Shallow Copy.
# معنى كده إن المثال البسيط اللي فوق فعلاً النسخة مستقلة،
# لكن لو عندنا Lists أو Dictionaries متداخلة جواها،
# الموضوع له تفاصيل إضافية هنتعلمها بعدين.


# ============================================================
# keys()
# ============================================================

# keys() returns all Dictionary Keys.

print(main.keys())

# Output:
# dict_keys(['name', 'skills'])


# ============================================================
# values()
# ============================================================

# values() returns all Dictionary Values.

print(main.values())

# Output:
# dict_values(['Osama', 'Fighting'])


# ============================================================
# Network Automation Example
# ============================================================

# نفس الأفكار دي مهمة جداً في Network Automation.
#
# مثلاً عندنا بيانات FortiGate:

device = {
    "hostname": "FGT-01",
    "ip": "10.0.0.1"
}


# نضيف معلومة جديدة:

device["vendor"] = "Fortinet"

print(device)

# Output:
# {'hostname': 'FGT-01', 'ip': '10.0.0.1', 'vendor': 'Fortinet'}


# أو باستخدام update():

device.update({"model": "FortiGate"})

print(device)

# Output:
# {
#   'hostname': 'FGT-01',
#   'ip': '10.0.0.1',
#   'vendor': 'Fortinet',
#   'model': 'FortiGate'
# }


# نقدر نشوف كل الـ Keys:

print(device.keys())

# Output:
# dict_keys(['hostname', 'ip', 'vendor', 'model'])


# ونشوف كل الـ Values:

print(device.values())

# Output:
# dict_values(['FGT-01', '10.0.0.1', 'Fortinet', 'FortiGate'])


# ============================================================
# Quick Summary
# ============================================================

# clear()
# --------
# Removes ALL items.
#
# user.clear()
#
# {'name': 'Osama'}
#       ↓
# {}


# update()
# --------
# Add or update Key : Value.
#
# member.update({"country": "Egypt"})


# Direct Addition
# ---------------
# Another way to add a new item:
#
# member["age"] = 36


# copy()
# ------
# Creates a copy of the Dictionary.
#
# b = main.copy()
#
# تعديل العناصر البسيطة في main بعد كده
# مش هيعدل نفس العناصر في b.


# keys()
# ------
# Returns all Keys.
#
# main.keys()
#
# -> dict_keys(['name', 'skills'])


# values()
# --------
# Returns all Values.
#
# main.values()
#
# -> dict_values(['Osama', 'Fighting'])


# أهم Methods في الدرس:
#
# Dictionary.clear()
# Dictionary.update()
# Dictionary.copy()
# Dictionary.keys()
# Dictionary.values()