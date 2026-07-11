%global tl_name xetexconfig
%global tl_revision 45845

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	crop.cfg for XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/pkg/xetexconfig
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexconfig.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
crop.cfg for XeLaTeX

