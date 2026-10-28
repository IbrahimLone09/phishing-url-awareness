# Phishing URL Awareness Checker — Test Samples

## Purpose
These tests check whether the program detects selected warning signs
in URL text. They use example domains and documentation IP addresses.

## Test 1: Normal example URL
**Input:** `https://www.example.com/login`

**Expected:** No listed warning signs found. This does NOT prove safety.

**Actual:** No listed warning signs found. This does NOT prove safety.

**Status:** PASS

## Test 2: HTTP and IP address
**Input:** `http://192.0.2.10/account`

**Expected:**
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

**Actual:** Both expected warnings were displayed.

**Status:** PASS

## Test 3: At symbol
**Input:** `http://example.com@sample.invalid/login`

**Expected:**
- Contains an @ symbol; inspect carefully.
- Uses HTTP. HTTPS alone does not prove trust.

**Actual:** Both expected warnings were displayed.

**Status:** PASS

## Test 4: Many hostname segments
**Input:** `https://a.b.c.d.e.example.invalid/path`

**Expected:** Contains many hostname segments/subdomains.

**Actual:** The expected warning was displayed.

**Status:** PASS

## Test 5: Punycode marker
**Input:** `https://xn--example.invalid/`

**Expected:** Contains a punycode-style hostname.

**Actual:** The expected warning was displayed.

**Status:** PASS

## Limitations
- These checks are simple warning signs, not a definitive phishing detector.
- A URL with no listed warning signs can still be malicious.
- The program checks URL text only and does not visit URLs.
-