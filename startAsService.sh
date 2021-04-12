#!/bin/bash
cp bashapi.service /etc/systemd/system/
systemctl start bashapi.service
systemctl enable bashapi.service