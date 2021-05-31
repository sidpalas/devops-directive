# Port Knocking (Network Security Technique) Explained and Demoed in 5 Minutes!

Video: https://youtu.be/IBR3oLqGBj4

## Test setup

A container running:

1) Python `http.server` on port 8888
2) [knock](https://linux.die.net/man/1/knockd) 

## To see it in action

```
make build
make run

make test # curl will timeout

make unlock

make test # <h1>Hello from the webserver!</h1>

make lock

make test # curl will timeout
```

More commonly, knockd would be configured to unlock a port for a specified period of time before automatically closing it again.

