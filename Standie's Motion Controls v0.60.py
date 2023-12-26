print("MOTION CONTROLS ACTIVATED! \nIf you are interested in my other motion control scripts, \ncontact me on Discord under the username 'standie'. \nBecause I am a terrible programmer, \nI welcome all help with this project. \nEventually I would like to have a program with GUI \nthat allows users to easily implement \nand customize motion controls \nfor any game they want :).")

import pyautogui
import vgamepad as vg
import time
from pyjoycon import JoyCon, get_R_id, get_L_id
import hid

JOYCON_VENDOR_ID = 0x057e
JOYCON_PRODUCT_ID = 0x2006
JOYCON_REPORT_SIZE = 49
gamepad = vg.VX360Gamepad()

def press_b():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()

def release_b():
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()

def press_a():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def release_a():
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
   

def get_joycon_device(joycon_id):
    joycon_devices = hid.enumerate(JOYCON_VENDOR_ID, JOYCON_PRODUCT_ID)
    for device_info in joycon_devices:
        if device_info['serial_number'] == joycon_id:
            joycon_device = hid.device()
            joycon_device.open_path(device_info['path'])
            return joycon_device

right_joycon_id = get_R_id()
left_joycon_id = get_L_id()

right_joycon = JoyCon(*right_joycon_id)
left_joycon = JoyCon(*left_joycon_id)

b_pressed = False
a_pressed = False
gyro_threshold = 12650  # 11000
accel_threshold = 10300    # 9000
last_b_press_time = 0
last_a_press_time = 0
cooldown_duration = 0.350  # 450 milliseconds
trigger_duration = 0.000  # 200 milliseconds

right_gyro_breached_time = 0
right_accel_breached_time = 0
left_gyro_breached_time = 0
left_accel_breached_time = 0

while True:
    right_report = right_joycon.get_status()
    left_report = left_joycon.get_status()

    right_accel_x = abs(right_report['accel']['x'])
    right_accel_y = abs(right_report['accel']['y'])
    right_accel_z = abs(right_report['accel']['z'])
    right_gyro_x = abs(right_report['gyro']['x'])
    right_gyro_y = abs(right_report['gyro']['y'])
    right_gyro_z = abs(right_report['gyro']['z'])

    left_accel_x = abs(left_report['accel']['x'])
    left_accel_y = abs(left_report['accel']['y'])
    left_accel_z = abs(left_report['accel']['z'])
    left_gyro_x = abs(left_report['gyro']['x'])
    left_gyro_y = abs(left_report['gyro']['y'])
    left_gyro_z = abs(left_report['gyro']['z'])

    current_time = time.time()

    if right_report['buttons']['right']['sl']:
        if (right_gyro_x > gyro_threshold or right_gyro_y > gyro_threshold or right_gyro_z > gyro_threshold):
            if right_gyro_breached_time is None:
                right_gyro_breached_time = current_time
            elif current_time - right_gyro_breached_time >= trigger_duration:
                if not b_pressed and (current_time - last_b_press_time) >= cooldown_duration:
                    press_b()
                    b_pressed = True
                    last_b_press_time = current_time
        elif (right_accel_x > accel_threshold or right_accel_y > accel_threshold or right_accel_z > accel_threshold):
            if right_accel_breached_time is None:
                right_accel_breached_time = current_time
            elif current_time - right_accel_breached_time >= trigger_duration:
                if not b_pressed and (current_time - last_b_press_time) >= cooldown_duration:
                    press_b()
                    b_pressed = True
                    last_b_press_time = current_time
        else:
            b_pressed = False
            gyro_breached_time = None
            accel_breached_time = None
            release_b()
    else:
        if (right_gyro_x > gyro_threshold or right_gyro_y > gyro_threshold or right_gyro_z > gyro_threshold):
            if right_gyro_breached_time is None:
                right_gyro_breached_time = current_time
            elif current_time - right_gyro_breached_time >= trigger_duration:
                if not b_pressed and (current_time - last_b_press_time) >= cooldown_duration:
                    press_b()
                    b_pressed = True
                    last_b_press_time = current_time
                    time.sleep(0.2)
                    release_b()
                    b_pressed = False
        elif (right_accel_x > accel_threshold or right_accel_y > accel_threshold or right_accel_z > accel_threshold):
            if right_accel_breached_time is None:
                right_accel_breached_time = current_time
            elif current_time - right_accel_breached_time >= trigger_duration:
                if not b_pressed and (current_time - last_b_press_time) >= cooldown_duration:
                    press_b()
                    b_pressed = True
                    last_b_press_time = current_time
                    time.sleep(0.2)
                    release_b()
                    b_pressed = False
        else:
            b_pressed = False
            gyro_breached_time = None
            accel_breached_time = None
            release_b()

    if left_report['buttons']['left']['sr']:
        if (left_gyro_x > gyro_threshold or left_gyro_y > gyro_threshold or left_gyro_z > gyro_threshold):
            if left_gyro_breached_time is None:
                left_gyro_breached_time = current_time
            elif current_time - left_gyro_breached_time >= trigger_duration:
                if not a_pressed and (current_time - last_a_press_time) >= cooldown_duration:
                    press_a()
                    a_pressed = True
                    last_a_press_time = current_time
        elif (left_accel_x > accel_threshold or left_accel_y > accel_threshold or left_accel_z > accel_threshold):
            if left_accel_breached_time is None:
                left_accel_breached_time = current_time
            elif current_time - left_accel_breached_time >= trigger_duration:
                if not a_pressed and (current_time - last_a_press_time) >= cooldown_duration:
                    press_a()
                    a_pressed = True
                    last_a_press_time = current_time
        else:
            a_pressed = False
            gyro_breached_time = None
            accel_breached_time = None
            release_a()
    else:
        if (left_gyro_x > gyro_threshold or left_gyro_y > gyro_threshold or left_gyro_z > gyro_threshold):
            if left_gyro_breached_time is None:
                left_gyro_breached_time = current_time
            elif current_time - left_gyro_breached_time >= trigger_duration:
                if not a_pressed and (current_time - last_a_press_time) >= cooldown_duration:
                    press_a()
                    a_pressed = True
                    last_a_press_time = current_time
                    time.sleep(0.2)
                    release_a()
                    a_pressed = False
        elif (left_accel_x > accel_threshold or left_accel_y > accel_threshold or left_accel_z > accel_threshold):
            if left_accel_breached_time is None:
                left_accel_breached_time = current_time
            elif current_time - left_accel_breached_time >= trigger_duration:
                if not a_pressed and (current_time - last_a_press_time) >= cooldown_duration:
                    press_a()
                    a_pressed = True
                    last_a_press_time = current_time
                    time.sleep(0.2)
                    release_a()
                    a_pressed = False
        else:
            a_pressed = False
            gyro_breached_time = None
            accel_breached_time = None
            release_a()

    time.sleep(0.005)
