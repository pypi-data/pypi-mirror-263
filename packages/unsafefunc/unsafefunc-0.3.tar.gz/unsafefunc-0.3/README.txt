Welcome to unsafefunc library!

Firstly you need install library. You can use command ``pip install unsafefunc``.

Run scripts only on VM!
Author not responding for any damage caused by this library!
Run scripts as admin.

Here are library functions:

MBR overwrite:
```
import unsafefunc as unsafe

buffer = bytes([
    # New MBR Here
])

unsafe.MBR.overwrite(buffer)
```

BSOD:
```
import unsafefunc as unsafe

unsafe.System.bsod()
```
