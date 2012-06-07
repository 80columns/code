#!/usr/bin/perl

use Digest::SHA;

$sha = Digest::SHA->new(sha256);

for ($i = 0; $i <= $#ARGV; $i++)
{
    if (-e $ARGV[$i])
    {
        $sha->addfile($ARGV[$i]);
        $digest = $sha->hexdigest;
        print "$digest  $ARGV[$i]\n";
    }
    else
    {
        print "$ARGV[$i]: No such file or directory\n";
    }
}
