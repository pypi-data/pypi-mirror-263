import enum
import logging
import threading
from abc import ABC
from time import sleep

import serial

from .classes import Pump, signalformfromstring, State, SignalForm


class BartelsLabtronix(Pump, ABC):
    """ """

    def __init__(
        self, port: str = "COM5", host: str = "localhost", loglevel: int = logging.INFO
    ) -> None:
        super().__init__(port=port, loglevel=loglevel)
        self.log.info("Bartels Labtronix control initialized.")
        self.ser = serial.Serial(port, 9600, timeout=1, xonxoff=True)
        while not self.ser.is_open:
            sleep(0.1)
        self.buffer = ""
        self.reading = False
        # start the reading thread
        x = threading.Thread(target=self.__read)
        x.start()

    # INTERNAL FUNCTIONS
    def __put(self, msg: str) -> None:
        msg += "\r"
        self.ser.write(msg.encode("utf-8"))
        self.ser.flush()

    def __read(self) -> None:
        while True:
            sleep(0.05)
            if self.ser.in_waiting > 0:
                self.reading = True
                self.buffer += self.ser.read(self.ser.in_waiting).decode("utf-8")
            else:
                self.reading = False

    # STATE FUNCTIONS
    def get_state(self) -> "State":
        self.buffer = ""
        self.__put("")
        while (len(self.buffer) < 1) | self.reading:
            sleep(0.01)
        state_str = self.buffer.split("\r\n")
        self.buffer = ""
        result = {}
        for r in state_str:
            if r:
                rsplit = r.split(":")
                if len(rsplit) == 2:
                    result[rsplit[0].strip()] = rsplit[1].strip()
                else:
                    rsplit = r.split(" ")
                    if len(rsplit) == 2:
                        result[rsplit[0].strip()] = rsplit[1].strip()
        state = State(
            signalform=signalformfromstring(mystring=result["Wavetype"]),
            frequency=int(result["Frequence"][0:4]),
            amplitude=int(result["Amplitude"][0:3]),
            running=(result["Signal"] == "on"),
        )
        return state

    def turnon(self) -> None:
        self.__put("bon")

    def turnoff(self) -> None:
        self.__put("boff")

    def setfrequency(self, freq: int) -> None:
        self.buffer = ""
        if (freq <= 250) & (freq > 0):
            self.__put(f"F{freq}")
            while (len(self.buffer) < 1) | self.reading:
                sleep(0.01)
            self.buffer = ""  # we could check if it went well...
        else:
            self.log.error(f"Invalid frequency: {freq} Hz")

    def setsignalform(self, sf: SignalForm) -> None:
        if sf == SignalForm.SRS:
            self.__put("MC")
        if sf == SignalForm.Sine:
            self.__put("MS")
        if sf == SignalForm.Rectangular:
            self.__put("MR")
        if sf == SignalForm.Unknown:
            self.log.error("Unknown SignalForm")

    def setamplitude(self, ampl: int) -> None:
        self.buffer = ""
        if (ampl <= 250) & (ampl > 0):
            self.__put(f"A{ampl}")
            while (len(self.buffer) < 1) | self.reading:
                sleep(0.01)
            self.buffer = ""  # we could check if it went well...
        else:
            self.log.error(f"Invalid Amplitude: {ampl} Hz")

    def disconnect(self) -> None:
        self.ser.close()
