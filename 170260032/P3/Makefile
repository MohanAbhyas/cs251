SHELL := /bin/bash
var := $(shell ls -t -1 ./*.o | tail -1)

all: main
.PHONY: skiprebuild
.PHONY: skiprebuildh

main: main.o depend.o
	g++ main.o depend.o -o main

depend.o: depend.cpp depend.h
	g++ -c depend.cpp

main.o: main.cpp depend.h
	g++ -c main.cpp

skiprebuild:
	make -t

skiprebuildh:
	echo $(var)
	touch -r $(var) -d '2 seconds ago' depend.h
