#!/usr/bin/env bash
#stop the service after execute
sed -i "s/8080/80/g" /etc/nginx/sites-enabled/default
sudo pkill -1 -f '/usr/sbin/nginx'
