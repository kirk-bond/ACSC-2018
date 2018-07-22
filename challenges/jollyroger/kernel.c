#include <elf.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#include <zlib.h>

#ifdef DEBUG
#define debug(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
#define debug(fmt, ...)
#endif

uint32_t cksum1 = 0xdeadbeef;
uint32_t cksum2 = 0xcafebabe;


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

    // find the first PT_LOAD segment
    Elf64_Phdr *phdr = (Elf64_Phdr *)(base + ehdr->e_phoff);
    while (phdr->p_type != PT_LOAD) {
        phdr = (Elf64_Phdr *)((intptr_t)phdr + ehdr->e_phentsize);
    }

    // crc the segment
    debug("crc32(0, %p, %lx)\n", (void *)phdr->p_vaddr, phdr->p_filesz);
    uint32_t crc1 = crc32(0, (void *)phdr->p_vaddr, phdr->p_filesz);

    // find the second PT_LOAD segment
    phdr = (Elf64_Phdr *)((intptr_t)phdr + ehdr->e_phentsize);
    while (phdr->p_type != PT_LOAD) {
        phdr = (Elf64_Phdr *)((intptr_t)phdr + ehdr->e_phentsize);
    }

    // crc the segment, skipping cksum1 and cksum2
    size_t len = (intptr_t)&cksum1 - phdr->p_vaddr;
    debug("crc32(0, %p, %lx)\n", (void *)phdr->p_vaddr, len);
    uint32_t crc2 = crc32(0, (void *)phdr->p_vaddr, len);
    len = (intptr_t)phdr->p_vaddr + phdr->p_filesz - (intptr_t)(&cksum2 + 1);
    debug("crc32(crc2, %p, %lx)\n", (void *)(&cksum2 + 1), len);
    crc2 = crc32(crc2, (void *)(&cksum2 + 1), len);

    debug("crc1   = %x\n", crc1);
    debug("cksum1 = %x\n", cksum1);
    debug("crc2   = %x\n", crc2);
    debug("cksum2 = %x\n", cksum2);
    if (crc1 != cksum1 || crc2 != cksum2) {
        return -1;
    }

    return 0;
}


int main(void)
{
    int ret = validate_checksums();
    if (ret == 0) {
        printf("secure!\n");
    }
    else {
        printf("not secure.\n");
    }
    return 0;
}
