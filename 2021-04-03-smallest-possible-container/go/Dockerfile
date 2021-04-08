### First Stage ###
FROM golang:1.14 as builder
COPY . .
RUN go build -ldflags \
  "-linkmode external -extldflags -static" \
  -a server.go

### Second Stage ###
FROM scratch
COPY --from=builder /go/server ./server
COPY index.html index.html
CMD ["./server"]