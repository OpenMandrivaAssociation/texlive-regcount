Name:		texlive-regcount
Version:	19979
Release:	2
Summary:	Display the allocation status of the TeX registers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regcount
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Adds a macro \rgcount which displays the allocation status of
the TeX registers. The display is written into the .log file as
it is a bit verbose. An automatic call to \rgcount is done at
\begin{document} and \end{document}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/regcount/regcount.sty
%doc %{_texmfdistdir}/doc/latex/regcount/readme
%doc %{_texmfdistdir}/doc/latex/regcount/regcount.pdf
#- source
%doc %{_texmfdistdir}/source/latex/regcount/regcount.dtx
%doc %{_texmfdistdir}/source/latex/regcount/regcount.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
