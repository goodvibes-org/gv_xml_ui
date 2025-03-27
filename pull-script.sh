#! /bin/bash
docker context use vps-calculator
docker pull ghcr.io/goodvibes-org/nginx-proxy:latest
docker pull ghcr.io/goodvibes-org/gv_xml_ui/app:latest
docker pull ghcr.io/goodvibes-org/gv_xml_ui/calculator:latest

