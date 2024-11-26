FROM ubuntu:24.04

RUN apt update -y
RUN apt install qemu-system-x86 socat -y

RUN mkdir /opt/msgbox
ADD bzImage flag rootfs.cpio run.py run.sh /opt/msgbox/

CMD socat tcp-listen:2357,reuseaddr,fork exec:/opt/msgbox/run.py,pty,echo=0,raw