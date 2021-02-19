#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yarl
Version  : 1.6.3
Release  : 20
URL      : https://files.pythonhosted.org/packages/97/e7/af7219a0fe240e8ef6bb555341a63c43045c21ab0392b4435e754b716fa1/yarl-1.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/97/e7/af7219a0fe240e8ef6bb555341a63c43045c21ab0392b4435e754b716fa1/yarl-1.6.3.tar.gz
Summary  : Yet another URL library
Group    : Development/Tools
License  : Apache-2.0
Requires: yarl-license = %{version}-%{release}
Requires: yarl-python = %{version}-%{release}
Requires: yarl-python3 = %{version}-%{release}
Requires: idna
Requires: multidict
Requires: typing_extensions
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : multidict
BuildRequires : typing_extensions

%description
====

%package license
Summary: license components for the yarl package.
Group: Default

%description license
license components for the yarl package.


%package python
Summary: python components for the yarl package.
Group: Default
Requires: yarl-python3 = %{version}-%{release}

%description python
python components for the yarl package.


%package python3
Summary: python3 components for the yarl package.
Group: Default
Requires: python3-core
Provides: pypi(yarl)
Requires: pypi(idna)
Requires: pypi(multidict)

%description python3
python3 components for the yarl package.


%prep
%setup -q -n yarl-1.6.3
cd %{_builddir}/yarl-1.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605547051
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yarl
cp %{_builddir}/yarl-1.6.3/LICENSE %{buildroot}/usr/share/package-licenses/yarl/629aef675d0010dc7bc7e08ef043868759e5fd09
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yarl/629aef675d0010dc7bc7e08ef043868759e5fd09

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
