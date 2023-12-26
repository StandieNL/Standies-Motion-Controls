print("MOTION CONTROLS ACTIVATED! \nIf you are interested in my other motion control scripts, \ncontact me on Discord under the username 'standie'. \nBecause I am a terrible programmer, \nI welcome all help with this project. \nEventually I would like to have a program with GUI \nthat allows users to easily implement \nand customize motion controls \nfor any game they want :).")

import vgamepad as vg
import time
from pyjoycon import JoyCon, get_R_id, get_L_id
import hid

JOYCON_VENDOR_ID = 0x057e
JOYCON_PRODUCT_ID = 0x2006
JOYCON_REPORT_SIZE = 49
gamepad = vg.VX360Gamepad()

gamepad.left_joystick_float(x_value_float=0.4, y_value_float=-0.4)  # values between -1.0 and 1.0
gamepad.right_joystick_float(x_value_float=0.4, y_value_float=-0.4)  # values between -1.0 and 1.0
gamepad.update()

def press_button(button):
    gamepad.press_button(button)
    gamepad.update()

def release_button(button):
    gamepad.release_button(button)
    gamepad.update()

def press_dpad_up():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

def release_dpad_up():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

def press_dpad_down():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

def release_dpad_down():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

def press_dpad_left():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

def release_dpad_left():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

def press_dpad_right():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

def release_dpad_right():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

def press_start():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

def release_start():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

def press_back():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

def release_back():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

def press_left_thumb():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

def release_left_thumb():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

def press_right_thumb():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

def release_right_thumb():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

def press_left_shoulder():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

def release_left_shoulder():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

def press_right_shoulder():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

def release_right_shoulder():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

def press_guide():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)

def release_guide():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)

def press_a():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

def release_a():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

def press_b():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

def release_b():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

def press_x():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

def release_x():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

def press_y():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

def release_y():
    release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

def press_left_trigger():
    gamepad.left_trigger(value=255)

def release_left_trigger():
    gamepad.left_trigger(value=0)    

def press_right_trigger():
    gamepad.right_trigger(value=255)

def release_right_trigger():
    gamepad.right_trigger(value=0)

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

def apply_calibration(value, offset, multiplier):
    return int((value - offset) * multiplier)

# Define the calibration offsets and multipliers for each stick
# These values should be extracted from your JoyCon's calibration data
left_stick_horizontal_offset = 2088
left_stick_vertical_offset = 2200
right_stick_horizontal_offset = 2008
right_stick_vertical_offset = 1896

left_stick_multiplier = 32767 / 1680
right_stick_multiplier = 32767 / 1720

b_pressed = False
a_pressed = False
gyro_threshold = 12650  # 11000
accel_threshold = 10300  # 9000
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

    right_stick_horizontal = right_report['analog-sticks']['right']['horizontal']
    right_stick_vertical = right_report['analog-sticks']['right']['vertical']
    left_stick_horizontal = left_report['analog-sticks']['left']['horizontal']
    left_stick_vertical = left_report['analog-sticks']['left']['vertical']

    gamepad.left_joystick_float(x_value_float=left_stick_horizontal, y_value_float=left_stick_vertical)
    gamepad.right_joystick_float(x_value_float=right_stick_horizontal, y_value_float=right_stick_vertical)

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
    
    if right_report['buttons']['right']['a']:
        press_b()
        b_pressed = True
    else:
        b_pressed = False
        release_b()

    if right_report['buttons']['right']['b']:
        press_a()
        a_pressed = True
    else:
        a_pressed = False
        release_a()

    if right_report['buttons']['right']['y']:
        press_x()
        x_pressed = True
    else:
        x_pressed = False
        release_x()
   
    if right_report['buttons']['right']['x']:
        press_y()
        y_pressed = True
    else:
        y_pressed = False
        release_y()
 
    if right_report['buttons']['right']['r']:
        press_right_shoulder()
        right_shoulder_pressed = True
    else:
        right_shoulder_pressed = False
        release_right_shoulder()

    if right_report['buttons']['right']['zr']:
        press_right_trigger()
        right_trigger_pressed = True
    else:
        right_trigger_pressed = False
        release_right_trigger()

    if left_report['buttons']['left']['down']:
        press_dpad_down()
        dpad_down_pressed = True
    else:
        dpad_down_pressed = False
        release_dpad_down()
 
    if left_report['buttons']['left']['up']:
        press_dpad_up()
        dpad_up_pressed = True
    else:
        dpad_up_pressed = False
        release_dpad_up()
 
    if left_report['buttons']['left']['right']:
        press_dpad_right()
        dpad_right_pressed = True
    else:
        dpad_right_pressed = False
        release_dpad_right()
 
    if left_report['buttons']['left']['left']:
        press_dpad_left()
        dpad_left_pressed = True
    else:
        dpad_left_pressed = False
        release_dpad_left()
 
    if left_report['buttons']['left']['l']:
        press_left_shoulder()
        left_shoulder_pressed = True
    else:
        left_shoulder_pressed = False
        release_left_shoulder()
 
    if left_report['buttons']['left']['zl']:
        press_left_trigger()
        left_trigger_pressed = True
    else:
        left_trigger_pressed = False
        release_left_trigger()
 
    if left_report['buttons']['shared']['minus']:
        press_back()
        back_pressed = True
    else:
        back_pressed = False
        release_back()
 
    if right_report['buttons']['shared']['plus']:
        press_start()
        start_pressed = True
    else:
        start_pressed = False
        release_start()
 
    if right_report['buttons']['shared']['r-stick']:
        press_right_thumb()
        right_thumb_pressed = True
    else:
        right_thumb_pressed = False
        release_right_thumb()
 
    if left_report['buttons']['shared']['l-stick']:
        press_left_thumb()
        left_thumb_pressed = True
    else:
        left_thumb_pressed = False
        release_left_thumb()
 
    if right_report['buttons']['shared']['home']:
        press_guide()
        guide_pressed = True
    else:
        guide_pressed = False
        release_guide()

    right_report = right_joycon.get_status()
    left_report = left_joycon.get_status()

    # Extract raw stick values from reports
    right_stick_x = right_report['analog-sticks']['right']['horizontal']
    right_stick_y = right_report['analog-sticks']['right']['vertical']
    left_stick_x = left_report['analog-sticks']['left']['horizontal']
    left_stick_y = left_report['analog-sticks']['left']['vertical']

    # Apply calibration data formula and sensitivity adjustment
    sensitivity = 1.0
    
      # Adjust this value to change overall sensitivity

    # Adjust sensitivity for each stick's X and Y directions separately
    right_stick_x_sensitivity = sensitivity
    right_stick_y_sensitivity = sensitivity
    left_stick_x_sensitivity = sensitivity
    left_stick_y_sensitivity = sensitivity * 1.0  # Adjust this value to make down direction more sensitive

    # Apply calibration to stick values with adjusted sensitivity
    mapped_right_stick_x = apply_calibration(right_stick_x, right_stick_horizontal_offset, right_stick_x_sensitivity * right_stick_multiplier)
    mapped_right_stick_y = apply_calibration(right_stick_y, right_stick_vertical_offset, right_stick_y_sensitivity * right_stick_multiplier)
    mapped_left_stick_x = apply_calibration(left_stick_x, left_stick_horizontal_offset, left_stick_x_sensitivity * left_stick_multiplier)
    mapped_left_stick_y = apply_calibration(left_stick_y, left_stick_vertical_offset, left_stick_y_sensitivity * left_stick_multiplier)

    # Update vgamepad with mapped values
    gamepad.right_joystick(x_value=mapped_right_stick_x, y_value=mapped_right_stick_y)
    gamepad.left_joystick(x_value=mapped_left_stick_x, y_value=mapped_left_stick_y)

    gamepad.update()

    time.sleep(0.005)
