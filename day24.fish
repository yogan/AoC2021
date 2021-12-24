#!/usr/bin/env fish
for line in (seq 18)
    echo
    echo Line $line
    for infile in inputs/24/*txt.*
        sed -n {$line}p $infile
    end
end
