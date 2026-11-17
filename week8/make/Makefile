CC = gcc
CFLAGS = -Wall

app : main.o calc.o
	$(CC) main.o calc.o -o app
main.o : main.c calc.h
	$(CC) $(CFLAGS) -c main.c -o main.o
calc.o : calc.c calc.h
	$(CC) $(CFLAGS) -c calc.c -o calc.o
clean : 
	rm -rf app main.o calc.o
.PHONY : clean