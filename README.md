# FaaS QBasic Morse

This repository contains all code required to run a QBasic program as a [FaaS](https://github.com/alexellis/faas) function.

## Building and deploying

1. Build the Docker image.

```
docker build . -t jmkhael/faas-qbasic-morse
```

2. Ship it to FaaS:

Either via faas-cli:

```
git clone https://github.com/alexellis/faas-cli
cd faas-cli/
go get -d -v
go build

./faas-cli -action=deploy \
   -image=jmkhael/faas-qbasic-morse \
   -name=morse \
   -lang=python
```

or via curl:

```
curl localhost:8080/system/functions -d '{
   "service": "morse",
   "image": "jmkhael/faas-qbasic-morse",
   "envProcess": "python handler.py",
   "network": "func_functions"
  }'
```
or via the UI portal: http://localhost:8080

3. Run it: `curl -X POST http://localhost:8080/function/morse -d "FaaS-inating!"`.

Now you can talk Morse via QBasic!

```
  ..-. .- .- ...  .. -. .- - .. -. --.
```

Check my blog post for a quick dive into Serverless FaaS:
http://jmkhael.io/serverless-and-on-my-own-servers/
