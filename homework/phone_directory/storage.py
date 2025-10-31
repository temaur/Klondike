import json
import os

def load_storage():
    try:
        with open('storage.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        base_data = {"name": "number"}
        save_storage(base_data)
        return base_data

def save_storage(data):
    with open('storage.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_to_storage(name, number):
    data = load_storage()
    data[name] = number
    save_storage(data)
    return f"Contact {name} added"

def get_storage():
    return load_storage()

def get_contact(name):
    data = load_storage()
    return data.get(name, "Контакт не найден")

def find_contact(number: str):
    data = load_storage()
    list_of_matching_values = []
    for x in data.values():
        if number in x:
            list_of_matching_values.append(x)
    final_dict = {(k, v) for k, v in data.items() if v in list_of_matching_values}
    return dict(final_dict)

def remove_contact(name):
    data = load_storage()
    if name not in data:
        raise KeyError(f"Contact {name} is not in directory")
    else:
        del data[name]
    save_storage(data)
    return f"Contact {name} deleted"