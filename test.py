import settings
import random

new_l = list(map(lambda c: c + random.random()*settings.MODUL - settings.MODUL/2 ,settings.KEY_l))
key = settings.get_key_from_list(new_l)
print(key == settings.KEY.replace('\n', ''))