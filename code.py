import time

import alarm
import board
import busio
import digitalio
from adafruit_emc2101 import EMC2101

# Conserve power by disabling the NeoPixel.
np_power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
np_power.switch_to_output(value=False)

# Use I2C on the Stemma Qt connector on the Qt PY RP2040.
i2c = busio.I2C(board.SCL1, board.SDA1)

# Set the fan speed to 40% which is nice and quite.
emc = EMC2101(i2c)
print("Setting fan speed to 40%")
emc.manual_fan_speed = 40
time.sleep(1.5)
print("Fan speed", emc.fan_speed)
time.sleep(1)

# Enter deep sleep to save power and don't worry about waking up.
# The free pin A0 is used here as a placeholder.
# Since I don't need to actually wake for any reason, the pin isn't actually connected to anything.
# pin_alarm = alarm.pin.PinAlarm(pin=board.A0, value=True, pull=True)
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 600_000_000)

alarm.exit_and_deep_sleep_until_alarms(time_alarm)
