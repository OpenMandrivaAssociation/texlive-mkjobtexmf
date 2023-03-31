Name:		texlive-mkjobtexmf
Version:	29725
Release:	2
Summary:	Generate a texmf tree for a particular job
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/mkjobtexmf
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-mkjobtexmf.bin = %{EVRD}

%description
The package provides a Perl script, which runs a program and
tries to find the names of file used. Two methods are
available, option -recorder of (Web2C) TeX and the program
strace. Then it generates a directory with a texmf tree. It
checks the found files and tries sort them in this texmf tree.
The script may be used for archiving purposes or to speed up
later TeX runs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkjobtexmf
%{_texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/README
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/clean-case.pl
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.html
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.ltx
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.pdf
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.txt
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/version.pl
%doc %{_mandir}/man1/mkjobtexmf.1*
%doc %{_texmfdistdir}/doc/man/man1/mkjobtexmf.man1.pdf
#- source
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/Makefile.in
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/configure
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/configure.ac
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/install-sh

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
