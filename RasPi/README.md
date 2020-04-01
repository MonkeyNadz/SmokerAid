# SmokerAid - RasPi
This section will long term host the code for the raspberry pi and the thermocouple/relay/fan code, and its interaction with other devices, and the future development 
of the API by which to interact with them (and DB links).
### Installation/Container Build
Build the container - docker build -t <reponame>/<name>:<tag>
 
 e.g.
 
    docker build -t monkeynadz/smokerpi:1
### Running the Container
You just cant run this container as it needs access to GPIO, simplest workaorund is to run with privileged mode docker run --privileged -d <reponame>/<name>:<tag> e.g. 
    docker run --privileged -d monkeynadz/smokerpi:1
