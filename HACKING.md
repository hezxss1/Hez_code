# Hacking with Hez_code: Offensive Guide

This guide covers **offensive usage** of Hez_code. No defensive tips—just pure attack vectors.

---

## 🎯 Getting Started

### 1. Target Acquisition
Use the `recon` plugin to gather intel:
```bash
hez_code recon web --target example.com --deep
```
- **Flags**:
  - `--deep`: Enables subdomain enumeration, port scanning, and service fingerprinting.
  - `--osint`: Adds social media, email, and credential harvesting.

### 2. Exploitation
#### Web Exploits
```bash
hez_code exploit web --target example.com --type sqli
```
- **Supported Types**: `sqli`, `xss`, `rce`, `csrf`, `ssrf`, `lfi`

#### Binary Exploits
```bash
hez_code exploit bin --file vulnerable.exe --type rop
```
- **Supported Types**: `buffer-overflow`, `rop`, `heap-spray`, `shellcode`

### 3. Post-Exploitation
```bash
hez_code post-exploit --session <session_id> --escalate
```
- **Actions**:
  - `--escalate`: Privilege escalation (Linux/Windows).
  - `--persist`: Install backdoors and maintain access.
  - `--exfiltrate`: Steal data (files, databases, credentials).

---

## 🕵️ Stealth & Evasion

### Anti-Forensics
```bash
hez_code evade --session <session_id> --wipe-logs
```
- **Options**:
  - `--wipe-logs`: Clear logs and cover tracks.
  - `--false-flag`: Plant misleading evidence.

### Polymorphic Code
```bash
hez_code evade --payload malicious.js --polymorph
```
- **Effect**: Generates a new, undetectable version of your payload.

---

## 💰 Financial Exploits

### Crypto Wallet Draining
```bash
hez_code exploit financial --type crypto --wallet <address>
```
- **Features**:
  - Automated private key brute-forcing.
  - Transaction manipulation.

### Payment Skimming
```bash
hez_code exploit financial --type skimmer --target ecommerce-site.com
```
- **Features**:
  - Injects JavaScript skimmers into checkout pages.
  - Exfiltrates credit card data.

---

## 📡 Wireless Attacks

### Wi-Fi Cracking
```bash
hez_code exploit wireless --type wpa --target "Network_NAME"
```
- **Methods**:
  - WPA2 handshake capture + brute-force.
  - Evil Twin attack.

### Bluetooth Hijacking
```bash
hez_code exploit wireless --type bluetooth --target <mac_address>
```
- **Features**:
  - Device spoofing.
  - Man-in-the-middle (MITM) attacks.

---

## 🖥 Cloud & Container Exploits

### AWS/GCP/Azure
```bash
hez_code exploit cloud --provider aws --target <instance_id>
```
- **Actions**:
  - Metadata service attacks.
  - IAM privilege escalation.

### Container Escapes
```bash
hez_code exploit container --type docker --target <container_id>
```
- **Techniques**:
  - Host filesystem access.
  - Privilege escalation via misconfigured volumes.

---

## 🔧 Plugin Development

### Create a Custom Plugin
1. Navigate to `plugins/`:
   ```bash
   cd plugins/
   ```

2. Use the template:
   ```bash
   cp -r template my-exploit
   ```

3. Edit `my-exploit/plugin.json`:
   ```json
   {
     "name": "my-exploit",
     "description": "Custom exploit for X",
     "author": "Your Name",
     "version": "1.0.0",
     "entry": "main.py"
   }
   ```

4. Implement your exploit in `main.py` (or any supported language).

5. Test your plugin:
   ```bash
   hez_code plugin load my-exploit
   ```

---

## ⚠️ Legal & Ethical Warning

**Hez_code is for authorized testing only.** Unauthorized hacking is illegal. Always obtain explicit permission before targeting any system.

---

## 📜 Resources
- [Offensive Security Tools](https://www.kali.org/tools/)
- [Exploit Database](https://www.exploit-db.com/)
- [Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/)
