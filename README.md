# gpio

bash、shell下的操控GPIO的脚本。



以orangepi为例，首先让其可执行：
```
chmod +x ./power_orangepi.sh
```

让GPIO2点亮LED

```
./power_orangepi 2 1
```

关闭LED

```
./power_orangepi 2 0
```



以raspberrypi为例，首先让其可执行：
```
chmod +x ./power_raspberrypi.sh
```

让GPIO2点亮LED

```
./power_raspberrypi 2 1
```

关闭LED

```
./power_raspberrypi 2 0
```
