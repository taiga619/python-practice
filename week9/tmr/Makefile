CC = gcc
CFLAGS = -Wall

app : main.o tmr.o
	$(CC) main.o tmr.o -o app
main.o : main.c tmr.h
	$(CC) $(CFLAGS) -c main.c -o main.o
tmr.o : tmr.c tmr.h
	$(CC) $(CFLAGS) -c tmr.c -o tmr.o
clean:
	rm -rf app main.o tmr.o
.PHONY : clean
