#Program that looks for all the words in a text that end with "illo" or "illa" and print them.
import re
dialoguesNedFlanders = "¡Hola vecinillo! ¡Mi amiguillo, estoy de acuerdillo! ¡Hijo de perrilla! Me encantan las películas de Woody Allen, menos por ese odioso personajillo que sale en todas ellas. Hey Homero, te veo la pilililla! ¡Perfectirijillo! Mi amigo estoy sumamente de acuerdirijillo"
nedFlanders = re.compile(r"\w{1,15}ill[o,a]")
mo =nedFlanders.findall(dialoguesNedFlanders)
for illo_or_illa in mo:
    print(illo_or_illa)
