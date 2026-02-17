#!/bin/bash

APP_NAME="RGBController"
INSTALL_DIR="/opt/$APP_NAME"
BIN_NAME="led_controller"

echo "Uninstalling $APP_NAME..."

sudo rm -rf $INSTALL_DIR
sudo rm -f /usr/local/bin/$BIN_NAME
sudo rm -f /usr/share/applications/rgb-controller.desktop

echo "Uninstalled successfully."
