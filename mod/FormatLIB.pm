#!/usr/bin/perl
#FormatLIB.pm

#=====================================#
# Functions to format movie and serie #
#=====================================#

package FormatLIB;

use Term::ANSIColor;
use strict;
use warnings FATAL => 'all';

=head1 NAME

mod::FormatLIB - The great formatting !!

=head1 VERSION

Version 1.0

=cut

our $VERSION = '1.0';

=head1 SYNOPSIS

FormatLIB is a perl module that rename the media files in the directory.

A little example of usage.

    require 'mod/FormatLIB.pm'

    FormatLIB::my_format($directory,$mode);

$mode = 1 for a verbose mode and 0 for a non verbose mode.

=cut

=head1 SUBROUTINES/METHODS

=head2 format_movie

=cut

sub format_movie
{
    my $var = shift @_;
    my @tab = ("20[0-9]{2}","19[0-9]{2}","(AC|ac)[0-9]{1}","(x|X)[0-9]{3}-Pop","(x|X)[0-9]{3}","(H|h)[0-9]{3}","R[0-9]{1}","Pimp[0-9]{4}","(DTS|HDTS)","DD[0-9]{1}","[0-9]{3}(MB|mb)","(V|R)[0-9]{1}","MP[0-9]{1}","dvdrip","(1080|720|480)(p|P)","(TRUEFRENCH|TRUFRENCH|truefrench)","(FRENCH|french)","(ENGLISH|ENG)","VOSTFR","BRR(iP|ip|IP)","(brrip|BRrip)","BD(Rip|RIP|RiP)","bdrip","(BluRay|bluray|Bluray|BLURAY)","DVDR(IP|ip|iP)","DVDrip","DVD(SCR|Scr|scr)","WiHD","HD(CAM|TV|Rip|RiP)","HD","C(AM|am)","WEB(Rip|RiP|riP)","WEB-DL","MD","X(ViD|viD|vid|VID|Vid)","RERIP","AUDIO","AAC","Source","New","PROPER","BladeBDP","ARTEFAC","(RARBG|rarbg)","QCP","VAiN","Visual","NEW","ShAaNiG","RARBG","SOURCE","HC","BLiTZCRiEG","CH","WEEDMADE","S.V","rough","YIFY","MOi","UTT","CRYS","Isisatis","goatlove","NIKOo","MAXSPEED","ATN","VERSUS","Dossinet","(DesTroY|destroy)","SHiFT","STVFRV","FRV","STR","SLaP","FB","FANSUB","SUBFORCED","BROTHERS","CARPEDIEM","REPACK","TiTAN","TMB","CPG","READNFO","SVR","US","SaM","ETRG","CpasBien","REsuRRecTioN","NIKOo","(GLUPS|glups)","FIRST","www\.torentz\.3xforum\.ro","TS","MrSeeN","SiMPLE","ADDiCTiON","KRiNe","(RELIC|relic|RELiC)","ooOoo","VENUM","LiBERTY","FIX","Hive","CM[0-9]{1}","(HQ|Hq|hq)","LiberTeam","Z[0-9]{1}","REMUX","MULTi","^Pop'$'","Ofek","MAXSPEED","BluDragon","(anoXmous|anoxmous)","AiRLiNE","Remastered","dvdsize","quality","murdoc[0-9]{2}","yify","aac","(extended|EXTENDED|Extended)","BLOW","x0r","AVC","w{3}","OMGTORRENT","com","cinefile","AtomicGdog","zetorrents","ofek","ShowFr","zip","(blu|Blu)","ray","MA","fullhd","best","gaia","filou","5.1","(Final|final)","(Cut|cut)","Rip","vf","vost","dir","MURD3R","AViTECH","AViTE","RaStA","walt\.disney\.","Walt Disney - ","UNRATED","WEB","RIP","FANTA","BLUB","KK3N","Slay3R","TeamSuW","ZT","cpasbien","pw","Mystic","BoSs","RUDY","LOST","VENUE","SANSDouTE","LYS","MZISYS","MRG","zone","telechargement","Cortex91","EXTREME","ViVi");
    $var =~ s/^\[.*\]\s*//;
    my $data;
    foreach $data (@tab)
    {
	$var =~ s/$data//;
    }
    $var =~ tr/)(//d;
    $var =~ tr/[\. \-\+]/\_/;
    $var =~ tr/{\. \-\+}/\_/;
    $var =~ tr/\[.*\]//;
    $var =~ s/\_(avi|mp4|mkv)$/\.$1/;
    $var =~ s/\_*\./\./;
    return $var;
}

=head2 format_serie

=cut

sub format_serie
{
    my $var = shift @_;
    $var =~ s/\(.*\)\s*//;
    $var =~ s/US\.//;
    $var =~ s/FASTSUB\.//;
    $var =~ s/VOSTFR\.//;
    $var =~ s/\.201[0-9]\./ /;
    $var =~ s/^\[.*\]\s*//;
    $var =~ tr/[\. \-]/\_/;
    $var =~ s/\_(avi|mp4|mkv)$/\.$1/;
    $var =~ s/(.*(S[0-9]{2}E[0-9]{2}))(.*)(\.(avi|mp4|mkv))$/$1$4/;
    return $var;
}

=head1 AUTHOR

sbksba, C<< <sbksba at gmail.com> >>

=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc mod::FormatLIB


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

Copyright 2016 sbksba

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

=cut

1;
