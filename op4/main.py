
from score import deadline_score
from late_list import late_list

while True:
    date_of_pass = input('Введите дату сдачи')
    deadline = input("введите дату окончания ")
    grade = {'sasha': '21-12-2012', 'Egor': '11-12-2012', 'Daniil': '13-11-2012', 'Nikita': '10-12-2012',
             'Pavel': '09-12-2012', 'Valeriya': '15-12-2012', '1': '11-11-2011'}
    menu = input('1 - список просрочивших\n 2-оценка')
    if menu == '1':
        print(late_list(grade, deadline))
    if menu == '2':
        print(deadline_score(date_of_pass, deadline))
    else:
        break
