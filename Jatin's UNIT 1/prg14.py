# Diffie-Hellman Key Exchange Algorithm

# Function to calculate (base^exp) % mod
def power(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod

    return result


# Function to generate public key
def diffie_hellman(p, g, private_key):
    return power(g, private_key, p)


# Example values
p = 23
g = 5

# Private keys
private_key_alice = 6
private_key_bob = 15

# Public keys
public_key_alice = diffie_hellman(p, g, private_key_alice)
public_key_bob = diffie_hellman(p, g, private_key_bob)

# Shared secret keys
shared_secret_alice = power(public_key_bob, private_key_alice, p)
shared_secret_bob = power(public_key_alice, private_key_bob, p)

# Print results
print("Public Key for Alice:", public_key_alice)
print("Public Key for Bob:", public_key_bob)
print("Shared Secret Key for Alice:", shared_secret_alice)
print("Shared Secret Key for Bob:", shared_secret_bob)