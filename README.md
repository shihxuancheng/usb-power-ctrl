# usb-power-ctrl

## Run

### A. control the usb power per-port on raspberry pi

1. list the status of all supported usb hub

```shell
$ uhubctl
```

2. cut the power of port2 of the usb hub 2

```shell
$ uhubctl -l 2 -a off -p 2
```

### B. run the python script in background

1. using the `nohup` command to start

```shell
(venv)$ nohup python -u main.py &
```

2. find the process id

```shell
(venv)$ ps ax | grep main.py
```

3. terminate the background process

```shell
(venv)$ kill $PID
```

## Reference

- https://github.com/mvp/uhubctl
- https://www.twblogs.net/a/5cb6cb69bd9eee0f00a1e039
