CFLAGS := -Wall -Werror -O1

all: voodoo1 voodoo2

key.h:
	./genkey.py > key.bin
	xxd -i key.bin > $@

key_hard.h:
	./genkey.py --hard > key_hard.bin
	xxd -i key_hard.bin > $@
	sed -i 's/key_hard/key/g' $@

voodoo1: chal.c key.h
	clang-6.0 $(CFLAGS) -Xclang -load -Xclang ./LLVMExtractBB.so $< -o $@
	strip $@

voodoo2: chal.c key_hard.h
	clang-6.0 $(CFLAGS) -Xclang -load -Xclang ./LLVMExtractInst.so -DHARD_MODE $< -o $@
	strip $@

clean:
	$(RM) voodoo1 voodoo2 key.h key.bin key_hard.h key_hard.bin
