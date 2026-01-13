import json

FILE = "lists.json"

def load_all():
    with open(FILE, "r") as f:
        return json.load(f)["lists"]

def save(lists):
    with open(FILE, "w") as f:
        json.dump({"lists": lists}, f, indent=2)

def load_category(category):
    lists = load_all()
    return lists.get(category, [])

def add_to_category(category, item):
    lists = load_all()

    if category not in lists:
        lists[category] = []

    lists[category].append(item)
    save(lists)

def add_category(category):
    lists = load_all()

    if category not in lists:
        lists[category] = []
        save(lists)
