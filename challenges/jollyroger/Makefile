CFLAGS := -Wall -Wextra -Werror -pedantic

all: firmware firmware.jr test
debug: CFLAGS += -g -DDEBUG
debug: all

kernel: kernel.c
	$(CC) $(CFLAGS) -o $@ $^ -lz

firmware: kernel
	./signtool.py sign -o $@ $<

firmware.jr: firmware
	./solve.py $<

# test target to strip the custom header off the signed kernel
test: firmware
	dd if=$< of=$@ bs=1 skip=32
	chmod a+x $@

clean:
	$(RM) kernel firmware firmware.jr test *.pyc
	$(RM) -r __pycache__
