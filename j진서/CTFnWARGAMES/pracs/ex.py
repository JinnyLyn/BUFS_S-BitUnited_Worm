#!/usr/bin/python3
# RazviOverflow

from pwn import *

context.binary = binary = ELF("./test", checksec=False)
#context.log_level = "debug"

p = process()
pid = util.proc.pidof(p)[0]
print(f"Pid is: {pid}")
util.proc.wait_for_debugger(pid)
