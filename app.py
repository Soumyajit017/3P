"""
Digital Farm Management Portal
A comprehensive solution for pig and poultry farmers to improve biosecurity measures and disease prevention.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime, timedelta
import altair as alt
# from streamlit_option_menu import option_menu  # Commented out for UI-only demo

# Configure page
st.set_page_config(
    page_title="Digital Farm Management Portal",
    page_icon="🐷",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Multilingual support
LANGUAGES = {
    "English": {
        "app_title": "Digital Farm Management Portal",
        "welcome": "Welcome to Digital Farm Management Portal",
        "description": "Comprehensive biosecurity and disease prevention solution for pig and poultry farmers",
        "home": "Home",
        "risk_assessment": "Risk Assessment",
        "training": "Training Modules",
        "compliance": "Compliance Tracking",
        "alerts": "Alerts & Notifications",
        "monitoring": "Monitoring Dashboard",
        "networking": "Farmer Network",
        "data_export": "Data Export",
        "language": "Language",
        "farm_type": "Farm Type",
        "pig": "Pig",
        "poultry": "Poultry",
        "submit": "Submit",
        "save": "Save",
        "download": "Download",
        "upload": "Upload",
        "view_details": "View Details",
        "mark_completed": "Mark as Completed",
        "in_progress": "In Progress",
        "completed": "Completed",
        "pending": "Pending",
        "verified": "Verified",
        "low_risk": "Low Risk",
        "medium_risk": "Medium Risk",
        "high_risk": "High Risk"
    },
    "हिंदी": {
        "app_title": "डिजिटल फार्म प्रबंधन पोर्टल",
        "welcome": "डिजिटल फार्म प्रबंधन पोर्टल में आपका स्वागत है",
        "description": "सुअर और मुर्गी पालन किसानों के लिए व्यापक जैव सुरक्षा और रोग निवारण समाधान",
        "home": "होम",
        "risk_assessment": "जोखिम मूल्यांकन",
        "training": "प्रशिक्षण मॉड्यूल",
        "compliance": "अनुपालन ट्रैकिंग",
        "alerts": "अलर्ट और सूचनाएं",
        "monitoring": "निगरानी डैशबोर्ड",
        "networking": "किसान नेटवर्क",
        "data_export": "डेटा निर्यात",
        "language": "भाषा",
        "farm_type": "फार्म प्रकार",
        "pig": "सुअर",
        "poultry": "मुर्गी पालन",
        "submit": "जमा करें",
        "save": "सेव करें",
        "download": "डाउनलोड",
        "upload": "अपलोड",
        "view_details": "विवरण देखें",
        "mark_completed": "पूर्ण के रूप में चिह्नित करें",
        "in_progress": "प्रगति में",
        "completed": "पूर्ण",
        "pending": "लंबित",
        "verified": "सत्यापित",
        "low_risk": "कम जोखिम",
        "medium_risk": "मध्यम जोखिम",
        "high_risk": "उच्च जोखिम"
    }
}


if 'language' not in st.session_state:
    st.session_state.language = 'English'
if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

def get_text(key):
    """Get text based on selected language, always return a string."""
    value = LANGUAGES.get(st.session_state.language, LANGUAGES["English"]).get(key)
    return value if value is not None else str(key)


def load_data(filename):
    # UI-only mode: return static dummy data
    if filename == "risk_assessments.json":
        return {
            "FarmA": {"risk_level": "Low", "timestamp": "2025-09-01T10:00:00"},
            "FarmB": {"risk_level": "High", "timestamp": "2025-09-02T12:00:00"}
        }
    if filename == "training_progress.json":
        return {
            "farmer_001": {"completion_rate": 100},
            "farmer_002": {"completion_rate": 60}
        }
    if filename == "farmers_directory.json":
        return {
            "farmer_001": {"farmer_name": "Amit", "location": "Kolkata", "farm_type": "Pig Farm", "farm_size": "Large (> 500 animals)", "specializations": ["Breeding"], "contact_phone": "1234567890", "contact_email": "amit@example.com", "farm_name": "Amit Farms", "additional_info": "", "registration_date": "2025-09-01T10:00:00", "verified": True},
            "farmer_002": {"farmer_name": "Priya", "location": "Delhi", "farm_type": "Poultry Farm", "farm_size": "Medium (100-500 animals)", "specializations": ["Feed Production"], "contact_phone": "9876543210", "contact_email": "priya@example.com", "farm_name": "Priya Poultry", "additional_info": "", "registration_date": "2025-09-02T12:00:00", "verified": False}
        }
    if filename == "compliance_records.json":
        return {
            "farm_001": {"checklist": {"vaccination_certificate": "Verified", "waste_disposal_permit": "Submitted"}},
            "farm_002": {"checklist": {"vaccination_certificate": "Pending"}}
        }
    if filename == "alert_preferences.json":
        return {}
    return {}

def save_data(filename, data):
    # UI-only mode: do nothing
    pass

def create_sidebar():
    """Create sidebar navigation"""
    with st.sidebar:
        st.image("https://via.placeholder.com/200x100/2E8B57/FFFFFF?text=Farm+Portal", width=200)
        
        # Language selector
        st.selectbox(
            get_text("language"),
            options=list(LANGUAGES.keys()),
            key='language',
            index=list(LANGUAGES.keys()).index(st.session_state.language)
        )
        
        st.markdown("---")
        
        # Navigation menu - Simple selectbox for UI demo
        selected = st.selectbox(
            "Navigate to:",
            options=[
                get_text("home"),
                get_text("risk_assessment"),
                get_text("training"),
                get_text("compliance"),
                get_text("alerts"),
                get_text("monitoring"),
                get_text("networking"),
                get_text("data_export")
            ],
            index=0
        )
    
    return selected

def home_page():
    """Home dashboard page"""
    st.title(get_text("app_title"))
    st.markdown(f"## {get_text('welcome')} 👋")
    st.markdown(f"### {get_text('description')}")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    # Load existing data for stats
    risk_data = load_data("risk_assessments.json")
    training_data = load_data("training_progress.json")
    farmers_data = load_data("farmers_directory.json")
    compliance_data = load_data("compliance_records.json")
    
    with col1:
        st.metric("Total Farms", len(risk_data))
    
    with col2:
        completed_trainings = sum(1 for user in training_data.values() 
                                if user.get('completion_rate', 0) == 100)
        st.metric("Completed Trainings", completed_trainings)
    
    with col3:
        st.metric("Registered Farmers", len(farmers_data))
    
    with col4:
        verified_compliance = sum(1 for record in compliance_data.values() 
                                if record.get('status') == 'Verified')
        st.metric("Verified Compliance", verified_compliance)
    
    # Recent activity
    st.markdown("### Recent Activity")
    activity_col1, activity_col2 = st.columns(2)
    
    with activity_col1:
        st.markdown("#### Latest Risk Assessments")
        if risk_data:
            recent_assessments = sorted(risk_data.items(), 
                                      key=lambda x: x[1].get('timestamp', ''), 
                                      reverse=True)[:5]
            for farm_id, data in recent_assessments:
                risk_level = data.get('risk_level', 'Unknown')
                st.write(f"• **{farm_id}**: {risk_level} Risk")
        else:
            st.write("No risk assessments yet")
    
    with activity_col2:
        st.markdown("#### System Alerts")
        st.info("🦠 Avian Flu reported in nearby district - Check prevention measures")
        st.warning("📊 Weekly compliance report due in 3 days")
        st.success("✅ New training module available: Waste Management")

def risk_assessment_page():
    """Risk assessment tool page"""
    st.title("🔍 " + get_text("risk_assessment"))
    st.markdown("Assess your farm's biosecurity risk level")
    
    st.info("This is a UI demo. No data will be saved.")
    with st.form("risk_assessment_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Farm ID/Name", placeholder="Enter your farm identifier")
            st.selectbox("Animal Type", ["Pig", "Poultry", "Mixed"])
            st.selectbox("Farm Size", ["Small (< 100 animals)", "Medium (100-500 animals)", "Large (> 500 animals)"])
        with col2:
            st.selectbox("Hygiene Practices", ["Excellent", "Good", "Average", "Poor"])
            st.selectbox("Vaccination Records", ["Up to date", "Partially updated", "Outdated"])
            st.selectbox("Waste Management", ["Proper disposal system", "Basic disposal", "Minimal disposal", "No proper system"])
        st.markdown("#### Additional Risk Factors")
        col3, col4 = st.columns(2)
        with col3:
            st.selectbox("Visitor Control", ["Strict protocols", "Basic controls", "Minimal controls", "No controls"])
            st.selectbox("Feed Storage", ["Proper storage", "Adequate storage", "Basic storage", "Poor storage"])
        with col4:
            st.selectbox("Water Quality", ["Tested regularly", "Tested occasionally", "Rarely tested", "Never tested"])
            st.selectbox("Disease History (Past Year)", ["No diseases", "Minor issues", "Major outbreak", "Multiple outbreaks"])
        st.form_submit_button(get_text("submit"))
    st.success("Demo: Risk Score = 45/100 (Medium Risk)")
    st.markdown("### Recommendations")
    st.write("• Improve daily cleaning and disinfection protocols")
    st.write("• Update vaccination schedules immediately")
    st.write("• Implement proper waste disposal and treatment system")

def calculate_risk_score(data):
    """Calculate risk score based on assessment data"""
    score = 0
    
    # Farm size risk (larger farms = higher risk)
    if data['farm_size'] == "Large (> 500 animals)":
        score += 20
    elif data['farm_size'] == "Medium (100-500 animals)":
        score += 10
    else:
        score += 5
    
    # Hygiene practices
    hygiene_scores = {"Poor": 20, "Average": 15, "Good": 8, "Excellent": 0}
    score += hygiene_scores.get(data['hygiene_practices'], 15)
    
    # Vaccination records
    vacc_scores = {"Outdated": 15, "Partially updated": 10, "Up to date": 0}
    score += vacc_scores.get(data['vaccination_records'], 10)
    
    # Waste management
    waste_scores = {"No proper system": 15, "Minimal disposal": 12, "Basic disposal": 8, "Proper disposal system": 0}
    score += waste_scores.get(data['waste_management'], 10)
    
    # Visitor control
    visitor_scores = {"No controls": 10, "Minimal controls": 8, "Basic controls": 5, "Strict protocols": 0}
    score += visitor_scores.get(data['visitor_control'], 8)
    
    # Feed storage
    feed_scores = {"Poor storage": 8, "Basic storage": 6, "Adequate storage": 3, "Proper storage": 0}
    score += feed_scores.get(data['feed_storage'], 6)
    
    # Water quality
    water_scores = {"Never tested": 8, "Rarely tested": 6, "Tested occasionally": 3, "Tested regularly": 0}
    score += water_scores.get(data['water_quality'], 6)
    
    # Disease history
    disease_scores = {"Multiple outbreaks": 15, "Major outbreak": 10, "Minor issues": 5, "No diseases": 0}
    score += disease_scores.get(data['disease_history'], 5)
    
    return min(score, 100)  # Cap at 100

def get_recommendations(risk_level, data):
    """Get recommendations based on risk level and specific issues"""
    recommendations = []
    
    if risk_level == "High":
        recommendations.append("🚨 Immediate action required - Implement strict biosecurity measures")
        recommendations.append("📞 Contact veterinarian for emergency consultation")
        
    if data['hygiene_practices'] in ["Poor", "Average"]:
        recommendations.append("🧼 Improve daily cleaning and disinfection protocols")
        
    if data['vaccination_records'] in ["Outdated", "Partially updated"]:
        recommendations.append("💉 Update vaccination schedules immediately")
        
    if data['waste_management'] in ["No proper system", "Minimal disposal"]:
        recommendations.append("🗑️ Implement proper waste disposal and treatment system")
        
    if data['visitor_control'] in ["No controls", "Minimal controls"]:
        recommendations.append("🚪 Establish strict visitor entry protocols")
        
    if data['water_quality'] in ["Never tested", "Rarely tested"]:
        recommendations.append("💧 Implement regular water quality testing")
        
    if risk_level == "Medium":
        recommendations.append("⚠️ Monitor closely and improve identified weak areas")
        
    if risk_level == "Low":
        recommendations.append("✅ Good practices! Continue current protocols")
        recommendations.append("📈 Consider advanced monitoring systems for optimization")
    
    return recommendations

def training_modules_page():
    """Training modules page"""
    st.title("📚 " + get_text("training"))
    st.markdown("Interactive training modules for farm biosecurity best practices")
    
    # Load training progress
    training_data = load_data("training_progress.json")
    user_id = st.text_input("Enter your User ID", value="farmer_001")
    
    if user_id not in training_data:
        training_data[user_id] = {
            'modules_completed': [],
            'completion_rate': 0,
            'last_updated': datetime.now().isoformat()
        }
    
    user_progress = training_data[user_id]
    
    # Training modules
    modules = [
        {
            'id': 'farm_hygiene',
            'title': 'Farm Hygiene & Sanitation',
            'icon': '🧼',
            'description': 'Learn proper cleaning and disinfection protocols',
            'content': [
                'Daily cleaning schedules for different farm areas',
                'Proper disinfectant selection and usage',
                'Personal protective equipment (PPE) requirements',
                'Hand washing and foot bath protocols',
                'Equipment sanitization procedures'
            ]
        },
        {
            'id': 'feed_storage',
            'title': 'Feed Storage & Management',
            'icon': '🌾',
            'description': 'Best practices for feed storage and handling',
            'content': [
                'Proper storage conditions (temperature, humidity)',
                'Pest control in storage areas',
                'Feed quality inspection procedures',
                'FIFO (First In, First Out) rotation system',
                'Contamination prevention measures'
            ]
        },
        {
            'id': 'worker_protocols',
            'title': 'Worker Entry Protocols',
            'icon': '👥',
            'description': 'Staff and visitor biosecurity protocols',
            'content': [
                'Visitor registration and screening',
                'Protective clothing requirements',
                'Shower and changing procedures',
                'Vehicle disinfection protocols',
                'Emergency response procedures'
            ]
        },
        {
            'id': 'waste_management',
            'title': 'Waste Management',
            'icon': '♻️',
            'description': 'Proper waste disposal and treatment',
            'content': [
                'Waste segregation and classification',
                'Treatment and disposal methods',
                'Composting procedures for organic waste',
                'Liquid waste management',
                'Record keeping and documentation'
            ]
        },
        {
            'id': 'disease_prevention',
            'title': 'Disease Prevention',
            'icon': '🛡️',
            'description': 'Disease prevention and early detection',
            'content': [
                'Common disease symptoms identification',
                'Vaccination schedules and protocols',
                'Quarantine procedures for new animals',
                'Early warning signs and reporting',
                'Emergency response protocols'
            ]
        }
    ]
    
    # Progress overview
    total_modules = len(modules)
    completed_modules = len(user_progress['modules_completed'])
    completion_rate = (completed_modules / total_modules) * 100 if total_modules > 0 else 0
    
    st.markdown(f"### Progress Overview")
    st.progress(completion_rate / 100)
    st.markdown(f"**{completed_modules}/{total_modules} modules completed ({completion_rate:.1f}%)**")
    
    # Display modules
    for module in modules:
        is_completed = module['id'] in user_progress['modules_completed']
        
        with st.expander(f"{module['icon']} {module['title']}" + (" ✅" if is_completed else ""), expanded=not is_completed):
            st.markdown(f"**{module['description']}**")
            
            st.markdown("#### Learning Objectives:")
            for item in module['content']:
                st.write(f"• {item}")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if is_completed:
                    st.success("✅ Module completed!")
                else:
                    st.info("📖 Click 'Mark as Completed' after studying the content")
            
            with col2:
                if not is_completed:
                    if st.button(f"Mark Completed", key=f"complete_{module['id']}"):
                        user_progress['modules_completed'].append(module['id'])
                        user_progress['completion_rate'] = (len(user_progress['modules_completed']) / total_modules) * 100
                        user_progress['last_updated'] = datetime.now().isoformat()
                        training_data[user_id] = user_progress
                        save_data("training_progress.json", training_data)
                        st.rerun()
                else:
                    if st.button(f"Reset", key=f"reset_{module['id']}"):
                        user_progress['modules_completed'].remove(module['id'])
                        user_progress['completion_rate'] = (len(user_progress['modules_completed']) / total_modules) * 100
                        user_progress['last_updated'] = datetime.now().isoformat()
                        training_data[user_id] = user_progress
                        save_data("training_progress.json", training_data)
                        st.rerun()

def compliance_tracking_page():
    """Compliance tracking page"""
    st.title("📋 " + get_text("compliance"))
    st.markdown("Track regulatory compliance and upload required documents")
    
    # Load compliance data
    compliance_data = load_data("compliance_records.json")
    
    farm_id = st.text_input("Farm ID", value="farm_001")
    
    if farm_id not in compliance_data:
        compliance_data[farm_id] = {
            'documents': {},
            'checklist': {},
            'last_updated': datetime.now().isoformat()
        }
    
    farm_compliance = compliance_data[farm_id]
    
    # Compliance checklist
    st.markdown("### Compliance Checklist")
    
    checklist_items = [
        {'id': 'vaccination_certificate', 'title': 'Vaccination Certificate', 'required': True},
        {'id': 'waste_disposal_permit', 'title': 'Waste Disposal Permit', 'required': True},
        {'id': 'water_quality_report', 'title': 'Water Quality Test Report', 'required': True},
        {'id': 'feed_safety_certificate', 'title': 'Feed Safety Certificate', 'required': True},
        {'id': 'biosecurity_plan', 'title': 'Biosecurity Management Plan', 'required': True},
        {'id': 'worker_training_records', 'title': 'Worker Training Records', 'required': False},
        {'id': 'insurance_policy', 'title': 'Farm Insurance Policy', 'required': False},
        {'id': 'emergency_response_plan', 'title': 'Emergency Response Plan', 'required': False}
    ]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for item in checklist_items:
            status = farm_compliance['checklist'].get(item['id'], 'Pending')
            required_text = " (Required)" if item['required'] else " (Optional)"
            
            if status == 'Verified':
                st.success(f"✅ {item['title']}{required_text}")
            elif status == 'Submitted':
                st.warning(f"⏳ {item['title']}{required_text} - Under Review")
            else:
                st.error(f"❌ {item['title']}{required_text} - Pending")
    
    with col2:
        st.markdown("#### Status Summary")
        total_items = len(checklist_items)
        verified_items = sum(1 for item in checklist_items 
                           if farm_compliance['checklist'].get(item['id']) == 'Verified')
        submitted_items = sum(1 for item in checklist_items 
                            if farm_compliance['checklist'].get(item['id']) == 'Submitted')
        
        st.metric("Verified", f"{verified_items}/{total_items}")
        st.metric("Under Review", submitted_items)
        st.metric("Completion Rate", f"{(verified_items/total_items)*100:.1f}%")
    
    # Document upload
    st.markdown("### Document Upload")
    
    selected_doc = st.selectbox(
        "Select Document Type",
        options=[item['title'] for item in checklist_items]
    )
    
    uploaded_file = st.file_uploader(
        f"Upload {selected_doc}",
        type=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'],
        help="Supported formats: PDF, JPG, PNG, DOC, DOCX"
    )
    
    if uploaded_file is not None:
        # Save uploaded file
        upload_path = UPLOADS_DIR / f"{farm_id}_{selected_doc}_{uploaded_file.name}"
        with open(upload_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Update compliance record
        doc_id = next(item['id'] for item in checklist_items if item['title'] == selected_doc)
        farm_compliance['documents'][doc_id] = {
            'filename': uploaded_file.name,
            'upload_date': datetime.now().isoformat(),
            'file_path': str(upload_path)
        }
        farm_compliance['checklist'][doc_id] = 'Submitted'
        farm_compliance['last_updated'] = datetime.now().isoformat()
        
        compliance_data[farm_id] = farm_compliance
        save_data("compliance_records.json", compliance_data)
        
        st.success(f"✅ {selected_doc} uploaded successfully!")
        st.rerun()
    
    # Admin verification section
    if st.session_state.admin_logged_in:
        st.markdown("---")
        st.markdown("### Admin: Document Verification")
        
        for item in checklist_items:
            if item['id'] in farm_compliance['documents']:
                doc_info = farm_compliance['documents'][item['id']]
                current_status = farm_compliance['checklist'].get(item['id'], 'Pending')
                
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.write(f"**{item['title']}** - {doc_info['filename']}")
                    st.write(f"Uploaded: {doc_info['upload_date'][:10]}")
                
                with col2:
                    if st.button(f"Verify", key=f"verify_{item['id']}"):
                        farm_compliance['checklist'][item['id']] = 'Verified'
                        compliance_data[farm_id] = farm_compliance
                        save_data("compliance_records.json", compliance_data)
                        st.rerun()
                
                with col3:
                    if st.button(f"Reject", key=f"reject_{item['id']}"):
                        farm_compliance['checklist'][item['id']] = 'Pending'
                        compliance_data[farm_id] = farm_compliance
                        save_data("compliance_records.json", compliance_data)
                        st.rerun()

def alerts_notifications_page():
    """Alerts and notifications page"""
    st.title("🚨 " + get_text("alerts"))
    st.markdown("Real-time alerts and disease outbreak notifications")
    
    # Load user preferences
    alert_prefs = load_data("alert_preferences.json")
    user_id = st.text_input("User ID", value="farmer_001")
    
    if user_id not in alert_prefs:
        alert_prefs[user_id] = {
            'subscribed': False,
            'alert_types': [],
            'location': '',
            'contact_method': 'email'
        }
    
    user_prefs = alert_prefs[user_id]
    
    # Alert subscription
    st.markdown("### Alert Subscription Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        subscribed = st.checkbox("Subscribe to Alerts", value=user_prefs['subscribed'])
        location = st.text_input("Your Location/District", value=user_prefs['location'])
        
    with col2:
        contact_method = st.selectbox(
            "Preferred Contact Method",
            ["Email", "SMS", "App Notification"],
            index=["email", "sms", "app"].index(user_prefs['contact_method'].lower()) if user_prefs['contact_method'].lower() in ["email", "sms", "app"] else 0
        )
    
    # Alert types
    st.markdown("#### Alert Types")
    alert_types = st.multiselect(
        "Select alert types to receive",
        ["Disease Outbreaks", "Weather Warnings", "Market Prices", "Regulatory Updates", "Training Reminders"],
        default=user_prefs['alert_types']
    )
    
    if st.button("Save Preferences"):
        user_prefs.update({
            'subscribed': subscribed,
            'alert_types': alert_types,
            'location': location,
            'contact_method': contact_method.lower(),
            'last_updated': datetime.now().isoformat()
        })
        alert_prefs[user_id] = user_prefs
        save_data("alert_preferences.json", alert_prefs)
        st.success("Preferences saved successfully!")
    
    # Current alerts
    st.markdown("### Current Alerts")
    
    # Simulated alerts
    alerts = [
        {
            'id': 1,
            'type': 'Disease Outbreak',
            'severity': 'High',
            'title': 'Avian Flu Outbreak Reported',
            'description': 'H5N1 Avian Influenza detected in poultry farms in neighboring district. Implement immediate biosecurity measures.',
            'date': (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M'),
            'location': 'District XYZ (50 km away)',
            'actions': ['Restrict farm access', 'Increase disinfection frequency', 'Monitor bird health closely']
        },
        {
            'id': 2,
            'type': 'Weather Warning',
            'severity': 'Medium',
            'title': 'Heavy Rainfall Expected',
            'description': 'Monsoon rainfall predicted for next 3 days. Ensure proper drainage and feed storage.',
            'date': (datetime.now() - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M'),
            'location': 'Regional Weather Center',
            'actions': ['Check drainage systems', 'Secure feed storage', 'Prepare backup power']
        },
        {
            'id': 3,
            'type': 'Regulatory Update',
            'severity': 'Low',
            'title': 'New Vaccination Guidelines',
            'description': 'Updated vaccination schedule released by Animal Husbandry Department.',
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M'),
            'location': 'State Animal Husbandry Dept',
            'actions': ['Review new guidelines', 'Update vaccination records', 'Consult veterinarian']
        }
    ]
    
    for alert in alerts:
        severity_color = {
            'High': 'red',
            'Medium': 'orange',
            'Low': 'blue'
        }
        
        with st.container():
            st.markdown(f"#### :{severity_color[alert['severity']]}[{alert['severity']} Alert] {alert['title']}")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"**Type:** {alert['type']}")
                st.write(f"**Description:** {alert['description']}")
                st.write(f"**Location:** {alert['location']}")
                st.write(f"**Date:** {alert['date']}")
                
                with st.expander("Recommended Actions"):
                    for action in alert['actions']:
                        st.write(f"• {action}")
            
            with col2:
                if alert['severity'] == 'High':
                    st.error("🚨 Immediate Action Required")
                elif alert['severity'] == 'Medium':
                    st.warning("⚠️ Monitor Closely")
                else:
                    st.info("ℹ️ For Your Information")
            
            st.markdown("---")

def monitoring_dashboard_page():
    """Monitoring dashboard page"""
    st.title("📊 " + get_text("monitoring"))
    st.markdown("Data visualization and farm monitoring dashboard")
    
    # Load data
    risk_data = load_data("risk_assessments.json")
    training_data = load_data("training_progress.json")
    compliance_data = load_data("compliance_records.json")
    
    # Data upload section
    st.markdown("### Upload Your Farm Data")
    uploaded_csv = st.file_uploader(
        "Upload CSV file with your farm data",
        type=['csv'],
        help="Upload your own data for custom visualizations"
    )
    
    custom_data = None
    if uploaded_csv is not None:
        try:
            custom_data = pd.read_csv(uploaded_csv)
            st.success(f"Data uploaded successfully! {len(custom_data)} records loaded.")
            st.dataframe(custom_data.head())
        except Exception as e:
            st.error(f"Error loading data: {e}")
    
    # Dashboard sections
    tab1, tab2, tab3, tab4 = st.tabs(["Risk Analysis", "Training Progress", "Compliance Status", "Custom Data"])
    
    with tab1:
        st.markdown("#### Risk Assessment Analysis")
        
        if risk_data:
            # Convert to DataFrame
            df_risk = pd.DataFrame.from_dict(risk_data, orient='index')
            df_risk.reset_index(inplace=True)
            df_risk.rename(columns={'index': 'farm_id'}, inplace=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Risk level distribution
                risk_counts = df_risk['risk_level'].value_counts()
                fig_pie = px.pie(
                    values=risk_counts.values,
                    names=risk_counts.index,
                    title="Risk Level Distribution",
                    color_discrete_map={
                        'Low': 'green',
                        'Medium': 'yellow',
                        'High': 'red'
                    }
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            
            with col2:
                # Risk scores by animal type
                fig_box = px.box(
                    df_risk,
                    x='animal_type',
                    y='risk_score',
                    title="Risk Scores by Animal Type",
                    color='animal_type'
                )
                st.plotly_chart(fig_box, use_container_width=True)
            
            # Risk score trend (if timestamps available)
            if 'timestamp' in df_risk.columns:
                df_risk['date'] = pd.to_datetime(df_risk['timestamp']).dt.date
                daily_avg = df_risk.groupby('date')['risk_score'].mean().reset_index()
                
                if len(daily_avg) > 1:
                    fig_line = px.line(
                        daily_avg,
                        x='date',
                        y='risk_score',
                        title="Average Risk Score Trend",
                        markers=True
                    )
                    st.plotly_chart(fig_line, use_container_width=True)
            
            # Detailed risk factors analysis
            st.markdown("#### Risk Factors Analysis")
            factors = ['hygiene_practices', 'vaccination_records', 'waste_management', 'visitor_control']
            
            if all(factor in df_risk.columns for factor in factors):
                factor_data = []
                for factor in factors:
                    factor_counts = df_risk[factor].value_counts()
                    for practice, count in factor_counts.items():
                        factor_data.append({'Factor': factor.replace('_', ' ').title(), 'Practice': practice, 'Count': count})
                
                df_factors = pd.DataFrame(factor_data)
                fig_factors = px.bar(
                    df_factors,
                    x='Factor',
                    y='Count',
                    color='Practice',
                    title="Farm Practices Distribution",
                    text='Count'
                )
                fig_factors.update_traces(texttemplate='%{text}', textposition='outside')
                st.plotly_chart(fig_factors, use_container_width=True)
        else:
            st.info("No risk assessment data available. Complete some assessments to see visualizations.")
    
    with tab2:
        st.markdown("#### Training Progress Analysis")
        
        if training_data:
            # Training completion rates
            completion_rates = [user_data.get('completion_rate', 0) for user_data in training_data.values()]
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Completion rate distribution
                fig_hist = px.histogram(
                    x=completion_rates,
                    nbins=10,
                    title="Training Completion Rate Distribution",
                    labels={'x': 'Completion Rate (%)', 'y': 'Number of Users'}
                )
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                # Average completion rate over time
                avg_completion = sum(completion_rates) / len(completion_rates)
                st.metric("Average Completion Rate", f"{avg_completion:.1f}%")
                
                completed_users = sum(1 for rate in completion_rates if rate == 100)
                st.metric("Fully Completed Users", f"{completed_users}/{len(training_data)}")
        else:
            st.info("No training data available.")
    
    with tab3:
        st.markdown("#### Compliance Status Overview")
        
        if compliance_data:
            compliance_stats = []
            for farm_id, farm_data in compliance_data.items():
                checklist = farm_data.get('checklist', {})
                total_items = len(checklist)
                verified_items = sum(1 for status in checklist.values() if status == 'Verified')
                completion_rate = (verified_items / total_items * 100) if total_items > 0 else 0
                
                compliance_stats.append({
                    'farm_id': farm_id,
                    'completion_rate': completion_rate,
                    'verified_items': verified_items,
                    'total_items': total_items
                })
            
            df_compliance = pd.DataFrame(compliance_stats)
            
            if not df_compliance.empty:
                col1, col2 = st.columns(2)
                
                with col1:
                    fig_compliance = px.bar(
                        df_compliance,
                        x='farm_id',
                        y='completion_rate',
                        title="Compliance Completion Rate by Farm",
                        labels={'completion_rate': 'Completion Rate (%)'}
                    )
                    st.plotly_chart(fig_compliance, use_container_width=True)
                
                with col2:
                    avg_compliance = df_compliance['completion_rate'].mean()
                    st.metric("Average Compliance Rate", f"{avg_compliance:.1f}%")
                    
                    fully_compliant = sum(1 for rate in df_compliance['completion_rate'] if rate == 100)
                    st.metric("Fully Compliant Farms", f"{fully_compliant}/{len(df_compliance)}")
        else:
            st.info("No compliance data available.")
    
    with tab4:
        st.markdown("#### Custom Data Analysis")
        
        if custom_data is not None:
            st.markdown("##### Data Overview")
            st.write(f"**Shape:** {custom_data.shape[0]} rows, {custom_data.shape[1]} columns")
            st.write(f"**Columns:** {', '.join(custom_data.columns)}")
            
            # Basic statistics
            if len(custom_data.select_dtypes(include=[float, int]).columns) > 0:
                st.markdown("##### Numerical Summary")
                st.dataframe(custom_data.describe())
            
            # Visualization options
            st.markdown("##### Create Visualizations")
            
            numeric_columns = custom_data.select_dtypes(include=[float, int]).columns.tolist()
            categorical_columns = custom_data.select_dtypes(include=[object]).columns.tolist()
            
            if len(numeric_columns) > 0:
                col1, col2 = st.columns(2)
                
                with col1:
                    x_axis = st.selectbox("Select X-axis", custom_data.columns)
                    
                with col2:
                    y_axis = st.selectbox("Select Y-axis", numeric_columns)
                
                chart_type = st.selectbox("Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram"])
                
                if st.button("Generate Chart"):
                    try:
                        if chart_type == "Scatter Plot":
                            fig = px.scatter(custom_data, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
                        elif chart_type == "Line Chart":
                            fig = px.line(custom_data, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
                        elif chart_type == "Bar Chart":
                            fig = px.bar(custom_data, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
                        elif chart_type == "Histogram":
                            fig = px.histogram(custom_data, x=y_axis, title=f"Distribution of {y_axis}")
                        
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"Error creating chart: {e}")
        else:
            st.info("Upload a CSV file to analyze your custom data.")

def farmer_network_page():
    """Farmer networking page"""
    st.title("👥 " + get_text("networking"))
    st.markdown("Connect with other farmers in your region")
    
    # Load farmers directory
    farmers_data = load_data("farmers_directory.json")
    
    # Registration form
    st.markdown("### Register Your Farm")
    
    with st.form("farmer_registration"):
        col1, col2 = st.columns(2)
        
        with col1:
            farmer_name = st.text_input("Farmer Name")
            farm_name = st.text_input("Farm Name")
            location = st.text_input("Location/District")
            
        with col2:
            contact_phone = st.text_input("Phone Number")
            contact_email = st.text_input("Email Address")
            farm_type = st.selectbox("Farm Type", ["Pig Farm", "Poultry Farm", "Mixed Farm"])
        
        farm_size = st.selectbox("Farm Size", ["Small (< 100 animals)", "Medium (100-500 animals)", "Large (> 500 animals)"])
        
        specializations = st.multiselect(
            "Specializations/Interests",
            ["Breeding", "Organic Farming", "Feed Production", "Disease Management", "Waste Management", "Technology Integration"]
        )
        
        additional_info = st.text_area("Additional Information (Optional)", placeholder="Any additional information you'd like to share...")
        
        submitted = st.form_submit_button("Register")
        
        if submitted and farmer_name and farm_name and location:
            farmer_id = f"farmer_{len(farmers_data) + 1:03d}"
            
            farmers_data[farmer_id] = {
                'farmer_name': farmer_name,
                'farm_name': farm_name,
                'location': location,
                'contact_phone': contact_phone,
                'contact_email': contact_email,
                'farm_type': farm_type,
                'farm_size': farm_size,
                'specializations': specializations,
                'additional_info': additional_info,
                'registration_date': datetime.now().isoformat(),
                'verified': False
            }
            
            save_data("farmers_directory.json", farmers_data)
            st.success(f"Registration successful! Your Farmer ID is: {farmer_id}")
            st.rerun()
    
    # Search and filter
    st.markdown("### Farmer Directory")
    
    if farmers_data:
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            location_filter = st.selectbox(
                "Filter by Location",
                ["All"] + list(set(farmer['location'] for farmer in farmers_data.values()))
            )
        
        with col2:
            farm_type_filter = st.selectbox(
                "Filter by Farm Type",
                ["All"] + list(set(farmer['farm_type'] for farmer in farmers_data.values()))
            )
        
        with col3:
            search_term = st.text_input("Search by name or specialization")
        
        # Apply filters
        filtered_farmers = farmers_data.copy()
        
        if location_filter != "All":
            filtered_farmers = {k: v for k, v in filtered_farmers.items() if v['location'] == location_filter}
        
        if farm_type_filter != "All":
            filtered_farmers = {k: v for k, v in filtered_farmers.items() if v['farm_type'] == farm_type_filter}
        
        if search_term:
            search_term = search_term.lower()
            filtered_farmers = {
                k: v for k, v in filtered_farmers.items()
                if (search_term in v['farmer_name'].lower() or
                    search_term in v['farm_name'].lower() or
                    any(search_term in spec.lower() for spec in v['specializations']))
            }
        
        # Display farmers
        st.markdown(f"**{len(filtered_farmers)} farmers found**")
        
        for farmer_id, farmer in filtered_farmers.items():
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    verified_badge = " ✅" if farmer.get('verified', False) else ""
                    st.markdown(f"#### {farmer['farmer_name']}{verified_badge}")
                    st.write(f"**Farm:** {farmer['farm_name']}")
                    st.write(f"**Location:** {farmer['location']}")
                    st.write(f"**Type:** {farmer['farm_type']} ({farmer['farm_size']})")
                    
                    if farmer['specializations']:
                        st.write(f"**Specializations:** {', '.join(farmer['specializations'])}")
                
                with col2:
                    if farmer['contact_phone']:
                        st.write(f"📞 {farmer['contact_phone']}")
                    if farmer['contact_email']:
                        st.write(f"📧 {farmer['contact_email']}")
                
                with col3:
                    if st.button(f"View Profile", key=f"profile_{farmer_id}"):
                        st.info(f"**Registration Date:** {farmer['registration_date'][:10]}")
                        if farmer['additional_info']:
                            st.write(f"**Additional Info:** {farmer['additional_info']}")
                
                st.markdown("---")
    else:
        st.info("No farmers registered yet. Be the first to register!")

def data_export_page():
    """Data export and admin page"""
    st.title("📥 " + get_text("data_export"))
    st.markdown("Export farm data for policy analysis and administrative functions")
    
    # Admin login
    if not st.session_state.admin_logged_in:
        st.markdown("### Admin Login")
        password = st.text_input("Enter admin password", type="password")
        
        if st.button("Login"):
            if password == "admin123":  # Simple password for demo
                st.session_state.admin_logged_in = True
                st.success("Admin login successful!")
                st.rerun()
            else:
                st.error("Invalid password")
        
        st.markdown("---")
        st.markdown("### Public Data Export")
        st.markdown("*Limited data export available without admin access*")
        
        # Basic export for farmers
        if st.button("Export My Training Progress"):
            training_data = load_data("training_progress.json")
            if training_data:
                df_training = pd.DataFrame.from_dict(training_data, orient='index')
                csv = df_training.to_csv(index=True)
                st.download_button(
                    label="Download Training Data CSV",
                    data=csv,
                    file_name=f"training_progress_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
            else:
                st.info("No training data available")
        
        return
    
    # Admin functions
    st.success("🔐 Admin access granted")
    
    # Load all data
    risk_data = load_data("risk_assessments.json")
    training_data = load_data("training_progress.json")
    compliance_data = load_data("compliance_records.json")
    farmers_data = load_data("farmers_directory.json")
    alert_prefs = load_data("alert_preferences.json")
    
    # Admin dashboard
    st.markdown("### Administrative Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Risk Assessments", len(risk_data))
    
    with col2:
        st.metric("Registered Farmers", len(farmers_data))
    
    with col3:
        completed_training = sum(1 for user in training_data.values() if user.get('completion_rate', 0) == 100)
        st.metric("Completed Training", completed_training)
    
    with col4:
        verified_compliance = sum(1 for farm in compliance_data.values() 
                                 if any(status == 'Verified' for status in farm.get('checklist', {}).values()))
        st.metric("Verified Compliance", verified_compliance)
    
    # Export options
    st.markdown("### Data Export Options")
    
    export_tab1, export_tab2, export_tab3 = st.tabs(["Individual Datasets", "Aggregated Reports", "System Analytics"])
    
    with export_tab1:
        st.markdown("#### Individual Dataset Export")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Export Risk Assessments"):
                if risk_data:
                    df_risk = pd.DataFrame.from_dict(risk_data, orient='index')
                    csv = df_risk.to_csv(index=True)
                    st.download_button(
                        label="Download Risk Assessment Data",
                        data=csv,
                        file_name=f"risk_assessments_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("No risk assessment data available")
            
            if st.button("Export Training Data"):
                if training_data:
                    df_training = pd.DataFrame.from_dict(training_data, orient='index')
                    csv = df_training.to_csv(index=True)
                    st.download_button(
                        label="Download Training Data",
                        data=csv,
                        file_name=f"training_data_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("No training data available")
        
        with col2:
            if st.button("Export Compliance Data"):
                if compliance_data:
                    # Flatten compliance data for CSV export
                    compliance_rows = []
                    for farm_id, farm_data in compliance_data.items():
                        checklist = farm_data.get('checklist', {})
                        for item, status in checklist.items():
                            compliance_rows.append({
                                'farm_id': farm_id,
                                'compliance_item': item,
                                'status': status,
                                'last_updated': farm_data.get('last_updated', '')
                            })
                    
                    df_compliance = pd.DataFrame(compliance_rows)
                    csv = df_compliance.to_csv(index=False)
                    st.download_button(
                        label="Download Compliance Data",
                        data=csv,
                        file_name=f"compliance_data_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("No compliance data available")
            
            if st.button("Export Farmers Directory"):
                if farmers_data:
                    df_farmers = pd.DataFrame.from_dict(farmers_data, orient='index')
                    csv = df_farmers.to_csv(index=True)
                    st.download_button(
                        label="Download Farmers Directory",
                        data=csv,
                        file_name=f"farmers_directory_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("No farmers directory data available")
    
    with export_tab2:
        st.markdown("#### Aggregated Reports")
        
        # Generate summary report
        if st.button("Generate Summary Report"):
            report_data = {
                'report_date': datetime.now().isoformat(),
                'total_farms': len(risk_data),
                'total_farmers': len(farmers_data),
                'total_training_users': len(training_data),
                'total_compliance_records': len(compliance_data),
                'avg_risk_score': sum(farm['risk_score'] for farm in risk_data.values()) / len(risk_data) if risk_data else 0,
                'avg_training_completion': sum(user.get('completion_rate', 0) for user in training_data.values()) / len(training_data) if training_data else 0,
                'high_risk_farms': sum(1 for farm in risk_data.values() if farm.get('risk_level') == 'High'),
                'completed_training_users': sum(1 for user in training_data.values() if user.get('completion_rate', 0) == 100),
                'verified_compliance_farms': sum(1 for farm in compliance_data.values() 
                                               if any(status == 'Verified' for status in farm.get('checklist', {}).values()))
            }
            
            report_df = pd.DataFrame([report_data])
            csv = report_df.to_csv(index=False)
            st.download_button(
                label="Download Summary Report",
                data=csv,
                file_name=f"summary_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
            
            # Display summary
            st.markdown("#### Report Summary")
            st.json(report_data)
    
    with export_tab3:
        st.markdown("#### System Analytics")
        
        # System usage analytics
        total_records = len(risk_data) + len(training_data) + len(compliance_data) + len(farmers_data)
        
        analytics_data = {
            'total_system_records': total_records,
            'risk_assessments_percentage': (len(risk_data) / total_records * 100) if total_records > 0 else 0,
            'training_records_percentage': (len(training_data) / total_records * 100) if total_records > 0 else 0,
            'compliance_records_percentage': (len(compliance_data) / total_records * 100) if total_records > 0 else 0,
            'farmer_registrations_percentage': (len(farmers_data) / total_records * 100) if total_records > 0 else 0,
            'system_health_score': 85,  # Simulated system health score
            'last_backup': datetime.now().isoformat()
        }
        
        st.json(analytics_data)
        
        if st.button("Export System Analytics"):
            analytics_df = pd.DataFrame([analytics_data])
            csv = analytics_df.to_csv(index=False)
            st.download_button(
                label="Download System Analytics",
                data=csv,
                file_name=f"system_analytics_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    # Logout
    st.markdown("---")
    if st.button("Logout Admin"):
        st.session_state.admin_logged_in = False
        st.rerun()

def main():
    """Main application function"""
    # Create sidebar and get selected page
    selected_page = create_sidebar()
    
    # Route to appropriate page
    page_mapping = {
        get_text("home"): home_page,
        get_text("risk_assessment"): risk_assessment_page,
        get_text("training"): training_modules_page,
        get_text("compliance"): compliance_tracking_page,
        get_text("alerts"): alerts_notifications_page,
        get_text("monitoring"): monitoring_dashboard_page,
        get_text("networking"): farmer_network_page,
        get_text("data_export"): data_export_page
    }
    
    # Execute selected page function
    if selected_page in page_mapping:
        page_mapping[selected_page]()
    else:
        home_page()  # Default to home page

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
    
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E8B57;
    }
    
    .alert-high {
        border-left: 4px solid #ff4b4b;
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .alert-medium {
        border-left: 4px solid #ff9800;
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .alert-low {
        border-left: 4px solid #2196f3;
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
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
