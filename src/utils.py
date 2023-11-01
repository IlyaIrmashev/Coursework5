from base.database_creation import create_db_and_tabl
from base.insert_db import insert_data
from base.db_manager import DBManager


def start_of_the_program():
    print("Добро пожаловать в программу по работе с базой данных PostgreSQL\n"
          "Программа позволяет получить сведения о работодателях, а так же, их вакансиях с ресурса HeadHunter.\n"
          "Полученные Вами данные будут сохраняться в базу данных.")

    while True:
        print("Если Вы хотите создать базу данных, введите цифру  1\n"
              "Если Вы хотите завершить работу с программой, введите цифру 2")
        choice = input("Ведите номер выбранного Вами варианта: ")
        if choice == '1':
            return 1
        elif choice == '2':
            break
        else:
            print("Вы сделали не правильный выбор, попробуйте еще раз.\n")


def creating_a_user_database():
    if start_of_the_program() == 1:
        db_input = input("Введите название Вашей базы данных: ").lower()
        create_db_and_tabl(db_input)
        return db_input


def data_entry(db_input):
    print(db_input)
    if db_input:
        insert_data(db_input)
        print(f"Данные о companys, а так же вакансиях компании успешно добавлены")


def user_interaction(db_name):
    print("Получение информацию из базы данных.")
    while True:
        print("Для продолжения работы введите цифру 1.\n"
              "Для выхода из программы введите цифру 2.\n")
        choice = input("Введите цифру: ")
        if choice == '1':
            db_manager = DBManager(db_name)
            job_options = "Для выхода из программы нажмите '1'\n" \
                          "Для получения списка всех компаний и количества вакансий у каждой компании нажмите '2'\n" \
                          "Для получения списка всех вакансий с указанием названия компании," \
                          " названия вакансии и зарплаты и ссылки на вакансию нажмите '3'\n" \
                          "Для получения средней зарплаты по вакансиям нажмите '4'\n" \
                          "Для получения списка всех вакансий," \
                          " у которых зарплата выше средней по всем вакансиям нажмите '5'\n" \
                          "Для получения списка всех вакансий," \
                          " в названии которых содержатся переданные в метод слова, нажмите '6'\n" \
                          "Для возврата в меню, нажмите '0'"
            print(job_options)
            while True:
                user_input = input("Выбор запроса: ")
                if user_input == '1':
                    break
                elif user_input == '2':
                    db_manager.get_companies_and_vacancies_count()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '3':
                    db_manager.get_all_vacancies()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '4':
                    db_manager.get_avg_salary()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '5':
                    db_manager.get_vacancies_with_higher_salary()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '6':
                    user_input = input()
                    db_manager.get_vacancies_with_keyword(user_input)
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '0':
                    print(job_options)
                else:
                    print("Неверное значение! Введите цифру от 1-6!")
        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Вы сделали не правильный выбор. Попробуйте еще раз.\n")


def main():
    db_input = creating_a_user_database()
    data_entry(db_input)
    user_interaction(db_input)
