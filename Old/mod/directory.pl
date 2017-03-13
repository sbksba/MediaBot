#!/usr/bin/perl
require 'mod/MediaLIB.pm';

if ($ARGV[2] eq "v")
{
    MediaLIB::list($ARGV[0],$ARGV[1],1);
}
else
{
    MediaLIB::list($ARGV[0],$ARGV[1],0);
}
