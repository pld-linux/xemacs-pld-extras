Summary:	Some facilities for xemacs
Summary(pl):	R�ne dodatki do xemacsa
Name:		xemacs-pld-extras
Version:	0.21
Release:	4
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	%{name}-%{version}.tgz
#Source1:	http://www.xemacs.org/~stigb/rpm-spec-mode.el
Requires:	xemacs
Requires:	xemacs-pc-pkg
Requires:	xemacs-cc-mode-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
	
%description
Some files that change default XEmacs behavior:
- rpm-spec-mode
- key shortcuts definitions for PSGML-mode

More information on http://www.pld.org.pl/ .

%description -l pl
Pakiet zawiera r�ne u�atwienia i dodatki do XEmacsa:
- tryb edycji rpm-spec-mode
- definicje skr�t�w klawiaturowych dla PSGML-mode
- w��czenie standardowego dzia�ania niekt�rych klawiszy

Wi�cej informacji na http://www.pld.org.pl/ .

%prep
%setup  -q -c


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp 

cp -a %{name} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp
#install %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/xemacs-packages/lisp/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/%{name}
