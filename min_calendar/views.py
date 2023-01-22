from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta


def calculate_date(request, add_or_sub=1):
    delta = request.query_params
    months = int(delta.get('month', 0))
    weeks = int(delta.get('week', 0))
    days = int(delta.get('days', 0))
    hr = int(delta.get('hour', 0))
    minute = int(delta.get('min', 0))
    curr_dt = delta.get('date', None)

    date_to_use = datetime.datetime.today()
    if curr_dt:
        try:
            date_to_use = pd.to_datetime(curr_dt)
        except Exception as e:
            print("date format wrong", e)

    new_dt = date_to_use + \
             datetime.timedelta(minutes=minute, hours=hr, days=days, weeks=weeks) * add_or_sub \
             + relativedelta(months=months) * add_or_sub
    if 'hour' in delta or 'min' in delta:
        return Response(str(new_dt))
    return Response(str(new_dt.date()))


class sub_from_date(APIView):
    def get(self, request):
        return calculate_date(request, add_or_sub=-1)


class add_into_date(APIView):
    def get(self, request):
        return calculate_date(request, add_or_sub=1)
