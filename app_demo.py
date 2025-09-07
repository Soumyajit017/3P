"""
P3 - Digital Farm Management Platform
Advanced Biosecurity Management System
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import base64

# Configure page
st.set_page_config(
    page_title="P3 - Digital Farm Management",
    page_icon="�️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Home'

# Color scheme and theme
PRIMARY_COLOR = "#2E7D32"      # Dark Green
SECONDARY_COLOR = "#4CAF50"    # Light Green
ACCENT_COLOR = "#FF9800"       # Orange
BACKGROUND_COLOR = "#F8F9FA"   # Light Gray
TEXT_COLOR = "#1A1A1A"         # Dark Gray
CARD_COLOR = "#FFFFFF"         # White

def create_logo():
    """Create P3 logo"""
    return """
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <div style="
            background: linear-gradient(135deg, #2E7D32, #4CAF50);
            width: 80px;
            height: 80px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 28px;
            font-weight: bold;
            box-shadow: 0 8px 25px rgba(46, 125, 50, 0.3);
        ">
            P3
        </div>
        <div>
            <h1 style="color: #2E7D32; margin: 0; font-size: 2.2rem; font-weight: 700;">
                Digital Farm Management
            </h1>
            <p style="color: #666; margin: 0; font-size: 1.1rem;">
                Advanced Biosecurity Management Platform
            </p>
        </div>
    </div>
    """

def create_card(title, content, icon="📊", color=PRIMARY_COLOR):
    """Create styled card component"""
    return f"""
    <div style="
        background: {CARD_COLOR};
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border-left: 5px solid {color};
        margin: 15px 0;
        transition: all 0.3s ease;
    ">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
            <div style="
                background: linear-gradient(135deg, {color}, {color}AA);
                width: 50px;
                height: 50px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
            ">
                {icon}
            </div>
            <h3 style="color: {color}; margin: 0; font-size: 1.3rem; font-weight: 600;">
                {title}
            </h3>
        </div>
        <div style="color: #555; line-height: 1.6;">
            {content}
        </div>
    </div>
    """

def create_sidebar():
    """Create beautiful sidebar navigation"""
    with st.sidebar:
        # Logo and branding
        st.markdown(create_logo(), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation menu with icons and styling
        pages = [
            ("🏠", "Home", "Main dashboard and overview"),
            ("🔍", "Risk Assessment", "Evaluate farm biosecurity"),
            ("�", "Analytics", "Data insights and reports"),
            ("�️", "Protection Hub", "Safety protocols and alerts")
        ]
        
        selected_page = None
        for icon, name, desc in pages:
            if st.button(
                f"{icon} {name}",
                key=f"nav_{name}",
                help=desc,
                use_container_width=True
            ):
                selected_page = name
        
        # Default to Home if no selection
        if selected_page is None:
            selected_page = "Home"
            
        # Farm status indicator
        st.markdown("---")
        st.markdown("### 🏥 Farm Status")
        
        status_col1, status_col2 = st.columns(2)
        with status_col1:
            st.metric("Risk Level", "Low", "↓ 15%")
        with status_col2:
            st.metric("Compliance", "98%", "↑ 2%")
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🚨 Report Emergency", use_container_width=True, type="secondary"):
            st.error("Emergency protocol activated!")
        if st.button("📋 Upload Document", use_container_width=True, type="secondary"):
            st.success("Document upload ready!")
        
        return selected_page

def home_page():
    """Beautiful home dashboard"""
    # Header with logo
    st.markdown(create_logo(), unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2E7D32, #4CAF50);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.3);
    ">
        <h2 style="margin: 0; font-size: 2rem; font-weight: 600;">
            🛡️ Protecting Your Livestock, Securing Your Future
        </h2>
        <p style="margin: 15px 0 0 0; font-size: 1.1rem; opacity: 0.9;">
            Advanced biosecurity solutions for pig and poultry farms
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics with modern cards
    st.markdown("### 📈 Farm Performance Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4CAF50, #66BB6A);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 5px;">156</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Protected Farms</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FF9800, #FFB74D);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(255, 152, 0, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">⚡</div>
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 5px;">98.5%</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">System Uptime</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #2196F3, #64B5F6);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🛡️</div>
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 5px;">24/7</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Protection</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #9C27B0, #BA68C8);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(156, 39, 176, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📱</div>
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 5px;">1.2K</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Active Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature highlights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(create_card(
            "🔬 AI-Powered Risk Detection",
            """
            • Advanced machine learning algorithms<br>
            • Real-time threat analysis<br>
            • Predictive disease modeling<br>
            • 99.2% accuracy rate
            """,
            "🤖",
            "#2196F3"
        ), unsafe_allow_html=True)
        
        st.markdown(create_card(
            "📊 Smart Analytics Dashboard",
            """
            • Interactive data visualizations<br>
            • Trend analysis and forecasting<br>
            • Custom report generation<br>
            • Export capabilities
            """,
            "📈",
            "#FF9800"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_card(
            "🚨 Emergency Response System",
            """
            • Instant alert notifications<br>
            • Emergency protocol activation<br>
            • Contact veterinary services<br>
            • Crisis management tools
            """,
            "🆘",
            "#F44336"
        ), unsafe_allow_html=True)
        
        st.markdown(create_card(
            "🔒 Compliance Management",
            """
            • Regulatory requirement tracking<br>
            • Document management system<br>
            • Audit trail maintenance<br>
            • Certification assistance
            """,
            "📋",
            "#9C27B0"
        ), unsafe_allow_html=True)
    
    # Latest updates
    st.markdown("### 📰 Latest Updates")
    
    updates = [
        {"icon": "🎉", "title": "New AI Model Released", "desc": "Enhanced disease prediction with 99.5% accuracy", "time": "2 hours ago", "color": "#4CAF50"},
        {"icon": "🔔", "title": "Security Update", "desc": "Enhanced encryption for data protection", "time": "1 day ago", "color": "#2196F3"},
        {"icon": "📱", "title": "Mobile App Update", "desc": "New features and improved performance", "time": "3 days ago", "color": "#FF9800"}
    ]
    
    for update in updates:
        st.markdown(f"""
        <div style="
            background: {CARD_COLOR};
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-left: 4px solid {update['color']};
            margin: 10px 0;
            display: flex;
            align-items: center;
            gap: 15px;
        ">
            <div style="
                background: {update['color']};
                width: 40px;
                height: 40px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 18px;
            ">
                {update['icon']}
            </div>
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #333; font-size: 1.1rem;">{update['title']}</h4>
                <p style="margin: 5px 0 0 0; color: #666; font-size: 0.9rem;">{update['desc']}</p>
            </div>
            <div style="color: #999; font-size: 0.8rem;">{update['time']}</div>
        </div>
        """, unsafe_allow_html=True)

def risk_assessment_page():
    """Advanced risk assessment with beautiful UI"""
    st.markdown(create_logo(), unsafe_allow_html=True)
    
    # Header section
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #F44336, #FF7043);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(244, 67, 54, 0.3);
    ">
        <h2 style="margin: 0; font-size: 1.8rem; font-weight: 600;">
            🔍 Advanced Biosecurity Risk Assessment
        </h2>
        <p style="margin: 10px 0 0 0; font-size: 1rem; opacity: 0.9;">
            AI-powered analysis for comprehensive farm protection
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Assessment form in elegant container
    st.markdown("""
    <div style="
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        margin: 20px 0;
    ">
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Farm Information")
    
    with st.form("risk_assessment_form", clear_on_submit=False):
        # Basic farm details
        col1, col2 = st.columns(2)
        
        with col1:
            farm_id = st.text_input("🏛️ Farm ID/Name", placeholder="Enter farm identifier", value="P3-Demo-Farm-001")
            animal_type = st.selectbox("🐷 Primary Livestock", ["Pig", "Poultry", "Mixed Operations"], index=0)
            farm_size = st.selectbox("📏 Farm Scale", [
                "Small Scale (< 100 animals)", 
                "Medium Scale (100-500 animals)", 
                "Large Scale (500-2000 animals)",
                "Industrial Scale (> 2000 animals)"
            ])
            
        with col2:
            location = st.text_input("📍 Farm Location", placeholder="District, State", value="West Bengal, India")
            years_operation = st.selectbox("⏳ Years in Operation", ["< 1 year", "1-5 years", "5-10 years", "> 10 years"])
            certification = st.selectbox("🏆 Current Certifications", ["None", "Basic", "ISO Certified", "Organic Certified"])
        
        st.markdown("### 🛡️ Biosecurity Measures")
        
        col3, col4 = st.columns(2)
        
        with col3:
            hygiene_practices = st.selectbox("🧼 Hygiene Protocols", [
                "Advanced (Multi-level disinfection)", 
                "Standard (Regular cleaning)", 
                "Basic (Minimal protocols)", 
                "Poor (Irregular maintenance)"
            ])
            vaccination_program = st.selectbox("💉 Vaccination Management", [
                "Comprehensive (AI-scheduled)", 
                "Standard (Vet-managed)", 
                "Basic (Manual tracking)", 
                "Irregular (As-needed only)"
            ])
            waste_management = st.selectbox("♻️ Waste Disposal System", [
                "Advanced Biogas/Composting", 
                "Standard Treatment Plant", 
                "Basic Disposal Methods", 
                "Minimal Treatment"
            ])
            
        with col4:
            visitor_control = st.selectbox("🚪 Access Control", [
                "Biometric + Quarantine", 
                "Standard Registration", 
                "Basic Log Maintenance", 
                "Open Access"
            ])
            feed_storage = st.selectbox("🌾 Feed Management", [
                "Climate-controlled Storage", 
                "Covered Storage Areas", 
                "Basic Storage Facilities", 
                "Open Storage"
            ])
            water_quality = st.selectbox("💧 Water Quality Control", [
                "Continuous Monitoring", 
                "Weekly Testing", 
                "Monthly Testing", 
                "Irregular Testing"
            ])
        
        st.markdown("### 📊 Risk Factors")
        
        col5, col6 = st.columns(2)
        
        with col5:
            disease_history = st.selectbox("🦠 Disease History (Past 2 years)", [
                "No incidents", 
                "Minor outbreaks (contained)", 
                "Major outbreak (significant loss)", 
                "Multiple severe outbreaks"
            ])
            proximity_farms = st.selectbox("🏘️ Nearby Farm Density", [
                "Isolated (> 5km)", 
                "Low density (2-5km)", 
                "Medium density (1-2km)", 
                "High density (< 1km)"
            ])
            
        with col6:
            emergency_plan = st.selectbox("🚨 Emergency Preparedness", [
                "Comprehensive plan + drills", 
                "Written plan available", 
                "Basic procedures", 
                "No formal plan"
            ])
            staff_training = st.selectbox("👥 Staff Training Level", [
                "Advanced biosecurity certified", 
                "Regular training sessions", 
                "Basic orientation", 
                "Minimal training"
            ])
        
        # Advanced features
        st.markdown("### 🤖 AI-Enhanced Analysis")
        col7, col8 = st.columns(2)
        
        with col7:
            iot_monitoring = st.checkbox("📱 IoT Sensor Integration", value=True)
            satellite_monitoring = st.checkbox("🛰️ Satellite Surveillance", value=False)
            
        with col8:
            predictive_analytics = st.checkbox("🔮 Predictive Disease Modeling", value=True)
            blockchain_records = st.checkbox("⛓️ Blockchain Record Keeping", value=False)
        
        submitted = st.form_submit_button(
            "🚀 Run AI Assessment", 
            use_container_width=True,
            type="primary"
        )
        
        if submitted:
            # Simulate AI processing
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            import time
            for i in range(100):
                progress_bar.progress(i + 1)
                if i < 20:
                    status_text.text("🔍 Analyzing farm data...")
                elif i < 40:
                    status_text.text("🤖 Running AI risk models...")
                elif i < 60:
                    status_text.text("📊 Processing biosecurity metrics...")
                elif i < 80:
                    status_text.text("🛡️ Calculating protection score...")
                else:
                    status_text.text("✅ Generating recommendations...")
                time.sleep(0.02)
            
            progress_bar.empty()
            status_text.empty()
            
            # Results display
            st.success("🎉 Assessment completed successfully!")
            
            # Calculate mock risk score based on selections
            risk_score = 45  # Base score
            
            # Adjust based on selections (simplified logic)
            if hygiene_practices and "Advanced" in hygiene_practices:
                risk_score -= 10
            elif hygiene_practices and "Poor" in hygiene_practices:
                risk_score += 15
                
            if vaccination_program and "Comprehensive" in vaccination_program:
                risk_score -= 8
            elif vaccination_program and "Irregular" in vaccination_program:
                risk_score += 12
            
            # Determine risk level and color
            if risk_score <= 30:
                risk_level = "Low"
                risk_color = "#4CAF50"
                risk_emoji = "🟢"
            elif risk_score <= 60:
                risk_level = "Medium"
                risk_color = "#FF9800"
                risk_emoji = "🟡"
            else:
                risk_level = "High"
                risk_color = "#F44336"
                risk_emoji = "🔴"
            
            # Results dashboard
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {risk_color}, {risk_color}AA);
                    padding: 30px;
                    border-radius: 15px;
                    color: white;
                    text-align: center;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                ">
                    <div style="font-size: 3rem; margin-bottom: 10px;">{risk_emoji}</div>
                    <div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 10px;">{risk_score}/100</div>
                    <div style="font-size: 1.2rem; margin-bottom: 5px;">Risk Score</div>
                    <div style="font-size: 1.5rem; font-weight: 600;">{risk_level} Risk</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 🎯 AI-Generated Recommendations")
                
                recommendations = [
                    "🧼 Implement advanced disinfection protocols at entry points",
                    "💉 Upgrade to AI-scheduled vaccination management system",
                    "🔬 Install real-time pathogen detection sensors",
                    "👥 Conduct monthly staff biosecurity training sessions",
                    "📱 Deploy IoT monitoring for early warning systems",
                    "🛰️ Consider satellite surveillance for perimeter security"
                ]
                
                for i, rec in enumerate(recommendations[:4]):
                    st.markdown(f"""
                    <div style="
                        background: #f8f9fa;
                        padding: 15px;
                        border-radius: 10px;
                        border-left: 4px solid {PRIMARY_COLOR};
                        margin: 10px 0;
                    ">
                        <strong style="color: {PRIMARY_COLOR};">Priority {i+1}:</strong> {rec}
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def analytics_page():
    """Advanced analytics dashboard"""
    st.markdown(create_logo(), unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2196F3, #64B5F6);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3);
    ">
        <h2 style="margin: 0; font-size: 1.8rem; font-weight: 600;">
            📊 Advanced Analytics & Intelligence
        </h2>
        <p style="margin: 10px 0 0 0; font-size: 1rem; opacity: 0.9;">
            Real-time insights powered by AI and machine learning
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Performance Indicators
    st.markdown("### 🎯 Key Performance Indicators")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4CAF50, #66BB6A);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
        ">
            <div style="font-size: 2rem; margin-bottom: 8px;">🛡️</div>
            <div style="font-size: 1.8rem; font-weight: bold;">98.7%</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Protection Rate</div>
            <div style="font-size: 0.75rem; color: #E8F5E8;">↑ 2.3% this month</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FF9800, #FFB74D);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 20px rgba(255, 152, 0, 0.3);
        ">
            <div style="font-size: 2rem; margin-bottom: 8px;">⚡</div>
            <div style="font-size: 1.8rem; font-weight: bold;">0.3s</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Response Time</div>
            <div style="font-size: 0.75rem; color: #FFF3E0;">↓ 0.1s improved</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #9C27B0, #BA68C8);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 20px rgba(156, 39, 176, 0.3);
        ">
            <div style="font-size: 2rem; margin-bottom: 8px;">🎯</div>
            <div style="font-size: 1.8rem; font-weight: bold;">99.2%</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">AI Accuracy</div>
            <div style="font-size: 0.75rem; color: #F3E5F5;">↑ 0.5% this week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col4:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #F44336, #E57373);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 20px rgba(244, 67, 54, 0.3);
        ">
            <div style="font-size: 2rem; margin-bottom: 8px;">🚨</div>
            <div style="font-size: 1.8rem; font-weight: bold;">3</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Active Alerts</div>
            <div style="font-size: 0.75rem; color: #FFEBEE;">2 resolved today</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Charts
    tab1, tab2, tab3 = st.tabs(["🔍 Risk Analysis", "📈 Trend Monitoring", "🌍 Geographic Insights"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk level distribution
            risk_data = pd.DataFrame({
                'Risk Level': ['Low Risk', 'Medium Risk', 'High Risk'],
                'Farms': [85, 45, 12],
                'Percentage': [59.9, 31.7, 8.4]
            })
            
            fig_pie = px.pie(
                risk_data, 
                values='Farms', 
                names='Risk Level',
                title="🛡️ Farm Risk Distribution",
                color_discrete_map={
                    'Low Risk': '#4CAF50',
                    'Medium Risk': '#FF9800', 
                    'High Risk': '#F44336'
                },
                hole=0.4
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            fig_pie.update_layout(
                font=dict(size=12),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Risk scores by farm type
            farm_data = pd.DataFrame({
                'Farm Type': ['Pig Farms', 'Poultry Farms', 'Mixed Operations'],
                'Average Risk Score': [28, 35, 42],
                'Count': [45, 67, 30]
            })
            
            fig_bar = px.bar(
                farm_data,
                x='Farm Type',
                y='Average Risk Score',
                title="📊 Risk Scores by Farm Type",
                color='Average Risk Score',
                color_continuous_scale='RdYlGn_r',
                text='Count'
            )
            fig_bar.update_traces(texttemplate='%{text} farms', textposition='outside')
            fig_bar.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                coloraxis_showscale=False
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab2:
        # Time series data
        dates = pd.date_range(start='2025-01-01', end='2025-09-07', freq='D')
        trend_data = pd.DataFrame({
            'Date': dates,
            'Protection Score': 95 + 5 * np.sin(np.arange(len(dates)) * 0.1) + np.random.normal(0, 1, len(dates)),
            'Threat Level': 15 + 10 * np.sin(np.arange(len(dates)) * 0.15) + np.random.normal(0, 2, len(dates)),
            'System Health': 98 + 2 * np.sin(np.arange(len(dates)) * 0.05) + np.random.normal(0, 0.5, len(dates))
        })
        
        fig_line = go.Figure()
        
        fig_line.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['Protection Score'],
            mode='lines',
            name='Protection Score',
            line=dict(color='#4CAF50', width=3)
        ))
        
        fig_line.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['Threat Level'],
            mode='lines',
            name='Threat Level',
            line=dict(color='#F44336', width=3)
        ))
        
        fig_line.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['System Health'],
            mode='lines',
            name='System Health',
            line=dict(color='#2196F3', width=3)
        ))
        
        fig_line.update_layout(
            title="📈 Performance Trends (2025)",
            xaxis_title="Date",
            yaxis_title="Score",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_line, use_container_width=True)
        
        # Additional metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(create_card(
                "🔥 Disease Outbreaks Prevented",
                "47 potential outbreaks detected and prevented using AI early warning system",
                "🛡️",
                "#4CAF50"
            ), unsafe_allow_html=True)
        
        with col2:
            st.markdown(create_card(
                "⚡ Average Response Time",
                "0.3 seconds average response time for threat detection and alert generation",
                "🚀",
                "#FF9800"
            ), unsafe_allow_html=True)
        
        with col3:
            st.markdown(create_card(
                "💰 Cost Savings",
                "₹2.3 Crores saved through preventive measures and early intervention",
                "💵",
                "#2196F3"
            ), unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🗺️ Geographic Distribution")
        
        # Simulated geographic data
        geo_data = pd.DataFrame({
            'State': ['West Bengal', 'Odisha', 'Jharkhand', 'Bihar', 'Assam'],
            'Protected Farms': [45, 32, 28, 22, 15],
            'Risk Score': [25, 30, 35, 40, 32],
            'Latitude': [22.9868, 20.9517, 23.6102, 25.0961, 26.2006],
            'Longitude': [87.8550, 85.0985, 85.2799, 85.3131, 92.9376]
        })
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Replace mapbox with a simpler scatter plot
            fig_map = px.scatter(
                geo_data,
                x='Longitude',
                y='Latitude',
                size='Protected Farms',
                color='Risk Score',
                hover_name='State',
                hover_data={'Protected Farms': True, 'Risk Score': True},
                color_continuous_scale='RdYlGn_r',
                size_max=30,
                title="🌍 Farm Distribution & Risk Levels"
            )
            fig_map.update_layout(
                xaxis_title="Longitude",
                yaxis_title="Latitude",
                height=400
            )
            
            fig_map.update_layout(
                height=500,
                margin=dict(l=0, r=0, t=50, b=0)
            )
            
            st.plotly_chart(fig_map, use_container_width=True)
        
        with col2:
            st.markdown("#### 📍 Regional Statistics")
            
            for _, row in geo_data.iterrows():
                risk_color = "#4CAF50" if row['Risk Score'] < 30 else "#FF9800" if row['Risk Score'] < 35 else "#F44336"
                
                st.markdown(f"""
                <div style="
                    background: white;
                    padding: 15px;
                    border-radius: 10px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                    border-left: 4px solid {risk_color};
                    margin: 10px 0;
                ">
                    <h4 style="margin: 0; color: #333;">{row['State']}</h4>
                    <p style="margin: 5px 0; color: #666;">
                        🏛️ {row['Protected Farms']} farms<br>
                        🎯 Risk: {row['Risk Score']}/100
                    </p>
                </div>
                """, unsafe_allow_html=True)

def analytics_dashboard_page():
    """Comprehensive analytics and insights dashboard"""
    st.markdown(create_logo(), unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2196F3, #64B5F6);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3);
    ">
        <h2 style="margin: 0; font-size: 1.8rem; font-weight: 600;">
            📊 Analytics Dashboard
        </h2>
        <p style="margin: 10px 0 0 0; font-size: 1rem; opacity: 0.9;">
            Comprehensive insights and data-driven decisions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI Section
    st.markdown("### 📈 Key Performance Indicators")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.metric("Total Farms", "156", "↑ 12")
    with kpi_col2:
        st.metric("Avg. Health Score", "94.2%", "↑ 2.1%")
    with kpi_col3:
        st.metric("Disease Prevention", "99.1%", "↑ 0.3%")
    with kpi_col4:
        st.metric("Cost Savings", "₹2.4M", "↑ ₹340K")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts section
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Farm performance over time
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        performance_data = pd.DataFrame({
            'Date': dates,
            'Health Score': 90 + 5 * np.sin(np.arange(30) * 0.2) + np.random.normal(0, 1, 30),
            'Biosecurity Score': 85 + 8 * np.cos(np.arange(30) * 0.15) + np.random.normal(0, 1.5, 30)
        })
        
        fig1 = px.line(performance_data, x='Date', y=['Health Score', 'Biosecurity Score'],
                      title="📈 Farm Performance Trends")
        fig1.update_layout(height=400)
        st.plotly_chart(fig1, use_container_width=True)
    
    with chart_col2:
        # Risk distribution
        risk_data = pd.DataFrame({
            'Risk Level': ['Low', 'Medium', 'High', 'Critical'],
            'Count': [95, 45, 12, 4],
            'Color': ['#4CAF50', '#FF9800', '#FF5722', '#F44336']
        })
        
        fig2 = px.pie(risk_data, values='Count', names='Risk Level',
                     title="🎯 Risk Level Distribution",
                     color_discrete_sequence=['#4CAF50', '#FF9800', '#FF5722', '#F44336'])
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Geographic insights
    st.markdown("### 🌍 Geographic Insights")
    
    # Regional data
    regions_data = pd.DataFrame({
        'Region': ['West Bengal', 'Odisha', 'Jharkhand', 'Bihar', 'Assam'],
        'Farms': [45, 32, 28, 35, 16],
        'Avg_Score': [92.5, 89.3, 91.2, 88.7, 93.1],
    })
    
    # Simple bar chart instead of map
    fig3 = px.bar(
        regions_data,
        x='Region',
        y='Farms',
        color='Avg_Score',
        title="🗺️ Regional Farm Distribution",
        color_continuous_scale='Viridis'
    )
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)
    
    # Regional statistics
    st.markdown("#### 📍 Regional Statistics")
    
    for _, row in regions_data.iterrows():
        score_color = "#4CAF50" if row['Avg_Score'] > 90 else "#FF9800" if row['Avg_Score'] > 85 else "#F44336"
        
        st.markdown(f"""
        <div style="
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-left: 5px solid {score_color};
            margin: 10px 0;
        ">
            <h4 style="margin: 0; color: #333;">{row['Region']}</h4>
            <p style="margin: 5px 0; color: #666;">
                🏛️ {row['Farms']} farms<br>
                🎯 Score: {row['Avg_Score']:.1f}/100
            </p>
        </div>
        """, unsafe_allow_html=True)

def protection_hub_page():
    """Advanced protection and emergency response hub"""
    st.markdown(create_logo(), unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #9C27B0, #BA68C8);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(156, 39, 176, 0.3);
    ">
        <h2 style="margin: 0; font-size: 1.8rem; font-weight: 600;">
            🛡️ Protection Hub & Emergency Response
        </h2>
        <p style="margin: 10px 0 0 0; font-size: 1rem; opacity: 0.9;">
            24/7 monitoring, alerts, and rapid response systems
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Emergency Status Dashboard
    st.markdown("### 🚨 Emergency Status Dashboard")
    
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4CAF50, #66BB6A);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">✅</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 5px;">ALL CLEAR</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">System Status</div>
            <div style="font-size: 0.8rem; margin-top: 10px;">Last Updated: Just now</div>
        </div>
        """, unsafe_allow_html=True)
    
    with status_col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FF9800, #FFB74D);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(255, 152, 0, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">⚠️</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 5px;">3 ALERTS</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Pending Review</div>
            <div style="font-size: 0.8rem; margin-top: 10px;">Highest: Medium Priority</div>
        </div>
        """, unsafe_allow_html=True)
    
    with status_col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #2196F3, #64B5F6);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3);
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🛰️</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 5px;">156 FARMS</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Under Protection</div>
            <div style="font-size: 0.8rem; margin-top: 10px;">Coverage: 98.7%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🔔 Active Alerts", "📋 Protocols", "🤖 AI Monitoring", "📞 Emergency Contacts"])
    
    with tab1:
        st.markdown("### 🚨 Real-Time Alert System")
        
        # Alert filters
        filter_col1, filter_col2, filter_col3 = st.columns(3)
        
        with filter_col1:
            severity_filter = st.selectbox("🎯 Severity Level", ["All", "Critical", "High", "Medium", "Low"])
        with filter_col2:
            type_filter = st.selectbox("📂 Alert Type", ["All", "Disease", "Security", "Weather", "Equipment"])
        with filter_col3:
            time_filter = st.selectbox("⏰ Time Range", ["Last 24h", "Last 7 days", "Last 30 days"])
        
        # Sample alerts
        alerts = [
            {
                "id": "ALT-001",
                "severity": "Medium",
                "type": "Disease",
                "title": "Unusual Behavior Pattern Detected",
                "description": "AI system detected abnormal feeding patterns in Sector 3, Farm PF-045",
                "time": "2 minutes ago",
                "location": "Farm PF-045, Sector 3",
                "status": "Investigating",
                "color": "#FF9800"
            },
            {
                "id": "ALT-002", 
                "severity": "Low",
                "type": "Weather",
                "title": "Heavy Rainfall Forecast",
                "description": "Meteorological data indicates 48-hour rainfall warning for regional farms",
                "time": "1 hour ago",
                "location": "Regional (West Bengal)",
                "status": "Active",
                "color": "#2196F3"
            },
            {
                "id": "ALT-003",
                "severity": "High",
                "type": "Security",
                "title": "Unauthorized Access Attempt",
                "description": "Motion sensors triggered outside normal hours at Farm PP-012",
                "time": "3 hours ago",
                "location": "Farm PP-012, Perimeter",
                "status": "Resolved",
                "color": "#F44336"
            }
        ]
        
        for alert in alerts:
            st.markdown(f"""
            <div style="
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                border-left: 5px solid {alert['color']};
                margin: 15px 0;
            ">
                <div style="display: flex; justify-content: between; align-items: start; margin-bottom: 10px;">
                    <div>
                        <h4 style="margin: 0; color: #333; font-size: 1.1rem;">
                            [{alert['id']}] {alert['title']}
                        </h4>
                        <div style="display: flex; gap: 15px; margin: 8px 0;">
                            <span style="
                                background: {alert['color']};
                                color: white;
                                padding: 3px 8px;
                                border-radius: 12px;
                                font-size: 0.75rem;
                                font-weight: 600;
                            ">{alert['severity']}</span>
                            <span style="
                                background: #f0f2f6;
                                color: #555;
                                padding: 3px 8px;
                                border-radius: 12px;
                                font-size: 0.75rem;
                            ">{alert['type']}</span>
                            <span style="
                                background: #e8f5e8;
                                color: #2e7d32;
                                padding: 3px 8px;
                                border-radius: 12px;
                                font-size: 0.75rem;
                            ">{alert['status']}</span>
                        </div>
                    </div>
                    <div style="text-align: right; color: #999; font-size: 0.8rem;">
                        {alert['time']}
                    </div>
                </div>
                <p style="margin: 10px 0; color: #666; line-height: 1.5;">
                    {alert['description']}
                </p>
                <div style="color: #888; font-size: 0.85rem;">
                    📍 {alert['location']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📋 Emergency Response Protocols")
        
        protocols = [
            {
                "title": "🦠 Disease Outbreak Response",
                "steps": [
                    "Immediate quarantine of affected area",
                    "Alert veterinary emergency team", 
                    "Implement enhanced biosecurity measures",
                    "Contact regulatory authorities",
                    "Begin contact tracing and assessment"
                ],
                "color": "#F44336"
            },
            {
                "title": "🔥 Fire Emergency Protocol",
                "steps": [
                    "Activate fire suppression systems",
                    "Evacuate personnel and animals safely",
                    "Contact fire department (101)",
                    "Secure hazardous materials",
                    "Document incident for insurance"
                ],
                "color": "#FF5722"
            },
            {
                "title": "🌊 Flood Response Plan",
                "steps": [
                    "Move animals to higher ground",
                    "Secure feed and equipment",
                    "Check structural integrity", 
                    "Prepare emergency supplies",
                    "Monitor water quality post-flood"
                ],
                "color": "#03A9F4"
            },
            {
                "title": "⚡ Power Outage Response",
                "steps": [
                    "Activate backup generators",
                    "Check ventilation systems",
                    "Monitor animal welfare",
                    "Contact utility provider",
                    "Prepare manual feeding if needed"
                ],
                "color": "#FF9800"
            }
        ]
        
        for protocol in protocols:
            with st.expander(f"{protocol['title']}", expanded=False):
                for i, step in enumerate(protocol['steps'], 1):
                    st.markdown(f"""
                    <div style="
                        background: #f8f9fa;
                        padding: 12px;
                        border-radius: 8px;
                        border-left: 4px solid {protocol['color']};
                        margin: 8px 0;
                    ">
                        <strong style="color: {protocol['color']};">Step {i}:</strong> {step}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style="text-align: center; margin: 15px 0;">
                    <button style="
                        background: {protocol['color']};
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 8px;
                        font-weight: 600;
                        cursor: pointer;
                    ">
                        🚨 Activate Protocol
                    </button>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🤖 AI Monitoring Systems")
        
        # Monitoring categories
        monitoring_col1, monitoring_col2 = st.columns(2)
        
        with monitoring_col1:
            st.markdown(create_card(
                "🔬 Pathogen Detection",
                """
                • Real-time air quality monitoring<br>
                • Pathogen identification algorithms<br>
                • Early warning system activation<br>
                • Automated quarantine protocols
                """,
                "🧪",
                "#4CAF50"
            ), unsafe_allow_html=True)
            
            st.markdown(create_card(
                "📹 Video Surveillance AI",
                """
                • 24/7 behavioral analysis<br>
                • Anomaly detection algorithms<br>
                • Automated threat assessment<br>
                • Security breach detection
                """,
                "👁️",
                "#2196F3"
            ), unsafe_allow_html=True)
        
        with monitoring_col2:
            st.markdown(create_card(
                "🌡️ Environmental Monitoring",
                """
                • Temperature and humidity tracking<br>
                • Air quality index monitoring<br>
                • Feed quality assessment<br>
                • Water quality analysis
                """,
                "🌡️",
                "#FF9800"
            ), unsafe_allow_html=True)
            
            st.markdown(create_card(
                "📊 Predictive Analytics",
                """
                • Disease outbreak prediction<br>
                • Risk pattern recognition<br>
                • Resource optimization<br>
                • Performance forecasting
                """,
                "🔮",
                "#9C27B0"
            ), unsafe_allow_html=True)
        
        # AI Performance Metrics
        st.markdown("### 🎯 AI System Performance")
        
        perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
        
        with perf_col1:
            st.metric("Detection Accuracy", "99.2%", "↑ 0.3%")
        with perf_col2:
            st.metric("Response Time", "0.3s", "↓ 0.1s")
        with perf_col3:
            st.metric("False Positives", "0.8%", "↓ 0.2%")
        with perf_col4:
            st.metric("System Uptime", "99.9%", "→ 0.0%")
    
    with tab4:
        st.markdown("### 📞 Emergency Contact Directory")
        
        # Emergency contacts organized by category
        contact_categories = [
            {
                "title": "🚨 Emergency Services",
                "contacts": [
                    {"name": "Fire Department", "number": "101", "type": "Emergency"},
                    {"name": "Police Emergency", "number": "100", "type": "Emergency"},
                    {"name": "Medical Emergency", "number": "108", "type": "Emergency"},
                    {"name": "Disaster Management", "number": "1070", "type": "Emergency"}
                ],
                "color": "#F44336"
            },
            {
                "title": "🏥 Veterinary Services",
                "contacts": [
                    {"name": "Dr. Rajesh Kumar", "number": "+91 98765 43210", "type": "Primary Vet"},
                    {"name": "Animal Hospital 24/7", "number": "+91 87654 32109", "type": "Emergency Vet"},
                    {"name": "Mobile Vet Service", "number": "+91 76543 21098", "type": "Mobile Service"},
                    {"name": "Livestock Specialist", "number": "+91 65432 10987", "type": "Specialist"}
                ],
                "color": "#4CAF50"
            },
            {
                "title": "🏛️ Government Authorities",
                "contacts": [
                    {"name": "Animal Husbandry Dept", "number": "+91 33 2234 5678", "type": "Government"},
                    {"name": "Disease Control Office", "number": "+91 33 2345 6789", "type": "Disease Control"},
                    {"name": "Rural Development", "number": "+91 33 3456 7890", "type": "Development"},
                    {"name": "Environmental Authority", "number": "+91 33 4567 8901", "type": "Environment"}
                ],
                "color": "#2196F3"
            }
        ]
        
        for category in contact_categories:
            st.markdown(f"""
            <div style="margin: 20px 0;">
                <h4 style="color: {category['color']}; margin-bottom: 15px;">
                    {category['title']}
                </h4>
            </div>
            """, unsafe_allow_html=True)
            
            for contact in category['contacts']:
                st.markdown(f"""
                <div style="
                    background: white;
                    padding: 15px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
                    border-left: 4px solid {category['color']};
                    margin: 10px 0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                ">
                    <div>
                        <strong style="color: #333; font-size: 1rem;">{contact['name']}</strong>
                        <div style="color: #666; font-size: 0.85rem; margin-top: 3px;">{contact['type']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="
                            background: {category['color']};
                            color: white;
                            padding: 8px 12px;
                            border-radius: 8px;
                            font-weight: 600;
                            font-size: 0.9rem;
                        ">
                            📞 {contact['number']}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Quick dial buttons
        st.markdown("### ⚡ Quick Dial")
        
        quick_col1, quick_col2, quick_col3 = st.columns(3)
        
        with quick_col1:
            if st.button("🚨 Emergency Services", use_container_width=True, type="primary"):
                st.error("🚨 Connecting to Emergency Services...")
        
        with quick_col2:
            if st.button("🏥 Veterinary Emergency", use_container_width=True, type="secondary"):
                st.success("📞 Connecting to Veterinary Services...")
        
        with quick_col3:
            if st.button("🏛️ Government Helpline", use_container_width=True):
                st.info("📞 Connecting to Government Helpline...")

def alerts_notifications_page():
    """Alerts and notifications page"""
    st.title("🚨 Alerts & Notifications")
    st.markdown("Real-time alerts and disease outbreak notifications")
    
    st.info("🔔 Demo Mode: Simulated alerts for presentation")
    
    # Alert subscription
    st.markdown("### Alert Subscription Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Subscribe to Alerts", value=True)
        st.text_input("Your Location/District", value="West Bengal")
        
    with col2:
        st.selectbox("Preferred Contact Method", ["Email", "SMS", "App Notification"])
    
    st.multiselect("Select alert types", 
                   ["Disease Outbreaks", "Weather Warnings", "Market Prices", "Regulatory Updates", "Training Reminders"],
                   default=["Disease Outbreaks", "Weather Warnings"])
    
    if st.button("Save Preferences"):
        st.success("Preferences saved successfully! (Demo)")
    
    # Current alerts
    st.markdown("### Current Alerts")
    
    # High severity alert
    st.error("🚨 **HIGH ALERT**: Avian Flu Outbreak Reported")
    st.write("H5N1 Avian Influenza detected in poultry farms in neighboring district.")
    st.write("**Actions:** Restrict farm access, Increase disinfection, Monitor bird health")
    
    # Medium severity alert  
    st.warning("⚠️ **MEDIUM ALERT**: Heavy Rainfall Expected")
    st.write("Monsoon rainfall predicted for next 3 days.")
    st.write("**Actions:** Check drainage systems, Secure feed storage")
    
    # Low severity alert
    st.info("ℹ️ **INFO**: New Vaccination Guidelines")
    st.write("Updated vaccination schedule released by Animal Husbandry Department.")

def monitoring_dashboard_page():
    """Monitoring dashboard page"""
    st.title("📊 Monitoring Dashboard")
    st.markdown("Data visualization and farm monitoring dashboard")
    
    st.info("📈 Demo Mode: Displaying sample visualizations")
    
    # Sample data
    risk_data = pd.DataFrame({
        'Farm': ['Farm A', 'Farm B', 'Farm C', 'Farm D', 'Farm E'],
        'Risk Score': [25, 45, 75, 30, 60],
        'Risk Level': ['Low', 'Medium', 'High', 'Low', 'Medium'],
        'Type': ['Pig', 'Poultry', 'Pig', 'Poultry', 'Mixed']
    })
    
    # Dashboard sections
    tab1, tab2, tab3 = st.tabs(["Risk Analysis", "Training Progress", "Compliance Status"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk level distribution
            risk_counts = risk_data['Risk Level'].value_counts()
            fig_pie = px.pie(values=risk_counts.values, names=risk_counts.index, 
                           title="Risk Level Distribution",
                           color_discrete_map={'Low': 'green', 'Medium': 'yellow', 'High': 'red'})
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Risk scores by farm type
            fig_bar = px.bar(risk_data, x='Farm', y='Risk Score', color='Type',
                           title="Risk Scores by Farm")
            st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab2:
        # Training completion rates
        training_data = pd.DataFrame({
            'User': ['Farmer 1', 'Farmer 2', 'Farmer 3', 'Farmer 4', 'Farmer 5'],
            'Completion Rate': [100, 80, 60, 40, 20]
        })
        
        fig_training = px.bar(training_data, x='User', y='Completion Rate',
                            title="Training Completion Rates")
        st.plotly_chart(fig_training, use_container_width=True)
    
    with tab3:
        # Compliance status
        compliance_data = pd.DataFrame({
            'Status': ['Verified', 'Under Review', 'Pending'],
            'Count': [3, 2, 3]
        })
        
        fig_compliance = px.pie(compliance_data, values='Count', names='Status',
                              title="Compliance Status Distribution")
        st.plotly_chart(fig_compliance, use_container_width=True)

def farmer_network_page():
    """Farmer networking page"""
    st.title("👥 Farmer Network")
    st.markdown("Connect with other farmers in your region")
    
    st.info("🌐 Demo Mode: Sample farmer directory")
    
    # Registration form
    st.markdown("### Register Your Farm")
    
    with st.form("farmer_registration"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Farmer Name", value="Demo Farmer")
            st.text_input("Farm Name", value="Demo Farm")
            st.text_input("Location/District", value="West Bengal")
            
        with col2:
            st.text_input("Phone Number", value="+91 9876543210")
            st.text_input("Email Address", value="demo@farm.com")
            st.selectbox("Farm Type", ["Pig Farm", "Poultry Farm", "Mixed Farm"])
        
        st.selectbox("Farm Size", ["Small (< 100 animals)", "Medium (100-500 animals)", "Large (> 500 animals)"])
        st.multiselect("Specializations", ["Breeding", "Organic Farming", "Feed Production", "Disease Management"])
        
        if st.form_submit_button("Register"):
            st.success("Registration successful! (Demo)")
    
    # Sample farmer directory
    st.markdown("### Farmer Directory")
    
    farmers = [
        {"name": "Amit Kumar", "location": "Kolkata", "type": "Pig Farm", "phone": "+91 9876543210"},
        {"name": "Priya Sharma", "location": "Delhi", "type": "Poultry Farm", "phone": "+91 8765432109"},
        {"name": "Raj Patel", "location": "Mumbai", "type": "Mixed Farm", "phone": "+91 7654321098"}
    ]
    
    for farmer in farmers:
        with st.container():
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"#### {farmer['name']} ✅")
                st.write(f"**Location:** {farmer['location']}")
                st.write(f"**Type:** {farmer['type']}")
                
            with col2:
                st.write(f"📞 {farmer['phone']}")
                st.button("View Profile", key=f"profile_{farmer['name']}")
            
            st.markdown("---")

def data_export_page():
    """Data export and admin page"""
    st.title("📥 Data Export")
    st.markdown("Export farm data for policy analysis and administrative functions")
    
    st.info("🔐 Demo Mode: Simulated data export functionality")
    
    # Admin login simulation
    if not st.session_state.get('admin_logged_in', False):
        st.markdown("### Admin Login")
        password = st.text_input("Enter admin password", type="password", placeholder="admin123")
        
        if st.button("Login"):
            if password == "admin123":
                st.session_state.admin_logged_in = True
                st.success("Admin login successful!")
                st.rerun()
            else:
                st.error("Invalid password (Try: admin123)")
        return
    
    # Admin dashboard
    st.success("🔐 Admin access granted")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Risk Assessments", "42")
    
    with col2:
        st.metric("Registered Farmers", "156")
    
    with col3:
        st.metric("Completed Training", "89")
    
    with col4:
        st.metric("Verified Compliance", "35")
    
    # Export options
    st.markdown("### Data Export Options")
    
    export_options = ["Risk Assessment Data", "Training Progress", "Compliance Records", "Farmer Directory", "Summary Report"]
    
    selected_export = st.selectbox("Select data to export", export_options, index=0)
    
    if st.button("Export Data") and selected_export:
        # Simulate CSV download
        sample_data = pd.DataFrame({
            'Date': ['2025-09-01', '2025-09-02', '2025-09-03'],
            'Farm_ID': ['Farm_001', 'Farm_002', 'Farm_003'],
            'Status': ['Verified', 'Pending', 'Submitted']
        })
        
        csv = sample_data.to_csv(index=False)
        st.download_button(
            label=f"Download {selected_export}",
            data=csv,
            file_name=f"{selected_export.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
        st.success(f"Exporting {selected_export}... (Demo)")
    
    # Logout
    if st.button("Logout Admin"):
        st.session_state.admin_logged_in = False
        st.rerun()

def main():
    """Main application function"""
    # Create sidebar and get selected page
    selected_page = create_sidebar()
    
    # Route to appropriate page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Risk Assessment":
        risk_assessment_page()
    elif selected_page == "Analytics Dashboard":
        analytics_dashboard_page()
    elif selected_page == "Protection Hub":
        protection_hub_page()
    elif selected_page == "Training Modules":
        st.info("🎓 Training Modules - Coming Soon! Professional development and educational content.")
    elif selected_page == "Compliance Tracking":
        st.info("📋 Compliance Tracking - Coming Soon! Regulatory compliance and document management.")
    elif selected_page == "Alerts & Notifications":
        alerts_notifications_page()
    elif selected_page == "Monitoring Dashboard":
        monitoring_dashboard_page()
    elif selected_page == "Farmer Network":
        farmer_network_page()
    elif selected_page == "Data Export":
        data_export_page()
    else:
        home_page()

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        width: 100%;
        background-color: #2E8B57;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    
    .stButton > button:hover {
        background-color: #246B47;
    }
</style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
