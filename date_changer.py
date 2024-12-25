# Исходные переменные
created_date = "10-11-2024"  # Дата создания заметки
issue_date = "10-12-2024"    # Дата истечения заметки

# Функция для изменения формата даты
def change_date_format(date_str):
    # Разделяем дату по разделителю
    if '-' in date_str:
        day, month, year = date_str.split('-')
    elif '.' in date_str:
        day, month, year = date_str.split('.')
    elif ':' in date_str:
        day, month, year = date_str.split(':')
    else:
        return date_str  # Если формат не распознан, возвращаем исходную строку

    # Возвращаем дату без года
    return f"{day}-{month}"  # Можно изменить формат на любой другой, например f"{day}.{month}"

# Изменяем формат дат
temp_created_date = change_date_format(created_date)
temp_issue_date = change_date_format(issue_date)

# Выводим изменённые даты
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)