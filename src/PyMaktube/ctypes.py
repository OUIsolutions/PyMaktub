


import ctypes
from platform import system as operating_system

from os.path import abspath,dirname

os_name = operating_system()
# get current file path
path = dirname(abspath(__file__))

# create shared library
if os_name == 'Windows':
    clib_path = f'{path}\\../bin/Maktub.dll'
else:
    clib_path = f'{path}/../bin/Maktub.so'



loader =ctypes.CDLL(clib_path)

loader.newMakTub.argtypes  = [ctypes.c_char_p]
loader.newMakTub.restype = ctypes.c_void_p


loader.MakTub_set_seed.argtypes = [ctypes.c_void_p,ctypes.c_char_p]

loader.MakTub_aply_seed_modification.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
    ctypes.c_char_p
]

loader.MakTub_get_seed.argtypes = [ctypes.c_void_p]
loader.MakTub_get_seed.restype = ctypes.c_char_p


#Maktub Obj
loader.Maktub_generate_num.argtypes = [ctypes.c_void_p,ctypes.c_long,ctypes.c_long]
loader.Maktub_generate_num.restype = ctypes.c_longlong

loader.MakTub_generate_token.argtypes = [ctypes.c_void_p,ctypes.c_int,ctypes.c_char_p]
loader.MakTub_generate_token.restype = ctypes.c_char_p

loader.MakTub_free.argtypes = [ctypes.c_void_p]
