obj-m := vuln.o
KDIR = # wherever you want~

all:
	make -C $(KDIR) M=$(PWD) modules
clean:
	make -C $(KDIR) M=$(PWD) clean
