%global tl_name mkjobtexmf
%global tl_revision 29725
%global tl_bin_links mkjobtexmf:%{_texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Generate a texmf tree for a particular job
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/mkjobtexmf
License:	artistic
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mkjobtexmf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a Perl script, which runs a program and tries to
find the names of file used. Two methods are available, option -recorder
of (Web2C) TeX and the program strace. Then it generates a directory
with a texmf tree. It checks the found files and tries sort them in this
texmf tree. The script may be used for archiving purposes or to speed up
later TeX runs.

