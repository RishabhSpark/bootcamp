def immutable_tuple_demo() -> None:
    my_tuple = (7, 8, 9)
    
    # Attempting to change an element of the tuple (this will raise an error)
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    immutable_tuple_demo()