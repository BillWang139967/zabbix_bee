#########################################################################
# File Name: install.sh
# Author: Bill
# mail: XXXXXXX@qq.com
# Created Time: 2016-07-06 09:30:34
#########################################################################
#!/bin/bash
cp -rf ./zabbix_bee  /opt/
ln -s /opt/zabbix_bee/zabbix_bee.py /usr/bin/zabbix_bee
chmod 777 /usr/bin/zabbix_bee
mkdir -p /var/spool/cron
if [  -f /var/spool/cron/root ]
then
    CHECK=`cat /var/spool/cron/root | grep zabbix_bee | wc -l`
    if [ ${CHECK} == 0 ]
    then
        echo "1 1 * * * /usr/bin/zabbix_bee -d" >> /var/spool/cron/root
    fi
else
    echo "1 1 * * * /usr/bin/zabbix_bee -d" >> /var/spool/cron/root
fi
