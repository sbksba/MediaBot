#!/usr/bin/perl -s
require 'mod/FormatLIB.pm';
$dir ||= ".";
$mode ||= 0;
FormatLIB::my_format($dir,$mode);
