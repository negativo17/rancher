%global debug_package %{nil}

Name:           rancher-cli
Version:        2.4.9
Release:        1%{?dist}
Summary:        Unified tool for interacting with your Rancher Server
License:        ASL 2.0
URL:            https://rancher.com/docs/rancher/v2.x/en/cli/

Source0:        https://github.com/rancher/cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang >= 1.13

%description
The Rancher Command Line Interface (CLI) is a unified tool for interacting with
your Rancher Server.

%prep
%autosetup -n cli-%{version}

%build
go build

%install
install -D -p -m 755 cli %{buildroot}%{_bindir}/rancher

%files
%license LICENSE
%doc README.md
%{_bindir}/rancher

%changelog
* Fri Dec 04 2020 Simone Caronni <negativo17@gmail.com> - 2.4.9-1
- Update to 2.4.9.

* Wed Oct 07 2020 Simone Caronni <negativo17@gmail.com> - 2.4.6-1
- Update to 2.4.6.

* Tue Jun 23 2020 Simone Caronni <negativo17@gmail.com> - 2.4.5-1
- Update to 2.4.5.

* Fri May 29 2020 Simone Caronni <negativo17@gmail.com> - 2.4.3-1
- First build.
