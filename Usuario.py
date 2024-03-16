
import win32net

usuarios = win32net.NetUserEnum(None, 0)
for usuario in usuarios[0]:
    print(usuario['name'])