Summary:	Polish keyboard definitions and other files for xemacs
Summary(pl): 	Definicje klawiatury pl i inne dodatki do xemacsa
Name:		xemacs-pld-extras
Version:	0.1
Release:	1
Copyright:	GPL
Group:		Applications/Archiving
Source:		xemacs-pld-extras.tgz
Requires:	xemacs
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch

%description
Some files to include in .emacs

%description -l pl
Pliki definiuj�ce klawiatur�, r�ne u�atwienia do edycji,
dodatkowe u�atwienia dla psgml.

%prep
%setup  -q -c %{name}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/xemacs/lisp 
cp -a * $RPM_BUILD_ROOT/%{_datadir}/xemacs/lisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs/lisp/*
