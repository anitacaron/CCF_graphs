#!/bin/sh

docker run -m 12g  -v $PWD:/work -w /work --rm -ti monarchinitiative/ubergraph "$@"
