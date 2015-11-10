Name:           avro
Version:        1.7.7
Release:        0
Summary:        Build schemas and validation.
Group:          Applications/Data
License:        Apache
URL:            https://avro.apache.org/
Vendor:         Apache Avro
Source:         http://mirrors.viethosting.vn/apache/avro/avro-1.7.7/c/avro-c-1.7.7.tar.gz
Prefix:         avrolib
Packager:           Hieu Tran Trung
BuildRoot:      /root/rpmbuild/BUILD

%description
Avro to build schema and validation

%prep
tar -xzvf /root/rpmbuild/SOURCES/avro-c-1.7.7.tar.gz

%build
cd avro-c-1.7.7
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=avrolib -DCMAKE_BUILD_TYPE=Release

%install
cd avro-c-1.7.7/build
make
make test
cp -f ../src/avro-c.pc.in ./src/avro-c.pc
sudo make install
mkdir -p $RPM_BUILD_ROOT/lib/
mkdir -p $RPM_BUILD_ROOT/src/
cp -rf  avrolib/lib/* $RPM_BUILD_ROOT/lib/
cp -rf  ../src/* $RPM_BUILD_ROOT/src/

%post
# the post section is where you can run commands after the rpm is installed.
cp -rf lib/* /usr/lib64/
cp -rf lib/* /usr/lib/
cp -rf src/avro.h /usr/include/
cp -rf src/avro /usr/include/

%files
%defattr(-,root,root)
/lib
/src
