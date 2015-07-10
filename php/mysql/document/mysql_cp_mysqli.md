## mysql和mysqli的比较 ##
###连接Demo
**mysql的连接**
<!-- lang: -->
	<?php
	/**
	 * User: xujianguo
	 * Mail: xujianguo@4399.com
	 * Date: 2015/7/9
	 * Time: 14:35
	 */
	//连接数据库
	$link = mysql_connect('192.168.137.222', 'root', 'xujianguo') or die('connect fail'.mysql_error());
	echo 'connect successfully'."<br>";
	//选择表
	mysql_select_db('php_db') or die('select fail');
	//SQL语句
	$query = 'select * from test';
	//获取结果
	$result = mysql_query($query) or die('query fail:'.mysql_error());
	//迭代结果
	while($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
	    foreach($line as $colName => $colValue) {
	        echo $colName."=>".$colValue."<br>";
	    }
	}
	//关闭资源
	mysql_free_result($result);
	mysql_close($link);

**mysqli的连接**
<!-- lang: -->
	<?php
	/**
	 * User: xujianguo
	 * Mail: xujianguo@4399.com
	 * Date: 2015/7/9
	 * Time: 14:36
	 */
	$link = new mysqli();
	//连接数据库
	$link->connect('192.168.137.222', 'root', 'xujianguo', 'php_db', 3306);
	//SQL语句
	$query = 'select * from test';
	//获取结果
	$result = $link->query($query);
	//迭代结果
	while($line = $result->fetch_array(MYSQLI_ASSOC)) {
	    foreach($line as $colName => $colValue) {
	        echo $colName."=>".$colValue."<br>";
	    }
	}
	//关闭资源
	$result->free();
	$link->close();
**pdo的连接**
<!-- lang: -->
	<?php
	/**
	 * User: xujianguo
	 * Mail: xujianguo@4399.com
	 * Date: 2015/7/10
	 * Time: 11:42
	 */
	//连接数据库
	$link = new PDO('mysql:host=192.168.137.222;dbname=php_db', 'root', 'xujianguo');
	//查询
	$result = $link->query('select * from test');
	//迭代结果
	foreach($result as $value) {
	    print_r($value);
	}
	$link = null;

### 三种方式的比较 ###
<table>
  <thead>
    <tr>
      <th></th>
      <th>mysql</th>
      <th>mysqli</th>
      <th>pdo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>prepare语句的支持</td>
      <td>否</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>存储过程的支持</td>
      <td>否</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>多语句执行的支持</td>
      <td>否</td>
      <td>是</td>
      <td>大多数</td>
    </tr>
	<tr>
      <td>MySQL4.1以上功能的支持</td>
      <td>否</td>
      <td>是</td>
      <td>大多数</td>
    </tr>
	<tr>
      <td>是否面向对象</td>
      <td>否</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>支持持久连接</td>
      <td>是</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>事务的支持</td>
      <td>否</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>API对字符集的支持</td>
      <td>是</td>
      <td>是</td>
      <td>是</td>
    </tr>
	<tr>
      <td>推荐</td>
      <td>候选</td>
      <td>首选</td>
      <td>次选</td>
    </tr>
  </tbody>
</table>
