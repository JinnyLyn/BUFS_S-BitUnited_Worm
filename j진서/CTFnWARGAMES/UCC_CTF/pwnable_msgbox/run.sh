#!/bin/bash

print_usage() 
{
    echo "Usage: $0 <Path to Exploit File>"
}

run_vm()
{
    RAM="256"
    CPU_CORES="1"

    args=(
        -m "$RAM"
        -smp "$CPU_CORES"
        -cpu kvm64,+smep,+smap
        -kernel $(dirname "$0")/bzImage
        -initrd $(dirname "$0")/rootfs.cpio
        -append "root=/dev/vda1 console=tty1 console=ttyS0 loglevel=3 oops=panic panic=-1 security=none"
        -monitor /dev/null
        -nographic
        -no-reboot
        -hda $1 # host: /path/to/exploit/file, guest: /dev/sda
        -hdb $(dirname "$0")/flag
    )

    exec qemu-system-x86_64 "${args[@]}" 2>&1
}

# Sanity check
if [ -z "$1" ]; then
    print_usage
    exit 1
fi

run_vm $1