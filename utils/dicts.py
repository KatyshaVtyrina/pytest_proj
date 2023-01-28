def get_val(collection, key, default='git'):
    if len(collection) == 0:
        return default
    elif key in collection:
        return collection[key]
    else:
        return default
