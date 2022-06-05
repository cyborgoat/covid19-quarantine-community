from django import template
import datetime
import pytz

register = template.Library()


@register.filter(name='passed_ddl')
def passed_ddl(time: datetime.datetime):
    return 8 <= time.hour < 12


if __name__ == '__main__':
    tz = pytz.timezone('Asia/Shanghai')
    beijing_now = datetime.datetime.now(tz)
    print(beijing_now.hour)
