complexity_db = {
    "stack": {
        "time": "Push: O(1), Pop: O(1), Peek: O(1)",
        "space": "O(n)",
        "reason": "Stacks follow LIFO order which is ideal for undo/redo operations and backtracking problems."
    },
    "queue": {
        "time": "Enqueue: O(1), Dequeue: O(1)",
        "space": "O(n)",
        "reason": "Queues follow FIFO order which is useful when processing tasks in the order they arrive."
    },
    "linked list": {
        "time": "Insert: O(1), Delete: O(1), Search: O(n)",
        "space": "O(n)",
        "reason": "Linked lists allow dynamic memory allocation and efficient insertions/deletions."
    },
    "tree": {
        "time": "Search: O(log n) average (BST), Insert/Delete: O(log n)",
        "space": "O(n)",
        "reason": "Trees are used to represent hierarchical data and enable efficient searching."
    },
    "hash": {
        "time": "Insert: O(1) average, Search: O(1) average",
        "space": "O(n)",
        "reason": "Hash tables provide extremely fast lookup using key-value mapping."
    }
}