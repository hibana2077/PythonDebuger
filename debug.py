import collections
import sys
class debuger:
    def __init__(self) -> None:
        self.watch=list()
    def showver(self):
        print("-----------------")
        print("|  version 0.1  |")
        print("-----------------")
    def showOSversion(self):
        print(sys.version)
    def vla(self,*new):
        for t in list(new):
            self.watch.append(t)
    def svl(self):
        for t in self.watch:
            print(t,type(t))
    def vlsame(self):
        test=[(name,times) for name,times in list(collections.Counter(self.watch).most_common(len(self.watch))) if times >=2]
        print("-----------------")
        print("|  most common  |")
        print("-----------------")
        for t in test:
            print(f"variable value: {t[0]}  variable times: {t[1]}")
    def egg(self):
        ar=[" _______________________ ","< Hello, bovine world!  >"," -----------------------",
        "        \   ^__^","         \  (oo)\_______","            (__)\       )\/\ ",
        "                ||----w |","                ||     ||"]
        for t in ar:print(t)
    def linux(self):
        linux=["< Hello, linux world!  >"," -----------------------","   \ ","    \ ",
        "        .--.","       |o_o |","       |:_/ |","      //   \ \ ","     (|     | )","    /'\_   _/`\ ","    \___)=(___/"]
        for t in linux:print(t)
    def me(self,value):
        return sys.getsizeof(value)
    