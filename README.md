# VVPD5
# НАЧАЛО РАБОТЫ

### Примеры кода
  
### функция 1
```python
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
 ```
 
#### функция 2
    
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
    
### Ссылки на источники
1.The Python standard library [Электронный ресурс]: official Python documentation for 3.8.6 version. – 2020. – Режим доступа: https://docs.python.org/3.8/library/index.html.

2.Модель ветвления Gitflow [Электронный ресурс]: перевод статьи в блоге компании Bitworks Software. – 2019. – Режим доступа: https://bitworks.software/2019-03-12-gitflow-workflow.html.

3.A successful Git branching model [Электронный ресурс]: оригинальная статья-руководство от «автора» Gitflow. – 2010. – Режим доступа: 
https://nvie.com/posts/a-successful-git-branching-model/.

    
    
    
