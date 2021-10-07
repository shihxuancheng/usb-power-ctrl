import os
import signal
from typing import Union

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def reset_power_status():
    print('before dprogram exit!!!')
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

    # job to switch power on at 21:00 from monday to friday
    scheduler.add_job(switch_power, CronTrigger(day_of_week='0-4', hour='21'), args=[2, '', '1'])

    # job to switch power off at 07:00 everyday  from monday to friday
    scheduler.add_job(switch_power, CronTrigger(day_of_week='0-4', hour='7'), args=[2, '', '0'])

    # job to switch power on at 07:00 on the saturday
    scheduler.add_job(switch_power, CronTrigger(day_of_week='5', hour='7'), args=[2, '', '1'])

    # job to switch power off at 21:00 on sunday
    scheduler.add_job(switch_power, CronTrigger(day_of_week='6', hour='21'), args=[2, '', '0'])

    # power on all ports when program exit
    signal.signal(signal.SIGTERM, reset_power_status)  # when program terminated by kill -15
    signal.signal(signal.SIGINT, reset_power_status)  # when program terminated by kill -2

    scheduler.start()
