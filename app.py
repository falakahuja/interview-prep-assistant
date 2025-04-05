import streamlit as st
from scraper.leetcode import LeetcodeScraper
from scraper.youtube import YouTubeScraper
from streamlit_theme import st_theme

# Page Config
st.set_page_config(
    page_title="Interview Prep Assistant",
    page_icon="💼",
    layout="wide"
)

# Custom CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- TAB FUNCTIONS (must be defined BEFORE main()) ----------


def display_leetcode_problems():
    st.header("Coding Problems")
    
    # Search controls
    col1, col2 = st.columns([3, 1])
    with col1:
        topic_search = st.text_input("Search problems by topic/keyword", 
                                   placeholder="e.g. binary search, array")
    with col2:
        difficulty = st.selectbox("Difficulty", ["All", "Easy", "Medium", "Hard"])
    
    if st.button("Search Problems") or topic_search:
        if not topic_search:
            st.warning("Try searching: arrays, DP, trees, etc.")
            return
            
        with st.spinner(f"Finding {difficulty.lower()} problems..."):
            scraper = LeetcodeScraper()
            problems = scraper.scrape_by_topic(topic_search.lower())
            
            if not problems:
                st.error("No problems found. Try different keywords")
                return
                
            filtered_problems = [
                p for p in problems 
                if difficulty == "All" or p['difficulty'].lower() == difficulty.lower()
            ]

            for problem in filtered_problems:
                with st.expander(f"{problem['title']} ({problem['difficulty']})"):
                    st.markdown(f"🔗 [View Problem]({problem['url']})")
                    
                    # Improved techniques display
                    techniques = []
                    if 'topicTags' in problem:
                        techniques.extend(tag['name'] for tag in problem['topicTags'])
                    
                    # Smart fallback if no tags
                    title_lower = problem['title'].lower()
                    if 'tree' in title_lower:
                        techniques.append('tree traversal')
                    if 'sort' in title_lower:
                        techniques.append('sorting')
                    if 'search' in title_lower:
                        techniques.append('search')
                        
                    if techniques:
                        st.markdown("**Techniques:** " + " • ".join(f"`{t}`" for t in techniques))
                    else:
                        st.markdown("**Focus:** Problem solving")


def display_youtube_videos():
    st.header("📺 Video Resources", divider="rainbow")
    
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            search_query = st.text_input("Search technical content", 
                                      placeholder="Try: 'Python interviews' or 'System design'")
        with col2:
            max_results = st.selectbox("Max results", [4, 8, 12], index=0)
    
    if search_query:
        with st.spinner(f"🔍 Finding best {search_query} videos..."):
            scraper = YouTubeScraper()
            # Enhanced search query
            query = (
                f"{search_query} "
                "(interview OR tutorial OR guide OR explanation OR walkthrough OR course) "
                "-music -song -cover -trailer -movie -lyrics -unboxing"
            )
            videos = scraper.search_videos(query)
            
            if not videos:
                st.warning("No focused videos found. Try different keywords")
                return
            
            # Professional card layout (unchanged)
            for video in videos[:max_results]:
                with st.container():
                    st.markdown(f"""
                    <div style='
                        border-radius: 8px;
                        padding: 16px;
                        margin-bottom: 16px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    '>
                        <div style='display: flex; gap: 16px;'>
                            <img src='{video['thumbnail']}' style='
                                width: 240px;
                                border-radius: 4px;
                                object-fit: cover;
                            '>
                            <div>
                                <h4 style='margin-top: 0;'>{video['title']}</h4>
                                <p style='color: #666; margin-bottom: 8px;'>
                                    <b>{video['channel']}</b> • {video['published_at'][:10]}
                                </p>
                                <a href='https://youtu.be/{video['video_id']}' target='_blank'>
                                    <button style='
                                        background: #FF4B4B;
                                        color: white;
                                        border: none;
                                        padding: 8px 16px;
                                        border-radius: 4px;
                                        cursor: pointer;
                                    '>Watch Video</button>
                                </a>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


def display_roadmaps():
    st.header("Study Roadmaps")
    roadmap_type = st.radio("Select Field", ["Frontend", "Backend", "DevOps"])
    
    # Check if file exists first
    file_path = f"assets/{roadmap_type.lower()}_roadmap.pdf"
    
    try:
        with open(file_path, "rb") as f:
            st.download_button(
                label="Download Roadmap",
                data=f,
                file_name=f"{roadmap_type}_roadmap.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning(f"Roadmap not available for {roadmap_type} yet")
        st.info("Sample roadmaps coming soon!")

def show_fallback_content():
    st.warning("Content unavailable. Showing cached data...")

# ---------- MAIN APP ----------
def main():
    st.title("📚 Interview Preparation Assistant")
    
    # Tab Layout
    tab1, tab2, tab3 = st.tabs(["Coding Problems", "Video Resources", "Roadmaps"])
    
    with tab1:
        display_leetcode_problems()
    
    with tab2:
        display_youtube_videos()
    
    with tab3:
        display_roadmaps()

if __name__ == "__main__":
    load_css()
    main()