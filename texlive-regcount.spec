# revision 19979
# category Package
# catalog-ctan /macros/latex/contrib/regcount
# catalog-date 2010-10-02 17:24:09 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-regcount
Version:	1.0
Release:	1
Summary:	Display the allocation status of the TeX registers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regcount
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Adds a macro \rgcount which displays the allocation status of
the TeX registers. The display is written into the .log file as
it is a bit verbose. An automatic call to \rgcount is done at
\begin{document} and \end{document}.

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
%{_texmfdistdir}/tex/latex/regcount/regcount.sty
%doc %{_texmfdistdir}/doc/latex/regcount/readme
%doc %{_texmfdistdir}/doc/latex/regcount/regcount.pdf
#- source
%doc %{_texmfdistdir}/source/latex/regcount/regcount.dtx
%doc %{_texmfdistdir}/source/latex/regcount/regcount.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
