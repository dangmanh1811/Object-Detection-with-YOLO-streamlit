import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def add_background(background_path):
    # Add background
    img_file = background_path
    img_base64 = get_base64(img_file)
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    }}
    </style>
    '''
    return page_bg_img
    