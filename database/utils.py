from datetime import datetime

from pyparsing import empty 

def time_stamp():
    return datetime.now().strftime("%H:%M:%S %Y-%m-%d")

def remove_empty_keys(dict_to_change: dict) -> dict:
    empty_keys = []
    for key in dict_to_change:
        if dict_to_change[key] == None:
            empty_keys.append(key)

    for key in empty_keys:
        dict_to_change.pop(key)

    return dict_to_change


def check_if_dict_has_key(dict_to_check: dict, key_to_check: str) -> bool:
    for key in dict_to_check.keys():
        if key == key_to_check:
            return True
    
    return False
