my $i = 0;
$c = 0;
while(<>)
{
	chomp;
	/^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$/;
	$s1 = $1;
	$e1 = $2;
	$s2 = $3;
	$e2 = $4;
	print "|$_| -> ($s1,$e1),($s2,$e2) : ";
	if (($s1 >= $s2 && $e1 <= $e2) || ($s2 >= $s1 && $e2 <= $e1)) {
		print "!";
		$c++;
	}

	if (
(($s1 <= $s2) && ($s2 <= $e1))||(($s1 <= $e2) && ($e2 <= $e1))
||
(($s2 <= $s1) && ($s1 <= $e2))||(($s2 <= $e1) && ($e1 <= $e2))
){
		print "*";
		$i++;
	}
	print "\n";
}
print "$c\n";
print "$i\n";
