from datetime import datetime, date

from django.shortcuts import render

from hotel.function import date_uuid
from hotel.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_ADMIN
from rooms.models import Room, Option, RoomOptions, RoomPhoto, RoomNumber
from django.shortcuts import get_object_or_404
from booking.forms import BookingForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from booking.models import Booking

from django.core.mail import send_mail


def rooms_list(request):
    # rooms = Room.objects.prefetch_related('option').prefetch_related('roomphoto')

    # return get_user_model().objects.select_related('profile').prefetch_related('notices').get(pk=user_id)
    # {{ user.profile.avatar }}
    # {{ user.notices.count }}

    rooms = Room.objects.all()
    options = RoomOptions.objects.all().select_related('option')
    photos = RoomPhoto.objects.all()

    return render(request,
                  'rooms/rooms_list.html',
                  {'rooms': rooms,
                   'options': options,
                   'photos': photos,
                   })


# https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django
def send_mail_booking(email_to, date_in, date_out, number_booking,
                      date_booking, count_night, count_guest,
                      fio, phone, comment,
                      type_room, price, ):
    subject = 'Подтверждение бронирования'
    text = f'''Бронь № {number_booking}
            Дата и время бронирования: {date_booking}
            Забронировано на официальном сайте tophotel.ru
            
            Отель TOP HOTEL PERM
            Адрес 614039, Пермский край, Пермь, ул. Швецова, 39
            Телефон +7(342)520-23-18
            Email info@hotel.ru
            
            Детали бронирования 
            Заезд {date_in}
            Выезд {date_out}
            Ночей {count_night}
            Гостей {count_guest}
            
            Данные заказчика
            ФИО {fio}
            Телефон {phone}
            Email {email_to}
            Комментарий {comment}
            
            Стоимость бронирования
            Тип номера {type_room}
            Цена за сутки проживания {price} руб/сутки
            К оплате гостем {price*count_night} руб
            
            ----------------------------------------------            
            Дополнительная информация
            Для заселения в отель требуется паспорт гражданина РФ на каждого проживающего гостя и свидетельство рождения для детей. Обратите внимание, что по заграничному паспорту гражданина РФ заселение в отель невозможно!
        '''
    # email_to = 'hotel.2023@bk.ru'

    try:
        send_mail(subject,
                  text,
                  EMAIL_ADMIN,
                  [email_to],
                  fail_silently=False,
                  )
    except Exception as e:
        print(e.__str__())


# вызов из шаблона booking_filter.html' с параметрами из get-запроса
# страница для бронирования номера
def room_detail(request, room_id, date_in, date_out, count_adult, count_night):
    room = get_object_or_404(Room, id=room_id)
    options = RoomOptions.objects.filter(room=room_id).select_related('option')
    photos = RoomPhoto.objects.filter(room=room_id)

    # найти room_number
    # забронированные номера в даты
    bookings = Booking.objects.filter(
        Q(date_in__range=(date_in, date_out)) |
        Q(date_out__range=(date_in, date_out)) |
        Q(Q(date_in__lte=date_in) &
          Q(date_out__gte=date_out))).values_list('room_number', flat=True)

    # отсечь забронированные номера, оставить только свободные
    if bookings:
        roomnumbers = RoomNumber.objects.all().filter(id__notin=list(bookings))
    else:
        roomnumbers = RoomNumber.objects.all()  # отсечь типы номеров у которых нет комнат

    # учесть вместимость, тип номера -> нашли свободные комнаты и взяли первый свободный номер
    roomnumbers_before = roomnumbers.filter(room__capacity__gte=count_adult).filter(
        room__id=room_id).first()  # capacity, id - поле модели Room

    # print(roomnubers.id, roomnubers.number, roomnubers.room_id)

    # если номера не нашлось то выдать ошибку и направить на страницу с бронированием
    if not roomnumbers_before:
        print("номера закончились")
        url = reverse('booking_filter')
        return HttpResponseRedirect(f'{url}?sent=-1')

    # заполнить форму данными
    number_booking = date_uuid()
    form = BookingForm(request.POST or None,
                       initial={'date_in': date_in,  # значения по умолчанию
                                'date_out': date_out,
                                'count_adult': count_adult,
                                'room': room_id,
                                'room_number': roomnumbers_before.id,
                                'number_booking': number_booking,
                                })

    if request.method == 'POST':
        if form.is_valid():
            try:
                # показать окно загрузки данных

                # проверить свободен ли номер

                # сохранить данные в БД
                form.save()
                print('сохранено')

                # отправить письмо
                ds = Booking.objects.get(number_booking=number_booking).ds
                send_mail_booking(form.cleaned_data['email'],
                                  form.cleaned_data['date_in'],
                                  form.cleaned_data['date_out'],
                                  form.cleaned_data['number_booking'],

                                  f'{ds.date()} {ds.time()}',  # date_booking,
                                  count_night,
                                  count_adult,
                                  f"{form.cleaned_data['surname']} {form.cleaned_data['name']} {form.cleaned_data['patronymic']}",
                                  form.cleaned_data['phone'],
                                  form.cleaned_data['comment'],
                                  room.name,
                                  room.price,

                                  )
                print(f'дата отправик {ds}')
            except Exception as e:
                print('При бронировании произошла ошибка ' + e.__str__())
                url = reverse('booking_filter')
                return HttpResponseRedirect(f'{url}?sent=-1')

            # редирект после брони и сообщить
            url = reverse('home')
            return HttpResponseRedirect(f'{url}?sent=1')

    return render(request,
                  'rooms/room_detail.html',
                  {'room': room,
                   'options': options,
                   'photos': photos,
                   'form': form,
                   'roomnumbers': roomnumbers_before,
                   'date_in': date_in,  # значения по умолчанию
                   'date_out': date_out,
                   'count_adult': count_adult,
                   'night': count_night,
                   # 'type_room': roomnumbers.room.name
                   })
