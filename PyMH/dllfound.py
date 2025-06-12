import ctypes
from platform import architecture
import os
from os import _exit as exitf
def DLLFound_MinhookX64():
    try:
        bits, linkage = architecture()
        if(bits == "64bit"):
            dllpath = os.path.join(os.path.dirname(__file__), 'x64\\MinHook-x64.dll')
            minhookpath = ctypes.cdll.LoadLibrary(dllpath)
            return minhookpath
        else:
            print("64-bit(MinHook) is not Supported or You're CPU is Supported only x32!!!")
            exitf(344)
        if(linkage != "WindowsPE"):
            print("Minhook Only Supports Windows!!!")
            exitf(455)
    except:
        print("Unknown Error has Occured!!!")
        exitf(344)

def DLLFound_MinhookX32():
    try:
        bits, linkage = architecture()
        if(bits == "32bit"):
            dllpath = os.path.join(os.path.dirname(__file__), 'x32\\MinHook-x86.dll')
            minhookpath = ctypes.cdll.LoadLibrary(dllpath)
            return minhookpath
        else:
            print("32-bit(MinHook) is not Supported or You're CPU is Supported only x64!!!")
            exitf(344)
        if(linkage != "WindowsPE"):
            print("Minhook Only Supports Windows!!!")
            exitf(492)
    except:
        print("Unknown Error has Occured!!!")
        exitf(21)
