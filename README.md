<h1>factory_database</h1>
<p>
Текст программы к курсовой работе по дисциплине:<br>
<b>Алгоритмические языки и программирование</b>
</p>

<h3>Тема работы</h3>Словари
<h3>Задание</h3>
При выполнении задания использовать процедурно-модульный вид, нисходящее проектирование алгоритмов, схемы алгоритмов. 

[Необходимо программно заполнить словарь информацией (чтобы меньше вводить данных при тестировании)](src/data/database.py), 

[предусмотреть систему меню с пунктами](src/main/console_menu.py):

- просмотр всех записей в базе данных;
- добавление N записей;
- удаление записи по ключу;
- поиск необходимой информации;
- завершение работы с базой данных.

<h3>Вариант</h3>
Вариант 23.
В базе данных содержатся сведения о некотором
числе сотрудников: 
- должность, 
- квалификация, 
- должностной оклад за месяц работы, 
- возможность подработки и оплата за подработку (0,5 ставки). 

Некоторый сотрудник решил сделать покупку. Через сколько
месяцев сотрудник сделает покупку, если в месяц он сможет
откладывать 60% своего заработка и 100% подработки.
Вариант 24. 
В варианте 23 среди сотрудников числится муж и
жена. Задание то же самое.

<h2>Установка приложения</h2>

Для запуска приложения необходимо выполнить следующие действия:
```bash
python3 -m venv venv
pip install -r requirements.txt
```

<h3>Использование виртуального окружения</h3>
macOS/Linux
```bash
source venv/bin/activate
```

Windows
```powershell
venv\Scripts\activate
```

<h3>[Запуск приложения](main.py)</h3>

```bash
python3 main.py
```