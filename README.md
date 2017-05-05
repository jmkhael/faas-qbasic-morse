# FaaS QBasic Morse

This repository contains all code required to run a QBasic program as a [FaaS]() function.

## Building and deploying

1. Build the Docker image.

```
docker build . -t jmkhael/morse
```

2. Publish it to DockerHub, e.g. as `jmkhael/morse`.

3. Ship it to FaaS:

```
curl localhost:8080/system/functions -d '
{"service": "morse", "image": "jmkhael/morse", "envProcess": "python handler.py", "network": "func_functions"}'
```

4. Run it: `curl -X POST http://localhost:8080/function/morse -d "FaaS-inating!"`.

```
..-. .- .- ...  .. -. .- - .. -. --.
```

