import streamlit as st
import time
import os

# Set page configuration with original brand theme
st.set_page_config(
    page_title="AIRBOTS Aerospace — Precision Agri-Drone Robotics",
    page_icon="airbots_website/airbot_favicon.png" if os.path.exists("airbots_website/airbot_favicon.png") else "🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injecting original brand colors:
# Primary Royal Blue: #4156AF | Primary Agri Green: #1D8D49 | Deep Forest Green: #0A632D
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700;
    }

    /* Primary Accent Highlights */
    .brand-blue { color: #4156AF !important; }
    .brand-green { color: #1D8D49 !important; }
    .bg-brand-blue { background-color: #4156AF !important; color: white !important; }
    .bg-brand-green { background-color: #1D8D49 !important; color: white !important; }

    /* Top Announcement Ribbon */
    .top-ribbon {
        background: linear-gradient(90deg, #111827 0%, #1E293B 100%);
        color: #ffffff;
        padding: 10px 18px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.9rem;
        border-left: 4px solid #1D8D49;
    }
    .ribbon-badge {
        background-color: #1D8D49;
        color: white;
        padding: 2px 10px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.75rem;
        text-transform: uppercase;
        margin-right: 10px;
    }

    /* Metric Cards */
    .metric-box {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        text-align: center;
    }
    .metric-box-val {
        font-family: 'Outfit', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 4px;
    }
    .metric-box-lbl {
        font-size: 0.85rem;
        color: #64748B;
        font-weight: 600;
    }

    /* High-Impact Stat Strip */
    .stat-strip {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: white;
        border-radius: 16px;
        padding: 24px;
        margin: 24px 0;
    }

    /* Streamlit Button override with brand colors */
    div.stButton > button:first-child {
        background-color: #4156AF;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 10px 24px;
        box-shadow: 0 4px 12px rgba(65, 86, 175, 0.25);
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #2F3E83;
        box-shadow: 0 6px 16px rgba(65, 86, 175, 0.4);
    }

    /* Savings Highlight Container */
    .savings-card {
        background: #F0FDF4;
        border: 2px solid #1D8D49;
        border-radius: 14px;
        padding: 22px;
        text-align: center;
        margin-bottom: 20px;
    }
    .savings-amount {
        font-family: 'Outfit', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        color: #0A632D;
        margin: 4px 0;
    }

    /* Telemetry HUD Cockpit */
    .hud-cockpit {
        background-color: #0F172A;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        color: #F8FAFC;
    }

    /* Footer styling */
    .site-footer {
        background: #0B1120;
        color: #94A3B8;
        border-radius: 16px;
        padding: 36px 30px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Top Announcement Ribbon
st.markdown("""
<div class="top-ribbon">
    <div>
        <span class="ribbon-badge">DGCA Certified</span>
        <strong>Surya Shakti 15L</strong> is officially DGCA Type Certified! Up to 50% Government Subsidy & Easy Agri-Financing Available across India.
    </div>
    <div>
        <a href="#calculator" style="color: #60A5FA; font-weight:600; text-decoration:none;">Calculate Subsidy &rarr;</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar with Official Logo & Navigation
with st.sidebar:
    if os.path.exists("airbots_website/airbot_logo.webp"):
        st.image("airbots_website/airbot_logo.webp", use_container_width=True)
    elif os.path.exists("airbot_logo.webp"):
        st.image("airbot_logo.webp", use_container_width=True)
    else:
        st.title("AIRBOTS AEROSPACE")

    st.markdown("---")
    st.markdown("### 🧭 Portal Navigation")
    section = st.radio(
        "Explore Platform",
        [
            "🏠 Overview & Mission",
            "🚁 Surya Shakti 15L",
            "🌾 Agri-Tech Solutions",
            "💰 Farm ROI Calculator",
            "🛰️ Mission Control HUD",
            "📞 Demo Booking & Contact"
        ],
        index=0
    )

    st.markdown("---")
    st.markdown("#### 📞 Direct Operations")
    st.markdown("""
    **Phone:** [+91 8097507260](tel:+918097507260)  
    **Email:** info@airbotsaerospace.com  
    **HQ:** Mumbai, Maharashtra, India
    """)

    st.markdown("---")
    st.caption("© 2026 Airbots Aerospace Pvt. Ltd.\nOriginal Color Palette & Logos Preserved.")

# -----------------------------------------------------------------------------
# 1. OVERVIEW & MISSION
# -----------------------------------------------------------------------------
if section == "🏠 Overview & Mission":
    col_left, col_right = st.columns([1.2, 0.9])

    with col_left:
        st.markdown('<span style="color:#4156AF; font-weight:700; font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase;">NEXT-GEN AGRI-ROBOTICS • DGCA TYPE CERTIFIED</span>', unsafe_allow_html=True)
        st.title("Autonomous Drone Robotics for Next-Gen Agriculture")
        st.markdown("""
        Engineered and manufactured in India, **AIRBOTS Aerospace** integrates precision aerial robotics, millimeter-accurate spraying, and AI cloud telemetry to safeguard crops, slash chemical expenditures by **30%**, and conserve **90%** water.
        """)

        bcol1, bcol2 = st.columns(2)
        with bcol1:
            st.button("Request Field Demo", on_click=lambda: st.toast("Opening demo scheduler..."))
        with bcol2:
            st.markdown("""
            <div style="padding-top:8px;">
                <span style="color:#1D8D49; font-weight:700;">✓ DGCA Certified</span> &bull; 
                <span style="color:#4156AF; font-weight:700;">Make in India</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 4 Key Metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-box-val brand-blue">15 L</div>
                <div class="metric-box-lbl">Smart Payload</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-box-val brand-green">23+ m</div>
                <div class="metric-box-lbl">Flight Time</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-box-val brand-blue">3 Ac</div>
                <div class="metric-box-lbl">Per Charge</div>
            </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-box-val brand-green">5G</div>
                <div class="metric-box-lbl">Cloud GCS</div>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        if os.path.exists("airbots_website/airbot_loader.jpeg"):
            st.image("airbots_website/airbot_loader.jpeg", caption="Surya Shakti 15L — DGCA Type Certified Smart Kisan Drone", use_container_width=True)
        elif os.path.exists("airbot_loader.jpeg"):
            st.image("airbot_loader.jpeg", caption="Surya Shakti 15L — DGCA Type Certified Smart Kisan Drone", use_container_width=True)

    # National Impact Banner
    st.markdown("""
    <div class="stat-strip">
        <div style="display:flex; justify-content:space-around; text-align:center; flex-wrap:wrap; gap:16px;">
            <div>
                <h2 style="color:#60A5FA; margin:0;">50,000+</h2>
                <div style="font-size:0.85rem; color:#94A3B8;">Acres Sprayed Autonomously</div>
            </div>
            <div style="border-left:1px solid #334155;"></div>
            <div>
                <h2 style="color:#4ADE80; margin:0;">30%</h2>
                <div style="font-size:0.85rem; color:#94A3B8;">Pesticide Cost Reduction</div>
            </div>
            <div style="border-left:1px solid #334155;"></div>
            <div>
                <h2 style="color:#60A5FA; margin:0;">90%</h2>
                <div style="font-size:0.85rem; color:#94A3B8;">Water Conservation Ratio</div>
            </div>
            <div style="border-left:1px solid #334155;"></div>
            <div>
                <h2 style="color:#4ADE80; margin:0;">10x</h2>
                <div style="font-size:0.85rem; color:#94A3B8;">Faster Than Manual Spray</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🇮🇳 Make in India Heritage")
    st.write(
        "Headquartered in Mumbai, Maharashtra, **Airbots Aerospace Pvt. Ltd.** was founded to equip farmers with world-class, rugged robotics. "
        "With **95% indigenously sourced components**, our platform eliminates foreign dependency and ensures low-cost spares and servicing nationwide."
    )

# -----------------------------------------------------------------------------
# 2. SURYA SHAKTI 15L
# -----------------------------------------------------------------------------
elif section == "🚁 Surya Shakti 15L":
    st.title("Surya Shakti 15L — Flagship Platform")
    st.markdown("The smart agricultural multi-rotor designed specifically for diverse Indian crop canopies and terrains.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "💧 Centrifugal Spray System",
        "✈️ Carbon Fiber Airframe",
        "🧠 5G Companion & Avionics",
        "🛡️ mmWave Radar & Safety"
    ])

    with tab1:
        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.subheader("Centrifugal Ultra-Fine Micron Atomization")
            st.write(
                "Eliminates nozzle clogging while providing adjustable droplet spectrum (60 to 200 microns). "
                "The twin high-pressure brushless magnetic pumps deliver uniform under-canopy penetration, ensuring pests hiding beneath leaves are reached without oversaturating the soil."
            )
            st.markdown("- **Flow Rate:** Dynamic synchronization up to 4.5 L/min.")
            st.markdown("- **Effective Swath:** 4.5 – 6.5 meter width.")
            st.markdown("- **Anti-Drift:** Propeller wash directs mist straight into the root and foliage canopy.")
        with c2:
            st.info("💧 **Spray Metrics:**\n- Tank Capacity: 15 Liters\n- Max Output: 4.5 L/min\n- Nozzle Type: 4x Centrifugal Brushless\n- Pump Type: Dual High-Pressure Magnetic")

    with tab2:
        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.subheader("Foldable High-Tensile Carbon Airframe")
            st.write(
                "Constructed from aerospace-grade carbon fiber tubes and CNC machined aviation aluminum joints. "
                "Reduces volume by **65% when folded**, allowing convenient transport by a single operator on standard farm motorcycles or mini-trucks."
            )
            st.markdown("- **Ingress Protection:** IP54 weatherproof & chemical wash-down resistant.")
            st.markdown("- **Setup Time:** Under 60 seconds from unboxing to flight readiness.")
        with c2:
            st.info("✈️ **Airframe Specs:**\n- Empty Weight: 12.8 kg\n- Max Takeoff Weight (MTOW): 31.5 kg\n- Arm Locking: Quick-Release Twist Lock\n- Folded Footprint: 65% reduction")

    with tab3:
        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.subheader("NEXTUAV 5G On-Board Companion Computer")
            st.write(
                "High-performance flight computer running real-time RTK waypoint algorithms for centimeter-level navigation accuracy. "
                "Synchronizes full flight telemetry, battery cycles, and hectare logs directly to the cloud dashboard."
            )
            st.markdown("- **Multilingual GCS:** Available in Hindi, Marathi, Telugu, Tamil, and English.")
            st.markdown("- **Breakpoint Memory:** Automatically resumes exact coordinate after battery change.")
        with c2:
            st.info("🧠 **Avionics Specs:**\n- Positioning: Dual GNSS (GPS + Glonass + NavIC) / RTK\n- Telemetry Link: 5G LTE + 2.4/5.8 GHz FHSS\n- Control Range: 3.5 km line-of-sight\n- Autopilot: Quad-redundant IMU")

    with tab4:
        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.subheader("Millimeter-Wave Radar & Geofence Matrix")
            st.write(
                "Equipped with front-facing obstacle radar and continuous terrain-following radar. "
                "Smoothly navigates slope variations across hilly terrace cultivation and avoids power lines, tree branches, and poles automatically."
            )
            st.markdown("- **Terrain Following:** Detects slope changes down to 0.1 meter resolution.")
            st.markdown("- **Autonomous RTL:** Automatically returns to home on low voltage, chemical empty, or link loss.")
        with c2:
            st.info("🛡️ **Safety Matrix:**\n- Obstacle Detection: Up to 30 meters ahead\n- Terrain Follow Range: 1.5 - 10 meters AGL\n- Failsafe Modes: Auto RTL, Land, Hover\n- DGCA Compliance: Full Green-Zone Geofence")

    st.markdown("---")
    st.subheader("📋 Technical Comparison Matrix")
    st.table({
        "Parameter": ["Tank Capacity", "DGCA Type Certification", "Flight Endurance", "Coverage / Charge", "Obstacle Radar", "Positioning", "Empty Weight"],
        "Surya Shakti 15L": ["15 Liters", "Certified ✓", "23+ Minutes", "3.0 - 3.5 Acres", "mmWave Radar (30m)", "Dual GNSS + NavIC", "12.8 kg"],
        "Industry Benchmark": ["10 - 12 Liters", "Pending", "12 - 15 Minutes", "1.5 - 2.0 Acres", "Ultrasonic (5m)", "Single Band GPS", "15.5 kg"]
    })

# -----------------------------------------------------------------------------
# 3. AGRI-TECH SOLUTIONS
# -----------------------------------------------------------------------------
elif section == "🌾 Agri-Tech Solutions":
    st.title("Agri-Tech Solutions & DaaS Ecosystem")
    st.write("Comprehensive aerial services designed to empower individual farmers, commercial plantations, and FPO cooperatives.")

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("### 💧 Precision Spraying")
        st.write("Ultra-uniform distribution over Paddy, Cotton, Sugarcane, Wheat, and Orchards. Reaches pests beneath foliage and cuts chemical wastage by 30%.")
    with s2:
        st.markdown("### 🚜 Drone-as-a-Service (DaaS)")
        st.write("Pay-per-acre on-demand spraying model. Certified pilots and drones dispatched directly to your village with zero capital machine investment required.")
    with s3:
        st.markdown("### 🎓 DGCA Pilot Academy")
        st.write("Official Remote Pilot Certificate (RPC) training programs empowering rural youth and agricultural graduates with high-income agri-aviation careers.")

    st.markdown("---")
    s4, s5, s6 = st.columns(3)
    with s4:
        st.markdown("### 🛰️ Multispectral Scouting")
        st.write("NDVI & NDRE high-resolution aerial mapping to detect nitrogen deficiency, water stress, and fungal infections before crop damage spreads.")
    with s5:
        st.markdown("### 📊 NEXTUAV Fleet Control")
        st.write("Enterprise cloud telemetry dashboard for FPOs, agri-corporates, and service providers to monitor multi-drone fleet hours and chemical logs.")
    with s6:
        st.markdown("### 📜 Subsidy & AIF Advisory")
        st.write("Direct turnkey documentation assistance to avail **40% – 50% central and state government subsidies** under SMAM and low-interest AIF loans.")

# -----------------------------------------------------------------------------
# 4. FARM ROI CALCULATOR
# -----------------------------------------------------------------------------
elif section == "💰 Farm ROI Calculator":
    st.title("Interactive Agricultural ROI & Savings Calculator")
    st.write("Evaluate your farm's economic return when transitioning from manual labor spraying to the DGCA-certified Surya Shakti 15L.")

    c_left, c_right = st.columns([1.1, 0.9])

    with c_left:
        st.subheader("Farm Parameters")
        farm_acres = st.slider("Total Cultivation Area (Acres)", min_value=2, max_value=150, value=25, step=1)
        crop = st.selectbox(
            "Primary Crop Type",
            ["Paddy / Rice (Heavy Water Need)", "Cotton / BT Cotton (High Spray Frequency)", "Sugarcane (Tall Canopy)", "Wheat / Cereals", "Horticulture & Orchards"]
        )
        spray_cycles = st.slider("Spraying Cycles per Year", min_value=2, max_value=14, value=6, step=1)
        manual_cost = st.slider("Current Manual Labor Cost per Acre (₹)", min_value=300, max_value=1200, value=600, step=50)

    # Calculation logic
    chem_rates = {
        "Paddy / Rice (Heavy Water Need)": (700, 180),
        "Cotton / BT Cotton (High Spray Frequency)": (900, 200),
        "Sugarcane (Tall Canopy)": (1100, 220),
        "Wheat / Cereals": (600, 150),
        "Horticulture & Orchards": (1400, 250)
    }
    chem_per_acre, water_per_acre = chem_rates[crop]

    total_events = farm_acres * spray_cycles
    trad_labor = total_events * manual_cost
    trad_chem = total_events * chem_per_acre
    trad_water = total_events * water_per_acre

    # Drone saves 30% chemical, 90% water, operating cost ~₹350/ac
    chem_saved = int(trad_chem * 0.30)
    drone_op_cost = total_events * 350
    labor_saved = max(0, trad_labor - drone_op_cost)
    water_saved = int(trad_water * 0.90)
    hours_saved = int(total_events * 3.8)
    net_savings = chem_saved + labor_saved

    with c_right:
        st.markdown(f"""
        <div class="savings-card">
            <div style="font-size:0.85rem; font-weight:700; color:#64748B; text-transform:uppercase;">Estimated Net Annual Savings</div>
            <div class="savings-amount">₹ {net_savings:,.0f}</div>
            <div style="font-size:0.85rem; color:#64748B;">Direct savings on chemical dosage, labor wages & water</div>
        </div>
        """, unsafe_allow_html=True)

        res1, res2 = st.columns(2)
        with res1:
            st.metric("🧪 Chemical Saved", f"₹ {chem_saved:,.0f}", delta="-30% reduction")
            st.metric("⏱️ Labor Hours Saved", f"{hours_saved:,} Hours", delta="10x faster")
        with res2:
            st.metric("💧 Water Conserved", f"{water_saved:,} L", delta="-90% water")
            st.metric("📈 Projected Yield Boost", "+8% to +12%", delta="Optimal foliage coverage")

    st.markdown("---")
    st.caption("💡 Estimates based on ICAR field trial benchmarks and actual AIRBOTS deployment data across Maharashtra, Gujarat, and Punjab.")

# -----------------------------------------------------------------------------
# 5. MISSION CONTROL HUD
# -----------------------------------------------------------------------------
elif section == "🛰️ Mission Control HUD":
    st.title("NEXTUAV Mission Control Cockpit Simulator")
    st.write("Live interactive simulation of the avionics telemetry feed transmitted from Surya Shakti 15L.")

    flight_mode = st.selectbox("Select Flight Automation Mode", ["Auto Waypoint Mission", "Terrace Contour Hold", "Active Precision Spray", "RTL Failsafe Trigger"])

    if flight_mode == "Active Precision Spray":
        alt = 3.0
        spd = 5.2
        tank = 11.2
        flow = "4.2 L/min"
        bat = 82
    elif flight_mode == "Terrace Contour Hold":
        alt = 2.8
        spd = 0.0
        tank = 14.5
        flow = "0.0 L/min"
        bat = 94
    elif flight_mode == "RTL Failsafe Trigger":
        alt = 15.0
        spd = 8.5
        tank = 1.2
        flow = "0.0 L/min"
        bat = 21
    else:
        alt = 3.2
        spd = 4.5
        tank = 12.8
        flow = "3.2 L/min"
        bat = 88

    st.markdown('<div class="hud-cockpit">', unsafe_allow_html=True)
    st.markdown("### 🟢 TELEMETRY FEED: SURYA-SHAKTI-ALPHA-09 (5G LTE CONNECTED)")

    h1, h2, h3, h4 = st.columns(4)
    with h1:
        st.metric("FLIGHT ALTITUDE", f"{alt} m AGL", "Terrain Lock Active")
    with h2:
        st.metric("GROUND SPEED", f"{spd} m/s", "Wind: 2.1 m/s Nominal")
    with h3:
        st.metric("SMART TANK LEVEL", f"{tank} / 15 L", f"Flow: {flow}")
    with h4:
        st.metric("BATTERY STATE", f"{bat}%", "22.2V Smart BMS")

    st.progress(bat / 100.0)

    st.markdown("""
    **Avionics Status:** NavIC + GPS (24 Satellites Fixed RTK) | **Radar Obstacle:** Clear (Next 42m) | **Motor Temp:** 41°C (Nominal)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. DEMO BOOKING & CONTACT
# -----------------------------------------------------------------------------
elif section == "📞 Demo Booking & Contact":
    st.title("Schedule a Field Flight Demo / Dealership Inquiry")
    st.write("Connect directly with AIRBOTS Aerospace flight coordinators and district franchise managers.")

    with st.form("inquiry_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *", placeholder="e.g. Ramesh Patel")
            phone = st.text_input("Mobile / WhatsApp Number *", placeholder="+91 98765 43210")
            state = st.selectbox("State / Region", ["Maharashtra", "Gujarat", "Madhya Pradesh", "Karnataka", "Andhra Pradesh / Telangana", "Punjab / Haryana", "Uttar Pradesh", "Other"])
        with col2:
            role = st.selectbox("I am inquiring as:", ["Progressive Farmer", "Authorized Dealership Applicant", "FPO / Cooperative Leader", "Pilot Training Aspirant", "Agri-Business Enterprise"])
            acres = st.number_input("Cultivation Area (Acres)", min_value=1, max_value=500, value=20)
            crop_interest = st.text_input("Primary Crops Grown", placeholder="e.g. Cotton, Paddy, Soybean")

        message = st.text_area("Specific Requirements or Questions", placeholder="Let us know your village, preferred demo date, or franchise location...")
        submitted = st.form_submit_button("Submit Demo / Inquiry Request")

        if submitted:
            if name and phone:
                st.success(f"✓ Thank you, {name}! Your request has been logged. Our regional flight coordinator for {state} will connect via WhatsApp/Call at {phone} within 4 business hours.")
            else:
                st.error("Please fill in your name and contact phone number.")

# Footer Section
st.markdown("""
<div class="site-footer">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
        <div>
            <h4 style="color:#ffffff; margin:0 0 6px 0;">AIRBOTS Aerospace Pvt. Ltd.</h4>
            <p style="margin:0; font-size:0.85rem;">Autonomous Agri-Drone Robotics • DGCA Type Certified • Make in India</p>
        </div>
        <div style="font-size:0.85rem;">
            📍 Mumbai, Maharashtra, India &nbsp;|&nbsp; 📞 +91 8097507260 &nbsp;|&nbsp; ✉️ info@airbotsaerospace.com
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
