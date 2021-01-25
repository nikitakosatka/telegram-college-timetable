import openpyxl
from datetime import datetime


class Week:
    def __init__(self):
        self.week_is_odd = False

    def is_odd(self):
        if datetime.today().isocalendar()[1] + 1 % 2 == 0:
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
    text = f'{surname}: {consultations[surname][0]}' + "Консультация на этой неделе:\n"
    if week.is_odd():
        text += consultations[surname][1][0] + consultations[surname][2][0]
    else:
        text += consultations[surname][2][0] + consultations[surname][2][1]

    return text
