# VVPD5
<h1> НАЧАЛО РАБОТЫ <h1>

<h3> Примеры кода <h3>
  
  <h3> функция 1 <h3>
  def deadline_score(pass_date: str, deadline_date: str):
    """

    функция, ставящая оценку ученику
    :param pass_date: список сроков сдавших
    :param deadline_date: дедлайн
    :return: оценка
    """

    a = 5
    x = []
    if re.fullmatch(r'\d\d-\d\d-2\d\d\d', pass_date) and re.fullmatch(r'\d\d-\d\d-2\d\d\d', deadline_date):
        if int(pass_date[0:2]) <= (int(deadline_date[0:2])):
            print((int(deadline_date[0:2])))
            return a
        elif int(pass_date[0:2]) > int(deadline_date[0:2]) + 21 or int(pass_date[4:5]) > int(deadline_date[4:5]):
            print(int(deadline_date[0:2]) + 7)
            return a - 4
        elif int(pass_date[0:2]) > int(deadline_date[0:2]) + 14 or int(pass_date[4:5]) > int(deadline_date[4:5]):
            print(int(deadline_date[0:2]))
            return a - 3
        elif int(pass_date[0:2]) > int(deadline_date[0:2]) + 7 or int(pass_date[4:5]) > int(deadline_date[4:5]):
            print(int(deadline_date[0:2]))
            return a - 2
        else:
            print(deadline_date[0:2])
            return a - 1
  
  <h3> функция 2<h3>
    
  def late_list(grades: dict, deadline_date: str) -> list[str]:
    """
    стиль rest
    Фуннкция, возращающая список сдавших вовремя
    :param grades: словарь всех студентов
    :param deadline_date: дедлайн
    :return: список сдавших
    """
    g = []
    for k, v in grades.items():
        if re.fullmatch('\d\d-\d\d-2\d\d\d', v) and re.fullmatch('\d\d-\d\d-2\d\d\d', deadline_date):
            if int(v[1:2]) >= int(deadline_date[1:2]) or int(v[3:4]) > int(deadline_date[3:4]):
                g.append(k)
        else:
            print('введена неверная дата')
    return g
    
    
    
    
