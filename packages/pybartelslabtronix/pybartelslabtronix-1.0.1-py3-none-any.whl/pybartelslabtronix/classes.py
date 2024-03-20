"""
General classes
"""

import abc  # Abstract base class
import enum
import logging
import sys


class Pump(abc.ABC):
    def __init__(self, port: str, loglevel: int) -> None:
        self.port = port
        logging.basicConfig(
            level=loglevel,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
        )
        self.log = logging.getLogger(__name__)

    @abc.abstractmethod
    def turnon(self) -> None:
        pass

    @abc.abstractmethod
    def turnoff(self) -> None:
        pass

    @abc.abstractmethod
    def get_state(self) -> "State":
        pass


class SignalForm(enum.IntEnum):
    Sine = 0
    Rectangular = 1
    SRS = 2
    Unknown = -1

    def __str__(self) -> str:
        return self.name


def signalformfromstring(mystring: str) -> SignalForm:
    if mystring == "SRS-Signal":
        return SignalForm.SRS
    if mystring == "Rectangle":
        return SignalForm.Rectangular
    if mystring == "Sine":
        return SignalForm.Sine
    print(f"Cannot identify SignalForm {mystring}")
    return SignalForm.Unknown


class State:
    def __init__(
        self,
        signalform: SignalForm = SignalForm.SRS,
        frequency: int = 200,
        amplitude: int = 250,
        running: bool = False,
    ):
        self.signalform = signalform
        self.frequency = frequency
        self.amplitude = amplitude
        self.running = running

    def __str__(self) -> str:
        runbool = "on" if self.running else "off"
        return (
            f"Wavetype: {self.signalform} \n"
            f"Frequency: {self.frequency} Hz \n"
            f"Amplitude: {self.amplitude} Vpp \n"
            f"Signal: {runbool}"
        )
