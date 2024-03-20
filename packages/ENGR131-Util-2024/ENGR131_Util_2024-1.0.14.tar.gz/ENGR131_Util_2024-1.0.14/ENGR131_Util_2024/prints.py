def print_data_saved(obj, responses, keys):
    """prints that the data was saved

    Args:
        obj (obj): object to be printed
        responses (dict): responses provided
        keys (list): key of values to include
    """    
    print("Data Saved.")
    # Print the responses
    for key, value in responses.items():
        # Only print the keys that are in the keys list
        if key in keys:
            print(f"               {key.replace('_', ' ').title()}: {value}")