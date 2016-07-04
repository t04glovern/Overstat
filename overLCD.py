from overStat import *
from HD44780 import *
from time import strftime, localtime

lcd = HD44780()


class OverLCD:
    def __init__(self, battle_tag):
        self.battle_tag = battle_tag

    def queryStats(self):
        ow = OverStatAPI('key')
        return ow.get_stats(self.battle_tag)

    def printIntro(self):
        lcd.clear()
        lcd.writeMsg('Overwatch Stats', 0.1)
        lcd.writeMsg('\nv0.1: t04glovern', 0.1)
        sleep(1)
        lcd.clear()

    def printWinLoss(self):
        lcd.clear()
        lcd.writeMsg('..Querying API..')
        stats = self.queryStats()
        lcd.clear()
        lcd.writeMsg(stats['battletag'], 0.1)
        lcd.writeMsg(('\nW/L:' +
                      str(stats['overall_stats']['wins']) +
                      '/' +
                      str(stats['overall_stats']['losses']) +
                      ' Lv' +
                      str(stats['overall_stats']['level'])), 0.1)
        sleep(5)
        lcd.clear()

    def highNoon(self):
        display.printIntro()
        while(1):
            lcd.writeMsg("    " + strftime("%H:%M:%S", localtime()))
            sleep(5)
            display.printWinLoss()


if __name__ == '__main__':
    battle_tag = 'GloverDude#1471'
    display = OverLCD(battle_tag)
    display.highNoon()
