from typing import Union
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def schedule_method():
    print('on Scheduler triggered!!!')


def switch_power(hub_id: int, port: str, on_off: Union[int, str]):
    if len(port) == 0:
        # 不指定usb port
        print('switch all ports  to ' + on_off)
        # os.system('dir')
    else:
        print('switch port ' + port + ' to ' + on_off)


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # job to switch power on
    scheduler.add_job(switch_power, CronTrigger(hour='15', minute='46'), args=[2, '', '0'])

    # job to switch power off
    scheduler.add_job(switch_power, CronTrigger(hour='15', minute='36'), args=[2, '', '1'])

    scheduler.start()
