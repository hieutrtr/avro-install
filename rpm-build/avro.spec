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
cp -rf  avrolib/lib/libavro.a $RPM_BUILD_ROOT/lib/
cp -rf  avrolib/lib/libavro.so $RPM_BUILD_ROOT/lib/
cp -rf  avrolib/lib/libavro.so.22.0.0 $RPM_BUILD_ROOT/lib/
cp -rf  ../src/avro.h $RPM_BUILD_ROOT/src/
cp -rf  ../src/avro $RPM_BUILD_ROOT/src/
cp -rf  ../src/avro-c.pc $RPM_BUILD_ROOT/src/

%post
# the post section is where you can run commands after the rpm is installed.
cp -rf lib/libavro.a /usr/lib64/
cp -rf lib/libavro.so /usr/lib64/
cp -rf lib/libavro.so.22.0.0 /usr/lib64/
cp -rf lib/libavro.a /usr/lib/
cp -rf lib/libavro.so /usr/lib/
cp -rf lib/libavro.so.22.0.0 /usr/lib/
cp -rf src/avro.h /usr/include/
cp -rf src/avro /usr/include/
cp -rf src/avro-c.pc /usr/lib64/pkgconfig/
cp -rf src/avro-c.pc /usr/lib/pkgconfig/

%files
%defattr(-,root,root)
/lib
/src
