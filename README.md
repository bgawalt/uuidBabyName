uuidBabyName
============

A python utility to turn a 36 hex-char UUID into a human-pronounceable baby name. Inspired by Darius "@tinysubversions" Kazemi: https://twitter.com/tinysubversions/status/336947808059936769

The pronounceability gag is stolen from hastebin, http://hastebin.com/, with their clever alternate-consonants-and-vowels trick.

The name-generation itself is fully deterministic, which is an interesting twist to me: a lot of the fun CPU-generated-text stuff I do depends on a random number generator to produce its fun outcomes (a la @fakespearean, http://twitter.com/fakespearean). I guess in this case I'm just outsourcing the RNG to the UUID part. But it's still cool that these names are kind of hiding inside the ugly "55ed2e23-bb45-4e25-abff-033a42927663" string -- given the UUID, we don't need to rely on (additional) luck in order to reveal the name "Wa Meka Rutoki-Boporez-Yu."

My favorite name yet: "edf881dc-c811-4e71-b316-3b3ad48ffe71" actually means "Fito Gipupod."

A WARNING: Some steps it takes, like stripping out multiple consecutive whitespace characters, means that the baby names are no longer (necessarily) unique themselves. Two different UUIDs can yield the same baby name.