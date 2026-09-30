def func1(text):
    return len(text)
print(func1("Привіт"))
#
def func2(text1, text2):
    return text1 + text2
print(func2("Привіт", "Україно"))
#
def func3(number1):
    return number1 ** 2
print(func3 (5))
#
def func4(number1, number2):
    return number1 + number2
print(func4(5, 5))
#
def func5(number1, number2):
    return number1 // number2, number1 % number2
print(func5(10, 12))

def func6 (numbers):
    return sum(numbers) / len(numbers)
print(func6([10,20,30]))

def func7 (list1, list2):
    result = []
    for number in list1:
        if number in list2:
            result.append(number)
    return result
print(func7([1,2,3,4,5],[1,2,7,5,6]))

def func8(data):
    keys = list(data.keys())
    print(keys)
func8({'Name': 1, 'age': 2, 'gender': 3})

def func9(data1,data2):
    keys = data1 | data2
    return keys
print(func9({'name': 'city'}, {'age': 'gender:'}))

def func10(set1, set2):
    return set1 | set2
print(func10 ({10,20,30}, {45,55,65}))

def func11(set1, set2):
    return set1 <= set2
print(func11 ({10,20,30}, {10,20,30,40}))

def func12(number):
    if number % 2 == 0:
        return 'Парне'
    else:
        return 'Непарне'
print(func12(11))
print(func12(12))

def func13(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
print(func13([1, 2, 3, 4, 5]))

func14 = lambda number: 'Парне' if number % 2 == 0 else 'Непарне'
print(func14(14))
print(func14(15))


