provider "docker" {
#    cert_path = "./certs/"
    host = "tcp://pi@192.168.0.24:2375"
}

resource "docker_container" "SmokerAid" {
    image = "monkeynadz/smokerpi:latest"
    name = "tfSmokerAid"
    privileged = true
}

