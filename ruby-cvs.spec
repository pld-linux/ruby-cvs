%define pkgname cvs
Summary:	CVS library for Ruby
Name:		ruby-%{pkgname}
Version:	0.0.0
Release:	0.1
License:	?
Source0:	https://github.com/akr/ruby-cvs/archive/c760e34/%{name}-%{version}.tar.gz
# Source0-md5:	7705179c54f7b38f5440f928151ce61c
Group:		Development/Languages
URL:		https://github.com/akr/ruby-cvs
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	cvs >= 1.11.1p1
Requires:	ruby >= 1:1.7.1
#Suggests:	flex.rb >= 0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/CVS is a library to access a CVS repository.

%prep
%setup -qc
mv %{name}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/cvs.rb
%{ruby_vendorlibdir}/cvs
%{ruby_vendorlibdir}/diff.rb
%{ruby_vendorlibdir}/diff
%{ruby_vendorlibdir}/rcs.rb
%{ruby_vendorlibdir}/rcs
%{ruby_vendorlibdir}/tempdir.rb
