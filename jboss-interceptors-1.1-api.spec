%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .20120319git49a904
%global namedversion %{version}%{?namedreltag}

Name:             jboss-interceptors-1.1-api
Version:          1.0.2
Release:          0.10%{namedreltag}.2
Summary:          Interceptors 1.1 API
Group:		  Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-interceptors-api_spec.git jboss-interceptors-1.1-api
# cd jboss-interceptors-1.1-api/ && git archive --format=tar --prefix=jboss-interceptors-1.1-api/ 49a90471d8108b5b2a2da6063b5591a9f41ed24a | xz > jboss-interceptors-1.1-api-1.0.2.20120319git49a904.tar.xz
Source0:          jboss-interceptors-1.1-api-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
This package contains The JavaEE Interceptors 1.1 API classes from JSR 318.

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-interceptors-1.1-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.7.20120319git49a904
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.2-0.6.20120319git49a904
- Resolves #961458 - Removed unneeded maven-eclipse-plugin and 
  maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.5.20120319git49a904
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-0.4.20120319git49a904
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.2-0.3.20120319git49a904
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.2.20120319git49a904
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-0.1.20120319git49a904
- Packaging after license cleanup upstream

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309git31d37b
- Packaging after license cleanup upstream

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

