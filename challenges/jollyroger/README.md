# jollyroger

It looks like this smart device provides an unauthenticated web portal to update
the firmware. They say that they cryptographically sign their code so there's no
need to authenticate, but I have a hunch it's not as secure as they think. Can
you find a way to upload a modified firmware image?

http://<challenge-server>:5000

## Flag

`acsc18{i_thought_crcs_were_secure}`

## Category

Reverse Engineering

## Hints

1. The header is 32 bytes long, followed by an ELF file.
2. They're using a generic crc32 checksum to verify data integrity.
3. There is only one checksum, present in both the header and the body of the
   image.
4. The code segment of the ELF is being checksummed. It looks like some bytes of
   the code segment are being skipped.
5. The structure of the proprietary header is:

    struct header {
        uint32_t magic;
        uint32_t version;
        uint32_t num_cksums;
        uint32_t c1_offset;
        uint32_t c1_cksum;
        uint8_t  pad[12];
    };

## Steps

1. Open in a hex editor. Recognize the ELF header of \x7fELF at offset 0x20.
   Realize this is an ELF file with a proprietary header.
2. Extract the ELF with `dd if=firmware of=elf bs=1 skip=32`.
3. Reverse engineer the ELF file. Recognize that if the firmware version is
   changed to "jollyroger", it will print the flag.
4. Reverse the checksum computation to determine that it's computing a crc32 of
   the text segment, skipping 4 bytes in the middle of the segment (the embedded
   checksum). Realize that these bytes that are being skipped are also in the
   custom header.
5. Patch the version string to "jollyroger".
6. Recompute the checksum of the code segment.
7. Replace the embedded checksum and the header checksum with the new recomputed
   one.
8. Upload the file for a flag.

## Resources Required

* Build the `firmware` image with `make`, and attach that file to the challenge
  description.
* A docker challenge server running the firmware upload webapp.
