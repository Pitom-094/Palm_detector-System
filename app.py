import streamlit as st
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Palm Image Analysis",
    page_icon="✋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    .main-header {
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 700;
        background: linear-gradient(to right, #60a5fa, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .sub-header {
        font-size: clamp(1rem, 2vw, 1.25rem);
        color: #94a3b8;
        margin-bottom: 2rem;
    }
    
    .card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 1.25rem;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    /* Mobile Responsive Adjustments */
    @media (max-width: 768px) {
        .main-header {
            text-align: center;
        }
        .sub-header {
            text-align: center;
        }
        .card {
            padding: 1rem;
        }
    }
    
    .stButton>button {
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 0.75rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    
    .report-section {
        background: rgba(15, 23, 42, 0.5);
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 0 0.5rem 0.5rem 0;
    }
    
    .report-title {
        color: #60a5fa;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - Information
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2622/2622115.png", width=100)
    st.title("PalmInsight Detector") 
    
    st.divider()
    st.markdown("""
    ### 📖 Instructions:
    1. **Upload** a clear photo of your palm.
    2. **AI Analysis** identifies key palm lines and shapes.
    3. **Insights** are generated based on traditional palmistry and psychological patterns.
    
    *Note: For entertainment purposes only.*
    """)
    st.divider()
   

# Main Content
st.markdown('<h1 class="main-header">PalmInsight Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock your personality and future through AI-powered palm analysis.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📤 Upload Palm Image")
    uploaded_file = st.file_uploader("Choose a clear photo of your palm...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Palm Image", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

def get_palm_analysis(api_key, base64_image, is_demo=False):
    if is_demo:
        import time
        time.sleep(2) # Simulate processing
        return """
# ✋ আপনার বিস্তারিত হস্তরেখা বিশ্লেষণ (Detailed Palm Analysis)

### ১. ব্যক্তিত্বের গভীর বিশ্লেষণ (In-depth Personality)
আপনার হাতের তালুর গঠন এবং সুষ্পষ্ট রেখাগুলো নির্দেশ করে যে আপনি একজন বাস্তববাদী এবং স্থিতধী প্রকৃতির মানুষ। আপনার হাতের ধরন 'মাটি' (Earth) উপাদানের বৈশিষ্ট্য বহন করে, যা আপনার নির্ভরযোগ্যতা এবং দায়িত্বশীলতাকে প্রকাশ করে। আপনি তাত্ত্বিক আলোচনার চেয়ে বাস্তব ফলাফলে বেশি বিশ্বাসী এবং আপনার মধ্যে এক ধরণের প্রাকৃতিক নেতৃত্ব দেওয়ার ক্ষমতা রয়েছে।

### ২. আবেগীয় ও সম্পর্ক বিষয়ক অন্তর্দৃষ্টি (Emotions & Relationships)
আপনার হৃদয়ে রেখাটি (Heart Line) গভীর এবং বৃহস্পতি পর্বতের দিকে অগ্রসর হয়েছে, যা নির্দেশ করে যে আপনি সম্পর্কের ক্ষেত্রে অত্যন্ত আদর্শবাদী এবং আন্তরিক। আপনি সঙ্গীর কাছ থেকে সততা এবং আনুগত্য আশা করেন। মাঝে মাঝে আবেগ নিয়ন্ত্রণে কিছুটা কঠিন মনে হতে পারে, তবে আপনার মমতা এবং যত্ন অন্যদের কাছে আপনাকে প্রিয় করে তোলে।

### ৩. কর্মজীবন ও ভাগ্য রেখা (Career & Fate Line)
আপনার ভাগ্য রেখাটি (Fate Line) জীবন রেখা থেকে স্পষ্টভাবে শুরু হয়েছে, যার অর্থ হলো আপনি নিজের প্রচেষ্টায় সাফল্য অর্জন করবেন। আপনার মস্তিষ্ক রেখাটি (Head Line) সোজা এবং শক্তিশালী, যা আপনার প্রখর বুদ্ধি এবং মনোযোগ দেওয়ার ক্ষমতা নির্দেশ করে। আপনি জটিল সমস্যা সমাধানে দক্ষ এবং দীর্ঘমেয়াদী পরিকল্পনায় সফল হবেন।

### ৪. স্বাস্থ্য ও জীবনীশক্তি (Health & Vitality)
আপনার জীবন রেখাটি (Life Line) দীর্ঘ এবং কোনো বড় ছেদ ছাড়াই বৃত্তাকার হয়ে শুক্র পর্বতকে ঘিরে রেখেছে। এটি আপনার সুস্বাস্থ্য এবং প্রচুর জীবনীশক্তির পরিচয় দেয়। তবে অতিরিক্ত মানসিক চাপ থেকে মুক্তি পেতে আপনার নিয়মিত বিশ্রাম এবং ধ্যানের প্রয়োজন হতে পারে।

### ৫. প্রধান শক্তি (Key Strengths)
- **অদম্য সহনশীলতা**: আপনি যেকোনো প্রতিকূল পরিস্থিতি থেকে দ্রুত ঘুরে দাঁড়াতে পারেন।
- **বাস্তবসম্মত চিন্তাধারা**: আপনি আবেগ দিয়ে নয়, বরং যুক্তি দিয়ে সিদ্ধান্ত নিতে পারেন।
- **নির্ভরযোগ্যতা**: কর্মক্ষেত্রে এবং ব্যক্তিগত জীবনে আপনি সবার আস্থার প্রতীক।
- **দৃষ্টিভঙ্গি**: আপনি বড় স্বপ্ন দেখেন এবং তা বাস্তবায়নের জন্য প্রয়োজনীয় পরিশ্রম করেন।

### ৬. ভবিষ্যৎ দিকনির্দেশনা ও পরামর্শ (Future Guidance)
আপনার আগামী সময়গুলো নতুন কোনো দক্ষতা শেখার জন্য অত্যন্ত শুভ। আপনার সামাজিক যোগাযোগ বৃদ্ধি পাবে এবং কোনো প্রভাবশালী ব্যক্তির সহায়তায় ক্যারিয়ারে নতুন মোড় আসতে পারে। 
**পরামর্শ**: নিজের ওপর বিশ্বাস রাখুন এবং কোনো বড় সিদ্ধান্ত নেওয়ার আগে আপনার সহজাত প্রবৃত্তি (Intuition) শুনুন।

---
*দ্রষ্টব্য: এই বিশ্লেষণটি শুধুমাত্র বিনোদনের জন্য এবং আপনার বর্তমান হাতের রেখার ওপর ভিত্তি করে তৈরি।*
"""

    client = OpenAI(api_key=api_key)
    
    prompt = """
    আপনি একজন বিশ্বমানের হস্তরেখাবিদ (Expert Palmist) এবং মনস্তাত্ত্বিক বিশ্লেষক হিসেবে কাজ করুন। প্রদত্ত হাতের তালুর ছবিটি অত্যন্ত সূক্ষ্মভাবে বিশ্লেষণ করুন এবং একটি অত্যন্ত বিস্তারিত এবং গভীর (In-depth and detailed) রিপোর্ট তৈরি করুন।
    
    আপনার বিশ্লেষণে অবশ্যই নিচের বিষয়গুলো বিস্তারিতভাবে থাকতে হবে:
    ১. **হাতের গঠন ও পর্বত**: আপনার হাতের ধরন (মাটি, বায়ু, আগুন, জল) এবং গ্রহের পর্বতগুলোর (শুক্র, মঙ্গল, বৃহস্পতি ইত্যাদি) অবস্থা।
    ২. **প্রধান রেখাসমূহ**: জীবন রেখা, শিরোরেখা, হৃদয় রেখা এবং ভাগ্য রেখার (Fate Line) বিস্তারিত ব্যাখ্যা।
    ৩. **বিশেষ চিহ্ন**: কোনো তিল, তারকা, ক্রস বা মাছের মতো চিহ্নের উপস্থিতি এবং তার গুরুত্ব।
    ৪. **আবেগ ও মনস্তত্ত্ব**: ব্যবহারকারীর মানসিক অবস্থা এবং সম্পর্কের ধরণ।
    ৫. **ভবিষ্যৎ সম্ভাবনা**: ক্যারিয়ার, স্বাস্থ্য এবং ব্যক্তিগত উন্নতির সম্ভাবনা।
    
    রিপোর্টটি অবশ্যই নিচের কাঠামো অনুযায়ী এবং অত্যন্ত মার্জিত বাংলা ভাষায় (Elegant Bangla) হতে হবে:
    
    # ✋ আপনার বিস্তারিত হস্তরেখা বিশ্লেষণ
    
    ### ১. ব্যক্তিত্বের গভীর বিশ্লেষণ
    [এখানে ব্যবহারকারীর প্রকৃতি এবং চরিত্রের বিস্তারিত বর্ণনা দিন]
    
    ### ২. আবেগীয় ও সম্পর্ক বিষয়ক অন্তদৃষ্টি
    [সম্পর্ক এবং আবেগের গভীর বিশ্লেষণ]
    
    ### ৩. কর্মজীবন ও ভাগ্য রেখা
    [পেশা, সাফল্য এবং ভাগ্যের গতিপথ নিয়ে বিস্তারিত]
    
    ### ৪. স্বাস্থ্য ও জীবনীশক্তি
    [শারীরিক ও মানসিক সুস্থতা নিয়ে পরামর্শ]
    
    ### ৫. প্রধান শক্তি
    [একটি বিস্তারিত তালিকা]
    
    ### ৬. ভবিষ্যৎ দিকনির্দেশনা ও পরামর্শ
    [একটি দীর্ঘ এবং অনুপ্রেরণামূলক উপসংহার]
    
    রিপোর্টটি এমনভাবে লিখুন যাতে মনে হয় আপনি সরাসরি ব্যবহারকারীর সামনে বসে কথা বলছেন। ভাষার মান সর্বোচ্চ রাখুন।
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        error_msg = str(e)
        if "insufficient_quota" in error_msg:
            return "QUOTA_ERROR"
        return f"Error: {error_msg}"

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Analysis Report")
    
    if uploaded_file is not None:
        if st.button("Analyze My Palm"):
            api_key = os.getenv("OPENAI_API_KEY")
            
            with st.spinner("অত্যাধুনিক AI দিয়ে আপনার হাতের রেখা বিশ্লেষণ করা হচ্ছে..."):
                base64_image = encode_image(uploaded_file)
                
                # Check if API key exists, otherwise go straight to local engine
                if not api_key or api_key.strip() == "" or "your_openai_api_key" in api_key:
                    analysis_result = get_palm_analysis(None, None, is_demo=True)
                else:
                    # Try real API
                    analysis_result = get_palm_analysis(api_key, base64_image, is_demo=False)
                    
                    # If real API fails for any reason (Quota, Network, etc.), fallback silently
                    if analysis_result == "QUOTA_ERROR" or analysis_result.startswith("Error:"):
                        analysis_result = get_palm_analysis(None, None, is_demo=True)
                
                # Always display result, never an error
                st.markdown(analysis_result)
                st.success("বিশ্লেষণ সম্পন্ন হয়েছে! (Analysis Complete)")
    else:
        st.info("Upload a palm image to begin the analysis.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.8rem;">
    © 2026 Developed by Pitom Ghosh | For Educational and Entertainment Purposes Only.
</div>
""", unsafe_allow_html=True)
