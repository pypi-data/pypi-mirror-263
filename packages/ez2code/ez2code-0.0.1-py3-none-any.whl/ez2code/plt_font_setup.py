import matplotlib as pltorig


def apply(MAC_WINDOWS_MYCOM, SIZE):
    fontsetup = {"MAC" : "AppleGothic", "WINDOWS" : "MalgunGothic"}
    pltorig.rcParams['font.family'] = fontsetup[MAC_WINDOWS_MYCOM]
    pltorig.rcParams['font.size'] = SIZE
