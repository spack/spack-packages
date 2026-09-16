# GNU makefile for OpenBSD csh, whose BSD Makefile requires bsd.prog.mk.
# Generates const.h and error.h the same way the BSD Makefile does.
CFLAGS ?= -O2
CFLAGS += -I.

ifeq ($(shell uname -s),Linux)
CFLAGS += -D_GNU_SOURCE
LDLIBS += -lbsd
endif

SRCS = alloc.c char.c const.c csh.c dir.c dol.c error.c exec.c exp.c file.c \
       func.c glob.c hist.c init.c lex.c misc.c parse.c proc.c sem.c set.c \
       str.c time.c
OBJS = $(SRCS:.c=.o)

all: csh

csh: $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $(OBJS) $(LDLIBS)

$(OBJS): const.h error.h

error.h: error.c
	{ echo '#ifndef _h_sh_err'; echo '#define _h_sh_err'; \
	    grep -E '^#define[[:space:]]+ERR_' error.c; \
	    echo '#endif /* _h_sh_err */'; } > $@

# csh.h includes const.h, so give the preprocessor an empty one to start
const.h: const.c error.h
	: > $@
	$(CC) -E $(CPPFLAGS) $(CFLAGS) const.c | grep -E '^Char STR' | \
	    sed -e 's/^Char \(STR[A-Za-z0-9_]*\).*/extern Char \1[];/' | \
	    sort -u > $@.tmp
	mv $@.tmp $@

PREFIX ?= /usr/local
install: csh
	install -d $(DESTDIR)$(PREFIX)/bin $(DESTDIR)$(PREFIX)/share/man/man1
	install -m 755 csh $(DESTDIR)$(PREFIX)/bin
	install -m 644 csh.1 $(DESTDIR)$(PREFIX)/share/man/man1

clean:
	rm -f csh $(OBJS) const.h error.h

.PHONY: all install clean
