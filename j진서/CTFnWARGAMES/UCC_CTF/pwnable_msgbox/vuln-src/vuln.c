#include <linux/module.h>
#include <linux/proc_fs.h>
#include <linux/miscdevice.h>
#include <linux/mutex.h>

#define CMD_ALLOC 0xa110c
#define CMD_FREE 0xf5ee

#define KMALLOC_512_SZ 0x200

#define MAX_OBJ_IDX 0x100

void *objs[MAX_OBJ_IDX];
DEFINE_MUTEX(global_lock);

static long vuln_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
{
    unsigned long idx = arg;
    int ret = 0;

    mutex_lock(&global_lock);

    if (idx >= MAX_OBJ_IDX) {
        mutex_unlock(&global_lock);
        return -EINVAL;
    }

    switch (cmd) {
    case CMD_ALLOC:
        objs[idx] = kzalloc(KMALLOC_512_SZ, GFP_KERNEL_ACCOUNT);
        if (!objs[idx])
            ret = -ENOMEM;
        break;
    case CMD_FREE:
        if (!objs[idx]) {
            ret = -EINVAL;
            break;
        }

        kfree(objs[idx]);
        // objs[idx] = NULL; 
        break;
    default:
        pr_info("vuln: Invalid `cmd` %u\n", cmd);
        ret = -EINVAL;
        break;
    }

    mutex_unlock(&global_lock);

    return ret;
}

static const struct file_operations vuln_fops = {
    .owner          = THIS_MODULE,
    .unlocked_ioctl = vuln_ioctl,
};

static struct miscdevice vuln_miscdev = {
    .minor = MISC_DYNAMIC_MINOR,
    .name = "vuln",
    .fops = &vuln_fops,
    .mode = 0666,
};

static int __init vuln_init(void)
{
    mutex_init(&global_lock);

    return misc_register(&vuln_miscdev);
}

static void __exit vuln_exit(void)
{
    mutex_destroy(&global_lock)
    
    misc_deregister(&vuln_miscdev);
}

module_init(vuln_init);
module_exit(vuln_exit);

MODULE_LICENSE("GPL v2");