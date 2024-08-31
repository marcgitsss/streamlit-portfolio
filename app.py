from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Marc Gomolon | Porfolio"
PAGE_ICON = ":wave:"
NAME = "Marc Gomolon"
DESCRIPTION = """
Hi, I'm Marc Francis B. Gomolon, a 23-year-old from Pusok, Lapu-Lapu City, Cebu. I was born on September 12, 2000, and I have a passion for cryptocurrency trading and riding motorbikes. I love exploring new places, and recently, I've traveled to beautiful spots like Bantayan Island, Boracay, and Moalboal.
"""
EMAIL = "marcfrancis.gomolon@cit.edu"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/mgomsss",
    "GitHub": "https://github.com/marcgitsss",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello There!")

# LOAD CSS, PICTURES
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=320)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.markdown("""
      <div class="social-links">
        <a href="https://github.com/marcgitsss">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="25" height="25" viewBox="0,0,300,150"
          style="fill:#FFFFFF; margin-bottom: 10px;">
          <g fill="#ffffff" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(4,4)"><path d="M32,6c-14.359,0 -26,11.641 -26,26c0,12.277 8.512,22.56 19.955,25.286c-0.592,-0.141 -1.179,-0.299 -1.755,-0.479v-5.957c0,0 -0.975,0.325 -2.275,0.325c-3.637,0 -5.148,-3.245 -5.525,-4.875c-0.229,-0.993 -0.827,-1.934 -1.469,-2.509c-0.767,-0.684 -1.126,-0.686 -1.131,-0.92c-0.01,-0.491 0.658,-0.471 0.975,-0.471c1.625,0 2.857,1.729 3.429,2.623c1.417,2.207 2.938,2.577 3.721,2.577c0.975,0 1.817,-0.146 2.397,-0.426c0.268,-1.888 1.108,-3.57 2.478,-4.774c-6.097,-1.219 -10.4,-4.716 -10.4,-10.4c0,-2.928 1.175,-5.619 3.133,-7.792c-0.2,-0.567 -0.533,-1.714 -0.533,-3.583c0,-1.235 0.086,-2.751 0.65,-4.225c0,0 3.708,0.026 7.205,3.338c1.614,-0.47 3.341,-0.738 5.145,-0.738c1.804,0 3.531,0.268 5.145,0.738c3.497,-3.312 7.205,-3.338 7.205,-3.338c0.567,1.474 0.65,2.99 0.65,4.225c0,2.015 -0.268,3.19 -0.432,3.697c1.898,2.153 3.032,4.802 3.032,7.678c0,5.684 -4.303,9.181 -10.4,10.4c1.628,1.43 2.6,3.513 2.6,5.85v8.557c-0.576,0.181 -1.162,0.338 -1.755,0.479c11.443,-2.726 19.955,-13.009 19.955,-25.286c0,-14.359 -11.641,-26 -26,-26zM33.813,57.93c-0.599,0.042 -1.203,0.07 -1.813,0.07c0.61,0 1.213,-0.029 1.813,-0.07zM37.786,57.346c-1.164,0.265 -2.357,0.451 -3.575,0.554c1.218,-0.103 2.411,-0.29 3.575,-0.554zM32,58c-0.61,0 -1.214,-0.028 -1.813,-0.07c0.6,0.041 1.203,0.07 1.813,0.07zM29.788,57.9c-1.217,-0.103 -2.411,-0.289 -3.574,-0.554c1.164,0.264 2.357,0.451 3.574,0.554z"></path></g></g>
        </svg>
        <span>
          marcgitsss
        </span>
        </a>
      </div>
    """, unsafe_allow_html=True)
    st.markdown("""
      <div class="social-links" style="margin-top: 5px;">
        <a href="https://www.facebook.com/mgomsss">
          <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="23" height="23" viewBox="0 0 48 48"
            style="margin-bottom: 5px;"
          >
            <linearGradient id="Ld6sqrtcxMyckEl6xeDdMa_uLWV5A9vXIPu_gr1" x1="9.993" x2="40.615" y1="9.993" y2="40.615" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2aa4f4"></stop><stop offset="1" stop-color="#007ad9"></stop></linearGradient><path fill="url(#Ld6sqrtcxMyckEl6xeDdMa_uLWV5A9vXIPu_gr1)" d="M24,4C12.954,4,4,12.954,4,24s8.954,20,20,20s20-8.954,20-20S35.046,4,24,4z"></path><path fill="#fff" d="M26.707,29.301h5.176l0.813-5.258h-5.989v-2.874c0-2.184,0.714-4.121,2.757-4.121h3.283V12.46 c-0.577-0.078-1.797-0.248-4.102-0.248c-4.814,0-7.636,2.542-7.636,8.334v3.498H16.06v5.258h4.948v14.452 C21.988,43.9,22.981,44,24,44c0.921,0,1.82-0.084,2.707-0.204V29.301z"></path>
          </svg>
        <span>
          Marc Gomolon
        </span>
        </a>
      </div>
    """, unsafe_allow_html=True)


st.write('\n')

tab1, tab2, tab3, tab4 = st.tabs(["About Me", "My Passion", "My Preferences", "Cool Places"])
    
with tab1:
  st.markdown(
    """
    <div class="container">
      <h2 class="section-heading">Personal Information</h2>
      <div class="personal-info">
        <p><strong>Name:</strong> Marc Francis B. Gomolon</p>
        <p><strong>Birthday:</strong> September 12, 2000</p>
        <p><strong>Address:</strong> Pusok, Lapu-Lapu City, Cebu</p>
      </div>
    </div>
    """,
  unsafe_allow_html=True
  )

with tab2:
  st.markdown(
    """
    <h2 class="section-heading">My Hobbies</h2>
    <h3>Riding Motorbike</h3>
    """,
    unsafe_allow_html=True
  )
  st.image('./assets/image.png', width=320)
  st.markdown(
    """
    <p style="margin-top: 20px;">Riding a motorbike is one of my greatest passions. It provides me with a sense of freedom and adventure. The wind in my face and the open road help me unwind and clear my mind, making it a perfect way to relax and de-stress after a long day. The thrill and excitement of riding are unmatched, and it truly rejuvenates my spirit.</p>
    """,
    unsafe_allow_html=True
  )
  



with tab3:
  st.markdown(
  """
   <div class="container">
        <h2 class="section-heading">Likes</h2>
        <ul class="list">
            <li class="list-item">Making Money</li>
            <li class="list-item">Beach</li>
            <li class="list-item">Buko Juice</li>
            <li class="list-item">Calm Waves</li>
        </ul>
        <h2 class="section-heading">Dislikes</h2>
        <ul class="list">
            <li class="list-item">Not Having Money</li>
            <li class="list-item">Matcha Tea</li>
            <li class="list-item">Being a Procrastinator</li>
        </ul>
    </div>
  """,
  unsafe_allow_html=True
)

with tab4:
  st.markdown(
    """
    <h2 class="section-heading">Places I've Been To</h2>
    """,
    unsafe_allow_html=True
  )
  # Define the latitude and longitude for the locations
  locations = {
      'Bantayan Island': {'latitude': 11.1999, 'longitude': 123.7406},
      'Boracay': {'latitude': 11.9674, 'longitude': 121.9248},
      'Moalboal': {'latitude': 9.9557, 'longitude': 123.4008}
  }

  # Create a DataFrame with the locations
  data = pd.DataFrame(locations).T.reset_index()
  data.columns = ['Place', 'latitude', 'longitude']


  # Display the map with the USC Talamban location
  st.map(data)

  st.markdown(
  """
   <div class="container">
        <ul class="list">
            <li class="list-item">Bantayan Island</li>
            <li class="list-item">Boracay</li>
            <li class="list-item">Moalboal</li>
        </ul>
    </div>
  """,
  unsafe_allow_html=True
  )