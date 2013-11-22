from datetime import datetime
from calendar import monthrange

def parse_timestamp(dt_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    m = (dt.year-2001)*12 + (dt.month-1)
    delta = dt - datetime(dt.year,dt.month,1)
    d = delta.days + (delta.seconds + delta.microseconds/1000000.0)/(3600.0*24.0)
    d /= float(monthrange(dt.year,dt.month)[1])
    return m + d
