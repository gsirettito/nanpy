from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod, returns


class TM1637Display(ArduinoObject):
    def __init__(self, clk, dio, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call("new", clk, dio)

    @arduinoobjectmethod
    def setBrightness(self, brightness):
        pass

    @arduinoobjectmethod
    def showNumberDec(self, num, leading_zero=False, length=4, pos=0):
        pass

    @arduinoobjectmethod
    def showNumberDecEx(self, num, dots=0, leading_zero=False, length=4, pos=0):
        pass

    @arduinoobjectmethod
    def showNumberHexEx(self, num, dots=0, leading_zero=False, length=4, pos=0):
        pass

    @returns(int)
    @arduinoobjectmethod
    def encodeDigit(self, digit):
        pass

    @arduinoobjectmethod
    def setSegments(self, segments, length=4, pos=0):
        pass

    @arduinoobjectmethod
    def clear(self):
        pass
