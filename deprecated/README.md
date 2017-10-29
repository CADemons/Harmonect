<p align="center">
    <img src="https://raw.githubusercontent.com/CADemons/Harmonect/master/deprecated/logo/logo.png"/>
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
### Installation (Mac)
1. Install Homebrew and OpenCV using steps 1 through 4 [here](http://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/). If you already have Xcode, Homebrew, and homebrewed Python 2.7 installed, you can skip steps 1 through 3.
2. Install libfreenect using Homebrew: `$ brew install libfreenect`
3. Install fluidsynth using Homebrew: `$ brew install fluidsynth pkg-config`
4. Clone the repository: `$ git clone https://github.com/CADemons/Harmonect.git`
5. Navigate to the cloned folder: `$ cd Harmonect`
6. Install the Python dependencies: `$ pip install -r requirements.txt`, `$ cd ..`
7. Download the libfreenect Python files: `$ git clone https://github.com/OpenKinect/libfreenect.git`
8. Install the libfreenect Python module: `$ cd libfreenect/wrappers/python/`, `$ sudo python setup.py install`, `$ cd ../../..`
9. Continue to "Configure and Run"

### Installation (Raspberry Pi Raspbian)
1. Install the dependencies using the instructions [here](http://blog.tunpixel.tn/2014/10/27/kinect-rasp/)
2. Clone the repository: `$ git clone https://github.com/CADemons/Harmonect.git`
3. Navigate to the cloned folder: `$ cd Harmonect`
4. Install the Python dependencies: `$ pip install -r requirements.txt`, `$ cd ..`
5. Continue to "Configure and Run"

### Configure and Run (All Platforms)
1. Navigate to the Harmonect folder: `$ cd Harmonect`
2. Clone `settings-template.ini` to `settings.ini` 
3. Edit `settings.ini` with your preferences
4. Run `$ sudo python musical_stairs.py` 
