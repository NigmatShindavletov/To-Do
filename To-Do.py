import os
import customtkinter as ctk
from datetime import datetime

tasks = []

selected_task = None
selected_button = None

def show_stats():
    for widget in stats_frame.winfo_children():
        widget.destroy()
    done = 0

    for task in tasks:
        if task.startswith("[✓]"):
            done += 1
    if len(tasks) == 0:
        percent = 0
    else:
        percent = done / len(tasks) * 100
    stats_frame.columnconfigure(0, weight=1)
    stats_frame.columnconfigure(1, weight=1)
    stats_frame.columnconfigure(2, weight=1)
    stats_frame.columnconfigure(3, weight=1)

    total_text = ctk.CTkLabel(stats_frame, text=f"Всего задач: {len(tasks)}", font=("Arial", 16, "bold"))
    total_text.grid(row=0, column=0, pady=15)

    done_text = ctk.CTkLabel(stats_frame, text=f"✓ Выполнено: {done}", font=("Arial", 16, "bold"))
    done_text.grid(row=0, column=1, pady=15)

    left_text = ctk.CTkLabel(stats_frame, text=f"Осталось: {len(tasks) - done}", font=("Arial", 16, "bold"))
    left_text.grid(row=0, column=2, pady=15)

    percent_text = ctk.CTkLabel(stats_frame, text=f"Прогресс: {percent:.1f}%", font=("Arial", 16, "bold"))
    percent_text.grid(row=0, column=3, pady=15)

    progress = ctk.CTkProgressBar(stats_frame, progress_color="#2ecc71")
    progress.grid(row=1, column=0, columnspan=4, sticky="ew", padx=20, pady=(0, 10))
    progress.set(percent / 100)
    
def edit_window():
    window_edit=ctk.CTkToplevel()
    window_edit.title("Редактировать")
    window_edit.geometry("400x800")
    window_edit.resizable(False, False)
    window_edit.grab_set()

    def edit_task():
        global selected_task
        global selected_button

        if selected_task is not None:
            change_window=ctk.CTkToplevel()
            change_window.title("Введите отредактированную задачу")
            change_window.geometry("400x150")
            change_window.resizable(False, False)
            change_window.grab_set()
            change_entry = ctk.CTkEntry(change_window)
            change_entry.pack(fill="x", padx=20, pady=(0,10))
            old_task = tasks[selected_task].split(" | ", 1)[1]
            change_entry.insert(0, old_task)
            def final_edit_task():
                global selected_task
                global selected_button
                edit_new_task=change_entry.get()
                info, text = tasks[selected_task].split(" | ")
                tasks[selected_task] = info + " | " + edit_new_task
                save_tasks()
                selected_task = None
                selected_button = None
                window_edit.destroy()
                change_window.destroy()
                show_tasks()
                show_stats()
            button_change_edit=ctk.CTkButton(change_window, text="Редактировать", width=200, height=100, command=final_edit_task)
            button_change_edit.pack(anchor="center")
            
    def back_edit_function():
        global selected_task
        global selected_button
        selected_task = None
        selected_button = None
        window_edit.destroy()
    
    edit_frame = ctk.CTkScrollableFrame(window_edit, fg_color="gray20")
    edit_frame.pack(fill="both", expand=True, padx=20, pady=20)
    for number, task in enumerate(tasks):
        task_text = task[4:]
        task_button = ctk.CTkButton(edit_frame, text=task_text)
        task_button.configure(command=lambda number=number, button=task_button: select_task(number, button))
        task_button.pack(fill="x", pady=5)

    buttons_edit_frame = ctk.CTkFrame(window_edit, fg_color="gray25")
    buttons_edit_frame.pack(fill="x", padx=20, pady=(0, 20))
    buttons_edit_frame.columnconfigure(0, weight=1)
    buttons_edit_frame.columnconfigure(1, weight=1)

    edit_button = ctk.CTkButton(buttons_edit_frame, text="Редактировать", command=edit_task)
    edit_button.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

    back_edit_button = ctk.CTkButton(buttons_edit_frame, text="Назад", command=back_edit_function)
    back_edit_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

def delete_all():
    if len(tasks)!=0:
        Warning_window=ctk.CTkToplevel()
        Warning_window.title("⚠ Внимание!")
        Warning_window.geometry("400x150")
        Warning_window.resizable(False, False)
        Warning_window.grab_set()
        def delete_yes():
            tasks.clear()
            save_tasks()
            show_tasks()
            show_stats()
            Warning_window.destroy()
        def delete_no():
            Warning_window.destroy()
        Warning_text=ctk.CTkLabel(Warning_window, text="Вы уверены, что хотите удалить все заметки?")
        Warning_text.pack()
        Warning_frame=ctk.CTkFrame(Warning_window)
        Warning_frame.pack(expand=True)
        Warning_yes=ctk.CTkButton(Warning_frame, text="Да", width=140, height=50, command=delete_yes)
        Warning_yes.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        Warning_no=ctk.CTkButton(Warning_frame, text="Нет", width=140, height=50, command=delete_no)
        Warning_no.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
    else:
        pass

def select_task(number, button):
    global selected_task
    global selected_button

    if selected_button != None:
        selected_button.configure(fg_color=["#3a7ebf", "#1f538d"])

    selected_task = number
    selected_button = button

    button.configure(fg_color="green")

if not os.path.exists("tasks To Do.txt"):
    with open("tasks To Do.txt", "w", encoding="utf-8"):
        pass

with open("tasks To Do.txt", "r", encoding="utf-8") as file:
    tasks = file.read().splitlines()

def save_tasks():
    with open("tasks To Do.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(tasks))

def add_window():
    add = ctk.CTkToplevel()
    add.title("Добавить задачу")
    add.geometry("400x150")
    add.resizable(False, False)
    add.grab_set()
    add_entry = ctk.CTkEntry(add)
    add_entry.pack(fill="x", padx=20, pady=(0,10))
    def add_task():
        time_today = datetime.now().strftime("%d.%m.%Y %H:%M")
        task=add_entry.get()
        tasks.append(f"[ ] {time_today} | {task}")
        save_tasks()
        add.destroy()
        show_tasks()
        show_stats()
    button_add=ctk.CTkButton(add, text="Добавить задачу", width=200, height=100, command=add_task)
    button_add.pack(anchor="center")

def delete_window():
    delete = ctk.CTkToplevel()
    delete.title("Удалить задачу")
    delete.geometry("400x800")
    delete.grab_set()

    def delete_task():
        global selected_task
        global selected_button

        if selected_task is not None:
            tasks.pop(selected_task)
            save_tasks()
            selected_task = None
            selected_button = None
            delete.destroy()
            show_tasks()
            show_stats()

    def back_delete_function():
        global selected_task
        global selected_button
        selected_task = None
        selected_button = None
        delete.destroy()

    delete_frame = ctk.CTkScrollableFrame(delete, fg_color="gray20")
    delete_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    for number, task in enumerate(tasks):
        task_text = task[4:]
        task_button = ctk.CTkButton(delete_frame, text=task_text)
        task_button.configure(command=lambda number=number, button=task_button: select_task(number, button))
        task_button.pack(fill="x", pady=5)

    buttons_frame = ctk.CTkFrame(delete, fg_color="gray25")
    buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)

    delete_button = ctk.CTkButton(buttons_frame, text="Удалить", command=delete_task)
    delete_button.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

    back_delete_button = ctk.CTkButton(buttons_frame, text="Назад", command=back_delete_function)
    back_delete_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("To Do v2.0")
app.state("zoomed")

title = ctk.CTkLabel(app, text="To-Do", font=("Arial", 30, "bold"))
title.pack(pady=20)

tasks_frame=ctk.CTkScrollableFrame(app, fg_color="gray20")
tasks_frame.pack(fill="both", expand=True, padx=20, pady=(10,5))

buttons_frame=ctk.CTkFrame(app, fg_color="gray25")
buttons_frame.pack(fill="x", padx=20, pady=(0,10))

for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)

button_add=ctk.CTkButton(buttons_frame, text="➕ Добавить", height=80, command=add_window)
button_add.grid(row=0, column=0, padx=5, sticky="ew")

button_edit=ctk.CTkButton(buttons_frame, text="📝 Редактировать", height=80, command=edit_window)
button_edit.grid(row=0, column=1, padx=5, sticky="ew")

button_delete=ctk.CTkButton(buttons_frame, text="🗑 Удалить", height=80, command=delete_window)
button_delete.grid(row=0, column=2, padx=5, sticky="ew")

button_clear=ctk.CTkButton(buttons_frame, text="🧹 Очистить", height=80, command=delete_all)
button_clear.grid(row=0, column=3, padx=5, sticky="ew")

stats_frame=ctk.CTkFrame(app, fg_color="gray20")
stats_frame.pack(fill="x", padx=20, pady=(0,20))

def change_task(number):
    if tasks[number].startswith("[✓]"):
        tasks[number] = "[ ]"+tasks[number][3:]
        save_tasks()
        show_stats()
    elif tasks[number].startswith("[ ]"):
        tasks[number] = "[✓]"+tasks[number][3:]
        save_tasks()
        show_stats()

def show_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()
    for number, task in enumerate(tasks):
        task_text = task[4:]
        if task.startswith("[✓]"):
            done = True
        else:
            done = False
        check_var = ctk.BooleanVar(value=done)
        check = ctk.CTkCheckBox(tasks_frame, text=task_text, variable=check_var, command=lambda number=number: change_task(number))
        check.pack(anchor="w", pady=5)

show_tasks()
show_stats()

app.mainloop()
