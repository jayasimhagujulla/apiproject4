import json
def is_json(data):
    try:
        real_data=json.load(data)
        valid=True
    except ValueError:
        valid=False
    return valid