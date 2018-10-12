CPPFLAGS += -Wall -Wextra -Wpedantic 

CFLAGS += -std=c11

bins = slot_machine 

slot_machine: slot_machine.c helper.c
	$(CC) $(CFLAGS) -o $@ $^

all: $(bins)

clean:
	rm slot_machine 
