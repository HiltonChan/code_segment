## MySQL的binlog ##

### 什么是binlog ###
binlog是日志系统中的一种，主要用于记录所有更新了的数据的所有SQL语句。

### binlog的作用 ###
- 用于备份
- 用于恢复数据库
- 用于主从复制

### 查看binlog ###
查看MySQL中binlog的名字和大小
<pre><code>
mysql> show binary logs; 
+------------------+-----------+
| Log_name         | File_size |
+------------------+-----------+
| mysql-bin.000001 |     19758 |
| mysql-bin.000002 |    765307 |
| mysql-bin.000003 |       691 |
| mysql-bin.000004 |       125 |
| mysql-bin.000005 |       125 |
| mysql-bin.000006 |       360 |
| mysql-bin.000007 |       557 |
| mysql-bin.000008 |       125 |
| mysql-bin.000009 |       125 |
| mysql-bin.000010 |      2169 |
| mysql-bin.000011 |      6207 |
| mysql-bin.000012 |       125 |
| mysql-bin.000013 |       106 |
+------------------+-----------+
13 rows in set (0.00 sec)
</code></pre>

查看binlog的具体内容
<pre><code>
[root@ /]# mysqlbinlog /var/lib/mysql/mysql-bin.000001 | more
</code></pre>

### 解读binlog内容 ###
抽取一条记录出来
<pre><code>
/*!*/;
# at 256
#150708  9:05:33 server id 1  end_log_pos 403   Query   thread_id=35    exec_time=0     error_code=0
SET TIMESTAMP=1436317533/*!*/;
UPDATE `message` SET `name`='吊炸天', `content`='我想静静' WHERE (`id`='2')
</code></pre>
格式</br>

- at 256表示的是位置，位于文件中的位置，说明了记录的起点是第256个字节
- 150708  9:05:33表示事件发生的时间戳
- server id是服务器标志
- Query表示的是查询
- thread_id是表示执行线程id
- exec_time=0表示事件执行的时间
- error_code是错误码标志

### binlog的使用 ###
查看binlog的状态
<pre><code>
mysql> show variables like '%log_bin%';
+---------------------------------+-------+
| Variable_name                   | Value |
+---------------------------------+-------+
| log_bin                         | ON    |
| log_bin_trust_function_creators | OFF   |
| log_bin_trust_routine_creators  | OFF   |
| sql_log_bin                     | ON    |
+---------------------------------+-------+
4 rows in set (0.00 sec)
</code></pre>

binlog的存储位置
<pre><code>
mysql> show variables like '%datadir%';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| datadir       | /var/lib/mysql/ |
+---------------+-----------------+
1 row in set (0.00 sec)
</code></pre>

查看binlog里面的event事件
<pre><code>
mysql> show binlog events in 'mysql-bin.000011';
+------------------+------+-------------+-----------+-------------+--------------------------------------------------------------------------------------------------------------------------------+
| Log_name         | Pos  | Event_type  | Server_id | End_log_pos | Info                                                                                                                           |
+------------------+------+-------------+-----------+-------------+--------------------------------------------------------------------------------------------------------------------------------+
| mysql-bin.000011 |    4 | Format_desc |         1 |         106 | Server ver: 5.1.73-log, Binlog ver: 4 
</code></pre>

### binlog的三种模式 ###
**第一种：Statement Level模式**<br>
简介：每一条会产生修改效果的SQL都会记录到master的binlog中，slave在复制的时候会解析成原来master执行过的语句来执行。<br>
优点：不需要记录每一行数据的变化，减少了binlog的日志量<br>
缺点：不同版本的MySQL对SQL的支持在复制执行的时候容易出现问题<br>

**第二种：Row Level模式**<br>
简介：对每行记录都记录被修改后的格式，然后在salve端对对应的行进行修改。<br>
优点：清楚记录了每行记录的变化，兼容性好，不会因为一些function或者trigger的调用而出现无法复制的问题。<br>
缺点：日志量大<br>

**第三种：Mixed模式**<br>
简介：根据执行的每一条具体的sql语句来区分对待记录日志的形式<br>

**模式的设置**
<pre><code>
set session binlog_format = 'statement';
set session binlog_format ='row';
set session binlog_format ='mixed';
</code></pre>

**应用场景**<br>
**Statement模式**：对于很大日志量的数据库的时候，若采用Row模式，会导致日志膨胀，传输时间也会变长，这是采用Statement模式适合。<br>
**Row模式**：若存在SQL是跨库操作的，会导致库之间的数据不一致，使用Row模式可以避免执行SQL，从记录的角度去保证一致性。<br>
**Mixed模式**:一般都采用这个模式，但是对于上述两种特别的情况，需要去选择一种。<br>


