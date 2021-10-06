import atexit
import os
from typing import Union
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


# power on all ports when program exit
@atexit.register
def reset_power_status():
    os.system('sudo uhubctl -l 2 -a 1')


def switch_power(hub_id: int, port: str, on_off: Union[int, str]):
    try:
        if len(port) == 0:
            # 不指定usb port
            # print('switch all ports  to ' + on_off)
            command = 'sudo uhubctl -l ' + str(hub_id) + ' -a ' + str(on_off)
            print('Command: ' + command)
            os.system(command)
        else:
            command = ' sudo uhubctl -l ' + str(hub_id) + ' -p ' + str(port) + ' -a ' + str(on_off)
            print('Command: ' + command)
            os.system(command)
            # print('switch port ' + port + ' to ' + on_off)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    switch_power(2, '', 0)  # turn off the power of all usb ports

    scheduler = BlockingScheduler()

    # scheduler.add_job(switch_power, CronTrigger(second='*/10'), args=[2, '', '1'])

    # job to switch power on at 20:00 everyday
    scheduler.add_job(switch_power, CronTrigger(hour='20'), args=[2, '', '1'])

    # job to switch power off at 07:00 everyday
    scheduler.add_job(switch_power, CronTrigger(hour='7'), args=[2, '', '0'])

    scheduler.start()
