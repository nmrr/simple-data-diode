# simple-data-diode
A simple data diode that allows data to travel in only one direction in the network


Data diodes are often used in isolated systems to transfer data securely from outside to inside and vice versa by using a single direction flow.
A server can send data to a client and the client will never communicate with the server. The server will never know if the client has received all data (there is no acknowledgment from the client). **UDP** socket is used to transfer data in the network and chuck of data are send several times to compensate loss of data.


More information: https://en.wikipedia.org/wiki/Unidirectional_network


Keep in mind this **data diode** is a **toy**, performance is really poor but the diode works !


**Python 3** is required. There is no dependency.

**On client side:**

Launch the client:
```
python3 client.py
```


**On server side:**

Create a 20MB random file:
```
dd if=/dev/urandom of=output.txt bs=1M count=20
```

Launch the server:
```
python3 server.py
```

**Port** and **binding address** can be modified easily in the header of scripts. Progression will be shown on client/server sides.