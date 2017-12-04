#
# Connects to the instrument at an address and port and obtains the instrumnet 
# identification.
# 
# usage ./instrument-hello.sh IP PORT
#

#!/bin/bash

ADDRESS=$1
PORT=$2

COMMAND=''
(
echo open "$ADDRESS $PORT"
sleep 2
echo "*IDN?"
sleep 2
) | telnet

