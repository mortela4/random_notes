# Zephyr on ESP32-S3
--------------------


## Zephyr SDK

Toolchain name: 'xtensa-espressif_esp32s3_zephyr-elf'	

Toolchain distribution package:
- [AArch64 buildhost] = "toolchain_linux-aarch64_xtensa-espressif_esp32s3_zephyr-elf.tar.xz" 
- [x86-64 buildhost] = "toolchain_linux-x86_64_xtensa-espressif_esp32s3_zephyr-elf.tar.xz"

Full path is then (for Linux x86-64 buildhost):
```
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/<version>/zephyr-<version>_linux-x86_64.tar.xz
```
for toolchain + libraries, and:
```
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/<version>/sha256.sum | shasum --check --ignore-missing
```
to verify file authenticity.

Then, extract with:
```
tar xvf zephyr-sdk-<version>_linux-x86_64.tar.xz 
```

And install:
```
cd zephyr-sdk-<version>
./setup.sh
```

## VScode IDE for Zephyr development

Currently (mid-2024) the best extension for VScode seems to be "Zephyr IDE" (from Mylonics inc.).
Unfortunately, this extension does *not* include debug-backend for ESP32, 
only some scarce "launch.json" examples for STlink & JLink used with STM32 devices and Rpi 'Pico' (RPi40).

### VScode debug
Install the "cortex-debug" extension. Although it is primarily used for ARM/Cortex-M debug, 
it can be used with any toolchain including relevant GDB + GDBserver executables.
This includes 'OpenOCD' which has a GDBserver-compliant backend, and can be used w. the built-in JTAG-over-USB 
connection found on most (recent) ESP32 kits. 

A working "launch.json" must be crafted manually for debug - 
with the one shown below as a working example:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            // more info at: https://github.com/Marus/cortex-debug/blob/master/package.json
            "name": "Zephyr IDE: Debug",
            "type": "cortex-debug",
            "request": "attach", // launch will fail when attempting to download the app into the target
            "cwd": "${workspaceRoot}/button",
            "executable": "${command:zephyr-ide.get-active-build-path}/zephyr/zephyr.elf", 
            "servertype": "openocd",
            "interface": "jtag",
            "armToolchainPath": "/home/mortenl/.local/zephyr-sdk-0.16.8/xtensa-espressif_esp32s3_zephyr-elf/bin",
            //"toolchainPrefix": "xtensa-esp32-elf", 
            "toolchainPrefix": "xtensa-espressif_esp32s3_zephyr-elf", 
            "openOCDPreConfigLaunchCommands": ["set ESP_RTOS none"],
            //"serverpath": "/usr/bin/openocd", 
            "serverpath": "/home/mortenl/.espressif/tools/openocd-esp32/v0.12.0-esp32-20240318/openocd-esp32/bin/openocd",
            "showDevDebugOutput": "raw",
            //"gdbPath": "~/.espressif/tools/xtensa-esp-elf-gdb/14.2_20240403/xtensa-esp-elf-gdb/bin/xtensa-esp32-elf-gdb", 
            //"gdbPath": "~/.local/zephyr-sdk-0.16.8/xtensa-espressif_esp32s3_zephyr-elf/bin/xtensa-espressif_esp32s3_zephyr-elf-gdb",
            "configFiles": ["board/esp32s3-builtin.cfg"], 
            "overrideAttachCommands": [
              "set remote hardware-watchpoint-limit 2",
              "mon halt",
              "flushregs",
              "set remotetimeout 20",
              "-target-select extended-remote localhost:50000"
            ],
            "overrideRestartCommands": ["mon reset halt", "flushregs", "c"],
        },
        {
            "type": "gdbtarget",
            "name": "ESP32 Debug",
            "cwd": "${workspaceFolder}/button",
            "gdb": "~/.espressif/tools/xtensa-esp-elf-gdb/14.2_20240403/xtensa-esp-elf-gdb/bin/xtensa-esp32s3-elf-gdb",
            "program": "${command:zephyr-ide.get-active-build-path}/zephyr/zephyr.elf",
            "request": "launch",
            //"debugServer": 3333,
            "initCommands": [
                "set remote hardware-watchpoint-limit 4",
                "mon reset halt",
                "maintenance flush register-cache",
                "thb app_main"
            ],
            "target": 
            {
                "connectCommands": 
                [
                    "set remotetimeout 20",
                    "-target-select extended-remote localhost:3333"
                ]
            },
            "preLaunchTask": "~/.espressif/tools/openocd-esp32/v0.12.0-esp32-20240318/openocd-esp32/bin/openocd -f ~/.espressif/tools/openocd-esp32/v0.12.0-esp32-20240318/openocd-esp32/share/openocd/scripts/board/esp32s3-builtin.cfg"
        }
    ]
}
```

NOTE: the 'gdbtarget' debug-type configuration *should* work as well, but fails - probably because of tool-PATH specifications not being picked up correctly!



