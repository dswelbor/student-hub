CC=g++
CFLAGS=-I.
DEPS = src/digraph.h
OBJ = src/digraph_test.o src/digraph.o
BUILDDIR = build
MKDIR = mkdir -p

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BUILDDIR)/digraph_test: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

$(shell   mkdir -p $(BUILDDIR))