%define oname inochi

Summary:    Gives life to Ruby projects
Name:       rubygem-%{oname}
Version:    5.1.0
Release:    %mkrel 1
Group:      Development/Ruby
License:    ISC License
URL:        http://snk.tuxfamily.org/lib/inochi/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(detest) >= 3.1.0
Requires:   rubygem(ember) >= 0.3.0
Requires:   rubygem(highline) >= 1.5
Requires:   rubygem(mechanize) >= 1
Requires:   rubygem(nokogiri) >= 1.4
Requires:   rubygem(rake) >= 0.8.4
Requires:   rubygem(yard) >= 0.5.8
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Inochi is an infrastructure that helps you create, test, document, package,
publish, and announce your [Ruby] projects.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

# Move manpages to mandir
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/* %{buildroot}/%{_mandir}
rmdir %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/inochi
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CREDITS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_mandir}/man1/%{oname}.1.*
