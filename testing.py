import json



tasks_file = "Tasks.json"
with open(tasks_file, "r") as f:
        tasks = json.load(f)
        print(tasks[5])