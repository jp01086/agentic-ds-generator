import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def generate_cpp(data_structure):

    ds = data_structure.lower()

    templates = {
        "priority queue": "templates/priority_queue.cpp",
        "stack": "templates/stack.cpp",
        "queue": "templates/queue.cpp",
        "linked list": "templates/linked_list.cpp",
        "tree": "templates/tree.cpp",
        "hash": "templates/hash_table.cpp"
}
    for key in templates:
        if key in ds or ds in key:
            path = os.path.join(BASE_DIR, templates[key])

            if os.path.exists(path):
                with open(path, "r") as f:
                    return f.read()

    return "// No template found"