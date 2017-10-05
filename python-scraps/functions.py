'''function defination'''
def testing_functions(value):
    print(value)
testing_functions("this argument")

'''Passing an Arbitrary Number of Arguments'''
def pizza_toppings(*toppings):
    print(*toppings)

def pizza_toppings_tuple(*toppings):
    print('tuple')
    print(toppings)

pizza_toppings('onions', 'pepperoni', 'mushrooms')
pizza_toppings_tuple('onions', 'pepperoni', 'mushrooms')

'''*works for as unpacking'''
print_this_list = ['one', 'two', 'three']
print(print_this_list)
print(*print_this_list)

'''using arbitrary keyword Arguments'''
person = {}
def build_profile(first, last, **user_info):
    person["first_name"] = first
    person["last_name"] = last
    print(user_info.items())
    print(*user_info.items())

    for key, value in user_info.items():
        person[key] = value
    return person

user_profile = build_profile("amith", "kn", location = "somewhere", quote = "liveNow")
print(user_profile)