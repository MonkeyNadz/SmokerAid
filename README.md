

# SmokerAid

DIY electronics solution for helping maintain stable temps when smoking meat on the Weber Smokey Mountain (WSM). Initially this is only going to be for pit temps at one or more locations but potentially for internal temps much like a standard iGrill would do.  Long term my hopes and dreams would be for this to be an iGrill with the ability to alter the pit temp automatically and apply analytics and learning to cooks.

## Status and Planned Features 

Very much a work in progress - and something I'm doing for fun - I'll update this as I complete parts.

 1. 12V and 5V Power Circuitry
 2. Basic Raspberry Pi Setup
 3. Wiring and Basic Thermocouple Testing
 4. Fan Control with Relay
 5. Temp Change Triggering Fan On/Off 
 6. Bringing it Together on the CLI.

Subject to time and the above being successful - I'm looking to add what I think would be some cool features - to help with my hobby as well as hone some skills with some fun tech.

 - Web GUI to control temps
 - Adding Internal Meat Probes
 - Log Storage and Analytics
 - Linking Temps to Weather 
 - Applying Learning
	 - Time to Temp - both when starting cooks but also if you want to change temp mid cook -  taking into account external factors such as weather.
	 - Cooked At - providing estimations based on pit, meat internal and weather temperatures to estimate when a piece of meat will reach the correct temp.
 - 

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

## Software Dependencies
I'm of course going to be leveraging some libraries  - and some key ones below:

### Python Libraries

#### Adafruit_CircuitPython_MAX31856

Reference [here](https://github.com/adafruit/Adafruit_CircuitPython_MAX31856), provides a simple library for querying the thermocouple amplifier - note that this requires the SPI interface to be enabled - reference to enable it  [here](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).

