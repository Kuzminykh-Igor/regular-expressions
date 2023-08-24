import csv
import re


def normalizes_list_full_names(contact_list):
    '''Помещает ФИО человека в поля lastname, firstname и surname соответственно.'''

    contacts = []
    for data in contact_list:
        split_data = ' '.join(data[:3]).split(' ')
        contacts.append([split_data[0], split_data[1], split_data[2], data[3], data[4], data[5], data[6]])

    return contacts


def normalizes_list_phones():
    '''
    Приводит все телефоны в формат +7(999)999-99-99.
    Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
    '''

    contacts = normalizes_list_full_names(contacts_list)

    for phone in contacts:
            result = re.sub(pattern, new_phone, phone[5])
            phone[5] = result.strip()

    return contacts


def merges_duplicate():
    '''Объединяет дублирующиеся записи.'''

    contacts = normalizes_list_phones()

    merged = {}
    for data in contacts:
        name = f'{data[0]} {data[1]}'
        if name in merged:
            for i, field in enumerate(data):
                if field == '':
                    continue
                merged[name][i] = field
        else:
            merged[name] = data
    filter_contacts = [field for field in merged.values()]

    return  filter_contacts


def writes_data_to_csv_file():
    '''
    Записывает обработанные данные в phonebook.csv
    '''

    contacts_list = merges_duplicate()

    with open("phonebook.csv", "w", newline="", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == "__main__":
    pattern = r'(\+7|8|7)?\s*\(?(\d{3})\)?\s*[-]?(\d{2,5})[-]?(\d{2})[-]?(\d{2})\s*\(?(доб\.?)?\s*(\d{2,5})?\)?'
    new_phone = r'+7(\2)\3-\4-\5 \6\7'

    with open("phonebook_raw.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    writes_data_to_csv_file()