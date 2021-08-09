from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from decimal import Decimal
#import sys

#sys.setrecursionlimit(2**3)

Window.size = (480 , 640)

class Screen_Manager(ScreenManager): 
    pass

class Main_Screen(Screen):
    pass

class Ether_Screen(Screen):
    def convert(self):

        if  self.wei.text:   
            self.kwei.text   = str("{:.18f}".format(float(self.wei.text)    /1000 ))
            self.mwei.text   = str("{:.18f}".format(float(self.kwei.text)   /1000 ))
            self.gwei.text   = str("{:.18f}".format(float(self.mwei.text)   /1000 ))
            self.micro.text  = str("{:.18f}".format(float(self.gwei.text)   /1000 ))
            self.mili.text   = str("{:.18f}".format(float(self.micro.text)  /1000 ))
            self.eth.text    = str("{:.18f}".format(float(self.mili.text)   /1000 ))
            self.kether.text = str("{:.18f}".format(float(self.eth.text)    /1000 ))
            self.mether.text = str("{:.18f}".format(float(self.kether.text) /1000 ))
            self.gether.text = str("{:.18f}".format(float(self.mether.text) /1000 ))
            self.tether.text = str("{:.18f}".format(float(self.gether.text) /1000 ))
  

        elif self.kwei.text:
            self.wei.text    = str(float(self.kwei.text)    *1000 )
            self.mwei.text   = str(float(self.kwei.text)    /1000 )
            self.gwei.text   = str(float(self.mwei.text)    /1000 )
            self.micro.text  = str(float(self.gwei.text)    /1000 )
            self.mili.text   = str(float(self.micro.text)   /1000 )
            self.eth.text    = str(float(self.mili.text)    /1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.mwei.text:
            self.kwei.text   = str(float(self.mwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )
            self.gwei.text   = str(float(self.mwei.text)    /1000 )
            self.micro.text  = str(float(self.gwei.text)    /1000 )
            self.mili.text   = str(float(self.micro.text)   /1000 )
            self.eth.text    = str(float(self.mili.text)    /1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.gwei.text:

            self.mwei.text   = str(float(self.gwei.text)    *1000)
            self.kwei.text   = str(float(self.mwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )   
            self.micro.text  = str(float(self.gwei.text)    /1000 )
            self.mili.text   = str(float(self.micro.text)   /1000 )
            self.eth.text    = str(float(self.mili.text)    /1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.micro.text:
            self.gwei.text   = str(float(self.micro.text)    *1000 )
            self.mwei.text   = str(float(self.gwei.text)    / 1000 )
            self.kwei.text   = str(float(self.mwei.text)    *1000 ) 
            self.wei.text    = str(float(self.kwei.text)    *1000 )
            self.mili.text   = str(float(self.micro.text)   /1000 )
            self.eth.text    = str(float(self.mili.text)    /1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.mili.text:
            self.micro.text  = str(float(self.mili.text)    *1000 )
            self.gwei.text   = str(float(self.micro.text)   /1000 )
            self.kwei.text   = str(float(self.mwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )

            self.eth.text    = str(float(self.mili.text)    /1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.eth.text:
            self.mili.text   = str(float(self.eth.text)     *1000 )
            self.micro.text  = str(float(self.mili.text)    *1000 )
            self.gwei.text   = str(float(self.micro.text)    *1000 )
            self.mwei.text   = str(float(self.gwei.text)    *1000 )
            self.kwei.text   = str(float(self.mwei.text)    *1000 )

            self.wei.text    = str(float(self.kwei.text)    *1000 )
            self.kether.text = str(float(self.eth.text)     /1000 )
            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.kether.text:
            self.eth.text    = str(float(self.kether.text)  *1000 )
            self.mili.text   = str(float(self.eth.text)     *1000 )
            self.micro.text  = str(float(self.mili.text)    *1000 )
            self.gwei.text   = str(float(self.micro.text)   *1000 )
            self.kwei.text   = str(float(self.gwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )

            self.mether.text = str(float(self.kether.text)  /1000 )
            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.mether.text:
            self.kether.text = str(float(self.mether.text)  *1000 )
            self.eth.text    = str(float(self.kether.text)  *1000 )
            self.mili.text   = str(float(self.eth.text)     *1000 )
            self.micro.text  = str(float(self.mili.text)    *1000 )
            self.gwei.text   = str(float(self.micro.text)   *1000 )
            self.kwei.text   = str(float(self.gwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )

            self.gether.text = str(float(self.mether.text)  /1000 )
            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.gether.text:
            self.mether.text = str(float(self.gether.text)  *1000 )
            self.kether.text = str(float(self.mether.text)  *1000 )
            self.eth.text    = str(float(self.kether.text)  *1000 )
            self.mili.text   = str(float(self.eth.text)     *1000 )
            self.micro.text  = str(float(self.mili.text)    *1000 )
            self.gwei.text   = str(float(self.micro.text)   *1000 )
            self.mwei.text   = str(float(self.gwei.text)    *1000 )
            self.kwei.text   = str(float(self.mwei.text)    *1000 )
            self.wei.text    = str(float(self.kwei.text)    *1000 )

            self.tether.text = str(float(self.gether.text)  /1000 )

        elif self.tether.text:
            self.wei.text    = str(float(self.kwei.text)    / 1000 )
            self.kwei.text   = str(float(self.mwei.text)    / 1000 )
            self.mwei.text   = str(float(self.gwei.text)    / 1000 )
            self.gwei.text   = str(float(self.micro.text)   / 1000 )
            self.micro.text  = str(float(self.mili.text)    / 1000 )
            self.mili.text   = str(float(self.eth.text)     / 1000 )
            self.eth.text    = str(float(self.kether.text)  / 1000 )
            self.kether.text = str(float(self.mether.text)  / 1000 )
            self.mether.text = str(float(self.gether.text)  / 1000 )
            self.gether.text = str(float(self.tether.text)  / 1000 )

        

    pass

class Btc_Screen(Screen):
    def sat_to_bit(self):
        if (self.satooshi.text == '.' or self.satooshi.text == '' or self.satooshi.text == '0'):
            pass
        else:
            self.btc.text = str(float(self.ids.satooshi.text)/100000000)
    def bit_to_sat(self):
        if (self.btc.text == '.' or self.btc.text == '' or self.btc.text == '0'):
            pass
        else:
            self.satooshi.text = str(float(self.ids.btc.text)*100000000)
    pass

class Trx_Screen(Screen):
    def sun_to_trx(self):
        if (self.sun.text == '.' or self.sun.text == '' or self.sun.text == '0'):
            pass
        else:
            self.trx.text = str(float(self.ids.sun.text)*1000000)
    def trx_to_sun(self):
        if (self.trx.text == '.' or self.trx.text == '' or self.trx.text == '0'):
            pass
        else:
            self.sun.text = str(float(self.ids.trx.text)/1000000)
    pass

class About_Screen(Screen):
    pass

class Donute_Screen(Screen):
    pass

kv = Builder.load_file('Token_converter.kv')
class Token_converter(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return kv



Token_converter().run()
