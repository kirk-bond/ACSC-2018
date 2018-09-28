CFLAGS := -Wall -Werror -O1

all: voodoo1

key.h:
	./genkey.py > key.bin
	xxd -i key.bin > $@

voodoo1: chal.c key.h
	clang-6.0 $(CFLAGS) -Xclang -load -Xclang ./LLVMExtractBB.so $< -o $@
	strip $@

clean:
	$(RM) voodoo1 key.h key.bin
