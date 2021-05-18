# drinknow
喂！三点几嚟！饮下水先！

## Linux
执行`crontab -e`  
添加以下语句，your_path换成你的drink.py文件路径  
`*/10`是每隔十分钟
```shell
*/10 * * * * python /your_path/drink.py
```
## Windows
自行添加定时任务
