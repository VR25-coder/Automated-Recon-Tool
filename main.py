from modules.subdomain_enum import run_sublist3r
from modules.dns_bruteforce import brute_force
from modules.email_osint import harvest_emails
from modules.tech_fingerprint import detect_technologies
from modules.report_generator import generate_report

domain = input("Enter target domain: ")

print("[+] Starting Recon...")

subdomains = run_sublist3r(domain)

dns_results = brute_force(
    domain,
    "wordlists/subdomains.txt"
)

emails = harvest_emails(domain)

technologies = detect_technologies(
    f"https://{domain}"
)

report_data = {
    "domain": domain,
    "subdomains": list(set(subdomains + dns_results)),
    "emails": emails,
    "technologies": technologies
}

generate_report(report_data)

print("[+] Recon Completed")
