Seeed Linux USB Display
====================================================================================
Drivers for Raspberry Pi USB Display Project

You can use it for multi-screen expansion display and multi-screen clone display.


WIKI
====================================================================================
Get more detail about Seeed Linux USB Display from: 
[WIKI](https://wiki.seeedstudio.com/Wio-Terminal-HMI)


Get Started
====================================================================================
    1) Copy the content of folder to your local path using git tool.

        $ git clone https://github.com/Seeed-Studio/seeed-linux-usbdisp.git

    2) Update the raspberry pi kernel and header files.

        $ sudo apt-get -y --force-yes install raspberrypi-kernel-headers raspberrypi-kernel

    3) Go to the linux-driver path.

        $ cd your_local_path/seeed-linux-usbdisp/drivers/linux-driver/

    4) Compile and install the driver.

        $ make && sudo make install

    5) Restart raspberry pi.

        $ sudo reboot

    6) Go to /seeed-linux-usbdisp/drivers/linux-driver/xserver_conf. And there are five xorg.config files in this folder. 
       Please copy one of the files according to your own needs to /usr/share/X11/xorg.conf.d/

        $ cd your_local_path/seeed-linux-usbdisp/drivers/linux-driver/xserver_conf/
        $ sudo cp the_file_you_need /usr/share/X11/xorg.conf.d/

    7) Restart the X11 Server.

        $ sudo service lightdm restart


Note
====================================================================================
This driver does not support hot plugging. If you pull out the USB monitor and plug in it right away that would cause the X11 Server to crash. In this time, you should restart your raspberry pi.

```shell
$ sudo reboot
```


Contact Us
====================================================================================
Website: https://www.seeedstudio.com/
