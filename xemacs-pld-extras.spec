Summary:	Some facilities for xemacs
Summary(pl.UTF-8):	Różne dodatki do xemacsa
Name:		xemacs-pld-extras
Version:	0.21
Release:	5
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	%{name}-%{version}.tgz
# Source0-md5:	d8dac9f947ce1df4b761018bb8c8b8e2
#Source1:	http://www.xemacs.org/~stigb/rpm-spec-mode.el
Requires:	xemacs
Requires:	xemacs-cc-mode-pkg
Requires:	xemacs-pc-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Some files that change default XEmacs behavior:
- rpm-spec-mode
- key shortcuts definitions for PSGML-mode

More information on <http://www.pld-linux.org/>.

%description -l pl.UTF-8
Pakiet zawiera różne ułatwienia i dodatki do XEmacsa:
- tryb edycji rpm-spec-mode
- definicje skrótów klawiaturowych dla PSGML-mode
- włączenie standardowego działania niektórych klawiszy

Więcej informacji na <http://www.pld-linux.org/>.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp

cp -a %{name} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp
#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/%{name}
