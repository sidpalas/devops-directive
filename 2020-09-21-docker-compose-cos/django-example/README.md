# Docker-compose on container optimized OS

## Customizing Makefile

Replace `PROJECT_ID` and `USER` to match your GCP project id and username

## Creating Static IP address and VM

`make create-static-ip && make create-vm`

## Deleting when done (so you dont keep getting charged)

`make delete-vm` --> `y`
`make delete-static-ip` -> `y`

## SSH onto VM:

`make ssh`

---

## Django docker-compose example

### link

https://docs.docker.com/compose/django/
