from django.shortcuts import render
from booking.forms import BookingFilterForm
from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    form = BookingFilterForm(request.GET)
    if form.is_valid():
        url = reverse('booking_filter')
        return HttpResponseRedirect(
            f'{url}?date_in={form.cleaned_data["date_in"]}&date_out={form.cleaned_data["date_out"]}&count_adult={form.cleaned_data["count_adult"]}')

    return render(request,
                  'hotel/main_page.html',
                  {'sent': request.GET.get('sent'),  # из room_detail
                   'form': form, }
                  )
