# enhanced_streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
from datetime import datetime
import io
import base64

# Page configuration
st.set_page_config(
    page_title="AI Supply Chain Intelligence",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .ai-response {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .agent-thinking {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        font-style: italic;
    }
    .risk-high { 
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 8px;
        font-weight: bold;
    }
    .risk-medium { 
        background: linear-gradient(135deg, #feca57 0%, #ff9ff3 100%);
        color: black;
        padding: 0.5rem;
        border-radius: 8px;
        font-weight: bold;
    }
    .risk-low { 
        background: linear-gradient(135deg, #48cae4 0%, #00b4d8 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 8px;
        font-weight: bold;
    }
    .tool-usage {
        background: #2d3436;
        color: #dfe6e9;
        padding: 0.5rem;
        border-radius: 8px;
        font-family: monospace;
        font-size: 0.9rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class EnhancedSupplyChainAI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.conversation_id = f"conv_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def chat_with_agent(self, message):
        """Send message to enhanced AI agent"""
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={"message": message},
                timeout=45
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "response": data['response'],
                    "history": data.get('conversation_history', []),
                    "agent_used": data.get('agent_used', False),
                    "success": True
                }
            else:
                return {
                    "response": f"API Error: {response.text}",
                    "history": [],
                    "agent_used": False,
                    "success": False
                }
        except Exception as e:
            return {
                "response": f"Connection error: {str(e)}",
                "history": [],
                "agent_used": False,
                "success": False
            }
    
    def analyze_route(self, origin, destination):
        """Enhanced route analysis"""
        try:
            response = requests.post(
                f"{self.base_url}/api/analyze_route",
                json={"origin": origin, "destination": destination},
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
    
    def generate_report(self, report_type="comprehensive"):
        """Generate enhanced report"""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate_report",
                json={"report_type": report_type},
                timeout=60
            )
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
    
    def clear_history(self):
        """Clear conversation history"""
        try:
            response = requests.post(f"{self.base_url}/api/clear_history", timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def get_port_risks(self):
        """Get port risk data"""
        try:
            response = requests.get(f"{self.base_url}/api/port_risks", timeout=10)
            if response.status_code == 200:
                return response.json()['data']
            return None
        except:
            return self.get_sample_data()
    
    def get_sample_data(self):
        return [
            {"port_name": "Shanghai", "country": "China", "overall_risk": 0.24, "risk_level": "LOW"},
            {"port_name": "Los Angeles", "country": "USA", "overall_risk": 0.266, "risk_level": "LOW"},
            {"port_name": "Hong Kong", "country": "China", "overall_risk": 0.277, "risk_level": "LOW"},
        ]

def display_ai_response(response_text):
    """Display AI response with enhanced formatting"""
    # Detect tool usage in response
    if "TOOL:" in response_text:
        st.markdown('<div class="tool-usage">🛠️ Agent is using tools to gather data...</div>', unsafe_allow_html=True)
    
    # Display the response with enhanced styling
    st.markdown(f'<div class="ai-response">{response_text}</div>', unsafe_allow_html=True)

def display_conversation_history(history):
    """Display conversation history"""
    if history:
        st.subheader("💬 Conversation History")
        for message in history[-6:]:  # Show last 3 exchanges
            if message.startswith("User:"):
                st.markdown(f'<div class="user-message"><strong>👤 You:</strong> {message[6:]}</div>', unsafe_allow_html=True)
            elif message.startswith("Assistant:"):
                st.markdown(f'<div class="ai-response"><strong>🤖 AI:</strong> {message[11:]}</div>', unsafe_allow_html=True)

def main():
    # Initialize enhanced AI client
    base_url = "https://preferable-margherita-undelegated.ngrok-free.dev"  # Replace with actual URL
    ai_client = EnhancedSupplyChainAI(base_url)
    
    # Header
    st.markdown('<h1 class="main-header">🚢 AI Supply Chain Intelligence Platform</h1>', unsafe_allow_html=True)
    st.markdown("Powered by **Enhanced AI Agent • Azure OpenAI • Real-time Analytics**")
    
    # Sidebar
    st.sidebar.title("🧭 Navigation")
    page = st.sidebar.radio("Go to", ["AI Assistant", "Risk Dashboard", "Route Analysis", "Reports"])
    
    # Health check
    try:
        health_response = requests.get(f"{base_url}/api/health", timeout=5)
        if health_response.status_code == 200:
            health_data = health_response.json()
            st.sidebar.success(f"✅ API Connected")
            if health_data.get('agent_initialized'):
                st.sidebar.success("🤖 Enhanced Agent Active")
            else:
                st.sidebar.warning("⚠️ Basic Mode - Configure AI")
        else:
            st.sidebar.warning("⚠️ Using demo data")
    except:
        st.sidebar.warning("⚠️ Using demo data")
    
    # Initialize session state for conversation
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'thinking' not in st.session_state:
        st.session_state.thinking = False
    
    if page == "AI Assistant":
        show_ai_assistant(ai_client)
    elif page == "Risk Dashboard":
        show_risk_dashboard(ai_client)
    elif page == "Route Analysis":
        show_route_analysis(ai_client)
    elif page == "Reports":
        show_reports(ai_client)

def show_ai_assistant(ai_client):
    """Enhanced AI Chat Assistant"""
    st.header("🤖 Enhanced Supply Chain AI Assistant")
    st.markdown("Ask me anything about port risks, shipping routes, disasters, or generate comprehensive reports")
    
    # Initialize session state for quick actions
    if 'last_action' not in st.session_state:
        st.session_state.last_action = None
    
    # Quick actions
    st.subheader("🚀 Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔍 Check Shanghai Risk", use_container_width=True, key="shanghai_btn"):
            st.session_state.last_action = "shanghai"
            st.rerun()
    
    with col2:
        if st.button("🗺️ Analyze Route", use_container_width=True, key="route_btn"):
            st.session_state.last_action = "route"
            st.rerun()
    
    with col3:
        if st.button("🌪️ Recent Disasters", use_container_width=True, key="disasters_btn"):
            st.session_state.last_action = "disasters"
            st.rerun()
    
    with col4:
        if st.button("📊 Full Report", use_container_width=True, key="report_btn"):
            st.session_state.last_action = "report"
            st.rerun()
    
    # Handle quick actions after rerun
    if st.session_state.last_action == "shanghai":
        query = "What's the current risk situation for Shanghai port with detailed analysis?"
        if not any(msg["content"] == query for msg in st.session_state.conversation[-5:] if msg["role"] == "user"):
            st.session_state.conversation.append({"role": "user", "content": query})
        st.session_state.last_action = None
    
    elif st.session_state.last_action == "route":
        query = "Analyze the shipping route from Shanghai to Los Angeles with all risk factors"
        if not any(msg["content"] == query for msg in st.session_state.conversation[-5:] if msg["role"] == "user"):
            st.session_state.conversation.append({"role": "user", "content": query})
        st.session_state.last_action = None
    
    elif st.session_state.last_action == "disasters":
        query = "Show me recent natural disasters in Asia that could affect supply chains"
        if not any(msg["content"] == query for msg in st.session_state.conversation[-5:] if msg["role"] == "user"):
            st.session_state.conversation.append({"role": "user", "content": query})
        st.session_state.last_action = None
    
    elif st.session_state.last_action == "report":
        query = "Generate a comprehensive risk intelligence report for our global supply chain"
        if not any(msg["content"] == query for msg in st.session_state.conversation[-5:] if msg["role"] == "user"):
            st.session_state.conversation.append({"role": "user", "content": query})
        st.session_state.last_action = None
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation", type="secondary", key="clear_btn"):
        if ai_client.clear_history():
            st.session_state.conversation = []
            st.session_state.last_action = None
            st.success("Conversation cleared!")
        st.rerun()
    
    # Display conversation
    st.subheader("💬 Conversation")
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message"><strong>👤 You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            display_ai_response(message["content"])
    
    # Chat input
    user_input = st.chat_input("Ask about supply chain risks, routes, disasters...")
    
    if user_input:
        # Add user message
        st.session_state.conversation.append({"role": "user", "content": user_input})
        
        # Show thinking indicator
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown('<div class="agent-thinking">🤔 Enhanced agent is analyzing your query...</div>', unsafe_allow_html=True)
        
        # Get AI response
        response_data = ai_client.chat_with_agent(user_input)
        
        # Remove thinking indicator
        thinking_placeholder.empty()
        
        if response_data["success"]:
            # Add AI response
            st.session_state.conversation.append({"role": "assistant", "content": response_data["response"]})
            
            # Show agent status
            if response_data.get("agent_used"):
                st.success("✅ Enhanced agent used tools for comprehensive analysis")
            else:
                st.info("ℹ️ Basic response - configure Azure OpenAI for full capabilities")
        else:
            st.error("❌ Failed to get response from AI agent")
        
        st.rerun()

def show_risk_dashboard(ai_client):
    """Enhanced Risk Dashboard"""
    st.header("📊 Enhanced Risk Intelligence Dashboard")
    
    # Load data
    port_risks = ai_client.get_port_risks()
    
    if port_risks:
        df = pd.DataFrame(port_risks)
        
        # Enhanced KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Ports Monitored", len(port_risks), "Global Coverage")
        with col2:
            avg_risk = df['overall_risk'].mean()
            st.metric("Average Risk", f"{avg_risk:.1%}", "Across All Ports")
        with col3:
            high_risk = len(df[df['risk_level'] == 'HIGH'])
            delta = f"+{high_risk}" if high_risk > 0 else "0"
            st.metric("High Risk Ports", high_risk, delta)
        with col4:
            total_news = df['news_mentions'].sum()
            st.metric("News Mentions", total_news, "Recent Activity")
        
        # Risk Map
        st.subheader("🌍 Global Port Risk Heatmap")
        
        coordinates = {
            'Shanghai': (31.23, 121.47), 'Los Angeles': (33.72, -118.27),
            'Hong Kong': (22.32, 114.17), 'Singapore': (1.26, 103.82),
            'Rotterdam': (51.92, 4.48), 'Hamburg': (53.55, 9.99),
            'Shenzhen': (22.54, 114.06), 'Busan': (35.18, 129.08)
        }
        
        df['lat'] = df['port_name'].map(lambda x: coordinates.get(x, (0, 0))[0])
        df['lon'] = df['port_name'].map(lambda x: coordinates.get(x, (0, 0))[1])
        df = df[df['lat'] != 0]
        
        if not df.empty:
            fig = px.scatter_geo(
                df, lat='lat', lon='lon', size='overall_risk',
                color='overall_risk', hover_name='port_name',
                hover_data={'overall_risk': ':.1%', 'country': True, 'risk_level': True},
                title="Enhanced Port Risk Distribution",
                color_continuous_scale="RdYlGn_r",
                size_max=25,
                projection="natural earth"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Enhanced Risk Analysis
        st.subheader("📈 Enhanced Risk Analytics")
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk distribution with enhanced styling
            risk_counts = df['risk_level'].value_counts()
            fig_pie = px.pie(
                values=risk_counts.values,
                names=risk_counts.index,
                title="Risk Level Distribution",
                color=risk_counts.index,
                color_discrete_map={'HIGH': '#FF6B6B', 'MEDIUM': '#FECA57', 'LOW': '#48CAE4'}
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Top risky ports with enhanced display
            st.write("🚨 Top Risky Ports - Enhanced View")
            top_risky = df.nlargest(6, 'overall_risk')
            for _, port in top_risky.iterrows():
                risk_class = "risk-high" if port['overall_risk'] > 0.4 else "risk-medium" if port['overall_risk'] > 0.2 else "risk-low"
                st.markdown(f"""
                <div style='background-color: #f8f9fa; padding: 1rem; margin: 0.5rem 0; border-radius: 10px; border-left: 5px solid #1f77b4;'>
                    <strong>🚢 {port['port_name']}</strong> ({port['country']})<br>
                    <span class="{risk_class}">Risk: {port['overall_risk']:.1%} | {port['risk_level']}</span><br>
                    📍 Disasters: {port['nearby_disasters_count']} | 📰 News: {port['news_mentions']}
                </div>
                """, unsafe_allow_html=True)

def show_route_analysis(ai_client):
    """Enhanced Route Analysis"""
    st.header("🗺️ Enhanced Shipping Route Analysis")
    
    port_risks = ai_client.get_port_risks()
    if port_risks:
        port_names = [p['port_name'] for p in port_risks]
        
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            origin = st.selectbox("📍 Origin Port", port_names, index=0)
        with col2:
            destination = st.selectbox("🎯 Destination Port", port_names, index=1)
        with col3:
            st.write("")  # Spacer
            st.write("")  # Spacer
            analyze_btn = st.button("🚀 Enhanced Analysis", type="primary", use_container_width=True)
        
        if analyze_btn:
            with st.spinner("🔄 Enhanced agent analyzing route with multiple data sources..."):
                analysis = ai_client.analyze_route(origin, destination)
                
            if analysis and analysis.get('success'):
                st.success("✅ Enhanced route analysis completed!")
                
                # Display enhanced results
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    risk_value = analysis['analysis'].get('overall_risk', 0) if isinstance(analysis['analysis'], dict) else 0.25
                    st.metric("Route Risk", f"{risk_value:.1%}")
                with col2:
                    risk_level = analysis['analysis'].get('risk_level', 'MEDIUM') if isinstance(analysis['analysis'], dict) else 'MEDIUM'
                    st.metric("Risk Level", risk_level)
                with col3:
                    st.metric("AI Agent", "✅ Used" if analysis.get('agent_used') else "❌ Basic")
                with col4:
                    st.metric("Analysis", "Enhanced" if analysis.get('agent_used') else "Standard")
                
                # Display analysis
                if isinstance(analysis['analysis'], str):
                    display_ai_response(analysis['analysis'])
                else:
                    st.json(analysis['analysis'])
                
                # Ask follow-up questions
                st.subheader("🔍 Deep Dive Analysis")
                follow_up = st.text_input("Ask specific questions about this route:", 
                                        placeholder="e.g., What are the main disaster risks? Compare with alternative routes...")
                
                if follow_up:
                    with st.spinner("🤔 Enhanced agent processing deep dive..."):
                        follow_up_response = ai_client.chat_with_agent(f"Regarding the route {origin} to {destination}: {follow_up}")
                    
                    if follow_up_response["success"]:
                        display_ai_response(follow_up_response["response"])

def show_reports(ai_client):
    """Enhanced Report Generation"""
    st.header("📄 Enhanced Risk Intelligence Reports")
    
    st.markdown("Generate comprehensive, AI-powered supply chain risk intelligence reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 Quick Reports")
        
        report_types = {
            "Executive Summary": "Brief overview for management",
            "Comprehensive Analysis": "Detailed risk assessment", 
            "Regional Focus - Asia": "Asia-specific risks",
            "Disaster Impact Report": "Natural disaster analysis",
            "Port Performance": "Individual port deep dive"
        }
        
        selected_report = st.selectbox("Report Type", list(report_types.keys()))
        st.caption(report_types[selected_report])
        
        if st.button("📊 Generate Enhanced Report", type="primary"):
            with st.spinner("🔄 Enhanced agent generating comprehensive report..."):
                report_data = ai_client.generate_report(selected_report.lower())
                
            if report_data and report_data.get('success'):
                st.success("✅ Enhanced report generated!")
                
                # Display report
                display_ai_response(report_data['report'])
                
                # Download options
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="📥 Download as Text",
                        data=report_data['report'],
                        file_name=f"enhanced_report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain"
                    )
                with col2:
                    try:
                        pdf_response = requests.get(f"{ai_client.base_url}/api/generate_pdf_report", timeout=30)
                        if pdf_response.status_code == 200:
                            st.download_button(
                                label="📄 Download as PDF",
                                data=pdf_response.content,
                                file_name=f"enhanced_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                                mime="application/pdf"
                            )
                    except:
                        st.info("PDF generation requires active API connection")
    
    with col2:
        st.subheader("🎨 Custom Reports")
        
        custom_focus = st.text_area("Specific Focus Areas:", 
                                  placeholder="e.g., Focus on climate risks, geopolitical factors, specific regions...")
        
        if st.button("🛠️ Generate Custom Report"):
            with st.spinner("🔄 Enhanced agent creating custom analysis..."):
                custom_prompt = f"Generate a custom risk intelligence report focusing on: {custom_focus}"
                response_data = ai_client.chat_with_agent(custom_prompt)
                
            if response_data["success"]:
                st.success("✅ Custom report generated!")
                display_ai_response(response_data["response"])

# Footer
def show_footer():
    st.markdown("---")
    st.markdown(
        "**Enhanced Supply Chain Intelligence** | "
        "Powered by Azure OpenAI • LangChain Agents • Real-time Analytics | "
        "Built with 🚀 by AI Engineering"
    )

if __name__ == "__main__":
    main()
    show_footer()  