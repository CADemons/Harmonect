<p align="center">
    <img src="https://raw.githubusercontent.com/CADemons/Harmonect/master/logo/logo.pngg"/>
</p>

Harmonect is `________`. It is currently in it's alpha phase of development. 

Harmonect makes use of the freenect python library, python-mingus, and an Xbox 360 Kinect to emulate "musical stairs" or other musical pathway. Harmonect is intended to be optimized to run on a Raspberry Pi with no delay or sound issues, however, with some configuration, Harmonect could be run on almost any system.

Thoroughly tested systems include:
- macOS

Currently, Harmonect is meant to be a standalone application. However, in the future, it could be used with other libraries.

# Requirements
1. Python 2.7 and Pip
2. freenect
3. An Xbox 360 Kinect
4. A "Microsoft Xbox 360 Kinect Sensor USB AC Adapter Power Supply Cable Cord"
5. (Optional) Raspberry Pi

## Getting Stared
1. Clone the repository: `$ git clone https://github.com/CADemons/kinect-musical-stairs.git`
2. Navigate to the cloned folder: `$ cd kinect-musical-stairs`
3. Install the dependencies: `$ pip install -r requirements.txt`
4. Clone `settings-template.ini` to `settings.ini` 
5. Edit `settings.ini` with your preferences
6. Run `musical_stairs.py` 
