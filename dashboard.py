import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Logistics Auditor Dashboard",
    page_icon="📦",
    layout="wide"
)

# Title
st.title("📦 The 'Last Mile' Logistics Auditor")
st.markdown("**Veridi Logistics - Delivery Performance Analysis**")

# Sidebar
st.sidebar.header("📊 Dashboard Navigation")
page = st.sidebar.selectbox("Choose Analysis", 
    ["Executive Summary", "Delivery Performance", "Geographic Analysis", "Customer Sentiment"])

if page == "Executive Summary":
    st.header("🎯 Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Orders", "99,441")
    with col2:
        st.metric("Late Delivery Rate", "7.9%")
    with col3:
        st.metric("Worst State", "Alagoas (AL)")
    with col4:
        st.metric("Review Impact", "2.39 stars")
    
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
    st.header("⏰ Delivery Performance Analysis")
    
    # Delivery status data
    delivery_data = {
        'Status': ['On Time', 'Late', 'Super Late', 'Not Delivered'],
        'Count': [90381, 3162, 4664, 1234],
        'Percentage': [90.9, 3.2, 4.7, 1.2]
    }
    
    df_delivery = pd.DataFrame(delivery_data)
    
    st.subheader("📊 Delivery Status Distribution")
    st.dataframe(df_delivery, use_container_width=True)
    
    # Simple bar chart using Streamlit
    st.bar_chart(df_delivery.set_index('Status')['Count'])
    
    # Review scores by delivery status
    st.subheader("⭐ Review Scores by Delivery Status")
    
    review_data = {
        'Delivery Status': ['On Time', 'Late', 'Super Late'],
        'Average Review Score': [4.25, 3.60, 1.86],
        'Order Count': [90381, 3162, 4664]
    }
    
    df_reviews = pd.DataFrame(review_data)
    st.dataframe(df_reviews, use_container_width=True)
    st.bar_chart(df_reviews.set_index('Delivery Status')['Average Review Score'])

elif page == "Geographic Analysis":
    st.header("🗺️ Geographic Performance Analysis")
    
    # Worst performing states
    worst_states = {
        'State': ['AL', 'MA', 'PI', 'CE', 'SE', 'BA', 'RJ', 'TO', 'ES', 'PA'],
        'Late Percentage': [23.1, 19.2, 15.5, 14.8, 14.8, 13.7, 13.1, 12.6, 12.1, 12.1],
        'Total Orders': [411, 736, 490, 1323, 345, 3344, 12698, 278, 2018, 969]
    }
    
    df_states = pd.DataFrame(worst_states)
    
    st.subheader("📋 Top 10 Worst Performing States")
    st.dataframe(df_states, use_container_width=True)
    
    # Simple bar chart
    st.bar_chart(df_states.set_index('State')['Late Percentage'])
    
    st.markdown("""
    ### Key Insights:
    - **Northeastern states dominate** the worst performers list
    - **Alagoas (AL)** has 23.1% late delivery rate - nearly 1 in 4 orders!
    - **Geographic pattern** suggests infrastructure challenges in remote areas
    """)

elif page == "Customer Sentiment":
    st.header("⭐ Customer Sentiment Analysis")
    
    # Review score data
    sentiment_data = {
        'Delivery Status': ['On Time', 'Late', 'Super Late'],
        'Average Stars': [4.25, 3.60, 1.86],
        'Order Count': [90381, 3162, 4664]
    }
    
    df_sentiment = pd.DataFrame(sentiment_data)
    
    st.subheader("📊 Review Scores by Delivery Performance")
    st.dataframe(df_sentiment, use_container_width=True)
    st.line_chart(df_sentiment.set_index('Delivery Status')['Average Stars'])
    
    # Impact summary
    st.subheader("💡 Business Impact")
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
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
    
    st.markdown("""
    ### The Numbers Don't Lie:
    - **On-time deliveries:** 4.25 stars ⭐⭐⭐⭐
    - **Late deliveries:** 3.60 stars ⭐⭐⭐
    - **Super late deliveries:** 1.86 stars ⭐
    
    **This 2.39-star drop proves that delivery delays are destroying customer satisfaction!**
    """)

# Footer
st.markdown("---")
st.markdown("**Data Source:** Olist Brazilian E-Commerce Dataset | **Analysis:** Logistics Auditor Dashboard")
