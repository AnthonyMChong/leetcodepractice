CC=g++
CFLAGS=-I.

jewels-and-stones: jewels-and-stones.o
	$(CC) -o jewels-and-stones jewels-and-stones.o