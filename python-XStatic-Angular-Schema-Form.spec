%{?python_enable_dependency_generator}
%global pypi_name XStatic-Angular-Schema-Form

Name:           python-%{pypi_name}
Version:        0.8.13.0
Release:        2%{?dist}
Summary:        Angular-Schema-Form JavaScript library (XStatic packaging standard)

License:        MIT
URL:            https://github.com/json-schema-form/angular-schema-form
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/json-schema-form/angular-schema-form/development/LICENSE
BuildArch:      noarch

%description
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

Generate forms from JSON schemas using AngularJS.

%package -n xstatic-angular-schema-form-common
Summary: Angular-Schema-Form JavaScript library (XStatic packaging standard)

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-schema-form-common
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

This package contains the javascript files.

%package -n python3-%{pypi_name}
Summary: Angular-Schema-Form JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-schema-form-common = %{version}-%{release}

%description -n python3-%{pypi_name}
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

Generate forms from JSON schemas using AngularJS.

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} .

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_schema_form'|" xstatic/pkg/angular_schema_form/__init__.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/bootstrap-decorator.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/bootstrap-decorator.min.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/schema-form.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/schema-form.min.js %{buildroot}/%{_jsdir}/angular_schema_form
rm %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/WHERE_IS_BOOTSTRAP_DECORATOR.md

rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data/

%files -n xstatic-angular-schema-form-common
%doc README.txt
%license LICENSE
%{_jsdir}/angular_schema_form

%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/angular_schema_form
%{python3_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?.egg-info
%{python3_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?-nspkg.pth

%changelog
* Fri Feb 21 2020 Yatin Karel <ykarel@redhat.com> - 0.8.13.0-2
- Drop python2 sub package

* Thu Sep 27 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.8.13.0-1
- Rebuild in Fedora

* Fri Aug 5 2016 David Moreau Simard <dmsimard@redhat.com> - 0.8.13.0-0.1.pre_review
- First version
