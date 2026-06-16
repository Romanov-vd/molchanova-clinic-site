from django.shortcuts import render

def index(request):
    features = [
        "Современное оборудование экспертного класса",
        "Врачи высшей категории с опытом от 10 лет",
        "Уютная атмосфера без очередей",
        "Индивидуальный план лечения",
        "Доступные цены и гибкая система скидок",
    ]
    schedule = [
        {"doctor": "Иванова М.С.", "specialty": "Терапевт", "mon": "9:00-18:00", "tue": "9:00-18:00", "wed": "9:00-18:00", "thu": "9:00-18:00", "fri": "9:00-16:00"},
        {"doctor": "Петров А.В.", "specialty": "Хирург", "mon": "10:00-17:00", "tue": "Выходной", "wed": "10:00-17:00", "thu": "10:00-17:00", "fri": "10:00-15:00"},
        {"doctor": "Смирнова Е.К.", "specialty": "Педиатр", "mon": "8:00-16:00", "tue": "8:00-16:00", "wed": "8:00-16:00", "thu": "Выходной", "fri": "8:00-14:00"},
        {"doctor": "Козлов Д.Н.", "specialty": "Кардиолог", "mon": "Выходной", "tue": "11:00-19:00", "wed": "11:00-19:00", "thu": "11:00-19:00", "fri": "11:00-17:00"},
    ]
    return render(request, 'index.html', {
        'features': features,
        'schedule': schedule,
        'active_page': 'index',
    })


def services(request):
    services_list = [
        {"name": "Приём терапевта", "price": "1 500 ₽", "duration": "40 мин"},
        {"name": "Приём педиатра", "price": "1 500 ₽", "duration": "40 мин"},
        {"name": "УЗИ-диагностика", "price": "от 2 000 ₽", "duration": "30 мин"},
        {"name": "ЭКГ", "price": "1 000 ₽", "duration": "20 мин"},
        {"name": "Анализы крови", "price": "от 500 ₽", "duration": "по готовности"},
        {"name": "Массаж лечебный", "price": "1 200 ₽ / сеанс", "duration": "60 мин"},
        {"name": "Консультация хирурга", "price": "2 000 ₽", "duration": "30 мин"},
        {"name": "Вакцинация", "price": "от 1 500 ₽", "duration": "30 мин"},
    ]
    return render(request, 'services.html', {
        'services_list': services_list,
        'active_page': 'services',
    })


def contacts(request):
    return render(request, 'contacts.html', {
        'active_page': 'contacts',
    })