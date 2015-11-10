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
cp -rf /root/rpmbuild/SOURCES/avro-c-1.7.7.tar.gz /root/rpmbuild/BUILD/

%install
mkdir -p $RPM_BUILD_ROOT/
cp -rf * $RPM_BUILD_ROOT/

%post
# the post section is where you can run commands after the rpm is installed.
tar -xzvf avro-c-1.7.7.tar.gz
cd avro-c-1.7.7
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=avrolib -DCMAKE_BUILD_TYPE=Release
make
make test
cp -f ../src/avro-c.pc.in ./src/avro-c.pc
sudo make install
cp -rf avrolib/lib/libavro.* /usr/lib64/
cp -rf avrolib/lib/libavro.* /usr/lib/
cp -rf ../src/* /usr/include/

%files
%defattr(-,root,root)
/
