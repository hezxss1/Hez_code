# Financial Exploit Models

This directory contains pre-trained models and logic for:
- **Vanilla Visa Gift Cards**: BIN patterns, validation logic, redemption flows.
- **Stripe**: API abuse patterns, webhook manipulation, SK key validation.
- **Adyen**: 3D Secure bypass, payment redirect logic.
- **Shopify**: Checkout skimming, admin panel exploits.
- **PayPal**: Account takeover, phishing templates.
- **Square**: POS exploits, card data exfiltration.

## Usage

### Vanilla Visa
- **Brute-forcing**: `models/financial/vanilla/bin_patterns.json`
- **Validation**: `models/financial/vanilla/validation.py`
- **Redemption**: `models/financial/vanilla/redeem.py`

### Stripe
- **SK Key Patterns**: `models/financial/stripe/sk_patterns.json`
- **API Abuse**: `models/financial/stripe/api_abuse.py`
- **Webhook Spoofing**: `models/financial/stripe/webhook_spoof.py`

### Shopify
- **Skimming Templates**: `models/financial/shopify/skimmer.js`
- **Admin Exploits**: `models/financial/shopify/admin_exploit.py`

## Notes
- **Evasion**: All models include proxy rotation and CAPTCHA bypass logic.
- **Stealth**: Randomized delays, user-agent rotation, and session mimicry.
- **Output**: Valid cards/keys are saved to `valid_*.txt` files.