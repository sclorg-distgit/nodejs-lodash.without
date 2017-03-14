%{?scl:%scl_package nodejs-lodash.without}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name lodash.without

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:        4.4.0
Release:        1%{?dist}
Summary:    The lodash method `_
License:    MIT
URL:        https://lodash.com/
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
The lodash method `_.without` exported as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.4.0-1
- Updated with script

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.2.0-2
- Initial build

