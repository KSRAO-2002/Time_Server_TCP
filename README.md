# Time_Server_TCP
Program reads time from reference clock, distributes it to clients via network. Uses pytz library for timezones to return time/date of specified country/city. Server code creates database for client requests, returns time based on request. TCP connection disconnects after last response.

Time Server TCP
Time Server TCP is a simple program written in Python that allows clients to connect to the server over TCP and receive the current date and time in the format "YYYY-MM-DD HH:MM:SS". This program can be useful in situations where clients need to synchronize their clocks with a reliable time source.

Installation
To use the Time Server TCP program, you will need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can download the Time Server TCP program from the GitHub repository: https://github.com/KSRAO-2002/Time_Server_TCP

Usage
To run the Time Server TCP program, navigate to the directory where the program is saved and execute the following command: "python time_server_tcp.py"

This will start the time server and it will begin listening for incoming connections on port 9999.

To test the time server, you can use the included client program by executing the following command: "python time_client_tcp.py"

This will connect to the time server and print the current date and time in the expected format.

Customization
If you want to customize the behavior of the time server, you can modify the source code in the time_server_tcp.py file. For example, you can change the port number that the server listens on or modify the format of the date and time string that is returned to clients.

Error Handling
The Time Server TCP program includes error handling to handle potential issues that may arise during execution. If an error occurs, the program will print an error message to the console and exit gracefully.

Conclusion
The Time Server TCP program provides a simple implementation of a time server using TCP sockets in Python. This program can be used as a starting point for more complex time synchronization applications, or as a reliable time source for other networked devices.

