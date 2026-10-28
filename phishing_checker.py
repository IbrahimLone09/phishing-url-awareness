import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Could not parse this URL."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("PHISHING URL AWARENESS CHECKER")
    print("Text checks only - URLs are not opened.")
    print("=" * 45)

    while True:
        raw_url = input("\nEnter a sample URL (or q to quit): ").strip()

        if raw_url.lower() == "q":
            print("Checker closed.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        warnings = [
            item for item in findings
            if item not in (
                "No listed warning signs found. This does NOT prove safety.",
                "No URL entered.",
                "Could not identify a hostname.",
                "Could not parse this URL."
            )
        ]

        if warnings:
            print("\nREVIEW CAREFULLY: Warning signs were found.")
        elif raw_url:
            print("\nNo listed warning signs detected.")

        print("Never enter passwords through unexpected links.")


if __name__ == "__main__":
    main()