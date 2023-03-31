Name:		texlive-amsldoc-vn
Version:	21855
Release:	2
Summary:	Vietnamese documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/amslatex/vietnamese
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-vn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-vn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a Vietnamese translation of amsldoc, the users' guide
to amsmath.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/Makefile
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/README
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/TODO
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/amsldoc-print-vi.pdf
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/amsldoc-print-vi.tex
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/amsldoc-vi.pdf
%doc %{_texmfdistdir}/doc/latex/amsldoc-vn/amsldoc-vi.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
