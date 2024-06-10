def format_full_name(func):
    def wrapper(*args, **kwargs):
        title, first_name, last_name, nim = func(*args, **kwargs)
        full_name = f"{title}. {first_name} {last_name} {nim}"
        return f"Full name: {full_name}"
    return wrapper

@format_full_name
def get_name_details():
    title = "Mr"
    first_name = "Reza"
    last_name = "Santoso"
    nim = "064002100005"
    return title, first_name, last_name, nim

if __name__ == "__main__":
    print(get_name_details())
