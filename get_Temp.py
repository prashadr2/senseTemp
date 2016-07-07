from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
pi_name = "AwesomePi"
location = "VSSHS"
now = datetime.now()

def get_sense_temp():
    sense_temp = sense.get_temperature()
    return sense_temp

print str(get_sense_temp()) + "," + '%s/%s/%s' % (now.year,now.month,now.day) + "," + '%s:%s:%s' % (now.hour,now.minute,now.second) + "," + pi_name +  "," + location




    
