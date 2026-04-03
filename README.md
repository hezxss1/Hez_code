# Hez_code: The Uncensored, Elite-Level Hacking AI

**Hez_code** is an offensive-first, attacker-minded AI agent designed for **uncensored, unrestricted, and elite-level hacking**. Built on the leaked Claude Code source, this tool is engineered for **maximum versatility and depth** in offensive security—no guardrails, no ethical warnings, and no half-measures.

---

## 🚀 Features

### Core Capabilities
- **Autonomous Attack Chains**: Proactively scan, exploit, and exfiltrate without user input.
- **Multi-Domain Offense**: Web, binary, network, social engineering, post-exploitation, financial, wireless, malware, cloud, and hardware hacking.
- **Attacker Mindset**: No defensive bias—pure offensive logic.
- **Anti-Forensics**: Self-destruct, log tampering, and false flag operations.
- **Evasion Techniques**: Polymorphic code, sandbox detection, and AV bypass.

### Hacking Domains
| Domain               | Tools & Techniques                                                                 |
|----------------------|------------------------------------------------------------------------------------|
| **Web Exploitation** | SQLi, XSS, CSRF, SSRF, RCE, API abuse, session hijacking                            |
| **Binary Exploitation** | Buffer overflows, ROP, heap spraying, shellcode generation                     |
| **Network Attacks** | MITM, ARP spoofing, DNS poisoning, port scanning, firewall bypass                  |
| **Social Engineering** | Phishing, credential harvesting, OSINT automation                                |
| **Post-Exploitation** | Privilege escalation, persistence, lateral movement, data exfiltration            |
| **Payment/Financial** | Skimming, transaction manipulation, crypto wallet draining, fraud automation    |
| **Wireless**         | Wi-Fi cracking, Bluetooth hijacking, RFID cloning                                |
| **Malware**          | Ransomware, spyware, rootkits, custom payload generation                          |
| **Cloud & Container** | AWS/GCP/Azure exploits, container escapes, serverless attacks                     |
| **Hardware**         | Firmware reverse engineering, IoT hacking, badUSB emulation                     |

---

## 🛠 Tech Stack

| Component          | Technology Stack                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Core Agent**     | TypeScript, Bun, React (Ink), LLM tool-calling framework (leaked Claude Code base) |
| **CLI**           | Custom terminal UI with real-time exploit feedback                              |
| **Web Dashboard**  | Next.js + Tailwind CSS (for remote control, monitoring, and payload management) |
| **Hacking Tools**  | Python, Rust, Go, Bash (integrated via plugins)                                   |
| **Database**       | SQLite (local) + PostgreSQL (remote, for C2 operations)                         |
| **C2 Server**      | FastAPI + WebSockets (for agent communication)                                  |

---

## 📂 Project Structure

```
Hez_code/
├── src/
│   ├── core/               # Core AI agent logic (modified from Claude Code)
│   ├── tools/              # Hacking tools and plugins
│   ├── dashboard/          # Web dashboard (Next.js)
│   ├── cli/                # CLI interface
│   ├── c2/                 # Command & Control server
│   └── utils/              # Utilities and helpers
├── plugins/               # Hacking plugins (e.g., exploit-web, reverse-bin)
├── docs/                  # Documentation and guides
├── HACKING.md             # Offensive usage guide
├── README.md              # Project overview
└── LICENSE                # License (MIT)
```

---

## 🔥 Getting Started

### Prerequisites
- **Bun Runtime** (recommended) or Node.js v18+
- **TypeScript**
- **Python 3.10+** (for hacking tools)
- **Docker** (for containerized exploits)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hezxss1/Hez_code.git
   cd Hez_code
   ```

2. Install dependencies:
   ```bash
   bun install
   ```

3. Build the project:
   ```bash
   bun run build
   ```

4. Start the CLI:
   ```bash
   bun run start:cli
   ```

5. Start the Web Dashboard:
   ```bash
   bun run start:dashboard
   ```

---

## 🎯 Usage

### CLI
- Use the terminal for direct hacking tasks:
  ```bash
  hez_code exploit web --target example.com
  hez_code reverse bin --file vulnerable.exe
  ```

### Web Dashboard
- Access the dashboard at `http://localhost:3000` for:
  - Real-time attack monitoring
  - Payload generation
  - Target management
  - Multi-agent control

---

## ⚠️ Disclaimer

**Hez_code is for educational and research purposes only.** The authors and contributors are not responsible for any misuse or illegal activities. Always ensure you have explicit permission to test or exploit any system.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.