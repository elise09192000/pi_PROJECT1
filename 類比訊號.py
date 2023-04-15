import gpiozero
#from signal import pause
#mcp3008 = gpiozero.MCP3008(channel=7)
#print(mcp3008.value)
#pause()
from time import sleep
mcp3008 = gpiozero.MCP3008(channel=7)

while(True):
    lightValue = round(mcp3008.value*1000)
    tmperature = round(mcp3008._temperature.value*3.3*100,)
    print(lightValue)
    if lightValue < 40:
        buzzer.on()
    else:
        buzzer.off()
    sleep(1)
