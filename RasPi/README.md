# SmokerAid - RasPi
This section will long term host the code for the raspberry pi and the thermocouple/relay/fan code, and its interaction with other devices, and the future development 
of the API by which to interact with them (and DB links).
### Container Build
Build the container as normal.
 
    docker build -t <reponame>/<name>:<tag>
 
 e.g.
 
    docker build -t monkeynadz/smokerpi:1

Main thing to note - is that the dependencies won't be picked up unless you build in a raspberry pi, tried building within another RasPi container being deployed elsewhere but no dice.

### Running the Container Locally
You just cant run this container as it needs access to GPIO, simplest workaorund is to run with privileged mode as below:

    docker run --privileged -d <reponame>/<name>:<tag> 

e.g. 

    docker run --privileged -d monkeynadz/smokerpi:1

### Setting up Docker Engine for remote access
Follow the instructions [here](https://docs.docker.com/install/linux/linux-postinstall/), which include configuring systemd to expose the docker on a given port, i did so by editing the systemd file.

Best practice is to follow the securing your connection steps - i.e. adding certificates to the socket.


### Terraform 
Mostly default Terraform commands - just worth noting that due to the requirement to access the GPIO pins - the docker container needs to be run in privileged mode.

I'd also set up a workspace per folder - believe thats a half decent practice to limit scope impact - but yet to learn properly.

If you havent completed the securing connections - then you should be able to navigate to the RasPi folder - and after cloning or adding a new file - hit it with a:

    terraform init
    
Then you can stage the changes and view what will update.
    
    terraform plan
    
When you're happy to run it - use the below
    
    terraform apply
    

   
