# 🛡️ ThreatLedger — Universal Security Workstation (V1.0)

ThreatLedger is a high-performance, dark-mode Security Operations (SecOps) ingestion workstation designed to parse, normalize, and visualize fragmented network telemetry logs. Built using a localized rule engine and an optimized front-end pipeline, the platform transforms raw server arrays into structured, real-time cryptographic audit trails.

### 🚀 [Click Here to Open the Live Interactive Dashboard](https://threatledger-081oo1jayshreee115rgs.streamlit.app/)

---

## ⚡ Core Engine Features (V1.0 Architecture)

* **Universal Log Parsing Normalization:** Ingests unstructured `.log`, `.txt`, and `.csv` network files seamlessly, normalizing varying input layouts into a single standard data schema.
* **Forensic Anomaly Triage Engine:** Automatically flags critical security events (e.g., active scanning, unauthorized state modifications) based on custom regex fallback engines and status code weights.
* **Persistent Archival Backend:** Backed by an optimized SQLite architecture, allowing users to cryptographically sign, log, and prevent duplicate entry preservation using `IntegrityError` constraints.
* **SHA-256 Cryptographic Signatures:** Every log entry undergoes localized string validation to generate a distinct cryptographic identity signature for data verification.
* **UI Performance Optimization:** Engineered with client-side message pagination constraints to effortlessly handle high-volume datasets exceeding 200+ MB without interface lag.

---

## 🛠️ Technology & Matrix Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend Framework** | Streamlit | Custom Material-Dark CSS Injection |
| **Data Processing** | Pandas & `re` | Matrix DataFrames, Regular Expressions |
| **Visualization** | Plotly | Graph Objects & Dynamic Telemetry Line Gauges |
| **Storage Layer** | SQLite3 | Localized Relational Database Storage Engine |
| **Data Verification** | Python Hashlib | Secure SHA-256 Arrays |

---

## 🔮 Future Scope: Road to Version 2.0

ThreatLedger V1.0 is engineered for localized standalone processing. Future releases target enterprise scaling through the following architecture updates:

1. **Live Cloud Ingestion:** Upgrading from manual file uploads to direct API webhooks from live AWS CloudTrail and Nginx servers.
2. **Mitre ATT&CK Matrix Mapping:** Expanding the static analytics fallback to dynamically cross-reference threats with a live Mitre API framework.
3. **Multi-User RBAC:** Introducing role-based access control and encrypted user logins using institutional database backends.

---

## 👤 Author
* **jayshree** - *Core Architecture & Development*
