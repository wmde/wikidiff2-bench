<?php

if(!extension_loaded("wikidiff2"))
{
    print("wikidiff2 extension not loaded\n");
    exit(1);
}

$best= 31337;
for($i= 0; $i<3; ++$i)  // take best of three
{
    $time= microtime(true);
    $result= wikidiff2_do_diff(file_get_contents($argv[1]), file_get_contents($argv[2]), 1);
    $time= microtime(true) - $time;
    if($time < $best)
        $best= $time;
}
print $best;
print "\n";

?>
