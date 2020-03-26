

# SmokerAid

DIY electronics solution for helping maintain stable temps when smoking meat on the Weber Smokey Mountain (WSM). Initially this is only going to be for pit temps at one or more locations but potentially for internal temps much like a standard iGrill would do.  Long term my hopes and dreams would be for this to be an iGrill with the ability to alter the pit temp automatically and apply analytics and learning to cooks.

## Installation
As the code is python only - I create a virtualenv, and then clone the code within it, then install dependencies within that using pip. n.b. some requirements may be raspberry pi specific.

    python3 -m venv <venv-name>
    source <venv-name>/bin/activate
    pip install -r path/to/requirements.txt

Here I use the venv package instead of virtualenv, as I don't need the flexibility of specifying a python version yet, and this allows me to execute the code without having to execute it as python3 due to the venv only having visibility of python3.

Keep your environment clean - and detach from it when you're not using it to prevent erroneously adding unwanted packages. do so by executing the below in the terminal.

    deactivate

As of now that's all you have to do to fetch dependencies,! Hopefully it doesn't get much more complicated

### Running the Python Code

If you're within the virtual environment from the install - then you're goed to just execute the scripts as you'd normally do, example as below:

    python ThermocoupleTest.py

Hopefully this'll get far more interactive over time

## Status and Planned Features

Very much a work in progress - and something I'm doing for fun - I'll update this as I complete parts.

 1. 12V and 5V Power Circuitry - Complete
 2. Basic Raspberry Pi Setup - Complete
 3. Wiring and Basic Thermocouple Testing - Complete
 4. Fan Control with Relay
 5. Temp Change Triggering Fan On/Off
 6. Bringing it Together on the CLI.
 7. Designing Enclosure
 8. 3D Printing and Mounting Solution.

Subject to time and the above being successful - I'm looking to add what I think would be some cool features - to help with my hobby as well as hone some skills with some fun tech.

 - Web GUI to control temps
 - Adding Internal Meat Probes
 - Log Storage and Analytics
 - Linking Temps to Weather
 - Applying Learning
	 - Time to Temp - both when starting cooks but also if you want to change temp mid cook -  taking into account external factors such as weather.
	 - Cooked At - providing estimations based on pit, meat internal and weather temperatures to estimate when a piece of meat will reach the correct temp.

## Hardware Components
This isn't a software solution - and is going to be mounted onto a WSM - needing some control circuitry as well as some mains attached power circuits... please do not mess about with this if you're not comfortable with electronics. If you are in doubt or do not have prior experience - please contact an electrician for assistance.

 - Raspberry Pi Zero W
	 - Small and low power,
 - Adafruit MAX31856 Thermocouple Amplifier
 - K Type Thermocouple
 - Centrifugal Fan with CFM over 10.
	 - Using the Sunon - -   PMB1275PNB1-AY(2).GN
- 5V Relays
	- Using - "SRD-05VDC-SL-C" based chips, they can handle the current we need here whilst being 5V control - simple enough for the Raspberry Pi to control.
 - Power Supply
	 - Using Mean Well  32W 5V/12V dc switch mode PSU ( SKU - RD-35A)
	 - I've also added a kettle lead adapter to make the wiring safer, it also has a dedicated on/off switch for ease of use.

### Thermocouple wiring
Specific Thermocouple wiring instructions found [here](https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier/python-circuitpython#python-computer-wiring-5-5)

## Software Dependencies
I'm of course going to be leveraging some libraries  - and some key ones below:

### Python Libraries
n.b. Python 3.7 was been used for testing - your mileage may vary.

#### Adafruit_CircuitPython_MAX31856
Installation will be done via the install of requirements.txt Dependencies, but if that fails, the reference is above will point you in the right direction.

Reference [here](https://github.com/adafruit/Adafruit_CircuitPython_MAX31856), provides a simple library for querying the thermocouple amplifier - note that this requires the SPI interface to be enabled - reference to enable it  [here](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).
