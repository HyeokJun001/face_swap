import streamlit as st
import cv2
from PIL import Image
import numpy as np
from face_utils import swap_part

st.set_page_config(page_title="AI 얼굴 부위 교체기", page_icon="🧠")
st.title("😎 얼굴 부위 교체기")

part_map = {
    "눈": "eyes",
    "코": "nose",
    "입": "mouth"
}

base_file = st.file_uploader("1. 얼굴 이미지 업로드 (A)", type=["jpg", "jpeg", "png"])
celeb_file = st.file_uploader("2. 연예인 이미지 업로드", type=["jpg", "jpeg", "png"])
part_name_kor = st.selectbox("3. 바꿀 부위 선택", list(part_map.keys()))

if base_file and celeb_file:
    base_img = Image.open(base_file).convert("RGBA")
    celeb_img = Image.open(celeb_file).convert("RGBA")

    base_cv = cv2.cvtColor(np.array(base_img), cv2.COLOR_RGB2BGR)
    celeb_cv = cv2.cvtColor(np.array(celeb_img), cv2.COLOR_RGB2BGR)

    result = swap_part(base_cv, celeb_cv, part_map[part_name_kor])
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    st.image(result_rgb, caption="최종 결과", use_column_width=True)