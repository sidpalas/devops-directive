build:
	docker build -t port-knock-demo .

run:
	docker run -d \
	  --rm --privileged \
		-p 8000:8000 \
		-p 7000:7000 \
		-p 9000:9000 \
		-p 8888:8888 \
		--name port-knock-demo \
		port-knock-demo

unlock:
	-telnet 127.0.0.1 7000
	-telnet 127.0.0.1 8000
	-telnet 127.0.0.1 9000

lock:
	-telnet 127.0.0.1 9000
	-telnet 127.0.0.1 8000
	-telnet 127.0.0.1 7000

test:
	curl -m 1 127.0.0.1:8888

view-logs:
	docker exec port-knock-demo cat /var/log/knockd.log