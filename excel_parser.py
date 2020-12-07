import openpyxl

wb = openpyxl.load_workbook(filename='timetable.xlsx')
sheet = wb['Лист1']

week_days = ['ABCDE', 'GHIJK', 'MNOPQ', 'ABCDE', 'GHIJK', 'MNOPQ']


def get_day_timetable(day, is_odd):
    if day in range(1, 4):
        if is_odd:
            start_row = 4
        else:
            start_row = 24
    else:
        if is_odd:
            start_row = 13
        else:
            start_row = 33
    text = ''

    for subject in range(4):
        if day == 7:
            return '- / -'
        if sheet[f'{week_days[day - 1][0]}{start_row + subject * 2}'].value:
            text += str(sheet[f'{week_days[day - 1][0]}{start_row + subject * 2}'].value) + ' '
            if sheet[f'{week_days[day - 1][1]}{start_row + subject * 2}'].value:
                text += str(
                    sheet[f'{week_days[day - 1][1]}{start_row + subject * 2}'].value) + ' | ' + str(
                    sheet[f'{week_days[day - 1][1]}{start_row + 1 + subject * 2}'].value)

                if sheet[f'{week_days[day - 1][3]}{start_row + subject * 2}'].value:
                    text += ' / ' + \
                            str(sheet[f'{week_days[day - 1][3]}{start_row + subject * 2}'].value) \
                            + ' | ' + str(
                        sheet[f'{week_days[day - 1][3]}{start_row + 1 + subject * 2}'].value) + '\n'
                else:
                    if sheet[f'{week_days[day - 1][4]}{start_row + 1 + subject * 2}'].value:
                        text += '\n'
                    else:
                        text += ' / - | -\n'
            else:
                text += '- | - / '
                text += str(
                    sheet[f'{week_days[day - 1][3]}{start_row + subject * 2}'].value) + ' | ' + str(
                    sheet[f'{week_days[day - 1][3]}{start_row + 1 + subject * 2}'].value) + '\n'

    return text
