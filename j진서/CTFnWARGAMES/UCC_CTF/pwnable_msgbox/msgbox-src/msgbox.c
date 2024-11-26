#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <seccomp.h>
#include <fcntl.h>
#include <sys/prctl.h>

#include "bpf-helper.h"

#define EXPLOIT_PATH "./exploit"

__attribute__((noreturn)) 
void fatal(const char *msg)
{
    perror(msg);
    exit(EXIT_FAILURE);
}

int apply_seccomp(void)
{
    struct sock_filter filter[] = {
        LOAD_ARCH,
        JNE32(AUDIT_ARCH_X86_64, DENY),

        LOAD_SYSCALL_NR,
        SYSCALL(__NR_msgget, ALLOW),
        SYSCALL(__NR_msgsnd, ALLOW),
        SYSCALL(__NR_msgrcv, ALLOW),

        SYSCALL(__NR_execve, ALLOW),
        SYSCALL(__NR_ioctl, ALLOW),

        DENY,
    };
    struct sock_fprog prog = {
        .filter = filter,
        .len = sizeof(filter) / sizeof(filter[0]),
    };

    int ret;

    ret = prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);
    if (ret < 0)
        return ret;

    ret = syscall(__NR_seccomp, SECCOMP_SET_MODE_FILTER, SECCOMP_FILTER_FLAG_TSYNC, &prog);
    if (ret < 0)
        return ret;

    return 0;
}

int run_exploit(void)
{
    char *argv[] = {
        EXPLOIT_PATH,
        NULL
    };

    return execve(EXPLOIT_PATH, argv, NULL);
}

void close_stdio(void)
{
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
}

int main(void)
{
    int fd;

    fd = open("/dev/vuln", O_RDWR);
    if (fd < 0)
        fatal("open");

    printf("[!] vuln fd: %d\n", fd);

    close_stdio();

    if (apply_seccomp() < 0)
        fatal("apply_seecomp");

    if (run_exploit() < 0)
        fatal("run_exploit");

    return 0;
}