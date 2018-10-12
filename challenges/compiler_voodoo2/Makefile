CFLAGS := -Wall -Werror -O1

all: voodoo2

key.h:
	./genkey.py > key.bin
	xxd -i key.bin > $@

voodoo2: chal.c key.h
	clang-6.0 $(CFLAGS) -Xclang -load -Xclang ./LLVMExtractInst.so $< -o $@
	strip $@

clean:
	$(RM) voodoo2 key.h key.bin
