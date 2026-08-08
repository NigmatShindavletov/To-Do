# To-Do

🇷🇺 **Русская версия** | 🇬🇧 **English version below**

\---

# 🇷🇺 Русский

## О проекте

**To-Do** — графическое приложение для управления задачами, написанное на Python с использованием библиотеки CustomTkinter.

Проект начинался как простое консольное приложение, созданное для изучения Python, и постепенно развивался с каждой новой версией.

В версии **2.0** приложение получило полноценный графический интерфейс, отдельные окна для управления задачами, статистику и индикатор прогресса.

\---

## Возможности

* ➕ Добавление задач
* 📋 Просмотр списка задач
* 📝 Редактирование задач
* 🗑 Удаление отдельных задач
* 🧹 Удаление всех задач
* ⚠ Подтверждение перед удалением всех задач
* ☑ Отметка задач как выполненных
* 💾 Автоматическое сохранение задач
* 📊 Статистика выполнения
* 📈 Индикатор прогресса
* 🔢 Подсчет общего количества задач
* ✅ Подсчет выполненных задач
* ⏳ Подсчет оставшихся задач
* 📊 Расчет процента выполнения
* 🎯 Выбор задачи перед редактированием или удалением
* 🪟 Отдельные окна для работы с задачами
* 🌙 Темный интерфейс
* 🖥 Полноэкранный режим
* 📐 Адаптивные кнопки интерфейса

\---

## Что нового в версии 2.0

### 🖥 Полностью новый интерфейс

Консольная версия приложения была переработана и получила полноценный графический интерфейс на базе **CustomTkinter**.

Теперь управление задачами осуществляется с помощью кнопок и отдельных окон.

### ➕ Добавление задач

Добавлена отдельная форма для создания новых задач.

При добавлении автоматически сохраняются:

* статус задачи;
* дата;
* время;
* текст задачи.

### 📝 Редактирование задач

Добавлено отдельное окно для выбора задачи перед редактированием.

После выбора задачи открывается форма, в которой можно изменить её текст.

Дата и время создания задачи при этом сохраняются.

### 🗑 Удаление задач

Добавлено отдельное окно со списком задач.

Пользователь может выбрать необходимую задачу и удалить её.

### 🧹 Очистка списка

Добавлена возможность удалить все задачи сразу.

Перед удалением появляется предупреждение с подтверждением действия.

### ☑ Выполнение задач

Задачу можно отметить как выполненную с помощью чекбокса.

После изменения статуса информация автоматически сохраняется.

### 📊 Статистика

В нижней части главного окна отображается статистика:

* общее количество задач;
* количество выполненных задач;
* количество оставшихся задач;
* процент выполнения.

### 📈 Индикатор прогресса

Добавлен визуальный индикатор выполнения.

Он показывает процент выполненных задач и изменяется автоматически при добавлении, удалении или выполнении задач.

### 💾 Сохранение задач

Все задачи автоматически сохраняются в файл:

```text
tasks To Do.txt
```

Если файла нет, приложение автоматически создаёт его при первом запуске.

### 🌙 Интерфейс

В приложении используется тёмная тема.

Основное окно работает в полноэкранном режиме, а кнопки автоматически подстраиваются под размер окна.

\---

## Используемые технологии

* Python 3
* CustomTkinter
* datetime
* os

\---

## Требования

Для запуска исходного кода требуется:

* Python 3.10 или новее
* CustomTkinter

\---

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/NigmatShindavletov/To-Do.git
```

Перейдите в папку проекта:

```bash
cd To-Do
```

Установите необходимые библиотеки:

```bash
pip install -r requirements.txt
```

\---

## Запуск

Запустите исходный код:

```bash
python "To Do v2.0.py"
```

Также можно использовать готовый `.exe` файл из релиза.

\---

## Хранение задач

Задачи сохраняются в файле:

```text
tasks To Do.txt
```

Пример записи:

```text
\\\[ ] 08.08.2026 12:30 | Изучить Python
\\\[✓] 08.08.2026 13:00 | Сделать To-Do v2.0
```

Где:

* `\\\[ ]` — задача не выполнена;
* `\\\[✓]` — задача выполнена;
* дата и время — момент создания задачи;
* после символа `|` находится текст задачи.

\---

## Версия

**2.0**

\---

## История проекта

|Версия|Описание|
|-|-|
|1.1|Улучшение консольной версии|
|1.2|Подготовка исполняемого `.exe` файла|
|2.0|Полный переход на графический интерфейс CustomTkinter|

\---

## Автор

**Нигмат Шиндавлетов**

GitHub: https://github.com/NigmatShindavletov/To-Do

\---

# 🇬🇧 English

## About

**To-Do** is a graphical task management application written in Python using the CustomTkinter library.

The project started as a simple console application created for learning Python and gradually evolved with each new version.

In version **2.0**, the application received a full graphical interface, separate windows for task management, statistics and a progress indicator.

\---

## Features

* ➕ Add tasks
* 📋 View task list
* 📝 Edit tasks
* 🗑 Delete individual tasks
* 🧹 Delete all tasks
* ⚠ Confirmation before deleting all tasks
* ☑ Mark tasks as completed
* 💾 Automatic task saving
* 📊 Task statistics
* 📈 Progress indicator
* 🔢 Total task counter
* ✅ Completed task counter
* ⏳ Remaining task counter
* 📊 Completion percentage
* 🎯 Task selection before editing or deleting
* 🪟 Separate windows for task management
* 🌙 Dark interface
* 🖥 Fullscreen mode
* 📐 Adaptive interface buttons

\---

## What's New in Version 2.0

### 🖥 Completely new interface

The console version was redesigned and received a full graphical interface built with **CustomTkinter**.

Tasks can now be managed using buttons and separate windows.

### ➕ Adding tasks

A separate form was added for creating new tasks.

When a task is added, the following information is automatically saved:

* task status;
* date;
* time;
* task text.

### 📝 Editing tasks

A separate window was added for selecting a task before editing it.

After selecting a task, an editing form appears where the task text can be changed.

The creation date and time remain unchanged.

### 🗑 Deleting tasks

A separate window with the task list was added.

The user can select a task and delete it.

### 🧹 Clearing the task list

The application can delete all tasks at once.

A confirmation window appears before deleting all tasks.

### ☑ Completing tasks

Tasks can be marked as completed using a checkbox.

The new status is automatically saved.

### 📊 Statistics

The bottom section of the main window displays:

* total number of tasks;
* completed tasks;
* remaining tasks;
* completion percentage.

### 📈 Progress indicator

A visual progress bar was added.

It shows the percentage of completed tasks and updates automatically when tasks are added, deleted or completed.

### 💾 Task saving

All tasks are automatically saved to:

```text
tasks To Do.txt
```

If the file does not exist, the application creates it automatically on the first launch.

### 🌙 Interface

The application uses a dark theme.

The main window runs in fullscreen mode, and the buttons automatically adapt to the window size.

\---

## Technologies

* Python 3
* CustomTkinter
* datetime
* os

\---

## Requirements

To run the source code, you need:

* Python 3.10 or newer
* CustomTkinter

\---

## Installation

Clone the repository:

```bash
git clone https://github.com/NigmatShindavletov/To-Do.git
```

Enter the project directory:

```bash
cd To-Do
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

\---

## Run

Run the source code:

```bash
python "To Do v2.0.py"
```

You can also use the ready-to-run `.exe` file from the release.

\---

## Task Storage

Tasks are stored in:

```text
tasks To Do.txt
```

Example:

```text
\\\[ ] 08.08.2026 12:30 | Learn Python
\\\[✓] 08.08.2026 13:00 | Finish To-Do v2.0
```

Where:

* `\\\[ ]` — task is not completed;
* `\\\[✓]` — task is completed;
* date and time — task creation time;
* text after `|` — task description.

\---

## Version

**2.0**

\---

## Project History

|Version|Description|
|-|-|
|1.1|Improvements to the console version|
|1.2|Preparation of the executable `.exe` file|
|2.0|Full transition to the CustomTkinter graphical interface|

\---

## Author

**Nigmat Shindavletov**

GitHub: https://github.com/NigmatShindavletov/To-Do

