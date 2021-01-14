import openpyxl

wb = openpyxl.load_workbook(filename='consultations.xlsx')
sheet = wb['19-20 I']

consultations = {}
cols = ['ABCD', 'FGHI', 'KLMN', 'PQRS', 'UVWX', ['Z', 'AA', 'AB', 'AC']]

for col in range(6):
    for row in range(7, 27):
        consultations[str(sheet[f'{cols[col][0]}{row}'].value).split()[0]] = [
            '🚪' + ' '.join(str(sheet[f'{cols[col][1]}{row}'].value).split()) + '\n',
            '📅' + ' '.join(str(sheet[f'{cols[col][2]}{row}'].value).split()) + '\n',
            '🕒' + ' '.join(str(sheet[f'{cols[col][3]}{row}'].value).split())]


def get_consultation_info(surname):
    text = f'{surname}: {" ".join(consultations[surname])}'

    return text
