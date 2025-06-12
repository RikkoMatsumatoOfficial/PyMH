import ctypes
from ctypes import wintypes
GetModuleHandleW = ctypes.windll.kernel32.GetModuleHandleW
GetModuleHandleW.restype = wintypes.LPVOID
GetModuleHandleW.argtypes = (wintypes.LPCWSTR,)

GetProcAddress = ctypes.windll.kernel32.GetProcAddress
GetProcAddress.restype = ctypes.c_void_p
GetProcAddress.argtypes = (wintypes.LPVOID, wintypes.LPCSTR)

def GetModuleHandle(modulename):
    return GetModuleHandleW(modulename)

def GetProcAddr(module, function : str):
    return GetProcAddress(module, function)