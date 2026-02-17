#!/bin/bash

APP_NAME="RGBController"
INSTALL_DIR="/opt/$APP_NAME"
BIN_NAME="led_controller"
ICON_NAME="led-light.png"

echo "Installing $APP_NAME..."

# Require sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo ./install.sh"
  exit
fi

# Create install directory
mkdir -p $INSTALL_DIR

# Copy files
cp dist/$BIN_NAME $INSTALL_DIR/
cp $ICON_NAME $INSTALL_DIR/

# Make executable
chmod +x $INSTALL_DIR/$BIN_NAME

# Create global shortcut command
ln -sf $INSTALL_DIR/$BIN_NAME /usr/local/bin/$BIN_NAME

# Create desktop entry
cat <<EOF > /usr/share/applications/rgb-controller.desktop
[Desktop Entry]
Name=RGB LED Controller
Comment=WS2812B Arduino RGB Controller
Exec=$INSTALL_DIR/$BIN_NAME
Icon=$INSTALL_DIR/$ICON_NAME
Terminal=false
Type=Application
Categories=Utility;
EOF

echo "RGB Controller v2.0"
echo "Installed successfully to $INSTALL_DIR."
echo "You can now search for 'RGB LED Controller' in your applications."
