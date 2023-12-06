def multilevel_index(documents, keys):
    result_dict = {}

    for document in documents:
        current_dict = result_dict

        for key in keys[:-1]:
            value = document[key]
            current_dict = current_dict.setdefault(value, {})

        last_key = keys[-1]
        last_value = document[last_key]

        if last_value not in current_dict:
            current_dict[last_value] = [document]
        else:
            current_dict[last_value].append(document)

    return result_dict

# Ejemplo de uso
objects = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    },
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    },
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]

result = multilevel_index(objects, ["age", "last_name"])
print(result)
