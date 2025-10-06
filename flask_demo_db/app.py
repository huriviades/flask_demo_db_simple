import random
from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo
from models.models import session, TimeZoneData

app = Flask(__name__)

@app.route('/')
def index():
    utc_now = datetime.now(ZoneInfo('UTC'))
    timezones = [tz[0] for tz in session.query(TimeZoneData.time_zone).distinct().all()]
    random_timezones = random.sample(timezones, min(5, len(timezones)))
    #####
    time_in_zones = {
        zone: utc_now.astimezone(ZoneInfo(zone)).strftime('%Y-%m-%d %H:%M:%S')
        for zone in random_timezones
    }
    ####
    time_info = '<br>'.join(f'{zone}: {time}' for zone, time in time_in_zones.items())
    response = f'Ejemplo de Django con DB!<br>Hora Actual (UTC): {time_info}'
    return response

if __name__ == '__main__':
    app.run()