import re


def deadline_score(pass_date: str, deadline_date: str):
    a = 5
    x = []
    if re.fullmatch(r'\d\d-\d\d-2\d\d\d', pass_date) and re.fullmatch(r'\d\d-\d\d-2\d\d\d', deadline_date):
        if int(pass_date[0:2]) > (int(deadline_date[0:2])):
            return a - 1
        elif int(pass_date[0:2]) > (int(deadline_date[0:2]) + 7) or int(pass_date[4:5]) > int(deadline_date[4:5]):
            return a - 2
        elif int(pass_date[0:2]) > (int(deadline_date[0:2]) + 14) and int(pass_date[4:5]) > int(deadline_date[4:5]):
            return a - 3
        elif int(pass_date[0:2]) > (int(deadline_date[0:2]) + 21) and int(pass_date[4:5]) > int(deadline_date[4:5]):
            return a - 4
        else:
            return a


print(deadline_score('13-11-2011', '11-11-2011'))
