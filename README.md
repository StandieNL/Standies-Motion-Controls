### This project has been replaced by my newer motion control application [BetterJoyMotion](https://github.com/StandieNL/BetterJoyMotion)!

### What is this?
Use fun Wii-style motion controls with Nintendo Joy-Cons in almost any PC game!

The Python scripts allows you to swing your joy-cons to input certain Xbox 360 buttons. For instance, you can set the right joy-con to the main attack button of a game and the left joy-con to the parry button. It is intended for people who want to game in a more physical manner, ideally while standing up instead of sitting down.

It works by setting thresholds for the gyro sensor speed and accelerometer speed on the Joy-Cons. Once one of the thresholds is breached, the assigned button is pressed. Because both gyro and the accelerometer are used, both swiping (rotational) and thrusting (straight) movements are registered.

### How do I use it?

The specific **v0.60.exe release** has the following functions:
- Shake the right joy-con to press the B button.
- Shake the left joy-con to press the A button.
- Hold the SL button on the right joy-con to allow continuous input. This means that you can hold the SL button and propel your right arm around to hold the B button. For instance if you want to charge an attack.
- Buttons, triggers, sticks and rumble are not enabled and require other input methods.

Make sure to download the requirement and connect a pair of Joy-Cons to Windows natively before opening the .exe file.

Right now, this script is only useful when using emulators which allow various various input devices, or when using an input mapper which allows various input devices to be emulated as one device.

_The script can also be adjusted to map motions to different buttons, to change the thresholds (sensitivity) and to change the cooldown after each input. The cooldown is important in preventing accidental inputs._

The **v0.80 script** has the same functions as v0.60 and also maps all Joy-con buttons and triggers to their Xbox 360 counterparts. However, joystick support is semi-broken and rumble isn't implemented at all.

### How do I contribute?

Anyone who wants to help me finish this script or wants my input on creating their own motion control script is very welcome. I am not a programmer or coder. I do not know what I am doing and worked on this script for many months to get this far. While I still suck at coding, I have gained a much better understanding of the possibilities and limitations of the joy-cons. In the end result, there will be various options. Like differentiating between horizontal and vertical motions. Or putting a joy-con in your pocket to detect jumps. To finish it may take me many more months, perhaps even years. But I am passionate about getting it working eventually.

### Requirements:

You need [ViGEmBus](https://github.com/nefarius/ViGEmBus) by [nefarius](https://github.com/nefarius) to run the script.

### Upcoming features (hopefully)

- Joystick support
- Rumble support
- Support three or four joy-cons instead of just two
- Provide a GUI to easily map and configure motion controls, with the option to save and load profiles

### What it looks like in practice:

https://github.com/StandieNL/Standies-Motion-Controls/assets/154834381/f1d1e899-8a0d-4be2-8e87-152f97d8423c

https://github.com/StandieNL/Standies-Motion-Controls/assets/154834381/62ed4cba-2a85-4e95-8e04-1a7bf62da06d


### All credit goes to:

[yannbouteiller](https://github.com/yannbouteiller) for creating [vgamepad](https://github.com/yannbouteiller/vgamepad), which is used in my script to create the virtual gamepad.

[tocoteron](https://github.com/tocoteron) for creating [joycon-python](https://github.com/tocoteron/joycon-python), which is used in my script to get data from the joy-cons.

[nefarius](https://github.com/nefarius) for [ViGEmBus](https://github.com/nefarius/ViGEmBus), which is required to run this script

[tomayac](https://github.com/tomayac) for creating [chrome-dino-webhid](https://github.com/tomayac/chrome-dino-webhid) and helping me understand motion programming a bit better.

[nondebug](https://stackoverflow.com/users/6529658/nondebug) on Stackoverflow for helping me understand vgamepad a little better.

[SuperLouis64](https://github.com/SuperLouis64) for representing the fun of motion controls on [YouTube](https://www.youtube.com/@SuperLouis64).

This code also would not have been possible without ChatGPT.
