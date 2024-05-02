# Zephyr problem areas

Zephyr have problematic areas almost 'everywhere'.
A lot of these come from wrong or missing configuration symbols, 
or wrong value thereof.


## VScode plugin

### Active Breakpoints in non-associated Projects

Fix: do 'remove all' in breakpoints, then add those relevant only.



## Generic

### RAM Usage

Although most of Zephyr's RAM usage is *predictable*, 
there is some *run-time* allocation that causes problems IF static usage is >90%.
This is also when HEAP_MEM_POOL is set to a 'reasonable' level - 
which is the RAM mem-pool that 'malloc()' takes into account (and allocates RAM from).

Symptom: application just 'hangs' (also in debugger).

Fix: ensure RAM usage *always* below 90% !!

### 'DT_<...>(...)' macro expansion fails in build

Fix: ensure no missing "#include <zephyr/device.h>" in C/C++ source.



## I2S driver for NRFX

### I2S Tx/Rx-buffers *configured* must be N+1 when using N.

Fix: set CONFIG_I2S_NRFX_TX_BLOCK_SIZE to (N+1) when using N buffers for I2S-Tx.


### I2S triggering for START of transmission

Fix: always write one, full buffer before issuing START-trigger.



## Networking

Generally very tricky, as **buffering** is *always* an issue - 
especially when up/down-loading large files.
Lots of config-symbols involved:
- CONFIG_NET_TX_STACK_SIZE=x    (suggested: x = 2048)
- CONFIG_NET_RX_STACK_SIZE=x    (suggested: x = 2048)
- CONFIG_NET_BUF_DATA_SIZE=x    (suggested: x = 1024)
- CONFIG_NET_PKT_RX_COUNT=x    (suggested: x = 10, must NOT be *larger* than CONFIG_NET_BUF_RX_COUNT!)
- CONFIG_NET_PKT_TX_COUNT=x    (suggested: x = 10, must NOT be *larger* than CONFIG_NET_BUF_TX_COUNT!)
- CONFIG_NET_BUF_RX_COUNT=x    (suggested: x = 20)
- CONFIG_NET_BUF_TX_COUNT=x    (suggested: x = 20)
- CONFIG_NET_MAX_CONTEXTS=x    (suggested: x = 10 --> very application-dependent!)  

In addition, workqueue-stack should be (at least) 2KB.

__NOTE__: 'CONFIG_NET_PKT_[RX/TX]_COUNT' value gets multiplied by corresponding 'CONFIG_NET_BUF_DATA_SIZE' value!
I.e. if the former both have value=10, and the latter 1KB, then RAM usage for packet-buffers become (10+10)*1KB = 20KB in total.


### (D)TLS usage


