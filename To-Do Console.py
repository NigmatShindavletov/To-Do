import os
from datetime import datetime
from colorama import Fore, Style, init
init()
tasks=[]
file=open("tasks To Do.txt", "r", encoding="utf-8")
tasks=file.read().splitlines()
file.close()
    
def clear():
    os.system("cls")
def pause():
    input("Нажмите Enter для продолжения")
def save_tasks():
    file = open("tasks To Do.txt", "w", encoding="utf-8")
    file.write("\n".join(tasks))
    file.close()
def print_tasks(show_back=False, show_delete_all=False):
    if len(tasks) == 0:
        print(Fore.YELLOW + "У вас нет запланированных задач" + Style.RESET_ALL)
        pause()
    else:
        if show_back:
            print(Style.BRIGHT + Fore.CYAN + "0. Назад" + Style.RESET_ALL)

        for number, task in enumerate(tasks, start=1):
            if task.startswith("[✓]"):
                print(Fore.GREEN + f"{number}. {task}" + Style.RESET_ALL)
            else:
                print(Fore.WHITE + f"{number}. {task}" + Style.RESET_ALL)
        if show_delete_all:
            print(Style.BRIGHT + Fore.CYAN + f"{len(tasks)+1}. Удалить все" + Style.RESET_ALL)
while True:
    clear()
    done = 0

    for task in tasks:
        if task.startswith("[✓]"):
            done += 1

    if len(tasks) == 0:
        percent = 0
    else:
        percent = done / len(tasks) * 100
    print(Style.BRIGHT+Fore.CYAN+"========== TO DO =========="+ Style.RESET_ALL)
    
    print(Fore.WHITE + f"Всего задач : {len(tasks)}")
    print(Fore.GREEN + f"Выполнено   : {done}")
    print(Fore.YELLOW + f"Осталось    : {len(tasks) - done}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Процент выполненных задач: {percent:.1f}%" + Style.RESET_ALL)

    print(Style.BRIGHT+Fore.CYAN + "===========================" + Style.RESET_ALL)
    print(Style.BRIGHT+Fore.YELLOW + "1. Показать задачи")
    print(Style.BRIGHT+Fore.YELLOW + "2. Добавить задачу")
    print(Style.BRIGHT+Fore.YELLOW + "3. Удалить задачу")
    print(Style.BRIGHT+Fore.YELLOW + "4. Отметить задачу как выполненную")
    print(Style.BRIGHT+Fore.YELLOW + "5. Редактировать задачу")
    print(Style.BRIGHT+Fore.RED + "6. Выход")
    print(Style.RESET_ALL)
    choice=input("Выберите пункт:")
    if choice=="1":
        print_tasks()
        if len(tasks) != 0:
            pause()
            continue
        if len(tasks) == 0:
            continue
    elif choice=="2":
        task=input(Fore.CYAN+"Введите задачу:"+Style.RESET_ALL)
        time_today=datetime.now().strftime("%d.%m.%Y %H:%M")
        tasks.append(f"[ ] {time_today} | {task}")
        save_tasks()
        print(Style.BRIGHT+Fore.GREEN+"Задача добавлена!"+Style.RESET_ALL)
        pause()
    elif choice=="3":
        print_tasks(True, True)
        if len(tasks) == 0:
            continue
        try:
            delete_task=int(input(Fore.CYAN+"Введите номер задачи которую хотите удалить:"+Style.RESET_ALL))
        except ValueError:
            print(Style.BRIGHT+Fore.RED+"Нужно ввести число!"+Style.RESET_ALL)
            pause()
            continue
        if 1<=delete_task<=len(tasks):
            tasks.pop(delete_task-1)
            save_tasks()
            print(Style.BRIGHT+Fore.GREEN+"Задача удалена!"+Style.RESET_ALL)
            pause()
        elif delete_task==0:
            continue
        elif delete_task==len(tasks)+1:
            print(Fore.RED + "⚠ Вы действительно хотите удалить ВСЕ задачи?")
            print(Fore.YELLOW + "Это действие нельзя отменить.")
            print()
            print("1. Да")
            print("2. Нет")
            try:
                DelItog=input(Fore.WHITE +"Ваш выбор:"+Style.RESET_ALL)
            except:
                print(Style.BRIGHT+Fore.RED+"Неверно введенный ответ!"+Style.RESET_ALL)
                pause()
                continue
            if DelItog == "1":
                tasks.clear()
                save_tasks()
                print(Style.BRIGHT+Fore.GREEN +"Все задачи удалены!"+Style.RESET_ALL)
                pause()
            elif DelItog == "2":
                continue
            else:
                print(Fore.RED + "Неверный выбор!" + Style.RESET_ALL)
                pause()
                continue
        else:
            print(Style.BRIGHT+Fore.RED+"Неверный номер задачи!"+Style.RESET_ALL)
            pause()
    elif choice=="4":
        print_tasks(True)
        if len(tasks) == 0:
            continue
        try:
            note_task=int(input(Fore.CYAN+"Введите номер задачи которую хотите отметить:"+Style.RESET_ALL))
        except ValueError:
            print(Style.BRIGHT+Fore.RED+"Нужно ввести число!"+Style.RESET_ALL)
            pause()
            continue
        if note_task==0:
                continue
        elif 1<=note_task<=len(tasks):
            if tasks[note_task-1].startswith("[✓]"):
                print(Style.BRIGHT+Fore.YELLOW+"Эта задача уже выполнена!"+Style.RESET_ALL)
                pause()
            else:
                tasks[note_task-1]="[✓]"+tasks[note_task-1][3:]
                save_tasks()
                print(Style.BRIGHT+Fore.GREEN+"Задача отмечена как выполненная!"+Style.RESET_ALL)
                pause()
        else:
            print(Style.BRIGHT+Fore.RED+"Неверный номер задачи!"+Style.RESET_ALL)
            pause()
    elif choice=="5":
        print_tasks(True)
        if len(tasks) == 0:
            continue
        try:
            edit_task=int(input(Fore.CYAN+"Введите номер задачи которую хотите отредактировать:"+Style.RESET_ALL))
        except ValueError:
            print(Style.BRIGHT+Fore.RED+"Нужно ввести число!"+Style.RESET_ALL)
            pause()
            continue
        if edit_task==0:
            continue
        elif 1<=edit_task<=len(tasks):
            new_task = input(Fore.CYAN + "Введите новый текст задачи:" + Style.RESET_ALL)
            info, text = tasks[edit_task - 1].split(" | ")
            tasks[edit_task - 1] = info + " | " + new_task
            save_tasks()
            print(Style.BRIGHT + Fore.GREEN + "Задача изменена!" + Style.RESET_ALL)
            pause()
        else:
            print(Style.BRIGHT+Fore.RED+"Неверный номер задачи!"+Style.RESET_ALL)
            pause()
    elif choice=="6":
        print(Fore.CYAN + "До встречи!" + Style.RESET_ALL)
        break
    else:
        print(Style.BRIGHT+Fore.RED+"Такого пункта не существует!"+Style.RESET_ALL)
        pause()
