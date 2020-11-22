import os 
# os.environ['CUDA_VISIBLE_DEVICES']='-1'

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROC = 0.3
STEP = 1024
CHANNELS_NUM = 14
BATCH_SIZE=32
EPOCHS=25
VALIDATION_SPLIT=0.2
VERBOSE=1
APLHABET = r"0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklmnbvcxz+/="
APLHABET_LEN = len(APLHABET)
MODUL = 1/(APLHABET_LEN - 1)
KEY_l = []


KEY = """MIIEpgIBAAKCAQEA2sLLuqz6e9vsTs++QHs528bgG4meV68mQx0vSacz7v2kwUm5
1Y2HP1JaIAXQKxmV0b07SyyKh9GX2dL65W/HU5bm8InwNX9G19wz9ArHhkvhs1jv
EWszbNX5M+4coD4wavH3+zJhj4hEZYxVlUSSYYZr/V28WRAOjd1UXLABbqoBgVx1
btnpb2Lw5lSr1tN11NW+Na0st57ZD9x56woRRbx0ihA7eQ6M07JnLBa1i8UWJSYm
aU23+D4dJI/gHbhmcmlLUdJW3Bu9yJ9gRUYC/ryljfOxLIUDe5EK+nYbQjJM0LrG
P89XrfOQ5PNWeRgsF5mhaPmQnivvPSf+6IsMJQIDAQABAoIBAQCDUb4UgHQY2AsB
wGlXseEokjjDrxfzUPvp++IAF7PwOiilswkwLbZLh7b8VCEDTmeGMU8fsEw0fdfm
9WSRSEliX0qgiF0+7/lp6RDy5Wmir3h8Pd29GhoTslrXFo/ujYZpHHmdPEAedlGA
l/5kDXbFvnii7pr6582k0YEr5qflcmI23BH/vxdN91PCGF+GDdFnan8T84Jweafa
8yB3/p1tMB/gjWDJXRi0W6hseZxNjuvKT6rHccdsdHKDbk6hF0QNDgTpg7mkHerr
2UHyaJbZY8U1z31UKn0GOunWCxWzLicYSl/uNEhnWgMymclSQ/s9cSXoQJsPurGE
4cOuT3jdAoGBAO47hUfxEp+PnUj8eZcB7gkLJLInWjmRMeP707sp2BtKXkYysJzf
yOCjpym8BvnPAtvocK2IjKrwC4HIMbYX9hWXP7t3TUPFVTgtQsZUj7IXxJEMWjnH
ZEA8KhvVc09X4PYJzjlSr/Drh68zgWueKriuJDI1v6uS++LeLHcqm5p7AoGBAOsT
gw9Z5AEphvRK1p0H+2c/qvqqcOthbq36AWVRnz8kygfxwwclKjLgm6s5+SyfjYr6
H8lMvns+OKpQrpsYeyBHGNAGMSnC14ZlUXZaw1x936eXYzcD1VsfBctNnCJPTCn4
2CEjGuT7a/0Y9jPxnBTYsmeVhUqqILc6HGGnnwHfAoGBAJZGPWCQFOtJsDFl8Vzr
/rb9rHwkjqlZiVsCcyDQ2Fz+oFEvkHCkSRZKpRuSW+QgTPFiwhD03abGHLwVCCaR
Hs2nxq/+JWLmi0cQZdqtZKc2juvgGtnviLFsQjOkhUQ7btBEhy1pl0oliEVf+/di
ohg04Og7N1iHMxR8iRfybI0ZAoGBAJBkQMlqHom0N0fQvDhiUcLesagcjxWVmEVW
3gqc8yL29v2gO3olEuGDYzrudiY5rthhwKqF8C6FTosW2dk8VUzDPvNwCjyriHTt
wPbg00T5sCoh6/g764535Lg26KOOb6sMRb088eUapf8lmPzY+FU5sYO8rM3q6AOD
tzEoo5ujAoGBANXLNhySc3F3iF1UrWbM90Cwx9MQ0/Bk6iRpW3w57SdBrNlPBPnE
17DV01lP6PMdaLcsG7xI7HaQkZc0A1Uyed39nSP7GzMVCJDCu9LJziwLFb1UeUeG
gCyelKJn2i4F4fovTTUaxnbTJ4JwLKsMrxkLw9rASBU+XioiTegu9oMu"""

def get_key_l():
    global KEY
    KEY = KEY.replace('\n', '')[:256]
    for k in KEY:
        i = APLHABET.find(k)
        if i != -1:
            KEY_l.append(i*MODUL)

def get_key_from_list(l):
    key_str = ''
    for c in l:
        m = c % MODUL
        key_code = (c - m)/MODUL
        if m >= MODUL / 2:
            key_code += 1
        key_str += APLHABET[int(key_code)]
    return key_str

get_key_l()