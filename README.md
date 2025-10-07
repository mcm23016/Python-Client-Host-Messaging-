# Overview

I originally wanted to write a networking program that would allow me to connect with another computer. At first I thought I was going to go with a Peer-to-Peer architecture, but ended up switching to a client-host architecture. I also decided to work in python as the more I researched about networking, the more complex I realized it was. This program is just the surface of networking. I don't have much experience with network security, so I made my server only open locally (127.0.0.1). In the future I would like to learn how to make it secure and less vaulnerable to malicious attacks.

[Software Demo Video](https://youtu.be/2a7zYqaNL9A)

# Network Communication

This program uses client-host architecture. It is hardcoded to use 127.0.0.1 (An IP address that only allows the same machine to connect) and port 65432 (This can change. Just make sure to pick something higher than 1024 and that is not already being used.) Messages are sent as bytes of information, decoded, and displayed as simple strings.

# Development Environment

I used Visual Studio code to write code and the widows terminal to run my program files.

I used the socket and threading libraries. Socket allows you to connect to other computers and threading allows you to do multiple things concurrently. 

# Useful Websites

* [Geeks for Geeks: Client or P2P server]([http://url.link.goes.here](https://www.geeksforgeeks.org/computer-networks/difference-between-client-server-and-peer-to-peer-network/#))
* [Python Socket Library]([http://url.link.goes.here](https://docs.python.org/3.6/library/socket.html))

# Future Work

* Security
* GUI
* More types of data to send
