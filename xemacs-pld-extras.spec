Summary:	Polish keyboard definitions and other files for xemacs
Summary(pl): 	Definicje klawiatury pl i inne dodatki do xemacsa
Name:		xemacs-pld-extras
Version:	0.6
Release:	1
Copyright:	GPL
Group:		Applications/Archiving
Source:		%{name}-%{version}.tgz
Requires:	xemacs
Requires:	xemacs-extras
Requires:	xemacs-pc-pkg
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
	

%description
Some files that changes default xemacs behavior.

%description -l pl
Pliki definiuj±ce klawiaturê, ró¿ne u³atwienia do edycji,
dodatkowe u³atwienia dla psgml.
Wystarczy tylko zainstalowaæ ten pakiet by uzyskaæ polskie znaki,
a tak¿e pewne u³atwienia w pos³ugiwaniu siê xemacsem.

%prep
%setup  -q -c %{name}-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/xemacs-packages/lisp 
cp -a * $RPM_BUILD_ROOT/%{_datadir}/xemacs-packages/lisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/default.el
%{_datadir}/xemacs-packages/lisp/kbd*
%{_datadir}/xemacs-packages/lisp/pld*
