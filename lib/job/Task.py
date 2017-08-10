class Task:
    def __init__(self, options, storage):
        self._options = options
        self._storage = storage

    def mark_as_complete(self):
        self._storage.complete()

    def execute(self):
        pass