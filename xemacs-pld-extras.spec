Summary:	Some facilities for xemacs
Summary(pl):	Ró¿ne dodatki do xemacsa
Name:		xemacs-pld-extras
Version:	0.10
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	%{name}-%{version}.tgz
Requires:	xemacs
Requires:	xemacs-pc-pkg
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
	
%description
Some files that changes default xemacs behavior.

%description -l pl
Pliki definiuj±ce klawiaturê, ró¿ne u³atwienia do edycji, dodatkowe
u³atwienia dla psgml. Wystarczy tylko zainstalowaæ ten pakiet by uzyskaæ
polskie znaki, a tak¿e pewne u³atwienia w pos³ugiwaniu siê xemacsem.

%prep
%setup  -q -c %{name}-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/xemacs-packages/lisp 
cp -a %{name} $RPM_BUILD_ROOT/%{_datadir}/xemacs-packages/lisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/%{name}
