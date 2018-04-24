import DatabaseConnection
from datetime import date, datetime, timedelta


TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

#
# for name, table in TABLES.items():
#     try:
#         DatabaseConnection.cursor.execute(table)
#     except DatabaseConnection.Error as err:
#         print('error')
tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%(first_name)s, %(last_name)s, %(hire_date)s, %(gender)s, %(birth_date)s)")

data_employee = {
    'first_name': 'Dawid',
    'last_name': 'Jagla',
    'hire_date': tomorrow,
    'gender': 'M',
    'birth_date': date(1990, 12, 9)
}

DatabaseConnection.cursor.execute(add_employee, data_employee)
DatabaseConnection.connect.commit()

get_employee = ("SELECT first_name,last_name FROM employees")
DatabaseConnection.cursor.execute(get_employee)
d = DatabaseConnection.cursor.fetchall()
print(d)
# for name,surname in DatabaseConnection.cursor:
#     print(name, surname)