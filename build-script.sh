#! /bin/zsh
docker context use default
cd nginx
docker build -t ghcr.io/goodvibes-org/gv_xml_ui/nginx-proxy .
docker push ghcr.io/goodvibes-org/nginx-proxy
cd .. 
docker build -t ghcr.io/goodvibes-org/gv_xml_ui/app .
docker push ghcr.io/goodvibes-org/gv_xml_ui/app
cd ../gv_xml
docker build -t ghcr.io/goodvibes-org/gv_xml_ui/calculator .
docker push ghcr.io/goodvibes-org/gv_xml_ui/calculator

