import openpyxl
from datetime import datetime, timedelta


class Week:
    def __init__(self):
        self.week_is_odd = False

    def is_odd(self):
        if datetime.today().isocalendar()[1] + 1 % 2 == 1:
            self.week_is_odd = False
        else:
            self.week_is_odd = True

        return self.week_is_odd


wb = openpyxl.load_workbook(filename='consultations.xlsx')
sheet = wb['19-20 I']

consultations = {}
cols = ['ABCD', 'FGHI', 'KLMN', 'PQRS', 'UVWX', ['Z', 'AA', 'AB', 'AC']]

for col in range(6):
    for row in range(7, 27):
        consultations[str(sheet[f'{cols[col][0]}{row}'].value).split()[0]] = [
            '🚪' + ' '.join(str(sheet[f'{cols[col][1]}{row}'].value).split()) + '\n']
        consultations[str(sheet[f'{cols[col][0]}{row}'].value).split()[0]].append(
            ['📅' + ' '.join(str(sheet[f'{cols[col][2]}{row}'].value).split()[:3]) + '\n',
             '📅' + ' '.join(str(sheet[f'{cols[col][2]}{row}'].value).split()[3:]) + '\n'])
        consultations[str(sheet[f'{cols[col][0]}{row}'].value).split()[0]].append([
            '🕒' + ' '.join(str(sheet[f'{cols[col][3]}{row}'].value).split()[:3]),
            '🕒' + ' '.join(str(sheet[f'{cols[col][3]}{row}'].value).split()[3:])])


def get_full_consultation_info(surname):
    text = f'{surname}: {consultations[surname][0] + consultations[surname][1][0][:-1]} {consultations[surname][1][1][1:] + consultations[surname][2][0]} {consultations[surname][2][1][1:]}'

    return text


def get_this_week_consultation_info(surname):
    week = Week()
    weekdays = 'пн вт ср чт пт сб вс'.split()
    text = f'{surname}: {consultations[surname][0]}' + "Ближайшая консультация:\n"
    date = datetime.today().weekday()
    i = 0
    if week.is_odd():
        while (datetime.date(datetime.today()) + timedelta(i)).weekday() != weekdays.index(consultations[surname][1][0].split()[-1][:-1]):
            i += 1
        date = (datetime.date(datetime.today()) + timedelta(i))
        text += consultations[surname][1][0][:-1] + ' ' + date.strftime("%d.%m.%Y") + '\n' + consultations[surname][2][0]
    else:
        while (datetime.date(datetime.today()) + timedelta(i)).weekday() != weekdays.index(
                consultations[surname][1][1].split()[-1][:-1]):
            i += 1
        date = (datetime.date(datetime.today()) + timedelta(i))
        text += consultations[surname][1][1][:-1] + ' ' + date.strftime("%d.%m.%Y") + '\n' + consultations[surname][2][1]

    return text
