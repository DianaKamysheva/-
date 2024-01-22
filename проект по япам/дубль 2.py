class RecruitingAgency:
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def remove_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)

    def show_all_vacancies(self):
        for vacancy in self.vacancies:
            print(vacancy)

    def sort_by_education_and_position(self):
        sorted_vacancies = sorted(self.vacancies, key=lambda x: (x['образование'], x['должность']))
        for vacancy in sorted_vacancies:
            print(vacancy)

    def sort_by_probation_period(self, min_probation_period):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if
                              vacancy['испытательный срок'] >= min_probation_period]
        sorted_vacancies = sorted(filtered_vacancies, key=lambda x: (
        x['испытательный срок'], x['необходимый стаж работы'], -x['максимальный возраст']))
        for vacancy in sorted_vacancies:
            print(vacancy)

    def sort_by_salary_range(self, min_salary, max_salary):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if
                              min_salary <= vacancy['минимальный оклад'] <= max_salary]
        sorted_vacancies = sorted(filtered_vacancies, key=lambda x: (x['наличие соцпакета'], -x['испытательный срок']))
        for vacancy in sorted_vacancies:
            print(vacancy)


# Пример использования
agency = RecruitingAgency()
agency.add_vacancy(
    {'должность': 'Developer', 'образование': 'Высшее', 'испытательный срок': 3, 'необходимый стаж работы': 2,
     'минимальный оклад': 100000, 'наличие соцпакета': True})
agency.add_vacancy(
    {'должность': 'Manager', 'образование': 'Среднее', 'испытательный срок': 2, 'необходимый стаж работы': 3,
     'максимальный возраст': 40, 'минимальный оклад': 80000, 'наличие соцпакета': False})

# Ваша программа должна предусматривать интерфейс для ввода и выбора действий пользователем

# Пример добавления новой записи
new_vacancy = {'должность': 'Designer', 'образование': 'Высшее', 'испытательный срок': 6, 'необходимый стаж работы': 4,
               'минимальный оклад': 120000, 'наличие соцпакета': True}
agency.add_vacancy(new_vacancy)

# Пример удаления записи
agency.remove_vacancy(new_vacancy)

# Вывести полный список вакансий
agency.show_all_vacancies()

# Сортировка по образованию и должности
agency.sort_by_education_and_position()

# Сортировка по испытательному сроку
agency.sort_by_probation_period(2)

# Сортировка по диапазону оклада
agency.sort_by_salary_range(80000, 120000)
