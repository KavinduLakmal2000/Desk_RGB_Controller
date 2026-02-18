[Setup]
AppName=RGB Controller
AppVersion=2.0
AppPublisher=KLTechnology
DefaultDirName={pf}\KLTechnology\LEDController
DefaultGroupName=KLTechnology
OutputDir=installer
OutputBaseFilename=RGB_WS2812b_Controller_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=led.ico
WizardImageFile=wiz.bmp
WizardSmallImageFile=wizSmall.bmp


[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "dist\led_controller.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\RGB Controller"; Filename: "{app}\led_controller.exe"
Name: "{commondesktop}\RGB Controller"; Filename: "{app}\led_controller.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\led_controller.exe"; Description: "Launch RGB Controller"; Flags: nowait postinstall skipifsilent
