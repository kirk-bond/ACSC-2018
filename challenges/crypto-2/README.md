# crypto-2

Can you crack the cipher? It looks like the server is using RSA to encrypt
secrets.

## Flag

acsc18{what_does_gcd_stand_for_again?}

## Hints

1. [deduct 15%] These number are too big to factor... What else can you do?
2. [deduct 70%] Is calculating the GCD of two numbers easier than factoring one?

## Steps

1. Realize that computing a GCD is a very inexpensive operation. If you have two
   numbers with shared factors, try to compute the GCD first.
2. If the GCD != 1, then you have a factor!
3. Calculate the private key from the factored modulus and decrypt the flag.
