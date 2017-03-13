#!/usr/bin/perl
#MediaLIB.pm

#=================#
# Media Functions #
#=================#

package MediaLIB;

use Term::ANSIColor;
use strict;
#use warnings FATAL => 'all';
require mod::FormatLIB;
require mod::TidyLIB;

=head1 NAME

mod::MediaLIB - The great media functions !!

=head1 VERSION

Version 1.0

=cut

our $VERSION = '1.0';

=head1 SYNOPSIS

MediaLIB is the main module for FormatLIB and TidyLIB

=cut

=head1 SUBROUTINES/METHODS

=head2 my_format

=cut

sub my_format
{
    my $dir  = shift @_;
    my $mode = shift @_;
    my $var  = "";
    my $cpt = 0;
    opendir (DIR, $dir) or die $!;
    chdir($dir);
    while (my $file = readdir(DIR))
    {
	# Use a regular expression to find files ending in .avi .mp4 and .mkv
	next unless ($file =~ m/\.(avi|mp4|mkv)$/);
	if    ($file =~ m/S[0-9]{2}E[0-9]{2}/)
	{
	    if ($mode == 1)
	    {
		print color("green"), "-- SERIE -- ", color("reset");
	    }
	    $var = &FormatLIB::format_serie($file);
	    if ($mode == 1)
	    {
		print "rename : $file => $var\n";
	    }
	}
	else
	{
	    if ($mode == 1)
	    {
		print color("red"), "-- MOVIE -- ", color("reset");
	    }
	    $var = &FormatLIB::format_movie($file);
	    if ($mode == 1)
	    {
		print "rename : $file => $var\n";
	    }
	}
	rename $file, $var;
    }
    closedir(DIR);
    exit 0;
}

=head2 list

=cut

sub list
{
    my $dir = shift @_;
    my $csv = shift @_;
    my $mode = shift @_;
    my $cpt = 0;
    opendir (DIR, $dir) or $!;
    chdir($dir);
    if ($mode == 1)
    {
	print "\tCreate Directory\n";
    }
    while (my $file = readdir(DIR))
    {
	next unless ($file =~ m/\.(avi|mp4|mkv)$/);
	if ($file =~ m/S[0-9]{2}E[0-9]{2}/)
	{
	    my $tmp1 = $file;
	    my $tmp2 = $file;
	    $tmp1 =~ s/S[0-9]{2}E[0-9]{2}\.(avi|mkv|mp4)//;
	    $tmp1 =~ s/\_$//;
	    $tmp2 =~ s/(.*)(S[0-9]{2})(.*)/$2/;
	    if (! -e $tmp1) {&TidyLIB::createDir($tmp1,$mode);$cpt++}
	    if (! -e "$tmp1/$tmp2") {&TidyLIB::createDir("$tmp1/$tmp2",$mode);$cpt++}
	    rename $file, "$tmp1/$tmp2/$file";
	}
	else
	{
	    &TidyLIB::readCSV($csv,0);
	    my $tmp3 = $file;
	    $tmp3 =~ tr/\_/ /;
	    $tmp3 =~ s/(.*)\.(avi|mp4|mkv)$/$1/;
	    my $tmp4 = &TidyLIB::findMovie($tmp3,0);
	    $tmp4 =~ s/^"(.*)"$/$1/;
	    $tmp4 =~ tr/ /\_/;
	    if ($tmp4 eq "") {$tmp4 = "none";}
	    if (! -e $tmp4) {&TidyLIB::createDir($tmp4,$mode);$cpt++}
	    rename $file, "$tmp4/$file";
	}
    }
    if ($mode == 1)
    {
	if ($cpt eq 0) {print color("red"), "\t-- Not Need To Create--\n", color("reset");};
    }
    closedir(DIR);
    exit 0;
}

=head1 AUTHOR

sbksba, C<< <sbksba at gmail.com> >>

=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc mod::MediaLIB


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
