CC = gcc
CFLAGS = -Wall

app : main.o uart.o
	$(CC) main.o uart.o -o app
main.o : main.c uart.h
	$(CC) $(CFLAGS) -c main.c -o main.o
uart.o : uart.c uart.h
	$(CC) $(CFLAGS) -c uart.c -o uart.o
clean :
	rm -rf app main.o uart.o
.PHONY : clean