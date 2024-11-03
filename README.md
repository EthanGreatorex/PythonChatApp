# PythonChatApp

## Live demo
Here is a video displaying the chat application running on my personal machine
https://youtu.be/XCFPc38gCDg


## About
The goal of this app is to create a local network chatting application. 
The first iteration will be using a command line inteface.
I want to further develop this to use a GUI using the module Tkinter.

## Modules Used
The python module sockets was used to handle connections between the client and server and to allow for broadcasting of messages.
Threading module was used to allow for multiple clients to connect to the server, and send messages simultaneously.
DateTime module is used to show the time of when the message was sent by the user. Queue module is used to be able to execute processes 
on the correct thread when needed. 

## CLI Progress
This reason behind the command line interface version of this application was to understand how the Sockets module works & the connection between the client and server.
The overall experience messaging using the CLI is not enjoyable and lacks readability and proper formatting.

### Current design of the command line interface version


![Screenshot 2024-10-24 084514](https://github.com/user-attachments/assets/9933941b-7edb-46f2-8104-810a5160dada)

## GUI Progress
The creation of a usable user interface will be created using the Tkinter module. The user will have a simple to use interface for sending and viewing messages.
Functionality goals:
- Save and reload chat history on application restart
- Remove any un-neccessary information about the server connection from the user and maintain simplisity
- Display messages in a clear and undersandable way

### Initial design of the application in its early stage
![image](https://github.com/user-attachments/assets/dedc1329-1ee9-417b-8668-1cd12a18e8a7)

### The final design
![image](https://github.com/user-attachments/assets/ffce20a0-ea3e-419f-a587-548ec512feda)
![image](https://github.com/user-attachments/assets/38b0fa9d-096e-42b9-b2bd-bf7927232df2)
