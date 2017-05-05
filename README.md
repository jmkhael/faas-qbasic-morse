# FaaS QBasic Morse

This repository contains all code required to run a QBasic program as a [FaaS](https://github.com/alexellis/faas) function.

## Building and deploying

1. Build the Docker image.

```
docker build . -t jmkhael/morse
```

2. Ship it to FaaS:

Either via the UI portal, faas-cli.

or via curl:

```
curl localhost:8080/system/functions -d '{
   "service": "morse", 
   "image": "jmkhael/morse", 
   "envProcess": 
   "python handler.py", 
   "network": "func_functions"
  }'
```

3. Run it: `curl -X POST http://localhost:8080/function/morse -d "FaaS-inating!"`.

Now you can talk Morse via QBasic!

```
  ..-. .- .- ...  .. -. .- - .. -. --.
```

Check my blog post for a quick dive into Serverless FaaS:
http://jmkhael.io/serverless-and-on-my-own-servers/

