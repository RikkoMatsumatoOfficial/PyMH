import PyMH.minhookfunc as mhfunc
import os
import ctypes
from time import sleep
from platform import architecture
def Main():
    bits, linkage = architecture()
    print("You're CPU bits: {}".format(bits))
    if(mhfunc.Hooks.MH_Initialize() == mhfunc.MH_Enum.MH_OK):
        print("MinHook Is Successfully Initializated!!!")
        sleep(43)
    else:
        print("Failed to Initialize MinHook!!!")
        sleep(4)
        os._exit(45)
    mhfunc.MH_Unitialize()
    sleep(3)
    os._exit(43)

if __name__ == "__main__":
    Main()