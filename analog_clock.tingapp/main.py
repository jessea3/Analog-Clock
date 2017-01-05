import tingbot
from tingbot import *
import time
import os
from math import sin, cos, pi



#clock_center = (90,90)
clock_center = (160,90)
clock_size = (160,160)
clock_radius = 45


# setup code here

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()

@every(seconds=1.0/30)
def loop():
    (tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst) = time.localtime()

    # drawing code here
    screen.fill(color='black')
    
#    screen.text("%02d:%02d:%02d" % (tm_hour,tm_min,tm_sec),xy=(20,230), align='bottomleft')
    screen.text(time.strftime("%A"), xy=(clock_center[0],clock_center[1]+clock_size[1]/2 + 15), align='center', font_size=20, color='silver')
    screen.text(time.strftime("%B %d, %Y"), xy=(clock_center[0],clock_center[1]+clock_size[1]/2 + 38), align='center', font_size=15, color='silver')

    screen.image('img/clockface.png', xy=clock_center, align='center',max_width=clock_size[0],max_height=clock_size[1])

    angle = pi * 1.5 + pi/6 * (tm_hour + tm_min/60.0)
    end_x, end_y = cos(angle)*0.70*clock_radius+clock_center[0],sin(angle)*0.70*clock_radius+clock_center[1]     
    screen.line(start_xy=clock_center,end_xy=(end_x,end_y),color='black',width=4)

    angle = pi*1.5 +pi/30 * (tm_min + tm_sec/60.0)
    end_x, end_y = cos(angle)*0.90*clock_radius+clock_center[0],sin(angle)*0.90*clock_radius+clock_center[1]
    screen.line(start_xy=clock_center,end_xy=(end_x,end_y),color='black',width=3)

    angle = pi*1.5 + pi/30 * tm_sec
    end_x, end_y =  cos(angle)*0.95*clock_radius+clock_center[0],sin(angle)*0.95*clock_radius+clock_center[1]
    screen.line(start_xy=clock_center,end_xy=(end_x,end_y),color='black',width=2)
    
tingbot.run()
