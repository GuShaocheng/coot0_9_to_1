https://drive.google.com/drive/u/1/folders/1klDIpBIr76bhaoQf1kKVQrSaTAzGoRuE

Due to XQuartz compatibility issues with the latest macOS, Coot 0.9 cannot be launched directly. As a workaround, we can run Coot 0.9.8.92 compiled for ARM Linux inside a virtual machine on Apple Silicon.

1. Install UTM on macOS
Note: you can install other virtual machine with VNC for display.

2. Download the ubuntu-20-04 ARM Linux:
https://mac.getutm.app/gallery/ubuntu-20-04
Note: This specific distribution is recommended, as the package was compiled against it.

3. Extract and click the .utm
Note: password is `ubuntu`.
Note: you can set up a share folder in UTM for seamless file exchange between the UTM and macOS.

4. Download the pre-built ARM64 Debian package: coot-0.9.8.92-arm64.deb.
Note: ARM build is essential for smooth performance on Apple Silicon.
Note: Only python scripting is supported (Guile Scheme was disabled at compiling time. If you mange to compile the Guile, please share with me)

5. Open the terminal and run: sudo apt install ./coot-0.9.8.92-arm64.deb
