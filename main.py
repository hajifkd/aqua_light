#!/usr/bin/env python3

from RPi import GPIO
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import datetime

LIGHT_PIN = 11


def on_light():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, True)


def off_light():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, False)


def main():
    start_hour = 15
    end_hour = 23

    now_hour = datetime.datetime.now().hour

    if start_hour < now_hour < end_hour:
        on_light()
    else:
        off_light()

    sc = BlockingScheduler()
    sc.add_job(on_light, "cron", hour=start_hour)
    sc.add_job(off_light, "cron", hour=end_hour)
    sc.start()


if __name__ == '__main__':
    main()
