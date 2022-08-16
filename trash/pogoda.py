from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
config = cfg.get_default_config()
config['language'] = 'ru'
owm = OWM('1a8ebdc76badeb07c3afe1b7753cbf6c', config)
mgr = owm.weather_manager()
 
city = input("Выберите город"'\n') 
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
wind = w.wind().get("speed",0)
status = w.detailed_status 
print("В вашем городе сейчас: " + str(temperature)+ "°С")
print("Скорость ветра: " + str(wind)+ " М/с")
print("Погода: " + str(status))