#!/bin/bash/

echo "Insatall R"

apt install dirmngr apt-transport-https ca-certificates software-properties-common gnupg2

apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'

add-apt-repository 'deb https://cloud.r-project.org/bin/linux/debian stretch-cran35/'


apt update

apt install r-base

echo "END R Insatall"


