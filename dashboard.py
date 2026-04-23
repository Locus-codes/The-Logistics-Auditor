import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Logistics Auditor Dashboard",
    page_icon="📦",
    layout="wide"
)

# Title
st.title("The 'Last Mile' Logistics Auditor")
st.markdown("**Veridi Logistics - Delivery Performance Analysis**")

# Sidebar
st.sidebar.header("📊 Dashboard Navigation")
page = st.sidebar.selectbox("Choose Analysis", 
    ["Executive Summary", "Delivery Performance", "Geographic Analysis", "Customer Sentiment"])

if page == "Executive Summary":
    st.header(" Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Orders", "99,441")
    with col2:
        st.metric("Late Delivery Rate", "7.9%", delta="-2.1%")
    with col3:
        st.metric("Worst State", "Alagoas (AL)", delta="23.1%")
    with col4:
        st.metric("Review Impact", "2.39 stars", delta="-2.39")
    
    st.markdown("""
    ### Key Findings
    Our analysis of nearly 100,000 orders confirms that delivery delays are directly damaging our customer ratings, especially in the Northeast. While our average late rate is 7.9%, states like Alagoas and Maranhão are seeing much higher delays, which is causing a significant drop in satisfaction. The data shows a clear slide from 4.25 stars for on-time deliveries down to just 1.86 stars for "super late" orders.
    
    ### Recommendations
    - 🎯 **Immediate Focus:** Improve logistics in AL, MA, PI
    - 📅 **Set realistic delivery estimates** for remote areas  
    - 🏢 **Invest in regional distribution centers**
    - 📊 **Monitor delivery performance** by state monthly
    """)

elif page == "Delivery Performance":
    st.header("Delivery Performance Analysis")
    
    # Delivery status pie chart
    delivery_counts = {
        'On Time': 90381,
        'Late': 3162, 
        'Super Late': 4664,
        'Not Delivered': 1234
    }
    
    fig_pie = px.pie(
        values=list(delivery_counts.values()),
        names=list(delivery_counts.keys()),
        title="Delivery Status Distribution",
        color_discrete_map={
            'On Time': '#2E8B57',
            'Late': '#FF8C00', 
            'Super Late': '#DC143C',
            'Not Delivered': '#696969'
        }
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Review scores by delivery status
    st.subheader("📊 Review Scores by Delivery Status")
    
    review_data = {
        'Delivery Status': ['On Time', 'Late', 'Super Late'],
        'Average Review Score': [4.25, 3.60, 1.86]
    }
    
    fig_bar = px.bar(
        x=review_data['Delivery Status'],
        y=review_data['Average Review Score'],
        title="Average Review Score by Delivery Status",
        color=review_data['Average Review Score'],
        color_continuous_scale=['red', 'orange', 'green']
    )
    fig_bar.update_layout(yaxis_range=[0, 5])
    st.plotly_chart(fig_bar, use_container_width=True)

elif page == "Geographic Analysis":
    st.header("🗺️ Geographic Performance Analysis")
    
    # Worst performing states
    worst_states = {
        'State': ['AL', 'MA', 'PI', 'CE', 'SE', 'BA', 'RJ', 'TO', 'ES', 'PA'],
        'Late Percentage': [23.1, 19.2, 15.5, 14.8, 14.8, 13.7, 13.1, 12.6, 12.1, 12.1],
        'Total Orders': [411, 736, 490, 1323, 345, 3344, 12698, 278, 2018, 969]
    }
    
    fig_geo = px.bar(
        x=worst_states['Late Percentage'],
        y=worst_states['State'],
        orientation='h',
        title="Top 10 Worst Performing States (Late Delivery %)",
        color=worst_states['Late Percentage'],
        color_continuous_scale='Reds'
    )
    fig_geo.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_geo, use_container_width=True)
    
    # State details table
    st.subheader("📋 State Performance Details")
    df_states = pd.DataFrame(worst_states)
    st.dataframe(df_states, use_container_width=True)

elif page == "Customer Sentiment":
    st.header("⭐ Customer Sentiment Analysis")
    
    # Review score trend
    sentiment_data = {
        'Delivery Status': ['On Time', 'Late', 'Super Late'],
        'Average Stars': [4.25, 3.60, 1.86],
        'Order Count': [90381, 3162, 4664]
    }
    
    fig_sentiment = go.Figure()
    fig_sentiment.add_trace(go.Scatter(
        x=sentiment_data['Delivery Status'],
        y=sentiment_data['Average Stars'],
        mode='lines+markers',
        line=dict(color='red', width=4),
        marker=dict(size=12)
    ))
    fig_sentiment.update_layout(
        title="Customer Satisfaction Decline",
        yaxis_title="Average Review Score (1-5 stars)",
        yaxis_range=[0, 5]
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)
    
    # Impact summary
    st.subheader("💡 Business Impact")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **The Problem:**
        - 2.39-star difference between best and worst delivery performance
        - Super late orders get 1.86 stars (terrible reviews)
        - Late deliveries directly cause customer dissatisfaction
        """)
    
    with col2:
        st.success("""
        **The Solution:**
        - Focus on northeastern states (AL, MA, PI)
        - Improve delivery time estimates
        - Invest in regional logistics infrastructure
        """)

# Footer
st.markdown("---")
st.markdown("**Data Source:** Olist Brazilian E-Commerce Dataset | **Analysis:** Logistics Auditor Dashboard")