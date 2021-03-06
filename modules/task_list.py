from webbrowser import get



## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    lengthy_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            lengthy_tasks.append(task)
    return lengthy_tasks


## Find a task with a given description
def get_task_with_description(list, description):    
    for task in list:
        if task["description"] == description:
            return task
    return None


# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    tasks_by_status = []
    for task in list:
        if task["completed"] == status:
            tasks_by_status.append(task)
    return tasks_by_status

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken
    return task

def add_to_list(list, task):
    list.append(task)

def import_task_list(list):
    import_tasks = input("Would you like to load your saved task list? (y)es, (n)o, or (q)uit?")
    if import_tasks.lower() == "y":
        pass
    elif import_tasks.lower() == "n":
        clear_task_list(list)
    elif import_tasks.lower() == "q":
        quit()
    else:
        print("Your input wasn't recognised, please try again.")
        import_task_list(list)


def clear_task_list(list):
    list.clear()