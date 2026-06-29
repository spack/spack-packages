# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *

class Mailutils(AutotoolsPackage, GNUMirrorPackage):
    """GNU Mailutils is a rich and powerful protocol-independent mail
    framework.  It contains a series of useful mail libraries, clients,
    and servers.  These are the primary mail utilities for the GNU system.
    The central library is capable of handling electronic mail in various
    mailbox formats and protocols, both local and remote.  Specifically,
    this project contains a POP3 server, an IMAP4 server, and a Sieve mail
    filter. It also provides a POSIX `mailx' client, and a collection of
    other handy tools.

    The GNU Mailutils libraries supply an ample set of primitives for
    handling electronic mail in programs written in C, C++, Python or
    Scheme.

    At the core of Mailutils is libmailutils, a library which provides
    universal access to various mailboxes and protocols: UNIX mailbox,
    Maildir, MH, POP3, IMAP4, Sendmail, SMTP.  Mailutils offers functions
    for almost any mail-related task, such as parsing of messages, email
    addresses and URLs, handling MIME messages, listing mail folders,
    mailcap facilities, extensible Sieve filtering, access control lists.
    It supports various modern data security and authentication
    techniques: TLS encryption, SASL and GSSAPI, to name a few.
    The framework is able to work with a wide variety of authorization
    databases, ranging from traditional system password database up to
    RADIUS, SQL and LDAP.

    The utilities provided by Mailutils include imap4d and pop3d mail
    servers, mail reporting utility comsatd, general-purpose mail delivery
    agent maidag, mail filtering program sieve, and an implementation of
    MH message handling system.

    All utilities share the same subset of command line options and use
    a unified configuration mechanism, which allows to easily configure
    the package as a whole.
    """

    license("LGPL-3.0-or-later", checked_by="cosmicexplorer")
