import json



tasks_file = "Tasks.json"
try: 
    with open(tasks_file, "r") as f:
        tasks = json.load(f)
except:
    with open(tasks_file, "w") as f:
        task = []
        json.dump(task, f)

def load_tasks():
    with open(tasks_file, "r") as f:
        tasks = json.load(f)
    
    return tasks

def view_tasks():
    tasks = load_tasks()
    print("Tasks in the list are:\n", 50 * '-')
    for i in range(len(tasks)):
        task = tasks[i]
        print(f"{i+1}.","Task: ", task["Task"] , "| Status:", task["Status"], "|")
    print(50 * '-')
def add_task():
    Task_name = input("Enter the Task: ")
    tasks = load_tasks()
    new_task = {"Task": Task_name, "Status": "Pending"}
    tasks.append(new_task)
    with open(tasks_file , "w" ) as file:
        json.dump(tasks, file, indent=4)
    print("Task Added Successfully!")
    view_tasks()

def mark_done():
    view_tasks()
    tasks = load_tasks()
    while True:
        try:
            task_index = int(input("Enter the Task Number to be marked as Done: "))
            if task_index == 0:
                break
            elif 1 <= task_index <= len(tasks):
                tasks[task_index-1]["Status"] = "Done"
                with open(tasks_file, 'w') as file:
                    json.dump(tasks, file, indent=4)
                    print("Task Marked as Done!")
                    break
        except Exception as e:
            print(e)
        
def delete_task():
    tasks = load_tasks()
    view_tasks()
    while True:
        print("Enter 0 to Exit.")
        try: 
            task_index = int(input("Enter the Task Number to be Deleted: "))
            if task_index == 0:
                break
            elif 1 <= task_index <= len(tasks):
                tasks.pop(task_index-1)
                with open(tasks_file, "w") as file:
                    json.dump(tasks, file, indent=4)
                print("Task Deleted Successfully!")
                view_tasks()
                break
        except Exception as e:
            print(e)
def exit_app():
    exit()


def main():

    print("Welcome to CLI TODO LIST\n", 50 * '=')
    view_tasks()
    Option = input(f"Select the Option you want to Perform!\n1. Add Task \n2. View Tasks\n3. Mark as Done\n4. Delete Task\n0. Exit\nSelect your option: ")
    
    if Option == "1":
        print("User Slected Add Task\n", 50 * '=')
        add_task()
    elif Option =="2":
        print("User Selected View Task\n", 50 * '=')
        view_tasks()

    elif Option == "3":
        print("User Selected Mark a task as done\n", 50 * '=')
        mark_done()
    elif Option == "4": 
        print("User Selected Delete Task\n", 50 * '=')
        delete_task()
    elif Option == "0":
        print("User Selected Exit\n", 50 * '=')
        exit_app()
    else:
        print(f"Option: {Option} is Invalid. Select a vailed Option\n", 50 * '=')

while True:
    main()



