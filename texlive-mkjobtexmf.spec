Name:		texlive-mkjobtexmf
Version:	0.7
Release:	1
Summary:	Generate a texmf tree for a particular job
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/mkjobtexmf
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkjobtexmf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-mkjobtexmf.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The progam mkjobtexmf runs a program and tries to find the used
file names. Two methods are available, option "-recorder" of
TeX (Web2C) or the program strace. Then it generates a
directory with a texmf tree. It checks the found files and
tries sort them in this texmf tree. It can be used for
archiving purposes or to speed up following TeX runs.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkjobtexmf
%{_texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/README
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.html
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.ltx
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.pdf
%doc %{_texmfdistdir}/doc/generic/mkjobtexmf/mkjobtexmf.txt
%doc %{_mandir}/man1/mkjobtexmf.1*
%doc %{_texmfdir}/doc/man/man1/mkjobtexmf.man1.pdf
#- source
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/Makefile.in
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/configure
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/configure.ac
%doc %{_texmfdistdir}/source/generic/mkjobtexmf/install-sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
