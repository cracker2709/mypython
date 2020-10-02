# mypython
# goRest

- Get docker image with

```shell script
docker pull cracker2709/mypython-utils
```
- Run if with
```shell script
docker run -p 5000:5000 cracker2709/mypython-utils:latest
```
Install it quickly on a kubernetes cluster
```
# Launch a temporary pod which will be destroyed when exiting the session
kubectl run tmp-pyp-pod --rm -i --tty --image cracker2709/mypython-utils:latest --namespace <your_namespace>


- test it locally with python 3
```
pip3 install Flask
python3 src/main.py
```

- browse
```
http://localhost:5000/
``` 
