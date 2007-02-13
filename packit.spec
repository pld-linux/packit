Summary:	Network auditing tool
Summary(pl.UTF-8):	Narzędzie do sprawdzania sieci
Name:		packit
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://packit.sourceforge.net/downloads/%{name}-%{version}.tgz
# Source0-md5:	270594ff97f6c203131136208bb4d2ca
Patch0:		%{name}-bpf.patch
URL:		http://packit.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libnet-devel >= 1:1.1.2
BuildRequires:	libpcap-devel
Requires:	libnet >= 1:1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Packit (Packet toolkit) is a network auditing tool. Its value is
derived from its ability to customize, inject, monitor, and manipulate
IP traffic. By allowing you to define (spoof) nearly all TCP, UDP,
ICMP, IP, ARP, RARP, and Ethernet header options, Packit can be useful
in testing firewalls, intrusion detection/prevention systems, port
scanning, simulating network traffic, and general TCP/IP auditing.
Packit is also an excellent tool for learning TCP/IP.

%description -l pl.UTF-8
Packit jest narzędziem służącym do sprawdzania sieci. Jego wartość
wywodzi się z możliwości dostosowywania, wysyłania, monitorowania i
manipulacji ruchem sieciowym. Packit umożliwia zdefiniowanie prawie
wszystkich opcji nagłówków TCP, UDP, ICMP, IP, ARP, RARP, i Ethernet,
przez co może być użytecznym w testowaniu zapór sieciowych, systemach
zapobiegania włamaniom, symulowaniu ruchu sieciowego, i ogólnym
sprawdzaniu TCP/IP. Packit jest także znakomitym narzędziem do nauki
TCP/IP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/packit.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/ICMP.txt ChangeLog
%attr(755,root,root) %{_sbindir}/packit
%{_mandir}/man8/*
