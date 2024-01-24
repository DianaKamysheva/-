
class Vacancy:
    def __init__(self, position, experience, gender, education, min_age, max_age, languages, salary, social_package,probation_period):
        self.position = position
        self.experience = experience
        self.gender = gender
        self.education = education
        self.min_age = min_age
        self.max_age = max_age
        self.languages = languages
        self.salary = salary
        self.social_package = social_package
        self.probation_period = probation_period


class RecruitmentAgency:
    def __init__(self):
        self.vacancies = []

    def hoare_sort(arr, left, right, key):
        if left >= right:
            return
        pivot = arr[(left + right) // 2][key]
        i, j = left, right
        while i <= j:
            while arr[i][key] < pivot:
                i += 1
            while arr[j][key] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
        hoare_sort(arr, left, j, key)
        hoare_sort(arr, i, right, key)

    def add_vacancy(self, vacancy):
        position = str(input('\n*****\n'
                         'Вы зашли в функцию создания новой вакансии\n'
                         'Введите "0", чтобы выйти\n'
                         'Либо введите название новой вакансии\nВаш ввод: '))
        if (position == '0'):
            print(f'Возвращаемся в главное меню\n*****\n')
            return
        try:
            experience = int(input(f'\nЗададим опыт работы в годах "{position}"\n'
                                 f'Сколько лет составляет опыт работы? Введите колличество лет в виде натурального числа\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому вакансия "{position}" не добавлена!\nВернемся в главное меню'
                f'\n*****\n')
            return
        try:
            gender = str(input(f'\nВведем необходимый пол сотрудника для вакансии "{position}" '
                                 f'(натуральное число)\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому дисциплина "{position}" не добавлена!\nВозвращаемся в главное меню'
                  f'\n*****\n')
            return
        try:
            education = str(input(f'\nВведите образование требуемое для вакансии "{position}" \nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому дисциплина "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return
        try:
            min_age = int(input(f'\nВведите минимальный возраст требуемый для вакансии "{position}"\n'
                                 f'Введите натуральное число\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому вакансия "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return
        try:
            max_age = int(input(f'\nВведите максимальный возраст требуемый для вакансии"{position}"\n'
                                 f'Введите натуральное число\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому вакансия "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return
        try:
            languages = str(input(f'\nВведем язык требуемый для вакансии "{position}"\n'
                                 f'С какого семестра читается эта дисциплина? Введите натуральное число\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому дисциплина "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return
        try:
            salary = int(input(f'\nВведите минимальный оклад вакансии "{position}" в тысячах рублей\n'
                                 f'Введите натуральное число\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому вакансия "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return
        try:
            social_package = str(input(f'\nВведем данные о соцпакете вакансии "{position}"\n'
                                 f'Присутствует ли в вакансии соцпает? Если да, введите True, если нет, введите False\nВаш ввод: '))
        except:
            print(f'Вы ввели не True или False, поэтому вакансия "{position}" не добавлена!\nВозвращаемся в главное меню')
            return
        try:
            probation_period = int(input(f'\nВведем испытательный срок для вакансии "{position}" в месяцах\n'
                                 f'Сколько длится испытательный срок? Введите натуральное число\nВаш ввод: '))
        except:
            print(f'Вы ввели не натуральное число, поэтому вакансия "{position}" не добавлена!\nВозвращаемся в главное меню'
                f'\n*****\n')
            return


        info_base.append(Vacancy(position, experience, gender, education, min_age, max_age, languages, salary, social_package, probation_period))
        print(f'\nНовая вакансия "{position}" успешно добавлена в базу данных!\n'
              f'Возвращаемся в главное меню\n*****\n')
        self.vacancies.append(vacancy)

    def remove_vacancy(self, position):
        for vacancy in self.vacancies:
            if vacancy.position == position:
                self.vacancies.remove(vacancy)
                break

        ln = len(info_base)
        if ln == 0:
            print('\n*****\n'
                  'Вы зашли в функцию удаления вакансии, на данный момент в базе данных нет ни одной вакансии\n'
                  'Возвращаемся в главное меню\n'
                  '\n*****\n')
            return
        position = str(input('\n*****\n'
                         'Вы зашли в функцию удаления вакансии\n'
                         'Введите название вакансии, которую вы хотите удалить\nВаш ввод: '))
        count = 0
        for i in range(ln):
            if position.lower() == str(info_base[i].position).lower():
                print(f'Вакансия "{info_base[i].position}" успешно удалена из базы данных!')
                info_base.pop(i)
                count += 1
                break
        if count == 0:
            print('Данная ваккансия не была обнаружена в базе данных. Возможно вы ошиблись при вводе её названия')
        print('\nВозвращаемся в главное меню\n*****\n')

    def edit_vacancy(self):
        for i,vacancy in enumerate(self.vacancies):
            print([i + 1].vacancy.position)

        index = int(input("Введите номер вакансии для изменения: "))
        print("Для изменения вам нужно будет полностью переписать данные вместе с изменениями по шаблону.")
        print("Ниже будет приведен шаблон: \n")
        shablon = (
        'Должность: Менеджер по продажам', 'Необходимый стаж(лет работы): 2', 'Пол: Любой', 'Образование: высшее',
        'Минимальный возраст(годы): 21', 'Максимальный возраст(годы): 35', 'Знание иностранных языков: английский',
        'Минимальный оклад(рублей): 30000', 'Наличие соцпакета: True', 'Испытательный срок(месяцев): 3')
        print(shablon)
        vacancies[index - 1] = input("Введите изменения: ")
        print("Вакансия успешно изменена.")

    def create_full_vacancy_list_report(self):
        def hoare_sort(arr, key):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2].__getattribute__(key)
            less, equal, greater = [], [], []
            for vacancy in arr:
                if vacancy.__getattribute__(key) < pivot:
                    less.append(vacancy)
                elif vacancy.__getattribute__(key) == pivot:
                    equal.append(vacancy)
                else:
                    greater.append(vacancy)
            return hoare_sort(less, key) + equal + hoare_sort(greater, key)

        sorted_vacancies = hoare_sort(self.vacancies, 'education')
        sorted_vacancies = hoare_sort(sorted_vacancies, 'position')
        for vacancy in sorted_vacancies:
            print(vacancy.position)



    def create_vacancy_with_probation_report(self, probation):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if vacancy.probation_period >= probation]
        sorted_vacancies = sorted(filtered_vacancies, key=lambda v: (v.probation_period, v.experience, v.max_age))
        for vacancy in sorted_vacancies:
            print(vacancy.position)

    def create_vacancy_with_salary_report(self, min_salary, max_salary):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if min_salary <= vacancy.salary <= max_salary]
        sorted_vacancies = sorted(filtered_vacancies, key=lambda v: (v.social_package, v.probation_period))
        for vacancy in sorted_vacancies:
            print(vacancy.position)


# Создание базы вакансий
recruitment_agency = RecruitmentAgency()
# Добавление записей в базу
# ...

info_base = [
    Vacancy( position :"Менеджер по продажам", experience: 2, gender: 'Любой', education: 'высшее', min_age: 21, max_age: 35, languages: 'английский', salary: 30000, social_package: True, probation_period: 3),
    Vacancy( position: 'HR-менеджер', experience: 3, gender: 'Любой', education: 'высшее', min_age: 23, max_age: 40, languages: 'французский', salary: 40000, social_package: True, probation_period: 6),
    Vacancy( position: 'Программист', experience: 5, gender: 'Мужской', education: 'высшее', min_age: 25, max_age: 45, languages: 'немецкий', salary: 50000, social_package: True, probation_period: 3),
    Vacancy( position: 'Бухгалтер',experience: 4, gender: 'Любой', education: 'Высшее экономическое', min_age: '30 лет',  max_age: 60, languages: 'Английский (средний уровень)', salary: 90000, social_package: True, probation_period: 6),
    Vacancy( position: 'Медицинская сестра', experience: 3, gender: 'Женский',education: 'Среднее медицинское',min_age: 25 ,max_age: 55,languages: 'Не требуется',salary: 60000, social_package: True, probation_period: 3),
    Vacancy( position: 'Адвокат', experience: 5, gender: 'Любой', education: 'Высшее юридическое', min_age: '30 лет', max_age: 65, languages: 'Английский (продвинутый уровень)', salary: 100000, social_package: True, probation_period: 6),
    Vacancy( position: 'Учитель начальных классов',experience: 2, gender: 'Женский', education: 'Высшее педагогическое', min_age: 25, max_age: 55, languages: 'Не требуется', salary: 55000, social_package: True, probation_period: 3),
    Vacancy( position: 'Механик',experience: 3, gender: 'Любой', education: 'Среднее профессиональное', min_age: 24, max_age: 58, languages: 'Не требуется', salary: 60000, social_package: True, probation_period: 4),
    Vacancy( position: 'Швея', experience: 2, gender: 'Женский', education: 'Среднее профессиональное', min_age: 23, max_age: 50, languages: 'Не требуется', salary: 48000, social_package: True, probation_period: 3),
    Vacancy( position: 'Архитектор', experience: 5, gender: 'Любой', education: 'Высшее архитектурное', min_age: 28, max_age: 60, languages: 'Английский (средний уровень)', salary: 90000, social_package: True, probation_period: 5),
    Vacancy( position: 'Менеджер по продажам', experience: 3, gender: 'Любой', education: 'Высшее экономическое или коммерческое', min_age: 25, max_age: 50, languages: 'Английский (разговорный уровень)', salary: 70000, social_package: True, probation_period: 3),
    Vacancy( position: 'Финансовый аналитик', experience: 2, gender: 'Любой', education: 'Высшее экономическое', min_age: 24, max_age: 55, languages: 'Английский (продвинутый уровень)', salary: 80000, social_package: True, probation_period: 4),
    Vacancy( position: 'Инженер-программист', experience: 2, gender: 'Любой', education: 'Высшее техническое', min_age: 23, max_age: 50, languages: 'Английский (продвинутый уровень)', salary: 75000, social_package: True, probation_period: 4),
    Vacancy( position: 'Медсестра', experience: 2, gender: 'Женский', education: 'Среднее медицинское', min_age: 22, max_age: 55, languages: 'Не требуется', salary: 40000, social_package: True, probation_period: 3),
    Vacancy( position: 'Разработчик веб-приложений', experience: 3, gender: 'Любой', education: 'Высшее техническое или информационные технологии', min_age: 24, max_age: 50, languages: 'Английский (продвинутый уровень)', salary: 85000, social_package: True, probation_period: 3),
    Vacancy( position: 'Специалист по маркетингу', experience: 2, gender: 'не имеет значения', education: 'высшее образование в области маркетинга или экономики', min_age: 25, max_age: 'не ограничено', languages: 'английский - свободное владение', salary: 50000, social_package: True, probation_period: 3),
    Vacancy( position: 'Программист', experience: 3, gender: 'не имеет значения', education: 'высшее образование в области информационных технологий или компьютерных наук', min_age: 22, max_age: 'не ограничено', languages: 'английский - технический перевод', salary: 70000, social_package: True, probation_period: 2),
    Vacancy( position: 'Медицинская сестра', experience: 1, gender: 'женский', education: 'медицинское', min_age: 21, max_age: 55, languages: 'не требуется', salary: 40000, social_package: True, probation_period: 3),
    Vacancy( position: 'Адвокат', experience: 5, gender: 'не имеет значения', education: 'высшее юридическое образование' ,min_age: 30, max_age: 60, languages: 'английский - свободное владение', salary: 80000, social_package: True, probation_period: 6),
    Vacancy( position: 'Бухгалтер', experience: 3, gender: 'не имеет значения', education: 'высшее образование в области бухгалтерского учета или экономики', min_age: 23, max_age: 55, languages: 'не требуется', salary: 55000, social_package: True, probation_period: 3),
    Vacancy( position: 'Инженер-конструктор', experience: 2, gender: 'не имеет значения', education: 'высшее техническое образование', min_age: 24, max_age: 65, languages: 'английский - технический перевод', salary: 60000, social_package: True, probation_period: 3),
    Vacancy( position: 'Менеджер по продажам', experience: 2, gender: 'не имеет значения', education: 'высшее образование в области маркетинга или экономики', min_age: 25, max_age: 45, languages: 'английский - свободное владение', salary: 50000, social_package: True, probation_period: 3),
    Vacancy( position: 'Учитель начальных классов', experience: 3, gender: 'не имеет значения', education: 'педагогическое образование', min_age: 30, max_age: 65, languages: 'не требуется', salary: 45000, social_package: True, probation_period: 3),
    Vacancy( position: 'Инфограф', experience: 2, gender: 'не имеет значения', education: 'высшее образование в области дизайна или искусств', min_age: 23, max_age: 55, languages: 'английский - свободное владение', salary: 55000, social_package: True, probation_period: 2),
    Vacancy( position: 'Веб-разработчик', experience: 2, gender: 'не имеет значения', education: 'высшее образование в области информационных технологий или компьютерных наук', min_age: 24, max_age: 50, languages: 'английский - технический перевод', salary: 60000, social_package: True, probation_period: 3)
]

# Пример взаимодействия с базой данных через дружественный интерфейс
while True:
    print("1. Добавить вакансию")
    print("2. Удалить вакансию")
    print("3. Изменить вакансию")
    print("4. Полный список всех вакансий")
    print("5. Список всех вакансий с определенным испытательным сроком")
    print("6. Список всех вакансий с окладом в определенном диапазоне")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        recruitment_agency.add_vacancy(info_base)
    elif choice == "2":
        recruitment_agency.remove_vacancy(info_base)
    # Удаление вакансии
    # ...
    elif choice == "3":
        recruitment_agency.edit_vacancy()
    elif choice == "4":
        recruitment_agency.create_full_vacancy_list_report()
    elif choice == "5":
        probation = int(input("Введите минимальный испытательный срок: "))
        recruitment_agency.create_vacancy_with_probation_report(probation)
    elif choice == "6":
        min_salary = int(input("Введите минимальный оклад: "))
        max_salary = int(input("Введите максимальный оклад: "))
        recruitment_agency.create_vacancy_with_salary_report(min_salary, max_salary)
    elif choice == "7":
        break
    else:
        print("Некорректный ввод")
