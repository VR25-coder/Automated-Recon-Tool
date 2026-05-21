import subprocess
import re

def harvest_emails(domain):

    command = [
        "python3",
        "theHarvester/theHarvester.py",
        "-d",
        domain,
        "-b",
        "all"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        result.stdout
    )

    return list(set(emails))
