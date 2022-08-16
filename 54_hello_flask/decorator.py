
# import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(function):
#     def wrapper_fuction():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#     return wrapper_fuction

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
        
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i


# fast_function()
# slow_function()


def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)