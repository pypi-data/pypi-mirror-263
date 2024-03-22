import pytz

utc = pytz.utc

def KittyColor(color, breed):
  return color + " kitty in " + utc.zone
