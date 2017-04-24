<?php

if(!extension_loaded("wikidiff2"))
    if(!dl("wikidiff2.so"))
    {
        print "couldn't load wikidiff2.so\n";
        exit(1);
    }

print_r(wikidiff2_do_diff("foo", "bar", 5));

?>
