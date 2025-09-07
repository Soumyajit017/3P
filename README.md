# P3 - Digital Farm Management Platform

A comprehensive Streamlit-based solution for pig and poultry farmers featuring advanced biosecurity management and disease prevention systems.

## 🌟 Features

### 🏠 Home Dashboard
- Beautiful landing page with modern UI design
- Real-time farm metrics and KPI tracking
- Interactive data visualizations
- Multi-language support (English/Hindi)

### 🔍 Risk Assessment Tool
- AI-powered farm risk evaluation system
- Intelligent biosecurity scoring algorithm
- Personalized recommendations and action plans
- Risk level categorization with visual indicators
- Historical data tracking and trend analysis

### 📊 Analytics Dashboard
- Comprehensive data insights and reporting
- Interactive charts and visualizations
- Geographic analysis and regional insights
- Performance tracking and forecasting
- KPI monitoring with trend indicators

### 🛡️ Protection Hub
- 24/7 emergency response system
- Real-time alert management
- Emergency contact directory
- AI monitoring systems status
- Safety protocols and procedures

### 📚 Training Modules
- Interactive step-by-step best practices
- Progress tracking with completion rates
- Modules covering:
  - Farm Hygiene & Sanitation
  - Feed Storage & Management
  - Worker Entry Protocols
  - Waste Management
  - Disease Prevention

### 📋 Compliance Tracking
- Document upload functionality
- Regulatory compliance checklist
- Status tracking (Pending/Submitted/Verified)
- Admin verification system

### 🚨 Alerts & Notifications
- Real-time outbreak alerts simulation
- Subscription management
- Alert categorization by severity
- Location-based filtering

### 📊 Monitoring Dashboard
- Interactive data visualizations using Plotly
- Risk analysis charts and trends
- Training progress analytics
- Compliance status overview
- Custom CSV data upload and visualization

### 👥 Farmer Network
- Farmer registration and directory
- Search and filter functionality
- Contact information sharing
- Specialization-based networking

### 📥 Data Export & Admin
- Admin authentication system
- Comprehensive data export capabilities
- Aggregated reporting
- System analytics

## Technical Stack

- **Frontend**: Streamlit
- **Data Visualization**: Plotly, Altair
- **Data Storage**: Local JSON/CSV files
- **Navigation**: streamlit-option-menu
- **Data Processing**: Pandas

## Installation & Setup

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://localhost:8501`

## Usage Guide

### For Farmers:
1. **Risk Assessment**: Complete the comprehensive farm assessment to get your risk score and recommendations
2. **Training**: Progress through interactive training modules to improve farm practices
3. **Compliance**: Upload required documents and track compliance status
4. **Networking**: Register your farm and connect with other farmers
5. **Monitoring**: Upload your data to visualize trends and patterns

### For Administrators:
1. **Login**: Use password "admin123" to access admin functions
2. **Document Verification**: Verify uploaded compliance documents
3. **Data Export**: Download comprehensive reports and analytics
4. **System Monitoring**: Track overall system usage and health

## File Structure

```
SIH-2025/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── data/                 # Data storage directory
│   ├── risk_assessments.json
│   ├── training_progress.json
│   ├── compliance_records.json
│   ├── farmers_directory.json
│   └── alert_preferences.json
└── uploads/              # Document upload directory
```

## Key Features Implemented

✅ **Multilingual Support**: English and Hindi language options
✅ **Mobile-Responsive Design**: Works on desktop and mobile devices
✅ **Interactive Forms**: Comprehensive data collection forms
✅ **Data Visualization**: Rich charts and graphs using Plotly
✅ **File Upload**: Document upload with multiple format support
✅ **Progress Tracking**: Training completion and compliance tracking
✅ **Search & Filter**: Advanced filtering in farmer directory
✅ **Admin Panel**: Secure admin access for data management
✅ **Data Export**: CSV export functionality for all data types
✅ **Real-time Updates**: Dynamic content updates and notifications

## Sample Data

The application will automatically create sample data as you use different features:
- Risk assessments are saved when completed
- Training progress is tracked per user
- Compliance documents can be uploaded and verified
- Farmer registrations are stored in the directory

## Security Features

- Admin authentication for sensitive operations
- Secure file upload handling
- Data validation and sanitization
- Session state management

## Customization

The application is designed to be easily customizable:
- **Languages**: Add more languages in the `LANGUAGES` dictionary
- **Risk Factors**: Modify risk calculation in `calculate_risk_score()`
- **Training Modules**: Add new modules in `training_modules_page()`
- **Compliance Items**: Update checklist in `compliance_tracking_page()`

## Support

For technical support or feature requests, please refer to the code comments or documentation within the application.

## License

This project is developed for the Smart India Hackathon 2025 and is intended for educational and demonstration purposes.
