#!/usr/bin/env bash
# add header http in gninx server

exec { 'add_header':
  command  => 'sudo apt-get update;
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
  sudo service nginx restart',
  provider => 'shell',
}
