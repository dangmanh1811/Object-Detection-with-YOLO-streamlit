from config.CONFIG import *
from utils.detects import *
from utils.background import add_background
from PIL import Image

if __name__ == '__main__':
    st.title(title)
    st.logo(logo_path)
    
    # Add background
    page_bg_img = add_background(background_path)
    st.markdown(page_bg_img, unsafe_allow_html=True)

    task = st.sidebar.selectbox("Select your Object Detection: ", (option1, option2, option3))

    if task == option1:
        st.header(option1)
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Detect Objects"):
                with st.spinner("Detecting..."):
                    annotated_image = detect_objects_on_image(image)
                    st.image(annotated_image, caption="Detected Image", use_column_width=True)

    elif task == option2:
        st.header(option2)
        uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

        if uploaded_video is not None:
            st.video(uploaded_video)
            if st.button("Detect Objects in Video"):
                detect_objects_on_video(uploaded_video)

    elif task == option3:
        st.header(option3)
        if st.button("Start Real-Time Detection"):
            detect_objects_real_time()
