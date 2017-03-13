#!/usr/bin/perl -s
require 'mod/MediaLIB.pm';
$dir ||= ".";
$mode ||= 0;
MediaLIB::my_format($dir,$mode);
