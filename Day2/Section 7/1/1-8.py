from memory_profiler import profile

@profile
def my_function():
    my_list = [x*x for x in range(1000000)]
    return my_list

if __name__ == "__main__":
    my_function()
