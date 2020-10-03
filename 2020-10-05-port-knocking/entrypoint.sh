#!/bin/sh
# NOTE: Docker opens up port 8888 because I am port forwarding
# to it in my docker run command so I have to reclose it here
/sbin/iptables -A INPUT -p tcp --dport 8888 -j DROP & \
knockd & \
python -m http.server 8888
