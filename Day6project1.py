# Create empty lists for tasks
checklist = []
completed_tasks = []
incomplete_tasks = []

# Step 1: Create the checklist
num_tasks = int(input("How many tasks do you want to add today? "))

for i in range(num_tasks):
    task = input(f"Enter task {i+1}: ")
    checklist.append(task)

print("\nYour checklist for today:")
for i, task in enumerate(checklist, start=1):
    print(f"{i}. {task}")

# Step 2: Review tasks at the end of the day
print("\nMark tasks as completed or incomplete:")
for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ").strip().lower()
    
    if status == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Step 3: Display results
print("\n✅ Completed Tasks:")
for task in completed_tasks:
    print(f"- {task}")

print("\n❌ Incomplete Tasks:")
for task in incomplete_tasks:
    print(f"- {task}")

print("\nTask review completed! You can try again tomorrow. 😊")


