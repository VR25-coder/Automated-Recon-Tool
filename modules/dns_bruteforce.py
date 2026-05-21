import dns.resolver

def brute_force(domain, wordlist):

    found = []

    with open(wordlist) as file:
        words = file.read().splitlines()

    for sub in words:

        target = f"{sub}.{domain}"

        try:
            dns.resolver.resolve(target, "A")

            print(f"[FOUND] {target}")

            found.append(target)

        except:
            pass

    return found
