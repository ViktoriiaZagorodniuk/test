import os
import platform
print('Module:', os.name, '// Name:',platform.system(),'// Version:',platform.release())



from platform import *
print(system(), release())