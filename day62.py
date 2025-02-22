
checklist = []
completed_tasks = []
incompleted_tasks = []

L = int(input("Enter the number of tasks for the day: "))

for i in range(L):
    task = input(f"Enter the task {i+1}: ")
    checklist.append(task)

    
    status = input(f"Did you complete '{task}'? (yes/no): ").strip().lower()

    if status == "yes":
        completed_tasks.append(task)
    else:
        incompleted_tasks.append(task)

print("\nChecklist:", checklist)
print("Completed Tasks:", completed_tasks)
print("Incomplete Tasks:", incompleted_tasks)
