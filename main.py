#!/usr/bin/env python3

from RPi import GPIO
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import datetime

LIGHT_PIN = 11
VALVE_OPEN_PIN = 40
VALVE_CLOSE_PIN = 38


def on_light():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, True)


def open_valve():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(VALVE_OPEN_PIN, GPIO.OUT)
    GPIO.output(VALVE_OPEN_PIN, True)
    time.sleep(10)
    GPIO.output(VALVE_OPEN_PIN, False)


def close_valve():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(VALVE_CLOSE_PIN, GPIO.OUT)
    GPIO.output(VALVE_CLOSE_PIN, True)
    time.sleep(10)
    GPIO.output(VALVE_CLOSE_PIN, False)


def off_light():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, False)


def main():
    start_hour = 12
    end_hour = 22

    now_hour = datetime.datetime.now().hour

    if start_hour < now_hour < end_hour - 1:
        open_valve()
    else:
        close_valve()

    if start_hour < now_hour < end_hour:
        on_light()
    else:
        off_light()

    sc = BlockingScheduler()
    sc.add_job(on_light, "cron", hour=start_hour)
    sc.add_job(open_valve, "cron", hour=start_hour)
    sc.add_job(off_light, "cron", hour=end_hour)
    sc.add_job(close_valve, "cron", hour=end_hour - 1)
    sc.start()


if __name__ == '__main__':
    main()
