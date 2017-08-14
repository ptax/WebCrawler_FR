class Executor:

    def __init__(self, task_list):
        self._task_list = task_list

    def run(self):
        while self._task_list.has_tasks():
            task = self._task_list.get_next()
            task.execute()
            task.mark_as_complete()
