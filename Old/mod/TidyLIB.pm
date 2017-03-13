#!/usr/bin/perl
#TidyLIB.pm

#=====================================#
# Functions to tidy up the media file #
#=====================================#

package TidyLIB;

use Term::ANSIColor;
use strict;
#use warnings FATAL => 'all';

=head1 NAME

mod::TidyLIB - The great tidying !!

=head1 VERSION

Version 1.0

=cut

our $VERSION = '1.0';

=head1 SYNOPSIS

TidyLIB is a perl module that places the directory containing the media files based on their type (film or series ) and gender.

A little example of usage.
    
    require 'mod/TidyLIB.pm'

    TidyLIB::list($directory,$csv_file,$mode);

$mode = 1 for a verbose mode and 0 for a non verbose mode.

=cut

my %tab = ();

=head1 SUBROUTINES/METHODS

=head2 readCSV

=cut

sub readCSV
{
    my $file = shift @_ or die "Error no CSV file\n";
    my $io = shift @_;
    open(my $data, '<', $file) or die "Could not open '$file' \n";
    while (my $line = <$data>)
    {
	chomp $line;
	my @fields = split ";", $line;
	$tab{$fields[0]} = $fields[1];
	if ($io eq 1)
	{
	    print "$fields[0] -- $fields[1]\n";
	}
    }
}

=head2 findMovie

=cut

sub findMovie
{
    my $film = shift @_;
    my $io = shift @_;
    while (my ($k,$v) = each (%tab))
    {
	$k =~ s/^"(.*)"$/$1/;
	if ($k eq "$film")
	{
	    if ($io eq 1) {print "$film trouve => $v\n";}
	    return $v;
	}	
    }
    
    if ($io eq 1) {print "$film non trouve\n";}
    return;
}

=head2 createDir

=cut

sub createDir
{
    my $directory = shift @_ or die "Error no directory in argument\n";
    my $mode = shift @_;
    if (! -e $directory) {if ($mode == 1) {print "create : $directory\n";}}
    unless(-e $directory or mkdir $directory) {die "Unable to create $directory\n";}
}

=head1 AUTHOR

sbksba, C<< <sbksba at gmail.com> >>

=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc mod::TidyLIB


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
