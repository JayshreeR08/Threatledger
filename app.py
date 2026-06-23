import streamlit as st
import pandas as pd
import csv
import re
import hashlib
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
import os

# --- 🚀 1. PROFESSIONAL BRANDING: Favicon & Layout Config ---
st.set_page_config(
    layout="wide", 
    page_title="ThreatLedger - Universal Workstation",
    page_icon="🛡️"
)

# --- 🎨 2. UI SPACING, ALIGNMENT & COLOR HIERARCHY ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0a0a0f !important;
    }
    
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }
    
    div[data-testid="stMetricValue"], .stDataFrame, .stPlotlyChart, .pet-card {
        background: rgba(15, 15, 26, 0.6) !important;
        border-radius: 16px;
        padding: 24px !important;
        border: 1px solid rgba(124, 58, 237, 0.15);
        margin-bottom: 24px !important;
    }

    div[data-testid="stMetricLabel"] p {
        font-size: 0.9rem !important;
        color: #94a3b8 !important;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    div[data-testid="stMetricValue"] > div {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #f8fafc !important;
    }

    h1, h2, h3, .logo-text {
        font-family: 'Syne', sans-serif !important;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .section-title {
        margin-top: 40px !important;
        margin-bottom: 20px !important;
        color: #f8fafc;
    }

    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 5px;
    }
    .logo-mark {
        background: linear-gradient(135deg, #7c3aed, #ec4899);
        padding: 10px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
    }
    .logo-text {
        font-size: 2.2rem;
        background: linear-gradient(to right, #ffffff, #cbd5e1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .logo-sub {
        color: #06b6d4;
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: -5px;
        margin-bottom: 30px;
    }

    /* --- 🐾 DYNAMIC INTERACTIVE WINDOW ANIMALS --- */
    .window-animals-container {
        position: fixed;
        bottom: 30px;
        right: 35px;
        display: flex;
        gap: 22px;
        padding: 12px 24px;
        background: rgba(15, 15, 26, 0.85);
        border: 1px solid rgba(124, 58, 237, 0.3);
        border-radius: 40px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(12px);
        z-index: 9999;
    }
    
    .window-animal {
        font-size: 1.7rem;
        cursor: pointer;
        position: relative;
        transition: transform 0.2s ease;
    }
    
    .window-animal:hover {
        transform: scale(1.4) translateY(-5px);
    }

    /* --- Dynamic Speech Bubbles on Hover --- */
    .window-animal::after {
        content: attr(data-hello); 
        position: absolute;
        bottom: 140%;
        left: 50%;
        transform: translateX(-50%) scale(0.8);
        background: #0f0f1a;
        color: #06b6d4;
        border: 1px solid rgba(6, 182, 212, 0.4);
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-family: 'Space Mono', monospace;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .window-animal::before {
        content: '';
        position: absolute;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%);
        border-width: 6px;
        border-style: solid;
        border-color: rgba(6, 182, 212, 0.4) transparent transparent transparent;
        opacity: 0;
        transition: all 0.2s ease;
    }

    .window-animal:hover::after, .window-animal:hover::before {
        opacity: 1;
    }
    
    .window-animal:hover::after {
        transform: translateX(-50%) scale(1);
    }

    .triage-card {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 16px;
        border-left: 6px solid;
    }
    .triage-high {
        background: rgba(236, 72, 153, 0.07);
        border-color: #ec4899;
        border-top: 1px solid rgba(236, 72, 153, 0.15);
        border-right: 1px solid rgba(236, 72, 153, 0.15);
        border-bottom: 1px solid rgba(236, 72, 153, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 🛡️ BRANDING HEADER RENDERING ---
st.markdown(
    """
    <div class="logo-container">
        <div class="logo-mark">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C12 22 20 18 20 12V5L12 2L4 5V12C4 18 12 22 12 22Z" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        <div class="logo-text">ThreatLedger</div>
    </div>
    <div class="logo-sub">Universal Security Intelligence Workstation</div>
    """, 
    unsafe_allow_html=True
)

# --- 🐾 FLOATING WINDOW ANIMALS ---
st.markdown(
    """
    <div class="window-animals-container">
        <span class="window-animal" data-hello="🇳🇴 Hallo! (Norwegian)" title="Fox Security Node">🦊</span>
        <span class="window-animal" data-hello="🇹🇭 สวัสดี! (Thai)" title="Bunny Tracker Engine">🐰</span>
        <span class="window-animal" data-hello="🇫🇮 Hei! (Finnish)" title="Panda Core Analyzer">🐼</span>
        <span class="window-animal" data-hello="🇷🇺 Привет! (Russian)" title="Cat Integrity Guard">🐱</span>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Fallback Intelligence Generators ---
def analyze_log_content(path_or_msg, status_or_event, ip):
    val = str(path_or_msg).lower()
    status = str(status_or_event)
    if "404" in status or "failed" in val or "critical" in val:
        return "Anomalous Vector Detected", "T1595 (Active Scanning)", 78, "High", "Investigate connection spikes from origin node immediately.", "Triggered due to anomalous file request signatures or non-standard server status responses."
    if "post" in val or "update" in val or "4625" in status:
        return "System State Modification", "T1059 (Execution)", 52, "Medium", "Review authorization parameters and session tokens.", "Flagged due to elevated payload submission vectors or credential state updates."
    return "Standard Baseline Event", "N/A", 12, "Low", "Log recorded seamlessly. Continue surveillance.", "No signatures matched malicious execution vectors."

def calculate_universal_hash(row_data):
    combined_string = "".join(str(val) for val in row_data).encode('utf-8')
    return hashlib.sha256(combined_string).hexdigest()

def universal_log_parser(file_bytes):
    raw_text = file_bytes.decode("utf-8")
    stringio = StringIO(raw_text)
    processed_records = []
    index_id = 5000
    
    conn = sqlite3.connect('threat_ledger.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS security_logs (
            Incident_ID TEXT PRIMARY KEY, Event_ID INTEGER, Attack_Time TEXT, Source_IP TEXT,
            Source_Country TEXT, Source_City TEXT, User_Identity TEXT, Target_Subsystem TEXT,
            Attack_Type TEXT, MITRE_Technique TEXT, Login_Attempts INTEGER, Risk_Score INTEGER,
            Confidence_Score INTEGER, Threat_Level TEXT, IOC TEXT, Detection_Rule TEXT, Cryptographic_Hash TEXT
        )
    """)
    conn.close()

    first_line = raw_text.splitlines()[0] if raw_text.strip() else ""
    
    if "," in first_line and "Incident_ID" in first_line:
        reader = csv.reader(stringio)
        headers = next(reader) 
        for row in reader:
            if not row or len(row) < 5: continue
            if len(row) >= 16:
                inc_id, event_id, attack_time, ip, country, city, user, subsystem, attack_type, mitre, attempts, risk, confidence, level, ioc, rule = row[:16]
                rec = "Log event cataloged. Maintain standard surveillance."
                reason = "Verified data entry from ledger baseline arrays."
                original_db_format = [inc_id, int(event_id), attack_time, ip, country, city, user, subsystem, attack_type, mitre, int(attempts), int(risk), int(confidence), level, ioc, rule]
                current_hash = calculate_universal_hash(original_db_format)
                
                display_row = original_db_format + [rec, reason, current_hash]
                processed_records.append(display_row)
            else:
                display_row = [f"INC-2026-{index_id}", 4624, "2026-06-22", row[0], "Unknown", "Unknown", "System", "Backend", "Activity Log", "N/A", 1, 10, 85, "Low", "N/A", "Default", "No base registry record found.", "Unknown context entry.", "N/A"]
                index_id += 1
                processed_records.append(display_row)
    else:
        clf_pattern = re.compile(r'(?P<ip>[\d\.]+) - - \[(?P<time>[^\]]+)\] "(?P<method>\w+) (?P<path>[^\s]+) [^"]+" (?P<status>\d+)')
        for line in raw_text.splitlines():
            line = line.strip()
            if not line: continue
            match = clf_pattern.match(line)
            if match:
                ip, attack_time, path, status = match.group("ip"), match.group("time"), match.group("path"), match.group("status")
                msg_vector = path
            else:
                parts = line.split()
                ip = parts[0] if len(parts) > 0 else "127.0.0.1"
                attack_time = parts[1] if len(parts) > 1 else "2026-06-22"
                status = "200"
                msg_vector = line
            
            inc_id = f"INC-2026-{index_id}"; index_id += 1
            att_type, mitre, risk, level, rec, reason = analyze_log_content(msg_vector, status, ip)
            base_data = [inc_id, 4624 if status == "200" else 4625, attack_time, ip, "Analyzed Endpoint", "Remote Node", "Web_Client", "App_Engine", att_type, mitre, 1 if status=="200" else 3, risk, 88, level, "N/A", "Universal_Policy", rec, reason]
            current_hash = calculate_universal_hash(base_data[:16])
            base_data.append(current_hash)
            processed_records.append(base_data)

    columns = ["Incident_ID", "Event_ID", "Attack_Time", "Source_IP", "Source_Country", "Source_City", "User_Identity", "Target_Subsystem", "Attack_Type", "MITRE_Technique", "Login_Attempts", "Risk_Score", "Confidence_Score", "Threat_Level", "IOC", "Detection_Rule", "Action_Recommendation", "Flagged_Reason", "Cryptographic_Hash"]
    return pd.DataFrame(processed_records, columns=columns)

# --- INGESTION CONTROLS ---
uploaded_file = st.file_uploader("Upload data log schema files (.csv, .txt, .log)", type=["txt", "csv", "log"])
st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    df = universal_log_parser(file_bytes)
    
    if not df.empty:
        if 'file_signed' in st.session_state and st.session_state.file_signed:
            st.success("🎉 Successfully registered new parsed records directly into threat_ledger.db local storage!")
            st.session_state.file_signed = False
            
        # --- 📈 HERO METRICS SPACING ---
        st.markdown("<h3 class='section-title'>⚡ High-Weight Vector Metrics</h3>", unsafe_allow_html=True)
        avg_risk = int(df['Risk_Score'].mean())
        avg_confidence = int(df['Confidence_Score'].mean())
        
        c_gauge1, c_gauge2 = st.columns(2)
        
        with c_gauge1:
            fig_risk = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_risk,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "⚠️ Average Operational Risk Score", 'font': {'color': "#ec4899", 'size': 15, 'family': 'Syne'}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#ffffff"},
                    'bar': {'color': "#ec4899"},
                    'steps': [
                        {'range': [0, 40], 'color': "rgba(16, 185, 129, 0.08)"},
                        {'range': [40, 75], 'color': "rgba(245, 158, 11, 0.08)"},
                        {'range': [75, 100], 'color': "rgba(236, 72, 153, 0.12)"}],
                }
            ))
            fig_risk.update_layout(template="plotly_dark", height=180, margin=dict(l=30, r=30, t=50, b=20), paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_risk, use_container_width=True)
            
        with c_gauge2:
            fig_conf = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_confidence,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "🎯 Parser Engine Confidence Gauge", 'font': {'color': "#06b6d4", 'size': 15, 'family': 'Syne'}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#ffffff"},
                    'bar': {'color': "#06b6d4"},
                    'steps': [
                        {'range': [0, 50], 'color': "rgba(236, 72, 153, 0.05)"},
                        {'range': [50, 85], 'color': "rgba(245, 158, 11, 0.05)"},
                        {'range': [85, 100], 'color': "rgba(6, 182, 212, 0.1)"}],
                }
            ))
            fig_conf.update_layout(template="plotly_dark", height=180, margin=dict(l=30, r=30, t=50, b=20), paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_conf, use_container_width=True)

        stat1, stat2, stat3 = st.columns(3)
        stat1.metric("🐼 Total Ingested Events", len(df))
        stat2.metric("💥 High Severity Vectors", len(df[df['Threat_Level'] == 'High']))
        stat3.metric("🔑 System Entry Attempt Blocks", int(df['Login_Attempts'].sum()))

        # --- 📊 VISUAL ANALYTICS ---
        st.markdown("<h3 class='section-title'>📈 Forensic Telemetry & Visual Analytics</h3>", unsafe_allow_html=True)
        
        graph_col1, graph_col2 = st.columns(2)
        
        with graph_col1:
            st.markdown("##### Incident Trends Over Timeline")
            trend_df = df.groupby('Attack_Time').size().reset_index(name='Incident Count')
            fig_trend = px.line(
                trend_df, x='Attack_Time', y='Incident Count',
                labels={'Attack_Time': 'Timeline Vector', 'Incident Count': 'Telemetry Rate'},
                markers=True
            )
            fig_trend.update_traces(line_color='#06b6d4', line_width=3, marker=dict(size=8, color='#7c3aed'))
            fig_trend.update_layout(template="plotly_dark", height=280, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig_trend, use_container_width=True)

        with graph_col2:
            st.markdown("##### Attack Type Signature Distribution")
            type_df = df['Attack_Type'].value_counts().reset_index(name='Count')
            fig_donut = px.pie(
                type_df, values='Count', names='Attack_Type',
                hole=0.5,
                color_discrete_sequence=['#7c3aed', '#ec4899', '#06b6d4', '#f59e0b']
            )
            fig_donut.update_layout(template="plotly_dark", height=280, paper_bgcolor='rgba(0,0,0,0)', showlegend=True, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig_donut, use_container_width=True)
            
        st.markdown("##### ⏳ Failed Login Tracking Array Matrix")
        login_df = df.groupby('Attack_Time')['Login_Attempts'].sum().reset_index()
        fig_login = px.bar(
            login_df, x='Attack_Time', y='Login_Attempts',
            labels={'Login_Attempts': 'Attempt Volumetrics', 'Attack_Time': 'Timeline Axis'}
        )
        fig_login.update_traces(marker_color='#ec4899', opacity=0.85)
        fig_login.update_layout(template="plotly_dark", height=240, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_login, use_container_width=True)

        # --- 🚨 HIGH-VISIBILITY EXPLAINABILITY BLOCK (HIGH THREATS ONLY) ---
        high_alerts = df[df['Threat_Level'] == 'High']
        
        if not high_alerts.empty:
            st.markdown("<h3 class='section-title'>🔍 Real-time Forensic Anomaly Triage (High Alerts Only)</h3>", unsafe_allow_html=True)
            st.markdown("<small style='color: #64748b;'>Critical incidents matching flagged threat definitions.</small><br><br>", unsafe_allow_html=True)
            
            for idx, row in high_alerts.iterrows():
                st.markdown(
                    f"""
                    <div class="triage-card triage-high">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span style="font-weight: 700; color: #f8fafc; font-size: 1.05rem;">📍 Node Incident ID: {row['Incident_ID']}</span>
                            <span style="font-weight: 800; font-family: 'Space Mono', monospace; font-size: 0.8rem; padding: 4px 10px; border-radius: 6px; background: rgba(0,0,0,0.3); color: #ec4899;">🔴 CRITICAL VECTOR</span>
                        </div>
                        <div style="font-size: 0.92rem; color: #cbd5e1; margin-bottom: 12px;">
                            <b>Classification Mapping:</b> {row['Attack_Type']} &nbsp;|&nbsp; 
                            <b>Target Vector Space:</b> {row['Target_Subsystem']} &nbsp;|&nbsp; 
                            <b>Origin Network Node:</b> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #38bdf8;">{row['Source_IP']}</code>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 0.88rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 10px;">
                            <div>
                                <span style="color: #94a3b8; font-weight: 600;">🕵️ WHY IT WAS FLAGGED:</span><br>
                                <span style="color: #cbd5e1;">{row['Flagged_Reason']}</span>
                            </div>
                            <div>
                                <span style="color: #94a3b8; font-weight: 600;">🛠️ MITIGATION / RECOMMENDED ACTION:</span><br>
                                <span style="color: #e2e8f0; font-weight: 500;">{row['Action_Recommendation']}</span>
                            </div>
                        </div>
                        <div style="margin-top: 8px; font-size: 0.75rem; color: #64748b; font-family: 'Space Mono', monospace; text-align: right;">
                            Severity Index Score: {row['Risk_Score']}/100 &nbsp;•&nbsp; Cryptographic Identity Signature: {row['Cryptographic_Hash'][:24]}...
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # --- DATA FRAME GRID MATRIX VIEW ---
        st.markdown("<h3 class='section-title'>📋 ThreatLedger Normalized Master Matrix</h3>", unsafe_allow_html=True)
        st.dataframe(df.head(100), use_container_width=True)
        
        # --- 🔒 DATABASE ARCHIVAL BUTTON CONTROL ---
        st.markdown("<br><h3 class='section-title'>✍️ Register Log File into ThreatLedger Database</h3>", unsafe_allow_html=True)
        if st.button("🔒 Cryptographically Sign & Lock File", key="sign_lock_btn"):
            conn = sqlite3.connect('threat_ledger.db')
            cursor = conn.cursor()
            for _, row in df.iterrows():
                try:
                    cursor.execute("""
                        INSERT INTO security_logs (
                            Incident_ID, Event_ID, Attack_Time, Source_IP, Source_Country, Source_City,
                            User_Identity, Target_Subsystem, Attack_Type, MITRE_Technique, Login_Attempts,
                            Risk_Score, Confidence_Score, Threat_Level, IOC, Detection_Rule, Cryptographic_Hash
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        row['Incident_ID'], int(row['Event_ID']), row['Attack_Time'], row['Source_IP'], 
                        row['Source_Country'], row['Source_City'], row['User_Identity'], row['Target_Subsystem'], 
                        row['Attack_Type'], row['MITRE_Technique'], int(row['Login_Attempts']), int(row['Risk_Score']), 
                        int(row['Confidence_Score']), row['Threat_Level'], row['IOC'], row['Detection_Rule'], 
                        row['Cryptographic_Hash']
                    ))
                except sqlite3.IntegrityError:
                    continue
            conn.commit()
            conn.close()
            
            st.session_state.file_signed = True
            st.rerun()
else:
    # --- 🐾 STANDBY DEFAULT LAYOUT ---
    st.info("👋 Workstation standing by. Ingest any network server data log array stream file above to unpack telemetry timelines.")
    st.write("### 🐾 Guard Pets on Active Duty:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pet-card">🦉 <b>Oliver the Owl</b><br><small style="color:#64748b;">Awaiting data streams to structure dynamically...</small></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pet-card">🦝 <b>Rocky the Raccoon</b><br><small style="color:#64748b;">Polishing the SHA-256 cryptographic check matrices...</small></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pet-card">🐱 <b>Cleo the Cat</b><br><small style="color:#64748b;">Scanning firewall barriers for sudden telemetry spikes...</small></div>', unsafe_allow_html=True)

# --- 🪐 PORTFOLIO METADATA BADGES ---
st.markdown("<br><hr>", unsafe_allow_html=True)
badge_col1, badge_col2, badge_col3 = st.columns(3)

with badge_col1:
    st.markdown("""
        <div style="text-align: center; background: rgba(124, 58, 237, 0.12); border: 1px solid rgba(124, 58, 237, 0.3); color: #e2e8f0; padding: 8px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
            🦊 <b>Studio Scope:</b> Security Operations Workbench
        </div>
    """, unsafe_allow_html=True)

with badge_col2:
    st.markdown("""
        <div style="text-align: center; background: rgba(236, 72, 153, 0.12); border: 1px solid rgba(236, 72, 153, 0.3); color: #e2e8f0; padding: 8px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
            📅 <b>System Clock Sync:</b> 22-06-26
        </div>
    """, unsafe_allow_html=True)

with badge_col3:
    st.markdown("""
        <div style="text-align: center; background: rgba(6, 182, 212, 0.12); border: 1px solid rgba(6, 182, 212, 0.3); color: #e2e8f0; padding: 8px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
            🪐 <b>Orbit Coordinates:</b> Live Production Pipeline
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 13px; font-weight: bold; letter-spacing: 1.5px; padding: 5px;">
         🛰️Direct from the great red spot🔴
    </div>
    """, 
    unsafe_allow_html=True
)