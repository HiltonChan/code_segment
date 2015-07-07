<?php
/**
 * User: xujianguo
 * Mail: xujianguo@4399.com
 * Date: 2015/7/5
 * Time: 22:39
 */

/**
 * Class User
 * Usage:用户类
 */
class User {
    //用户名
    private $name = null;
    //密码
    private $password = null;

    /**
     * 构造方法
     * @param $name 用户名
     * @param $password 密码
     */
    public function __construct($name, $password) {
        $this->name = $name;
        $this->password = $password;
    }

    /**
     * @return null|用户名
     */
    public function getName() {
        return $this->name;
    }

    /**
     * @return null|密码
     */
    public function getPassword() {
        return $this->password;
    }
}

/**
 * Class DBMessage
 * Usage:数据库基本常量的封装类
 */
class DBMessage {
    const host = "127.0.0.1";
    const username = "root";
    const password = "root";
    const db = "php_db";
    const port = 3306;
}

//从POST请求中中解析参数的值
$user_name = $_POST['user_name'];
$user_password = $_POST['user_password'];

//将参数对应到User类中
$user = new User($user_name, $user_password);

//数据库操作
//实例化MYSQL操作类
$connection = new mysqli();
//连接数据库
$connection->connect(DBMessage::host, DBMessage::username, DBMessage::password, DBMessage::db, DBMessage::port);
//判断数据是否连接不到
if($connection->connect_error) {
    echo "数据库连接不上，连接错误为：",$connection->connect_error;
    exit;
}
//插入SQL
$insert_sql = "insert into user values(?, ?)";
//使用预处理
$statement = $connection->prepare($insert_sql);
//绑定参数
$statement->bind_param("ss", $user->getName(), $user->getPassword());
//执行
$statement->execute();
//获取影响行数
$result = $statement->affected_rows;
//关闭有关数据库连接
$statement->close();
$connection->close();

//处理返回结果
if($result == 1) {
    echo "true";
} else {
    echo "false";
}