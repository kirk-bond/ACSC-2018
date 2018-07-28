#include <elf.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <zlib.h>

#ifdef DEBUG
#define debug(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
#define debug(fmt, ...)
#endif

#define VERSION_STR "SecureSystems Kernel 3.10.0"
//#define VERSION_STR "jollyroger"

uint32_t cksum1 __attribute__((section (".text"))) = 0xdeadbeef;
uint32_t cksum2 __attribute__((section (".text"))) = 0xcafebabe;


int validate_checksums(void)
{
    // get the ELF base
    char *base = (char *)((intptr_t)&validate_checksums & (~0xfff));
    while (base[EI_MAG0] != ELFMAG0 ||
           base[EI_MAG1] != ELFMAG1 ||
           base[EI_MAG2] != ELFMAG2 ||
           base[EI_MAG3] != ELFMAG3) {
        base -= 0x1000;
    }

    // calculate the crc of each segment
    // assume that there are only two LOAD segments
    Elf64_Ehdr *ehdr = (Elf64_Ehdr *)base;

    // find the text segment (PT_LOAD and RX permissions)
    Elf64_Phdr *phdr = (Elf64_Phdr *)(base + ehdr->e_phoff);
    for (int i = 0; i < ehdr->e_phnum; i++) {
        if (phdr->p_type == PT_LOAD && phdr->p_flags == (PF_R | PF_X)) {
            break;
        }
        phdr = (Elf64_Phdr *)((intptr_t)phdr + ehdr->e_phentsize);
    }

    usleep(500 * 1000);

    // crc the segment, skipping cksum1 and cksum2
    size_t len = (intptr_t)&cksum1 - phdr->p_vaddr;
    debug("crc32(0, %p, %lx)\n", (void *)phdr->p_vaddr, len);
    uint32_t crc1 = crc32(0, (void *)phdr->p_vaddr, len);
    len = (intptr_t)phdr->p_vaddr + phdr->p_filesz - (intptr_t)(&cksum2 + 1);
    debug("crc32(crc1, %p, %lx)\n", (void *)(&cksum2 + 1), len);
    crc1 = crc32(crc1, (void *)(&cksum2 + 1), len);

    usleep(500 * 1000);

    // only verify cksum1 (text segment) since the .got.plt section
    // was modified during load.
    debug("crc1   = %x\n", crc1);
    debug("cksum1 = %x\n", cksum1);
    debug("cksum2 = %x\n", cksum2);
    if (crc1 != cksum1) {
        return -1;
    }

    return 0;
}


int main(void)
{
    int ret = 0;
    int fd = -1;
    char buf[128] = {0};

    puts("(kernel) Starting self-validation...");
    fflush(stdout);
    ret = validate_checksums();
    if (ret == 0) {
        puts("(kernel) Validation succeeded!");
    }
    else {
        puts("(kernel) Validation failed!");
        puts("(kernel) Kernel panic - corrupted image");
        _exit(EXIT_FAILURE);
    }

    printf("(kernel) Kernel version: %s\n", VERSION_STR);
    if (strcmp(VERSION_STR, "jollyroger") == 0) {
        fd = open("/flag.txt", O_RDONLY);
        if (fd >= 0) {
            read(fd, buf, sizeof(buf) - 1);
            printf("(kernel) %s", buf);
        }
    }

    return 0;
}
