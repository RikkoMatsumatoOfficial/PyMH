import ctypes
from enum import Enum
import platform
import os
import sys
import dllfound
from ctypes import wintypes
minhook_x32 = dllfound.DLLFound_MinhookX32()
minhook_x64 = dllfound.DLLFound_MinhookX64()

fp_orginal = None
fp_target = None
def MH_ALL_HOOKS():
    return 0
class MH_Enum(Enum):

    MH_UNKNOWN = -1,

    MH_OK = 0,

    MH_ERROR_ALREADY_INITIALIZED = 1,

    MH_ERROR_NOT_INITIALIZED = 2,

    MH_ERROR_ALREADY_CREATED = 3,

    MH_ERROR_NOT_CREATED = 4,

    MH_ERROR_ENABLED = 5,

    MH_ERROR_DISABLED = 6,

    MH_ERROR_NOT_EXECUTABLE = 7,

    MH_ERROR_UNSUPPORTED_FUNCTION = 8,

    MH_ERROR_MEMORY_ALLOC = 9,

    MH_ERROR_MEMORY_PROTECT = 10,

    MH_ERROR_MODULE_NOT_FOUND = 11,

    MH_ERROR_FUNCTION_NOT_FOUND = 12,

class Hooks:
    modulename : str = None
    funcname : str = None
    def MH_Initialize():
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_Initialize = minhook_x64.MH_Initialize()
            minhook_x64.MH_Initialize.argtypes = MH_Enum 
            return MH_Initialize()
        elif(bits == "32bit"):
            MH_Initialize = minhook_x32.MH_Initialize()
            minhook_x32.MH_Initialize.argtypes = minhook_x32.MH_Initialize()
            return MH_Initialize()
    @property
    def modname():
        return Hooks.modulename
    @property
    def apiname():
        return Hooks.funcname
    def MH_CreateHook(org_func, hk_func, voidptr_func):
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_CreateHook = minhook_x64.MH_CreateHook
            MH_CreateHook.argtypes = (wintypes.LPVOID, wintypes.LPVOID, ctypes.POINTER(wintypes.LPVOID),)
            return MH_CreateHook(org_func, hk_func, voidptr_func)
        elif(bits == "32bit"):
            MH_CreateHook = minhook_x32.MH_CreateHook
            MH_CreateHook.argtypes = (wintypes.LPVOID, wintypes.LPVOID, ctypes.POINTER(wintypes.LPVOID),)
            return MH_CreateHook(org_func, hk_func, voidptr_func)
    def MH_EnableHook(hook):
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_EnableHook = minhook_x64.MH_EnableHook
            MH_EnableHook.argtypes = (wintypes.LPVOID,)
            return MH_EnableHook(hook)
        elif(bits == "32bit"):
            MH_EnableHook = minhook_x32.MH_EnableHook
            MH_EnableHook.argtypes = (wintypes.LPVOID, wintypes.LPVOID, ctypes.POINTER(wintypes.LPVOID),)
            return MH_EnableHook(hook)

    def MH_StatusToString(status : int):
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_StatusToString = minhook_x64.MH_StatusToString
            MH_StatusToString.restype = ctypes.c_char_p
            MH_StatusToString.argtypes = (ctypes.c_long,)
            return MH_StatusToString(status)
        elif(bits == "32bit"):
            MH_StatusToString = minhook_x32.MH_StatusToString
            MH_StatusToString.restype = ctypes.c_char_p
            MH_StatusToString.argtypes = (ctypes.c_long,)
            return MH_StatusToString(status)

    def MH_DisableHook(hook_f):
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_DisableHook = minhook_x64.MH_DisableHook
            MH_DisableHook.argtypes = (wintypes.LPVOID,)
            return MH_DisableHook(hook_f)
        elif(bits == "32bit"):
            MH_DisableHook = minhook_x32.MH_DisableHook
            MH_DisableHook.argtypes = (wintypes.LPVOID,)
            return MH_DisableHook(hook_f)

    def MH_Unitialize():
        bits = platform.architecture()
        if(bits == "64bit"):
            MH_Uninitialize = minhook_x64.MH_Uninitialize
            return MH_Uninitialize()
        elif(bits == "32bit"):
            MH_Uninitialize = minhook_x32.MH_Uninitialize
            return MH_Uninitialize()
