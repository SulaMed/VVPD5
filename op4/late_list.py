import re


def late_list(grades: dict, deadline_date: str) -> list[str]:
    g = []
    for k, v in grades.items():
        if re.fullmatch('\d\d-\d\d-2\d\d\d', v) and re.fullmatch('\d\d-\d\d-2\d\d\d', deadline_date):
            if int(v[1:2]) >= int(deadline_date[1:2]) or int(v[3:4]) > int(deadline_date[3:4]):
                g.append(k)
        else:
            print('введена неверная дата')
    return g
