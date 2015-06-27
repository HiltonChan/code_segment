###有关网络方面的命令

####netstat -i
&nbsp;&nbsp;&nbsp;&nbsp;提供网络接口的信息.
```shell
xujianguo@guo:~/github/code_segment/shell/network$ netstat -i
Kernel Interface table
Iface   MTU Met   RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0       1500 0    143286      0      1 0         80006      0      0      0 BMRU
lo        65536 0      3170      0      0 0          3170      0      0      0 LRU
vmnet1     1500 0         0      0      0 0            75      0      0      0 BMRU
vmnet8     1500 0         0      0      0 0            75      0      0      0 BMRU
wlan0      1500 0      7988      0      0 0          6925      0      0      0 BMRU
```

####netstat -r
&nbsp;&nbsp;&nbsp;&nbsp;展示路由表，也是另一种确定接口的方式，它还给出了路由器的默认地址。
```shell
xujianguo@guo:~/github/code_segment/shell/network$ netstat -r
内核 IP 路由表
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         10.10.115.65    0.0.0.0         UG        0 0          0 eth0
10.10.115.64    *               255.255.255.192 U         0 0          0 eth0
10.42.0.0       *               255.255.255.0   U         0 0          0 wlan0
172.16.159.0    *               255.255.255.0   U         0 0          0 vmnet1
192.168.142.0   *               255.255.255.0   U         0 0          0 vmnet8
```

####ifconfig eth0
&nbsp;&nbsp;&nbsp;&nbsp;根据网络接口名字，展示详细信息
```shell
xujianguo@guo:~/github/code_segment/shell/network$ ifconfig eth0
eth0      Link encap:以太网  硬件地址 5c:f9:dd:48:b6:18
          inet 地址:10.10.115.95  广播:10.10.115.127  掩码:255.255.255.192
          inet6 地址: fe80::5ef9:ddff:fe48:b618/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:151843 错误:0 丢弃:1 过载:0 帧数:0
          发送数据包:85983 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000
          接收字节:109657684 (109.6 MB)  发送字节:12668158 (12.6 MB)
          中断:16
```



