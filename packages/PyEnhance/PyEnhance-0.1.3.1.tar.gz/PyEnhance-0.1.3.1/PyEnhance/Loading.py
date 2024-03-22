import time
import threading as t
import shutil
from PyEnhance import Counter
import sys

import cursor

cursor.hide()

Counter = Counter.Counter

Rotate = ['|', '/', '-', '\\', '|', '/', '-', '\\']


class Loading:

    def __init__(self):
        self.StopFlag = False
        self.thread = None
        self.CounterObject = Counter()

    def Stop(self):
        if self.thread.is_alive():
            self.StopFlag = True
            self.thread.join()

    def SpinStart(self, Text, TextBack):

        while self.StopFlag is False:
            for i in Rotate:
                if self.StopFlag: break
                print(f'{Text} {i}', end="", flush=True)
                time.sleep(0.4)
                print(f'{TextBack}', end="", flush=True)

    def Spin(self, Text):
        Text = Text
        textlen = len(Text)
        TextBack = '\b' * (textlen + 2)
        if self.thread is None or not self.SpinStart:
            self.thread = t.Thread(target=self.SpinStart, args=(Text, TextBack))
            self.thread.start()

    def BarStart(self, PrintSpeed):

        columns = shutil.get_terminal_size()

        Width = columns

        Width = Width.columns

        Range = Width

        while self.StopFlag is False:

            if self.StopFlag:
                break

            BufferBackSpace = '\b' * (Width)
            print(f"{BufferBackSpace}", end="")
            Text = 'Loading'
            Buffer = ' ' * 4
            SidesWidth = (Width - len(Text) - len(Buffer * 2))

            for x in range(int(SidesWidth / 2)):

                if self.StopFlag:
                    break

                print(f'|', end="", flush=True)
                time.sleep(PrintSpeed)

            for i in Buffer:

                if self.StopFlag:
                    break

                print(f'{i}', end="", flush=True)
                time.sleep(PrintSpeed)

            for i in Text:

                if self.StopFlag:
                    break

                print(f"{i}", end="", flush=True)
                time.sleep(PrintSpeed)

            for i in Buffer:
                if self.StopFlag:
                    break

                print(f'{i}', end="", flush=True)
                time.sleep(PrintSpeed)

            for x in range(int(SidesWidth / 2)):

                if self.StopFlag:
                    break

                print(f'|', end="", flush=True)
                time.sleep(PrintSpeed)

            Text = 'Loading'

            Buffer = ' ' * 4

            NewRange = Width + len(Buffer * 2)

            for i in range(int(NewRange)):

                if self.StopFlag:
                    break

                sys.stdout.write('\b \b')
                sys.stdout.flush()
                time.sleep(PrintSpeed)

    def Bar(self, PrintSpeed):

        if self.thread is None or not self.BarStart:
            self.thread = t.Thread(target=self.BarStart, args=(PrintSpeed,))
            self.thread.start()

    def StatsStart(self, Range, Counter):
        CounterVal = Counter.Total

        Progress = CounterVal / Range * 100

        Progress = str(Progress)

        if CounterVal == Range:
            OutputString = f"Progress: {CounterVal}/{Range}({Progress[:5]}%)"
            TextBack = '\b' * len(OutputString)
            print(f"{TextBack}{OutputString}", end="", flush=True)


        else:
            OutputString = f"Progress: {CounterVal}/{Range}({Progress[:4]}%)"
            TextBack = '\b' * len(OutputString)
            print(f"{TextBack}{OutputString}", end="", flush=True)

    def Stats(self, Range):
        self.CounterObject.Add()
        if self.thread is None or not self.thread.is_alive():
            self.thread = t.Thread(target=self.StatsStart, args=(Range, self.CounterObject,))
            self.thread.start()


"""

===EXAMPLES===

Stats:

ExampleList = [1, 2, 3, 4, 5]

for i in range(len(ExampleList)):
    time.sleep(0.5)

    Loading.Stats(Range=len(ExampleList))


Bar:

	print("\n"*5)

	Loading.Bar(PrintSpeed=0.1)

	time.sleep(60)

	Loading.Stop()


Spin:

	Loading.Spin(Text="Loading")
	time.sleep(30)
	Loading.Stop()

"""
