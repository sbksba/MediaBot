#!/usr/bin/perl
require 'mod/TidyLIB.pm';

if ($ARGV[2] eq "v")
{
    TidyLIB::list($ARGV[0],$ARGV[1],1);
}
else
{
    TidyLIB::list($ARGV[0],$ARGV[1],0);
}
