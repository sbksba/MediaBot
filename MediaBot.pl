#!/usr/bin/perl -s
#===========#
# Media Bot #
#===========#
#
# this script wait new download, format it and xml file (also sort them in directory)
# and it is a bot so it works always !!!!
#
use strict;

my $defaultDir = "test";
my $defaultCSV = "films.csv";

if ($ARGV[0] eq "v")
{
    print '
 ___  ___ ___________ _____  ___   ______  _____ _____ 
 |  \/  ||  ___|  _  \_   _|/ _ \  | ___ \|  _  |_   _|
 | .  . || |__ | | | | | | / /_\ \ | |_/ /| | | | | |  
 | |\/| ||  __|| | | | | | |  _  | | ___ \| | | | | |  
 | |  | || |___| |/ / _| |_| | | | | |_/ /\ \_/ / | |  
 \_|  |_/\____/|___/  \___/\_| |_/ \____/  \___/  \_/

';
    print "MediaBot running...\n";
    print "[verbose mode]\n";
    if ($ARGV[1] eq "")
    {
	print "\n\tDirectory : $defaultDir\n";
	system "./mod/format.pl -dir=$defaultDir -mode=1";
	system "./mod/directory.pl $defaultDir $defaultCSV v";
    }
    else
    {
	foreach my $dir(@ARGV)
	{
	    if ($dir eq "v"){}
	    else
	    {
		print "\n\tDirectory : $dir\n";
		system "./mod/format.pl -dir=$dir -mode=1";
		system "./mod/directory.pl $dir $defaultCSV v";
	    }
	}
    }
}
else
{
    if ($ARGV[0] eq "")
    {
	system "./mod/format.pl -dir=$defaultDir -mode=0";
	system "./mod/directory.pl $defaultDir $defaultCSV";
    }
    else
    {
	foreach my $dir(@ARGV)
	{
	    system "./mod/format.pl -dir=$dir -mode=0";
	    system "./mod/directory.pl $dir $defaultCSV";
	}
    }
}
