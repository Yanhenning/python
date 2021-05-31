def is_isogram(string):
    cleaned_string = [char for char in string.lower() if char.isalpha()]
    return len(cleaned_string) == len(set(cleaned_string))
