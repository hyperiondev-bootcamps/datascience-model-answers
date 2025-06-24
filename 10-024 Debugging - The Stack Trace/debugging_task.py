# Function to print dictionary values given a list of keys
def print_values_of(dictionary, keys):
    """
    Prints the values from the given dictionary for the provided list of keys.

    Args:
        dictionary (dict): The dictionary from which values will be printed.
        keys (list): A list of keys whose values will be printed from the dictionary.
    """
    for key in keys:
        print(dictionary[key])  # Use key instead of k


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",  # Corrected quotation mark
                         "maggie": "(Pacifier Suck)"
                         }

# Passed list of keys as argument
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  # Names in a list