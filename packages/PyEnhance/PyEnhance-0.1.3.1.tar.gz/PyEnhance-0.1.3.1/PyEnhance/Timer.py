import time
import threading

def TimeFormat(Counter=None, Form=None):

    Counter = Counter[0] / 60 # Divides the int representing the time elapsed in seconds stored in the Counter list at index 0 by 60 turning it to a float type
    Counter = str(Counter)
    DotIndex = Counter.index('.')

    OutputMin = f"{Counter[:DotIndex]}"
    OutputSec = f"{Counter[DotIndex:]}"

    if DotIndex == 1 and not (round(float(OutputSec) * 60)) > 60 and int(OutputMin) == 0:  # Triggers if output seconds in total are less then a min

        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        # ===| Start Output Code |===

        if Form == "Long":
            # Long Form Output Code
            if OutputSec > 1: SecText = "seconds"
            else: SecText = "second"
            print(f'{OutputSec} {SecText}')

        else:
            # Short Form Output Code
            if len(str(OutputSec)) == 1:
                OutputSec = f"0{OutputSec}"
            print(f'00:{OutputSec}')

        # ===| End of Output Code |===


    if DotIndex == 2 or int(OutputMin) > 0 and DotIndex == 1: # triggers if DotIndex is 2 or OutputMin's value is grater then 1 and DotIndex is 1
        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        OutputMin = ((int(OutputMin) + (int(OutputSec / 60))))

        if int(OutputMin) < 60:  # Triggers if output min sum is less then an hour

            # ===| Start Output Code |===

            if Form == "Long":
                # Long Form Output Code
                if OutputMin > 1: MinText = "minutes"
                else: MinText = "minute"
                if OutputSec > 1: SecText = "seconds"
                else: SecText = "second"

                if OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputMin} {MinText}')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputSec} {SecText}')
                else:
                    print(f'{OutputMin} {MinText} {OutputSec} {SecText}')

            else:
                # Short Form Output Code
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                print(f'{OutputMin}:{OutputSec}')

            # ===| End of Output Code |===

        else: # Triggers if out min total is more sum an hour

            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))

            # ===| Start Output Code |===

            if Form == "Long":
                # Long Form Output Code
                if OutputHours > 1: HourText = "hours"
                else: HourText = "hour"
                if OutputMin > 1: MinText = "minutes"
                else: MinText = "minute"
                if OutputSec > 1: SecText = "seconds"
                else: SecText = "second"

                if OutputMin == 0 and OutputSec == 0:
                    print(f'{OutputHours} {HourText}')
                elif OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputHours} {HourText} {OutputMin} {MinText}')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputHours} {HourText} {OutputSec} {SecText}')
                else:
                    print(f'{OutputHours} {HourText} {OutputMin} {MinText} {OutputSec} {SecText}')

            else:
                # Short Form Output Code
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                if len(str(OutputMin)) == 1: OutputMin = f"0{OutputMin}"
                print(f'{OutputHours}:{OutputMin}:{OutputSec}')

            # ===| End of Output Code |===

    if DotIndex == 3 or DotIndex == 4:

        if OutputSec == ".":
            OutputSec = "0"

        OutputMin = int(OutputMin)
        OutputSec = float(OutputSec)

        OutputMin = ((OutputMin + (int(OutputSec / 60))))
        OutputSec = (round(float(OutputSec) * 60))

        if OutputMin >= 60: # Checks if out min sum is less then or equal to an hour
            OutputMin = int(OutputMin)
            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))

            # ===| Start of Output Code |===

            if Form == "Long":
                # Long Form Output Code

                if OutputHours > 1: HourText = "hours"
                else: HourText = "hour"
                if OutputMin > 1: MinText = "minutes"
                else: MinText = "minute"
                if OutputSec > 1: SecText = "seconds"
                else: SecText = "second"

                if OutputMin == 0 and OutputSec == 0:
                    print(f'{OutputHours} {HourText}')
                elif OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputHours} {HourText} {OutputMin} {MinText}')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputHours} {HourText} {OutputSec} {SecText}')
                else:
                    print(f'{OutputHours} {HourText} {OutputMin} {MinText} {OutputSec} {SecText}')
            else:
                # Short Form Output Code
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                if len(str(OutputMin)) == 1: OutputMin = f"0{OutputMin}"
                print(f'{OutputHours}:{OutputMin}:{OutputSec}')

            # ===| End of Output Code |===

class Timer:
    def __init__(self):
        self.stop_flag = True
        self.thread = None
        self.counter = 0
        self.Stamps = None

        self.Form = None

    def counterlist(self):
        return self.counterlist

    def _run(self):

        while not self.stop_flag:
            time.sleep(1)
            self.counter += 1

    def Start(self, Form=None):

        self.Form = Form

        if self.thread is None or not self.Start:
            self.stop_flag = False
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

        else:
            print(f"[ERROR] Timer already running")

    def Stop(self):
        if self.thread and self.thread.is_alive():
            self.stop_flag = True
            self.thread.join()

            self.counterlist = []

            if self.stop_flag is True:
                self.counterlist.append(self.counter)

                TimeFormat(self.counterlist, Form=self.Form)
        else:
            print(f"[ERROR] Timer not running")

"""

=== Examples ===

Short form output:

Timer.Start()

time.sleep(30)

Timer.Stop()


Long form output:

Timer.Start(Form="Long")

time.sleep(30)

Timer.Stop()

"""
"""

TestCases = [
    3661,  # Slightly more than an hour
    45,  # Less than a minute
    7322,  # A bit more than two hours
    86399,  # One second less than a full day
    0,  # No time
    12345,  # Random intermediate value
    5400,  # Exactly one and a half hour
    3599,  # One second less than an hour
    86400,  # Exactly one day
    18000  # Exactly five hours
]

Timer.Start(TestInt=18000)

time.sleep(1)

Timer.Stop()

"""

####
"""
Left off with the issue of stamps not working 

"""
####