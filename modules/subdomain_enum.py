import subprocess

def run_sublist3r(domain):

    print(f"[+] Running Sublist3r on {domain}")

    command = [
        "python3",
        "Sublist3r/sublist3r.py",
        "-d",
        domain
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    subdomains = []

    for line in result.stdout.splitlines():

        if domain in line:
            subdomains.append(line.strip())

    return list(set(subdomains))
