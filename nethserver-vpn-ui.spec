Summary: NethServer VPN UI module
Name: nethserver-vpn-ui
Version: 1.2.6
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
# Build Source1 by executing prep-sources
Source1: %{name}-cockpit.tar.gz

BuildArch: noarch

Requires: nethserver-firewall-base

BuildRequires: nethserver-devtools

%description
VPN UI module for NethServer.


%prep
%setup -q

%build
sed -i 's/_RELEASE_/%{version}/' %{name}.json
%{makedocs}

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/nethserver-vpn-ui/
tar xf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/nethserver-vpn-ui/

%{genfilelist} %{buildroot} --file /etc/sudoers.d/50_nsapi_nethserver_vpn_ui 'attr(0440,root,root)' > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Fri Nov 22 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.6-1
- OpenVPN: re-created user can't access roadwarrior server - Bug NethServer/dev#5949

* Thu Nov 21 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.5-1
- UI: domain menu not correctly shown - Bug Nethserver/dev#5942

* Thu Nov 21 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.4-1
- OpenVPN tunnel: Wrong protocol written in the client configuration file - Bug NethServer/dev#5929

* Mon Oct 28 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.3-1
- Cockpit: error in managing more than 100 tunnels openvpn-server - Bug Nethserver/dev#5886
- Logs page in Cockpit - Bug NethServer/dev#5866

* Thu Oct 10 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- Cockpit: improve English labels - NethServer/dev#5856

* Mon Oct 07 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Cockpit downloads fail on Firefox - Bug Nethserver/dev#5855

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- OpenVPN RW: host duplication when editing reserved IP - Bug NethServer/dev#5850
- Sudoers based authorizations for Cockpit UI - NethServer/dev#5805

* Wed Sep 18 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- Statistics on OpenVPN connections - NethServer/dev#5827

* Tue Sep 03 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Cockpit. List correct application version - Nethserver/dev#5819

* Fri Jul 05 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Prevent failures if some VPN  modules are not installed

* Wed Jun 19 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- VPN Cockpit UI - NethServer/dev#5760

* Thu May 16 2019 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 0.0.0-0
- First implementation
