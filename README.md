# 🛡️ ThreatLedger — Universal Security Workstation (V1.0)

ThreatLedger is a high-performance, dark-mode Security Operations (SecOps) ingestion workstation designed to parse, normalize, and visualize fragmented network telemetry logs. Built using a localized rule engine and an optimized front-end pipeline, the platform transforms raw server arrays into structured, real-time cryptographic audit trails.

### 🌐 [Launch Live App: Upload & Analyze Your Own Logs Now](https://threatledger-081oo1jayshreee115rgs.streamlit.app/)
*(This is a fully interactive live website—feel free to upload any `.log`, `.csv`, or `.txt` log array file to test the universal parsing engine!)*

---

## ⚡ Core Engine Features (V1.0 Architecture)

* **Universal Log Parsing Normalization:** Ingests unstructured `.log`, `.txt`, and `.csv` network files seamlessly, normalizing varying input layouts into a single standard data schema.
* **Forensic Anomaly Triage Engine:** Automatically flags critical security events (e.g., active scanning, unauthorized state modifications) based on custom regex fallback engines and status code weights.
* **Persistent Archival Backend:** Backed by an optimized SQLite architecture, allowing users to cryptographically sign, log, and prevent duplicate entry preservation using `IntegrityError` constraints.
* **SHA-256 Cryptographic Signatures:** Every log entry undergoes localized string validation to generate a distinct cryptographic identity signature for data verification.
* **UI Performance Optimization:** Engineered with client-side message pagination constraints to effortlessly handle high-volume datasets exceeding 200+ MB without interface lag.

---

## 📋 Data Dictionary & Enterprise Schema

Below is the structured data dictionary outlining how all 18 parameters are managed under the hood within the database schema:

| Parameter Name | Data Type | Production Value & Real-World Context |
| :--- | :--- | :--- |
| **Incident_ID** | String | Unique attack session grouping tracking ID (e.g., `INC-2026-004`). |
| **Event_ID** | Integer | Real Windows/Linux event IDs (4625=Failed Login, 4624=Success, 4672=Priv Escalation). |
| **Attack_Time** | Timestamp | Exact millisecond timestamp of telemetry generation. |
| **Source_IP** | String | Threat actor's remote host IP address. |
| **Source_Country**| String | Geolocation tracking (e.g., United States, Romania, Unknown IP Proxy). |
| **Source_City** | String | Local city mapping for granular tracking (e.g., Bucharest, Austin). |
| **User_Identity** | String | Account under fire or compromise point (e.g., `Administrator`, `root`). |
| **Target_Subsystem**| String | Targeted network node, protocol daemon, or API Gateway routing layer. |
| **Attack_Type** | String | Deep-dive classification (e.g., Malware Execution, SYN Flood, Session Hijacking). |
| **MITRE_Technique**| String | Standard industry classification mapping (e.g., `T1110 - Brute Force`). |
| **Login_Attempts** | Integer | Rolling counter monitoring baseline auth failure velocity thresholds. |
| **Risk_Score** | Integer | Calculated threat metric weighting base severity, asset value, and time windows (0–100). |
| **Confidence_Score**| Integer | Statistical model precision confidence indicating your system's trust in the alert (0–100%). |
| **Threat_Level** | String | Qualitative category output derived from the Risk Score (Low, Medium, High, Critical). |
| **IOC** | String | The forensic fingerprint flagged (e.g., `malicious_payload.exe`, a rogue hash, or bad IP). |
| **Detection_Rule** | String | The exact logic/rule name triggered (e.g., `SIG_MALWARE_EXEC_01`, `BRUTE_FORCE_THRESHOLD`). |
| **Integrity_Status** | String | The cryptographic ledger status via SHA-256 validation (✅ SECURE or 🚨 TAMPERED). |
| **Action_Recommendation** | String | Immediate, step-by-step containment playbook guidelines for incident handling. |

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
