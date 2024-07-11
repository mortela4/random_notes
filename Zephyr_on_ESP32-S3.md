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
with the one shown below as a working template:
```
{
	"version": "0.2.0",
	"configurations": 
	[
		{
		    // more info at: https://github.com/Marus/cortex-debug/blob/master/package.json
		    "name": "Zephyr IDE: Debug",
		    "type": "cortex-debug",
		    "request": "attach", // do NOT use "launch" - will fail when attempting to download the app into the target!
		    "cwd": "${workspaceRoot}/<project-name>",
		    "executable": "${command:zephyr-ide.get-active-build-path}/zephyr/zephyr.elf",  // NOTE: should always be 'zephyr.elf'!!
		    "servertype": "openocd",
		    "interface": "jtag",
		    "armToolchainPath": "<Zephyr SDK install-HOME>/zephyr-sdk-<version>/<ARCH>-espressif_esp32<variant>_zephyr-elf/bin",
		    "toolchainPrefix": "<ARCH>-espressif_esp32<variant>_zephyr-elf", 
		    "openOCDPreConfigLaunchCommands": ["set ESP_RTOS none"],
		    "serverpath": "<PATH to OpenOCD binary for ESP32 from ESP-IDF>/openocd",
		    "showDevDebugOutput": "raw",
		    "svdPath": "/home/mortenl/.espressif/svd/svd/esp32s3.svd",   // Cloned from 'github.com/espressif/svd' NOTE: may also use "${idf.svdFilePath}" (???)
		    "configFiles": ["board/esp32<variant>-builtin.cfg"],  // If the built-in USB-to-JTAG debug connection (found on devkits) is used! 
		    // Else, custom config combined w. "target/esp32<variant>.cfg" may be required (using J-Link, FTDI-based adapter or 'whatever').
		    // Typically, a 'generic' FTDI-adapter config is defined as "interface/ftdi/esp32_devkitj_v1.cfg".
		    "overrideAttachCommands": [
		      "set remote hardware-watchpoint-limit 2",
		      "mon halt",
		      "flushregs",
		      "set remotetimeout 20",
		      "-target-select extended-remote localhost:50000"	// NOTE: 'cortex-debug' launches OpenOCD server w. GDB-port(TCP)=50000 by default! (and TCL-port=50001, Telnet-port=50002)
		    ],
		    "overrideRestartCommands": ["mon reset halt", "flushregs", "c"],
		}
	]
```
Edit the text between angle brackets ('<>').


On my (typical) system, referencing the toolchain within Zephyr SDK, 
using ESP32-S3 (i.e. ARCH='xtensa' and variant='s3'),
and OpenOCD for ESP32 from 'ESP-IDF' SDK, this becomes:
```
{
	"version": "0.2.0",
	"configurations": 
	[
		{
		    // more info at: https://github.com/Marus/cortex-debug/blob/master/package.json
		    "name": "Zephyr IDE: Debug",
		    "type": "cortex-debug",
		    "request": "attach", // do NOT use "launch" - will fail when attempting to download the app into the target!
		    "cwd": "${workspaceRoot}/button",
		    "executable": "${command:zephyr-ide.get-active-build-path}/zephyr/zephyr.elf", 
		    "servertype": "openocd",
		    "interface": "jtag",
		    "armToolchainPath": "/home/mortenl/.local/zephyr-sdk-0.16.8/xtensa-espressif_esp32s3_zephyr-elf/bin",
		    "toolchainPrefix": "xtensa-espressif_esp32s3_zephyr-elf", 
		    "openOCDPreConfigLaunchCommands": ["set ESP_RTOS none"],
		    "serverpath": "/home/mortenl/.espressif/tools/openocd-esp32/v0.12.0-esp32-20240318/openocd-esp32/bin/openocd",
		    "showDevDebugOutput": "raw",
		    "configFiles": ["board/esp32s3-builtin.cfg"], 
		    "overrideAttachCommands": [
		      "set remote hardware-watchpoint-limit 2",
		      "mon halt",
		      "flushregs",
		      "set remotetimeout 20",
		      "-target-select extended-remote localhost:50000"	
		    ],
		    "overrideRestartCommands": ["mon reset halt", "flushregs", "c"],
		}
	]
```

NOTE: it is probably also OK to use 'vanilla' OpenOCD as long as all required .cfg-files are in place, 
and also the GDB debugger from Xtensa-Espressif-ESP32 toolchain installed by ESP-IDF SDK installer (or ditto VScode IDF extension).

 


