We know that a byte is 8 bits

with numbers that means we have 256 integers to select from which is not nearly enough, someone could request 20,000 bytes for a buffer

So how do we generate them in such a way that:

Guarentee they are unique

Maybe numbers are the wrong solution, characters offer much more choice
We cant use badchars though


UTF8 has 32 bits per character and we can combine them in unique ways so lets do that


Example

User says they was 2500 bytes

That would require 625 4 byte chunks


What about using UUIDs? Govered by RFC 4122 they can be 128 bits (16 bytes)

So each UUID generated gives us 16 bytes, the length is what protectects against collisions though

We just need to avoid reuse


We are running this stuff on 32 bit and 64 bit machines though so these values should hold as unique for the number of bytes we will generate?

For 32 bit registers this means we can have 4294967296 unique combinations which should be about 17 GB of random info?

So in theory all we need to do is generate all possible permutations of 32 bits

Could we just count numbers? No that will not be all possible combinations, would it be?

Largest possible 32 bit number is 2,147,483,647

We have to remember that with combinations order does not matter, permutations it does

Aka 10-17-23 is the same as 23-17-10 with combinations, in permutations this is not the same thing they are both different

Question still remains if we counted from 1 to 2,147,483,647 would we generate all possible 32 bit permutations. Would it not have to be?

So back to scenario, we get a request for 2501 bytes going to return that we need 625.25 numbers which is a problem because if we just take 1 byte from the 623rd number it will not be unique, so we have to round up the requested byte number to something evenly divisible (round up)


