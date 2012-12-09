# revision 21855
# category Package
# catalog-ctan /info/amslatex/vietnamese
# catalog-date 2007-01-26 22:11:52 +0100
# catalog-license lgpl
# catalog-version 2.0
Name:		texlive-amsldoc-vn
Version:	2.0
Release:	2
Summary:	Vietnamese documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/amslatex/vietnamese
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-vn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-vn.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 749224
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 717824
- texlive-amsldoc-vn
- texlive-amsldoc-vn
- texlive-amsldoc-vn
- texlive-amsldoc-vn

