%global debug_package %{nil}
Name:           linglong-box
Version:        2.0.0
Release:        1
Summary:        Linglong sandbox
License:        LGPLv3
URL:            https://github.com/OpenAtom-Linyaps/linyaps-box
Source0:        linyaps-box.zip

BuildRequires:  cmake gcc-c++ glib2-devel glibc-static libstdc++-static gtest-devel gmock-devel libseccomp-devel libcap-devel
Requires:       linglong-bin >= 1.9.0
Requires:       desktop-file-utils erofs-fuse
Requires:       glib2 shared-mime-info erofs-utils
Requires:       google-noto-sans-mono-fonts wqy-zenhei-fonts wqy-microhei-fonts

%description
Linglong sandbox with OCI standard.

%prep
%autosetup -p1 -n linyaps-box-%{version}

%define _debugsource_template %{nil}

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
      -DBUILD_SHARED_LIBS=OFF \
      -Dlinyaps-box_CPM_LOCAL_PACKAGES_ONLY=ON ..
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%files
%license LICENSE
%{_bindir}/ll-box


%changelog
* Thu Jun 26 2025 chenchenjun <chenjiehai1024@gmail.com> - 2.0.0-1
- Follow the upstream version 2.0.0-1
