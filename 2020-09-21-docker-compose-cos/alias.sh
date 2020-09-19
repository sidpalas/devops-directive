echo alias docker-compose="'"'docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:$PWD" \
    -w="$PWD" \
    cryptopants/docker-compose-gcr@sha256:a59f0d61e424e52d3fed72a151241bfe6f4f4611f2e4f5e928ef4eeb47662a54'"'" >> ~/.bashrc; \
source ~/.bashrc;