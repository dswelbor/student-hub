CC=g++
CFLAGS=-I.
DEPS = src/digraph.h src/catch/catch.hpp
OBJ = src/test.o src/test_digraph.o src/digraph.o
BUILDDIR = build
MKDIR = mkdir -p

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BUILDDIR)/test: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

$(shell   mkdir -p $(BUILDDIR))