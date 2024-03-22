from colorama import init, Fore, Back, Style
from enum import Enum

import sys

class Color(Enum):
    init(autoreset=True)
    Green = Fore.GREEN
    Red = Fore.RED
    Yellow = Fore.YELLOW
    WarningYellow = Fore.LIGHTYELLOW_EX
    White = Fore.WHITE
    Cyan = Fore.CYAN
    Magenta = Fore.MAGENTA

    def __str__(self):
        return self.value
class Type(Enum):
    Bright = Style.BRIGHT
    Normal = Style.NORMAL
    Dim = Style.DIM

    def __str__(self):
        return self.value
class Stamp(Enum):

    Info = f'{Color.Green}{Type.Bright}[INFO]{Fore.RESET}'
    Warring = f'{Color.WarningYellow}{Type.Bright}[WARRING]{Fore.RESET}'
    Output = f'{Color.Cyan}{Type.Bright}[OUTPUT]{Fore.RESET}'
    Input = f'{Color.Magenta}{Type.Bright}[INPUT]{Fore.RESET}'
    Error = f'{Color.Red}{Type.Bright}[ERROR]{Fore.RESET}'

    def __str__(self):
        return self.value


# Currently Testing
#Info = Stamp.Info
#Warn = Stamp.Warn
#Output = Stamp.Output
#Input = Stamp.Input
#Error = Stamp.Error
#
"""

=== Examples ===

print("\n")
print(Stamp.Info)
print(Stamp.Warn)
print(Stamp.Input)
print(Stamp.Output)
print(Stamp.Error)

"""