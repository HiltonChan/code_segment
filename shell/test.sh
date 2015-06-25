#########################################################################
# File Name: test.sh
# Author: xujianguo
# mail: ray_xujianguo@yeah.net
# Created Time: 2015年06月06日 星期六 22时26分04秒
#########################################################################
#!/bin/bash

for port in {1..65535}; do
	echo >/dev/tcp/www.baidu.com/$port &&
	echo "port $port is open" ||
	echo "port $port is closed"
done
