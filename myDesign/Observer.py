from abc import ABCMeta,abstractmethod
# 引入ABCMeta,abstractmethod来定义抽象类和抽象方法

class WaterHeater:
      # ```热水器```
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self,temperature):
        self.__temperature = temperature
        print("当前温度是：" + str(self.__temperature)+"C")
        self.notifies()

    def addObserver(self,observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    # 抽象类
    @abstractmethod
    def update(self,waterHeater):
        pass


class WashingMode(Observer):
    # 用于监听热水器洗澡模式
    def update(self,waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() <= 70:
            print("水已烧好，温度正好，可以来洗澡了")

class DrinkingMode(Observer):
    # 用于监听热水器引用模式
    def update(self,waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开，可以用来饮用了")

def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)

    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


if __name__ == "__main__":
    testWaterHeater()