import streamlit as st
import pandas as pd
from PIL import Image
import warnings
warnings.filterwarnings("ignore")
from pickle import load
import numpy as np



st.markdown("# :mushroom: Classifier : :fork_and_knife: or :skull:?") 
image = Image.open("mushrooms.jpg")
st.image(image, caption="Mushrooms", use_column_width="auto")

mappings = load(open("mushroom_encoder.pkl", "rb"))


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-right:30px;}</style>', unsafe_allow_html=True)



st.header("cap-shape: ")
if "cap-shape" not in st.session_state:
    st.session_state["cap-shape"] = ""
encoder_cap_shape = {v: int(k) for k,v in mappings[1].items()}
dico_cap_shape = {"bell": "b", "conical": "c", "convex": "x", "flat": "f", "knobbed": "k", "sunken": "s"}
st.session_state["cap-shape"] = encoder_cap_shape[dico_cap_shape[st.radio("",("bell", "conical", "convex", "flat", "knobbed", "sunken"))]]

st.header("cap-surface: ")
if "cap-surface" not in st.session_state:
    st.session_state["cap-surface"] = ""
encoder_cap_surface = {v: int(k) for k,v in mappings[2].items()}
dico_cap_surface = {"fibrous": "f","grooves":"g","scaly":"y","smooth":"s"}
st.session_state["cap-surface"] = encoder_cap_surface[dico_cap_surface[st.radio("",("fibrous","grooves","scaly", "smooth"))]]

st.header("cap-color: ")
if "cap-surface" not in st.session_state:
    st.session_state["cap-color"] = ""
encoder_cap_color = {v: int(k) for k,v in mappings[3].items()}
dico_cap_color = {"brown":"n","buff":"b","cinnamon":"c","gray":"g","green":"r","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"}
st.session_state["cap-color"] = encoder_cap_color[dico_cap_color[st.radio("",("brown", "buff", "cinnamon", "gray", "green", "pink", "purple", "red", "white", "yellow"))]]

st.header("bruises?: ")
if "bruises?" not in st.session_state:
    st.session_state["bruises?"] = ""
encoder_bruises = {v: int(k) for k,v in mappings[4].items()}
dico_bruises = {"yes":"t","no":"f"}
st.session_state["bruises?"] = encoder_bruises[dico_bruises[st.radio("",("yes", "no"))]]

st.header("odor: ")
if "odor" not in st.session_state:
    st.session_state["odor"] = ""
encoder_odor = {v: int(k) for k,v in mappings[5].items()}
dico_odor = {"almond":"a","anise":"l","creosote":"c","fishy":"y","foul":"f","musty":"m","none":"n","pungent":"p","spicy":"s"}
st.session_state["odor"] = encoder_odor[dico_odor[st.radio("",("almond", "anise", "creosote", "fishy", "foul", "musty", "none", "pungent", "spicy"))]]

st.header("gill-attachment: ")
if "gill-attachment" not in st.session_state:
    st.session_state["gill-attachment"] = ""
encoder_gill_attachment = {v: int(k) for k,v in mappings[6].items()}
dico_gill_attachment = {"attached":"a","free":"f"}
st.session_state["gill-attachment"] = encoder_gill_attachment[dico_gill_attachment[st.radio("",("attached", "free"))]]


st.header("gill-spacing: ")
if "gill-spacing" not in st.session_state:
    st.session_state["gill-spacing"] = ""
encoder_gill_spacing = {v: int(k) for k,v in mappings[7].items()}
dico_gill_spacing = {"close": "c", "crowded": "w"}
st.session_state["gill-spacing"] = encoder_gill_spacing[dico_gill_spacing[st.radio("",("close", "crowded"))]]


st.header("gill-size: ")
if "gill-size" not in st.session_state:
    st.session_state["gill-size"] = ""
encoder_gill_size = {v: int(k) for k,v in mappings[8].items()}
dico_gill_size = {"broad":"b","narrow":"n"}
st.session_state["gill-size"] = encoder_gill_size[dico_gill_size[st.radio("",("broad", "narrow"))]]

st.header("gill-color: ")
if "gill-color" not in st.session_state:
    st.session_state["gill-color"] = ""
encoder_gill_color = {v: int(k) for k,v in mappings[9].items()}
dico_gill_color = {"black":"k","brown":"n","buff":"b","chocolate":"h","gray":"g","green":"r","orange":"o","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"}
st.session_state["gill-color"] = encoder_gill_color[dico_gill_color[st.radio("",("black", "brown", "buff", "chocolate", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"))]]

st.header("stalk-shape: ")
if "stalk-shape" not in st.session_state:
    st.session_state["stalk-shape"] = ""
encoder_stalk_shape = {v: int(k) for k,v in mappings[10].items()}
dico_stalk_shape = {"enlarging": "e", "tapering": "t"}
st.session_state["stalk-shape"] = encoder_stalk_shape[dico_stalk_shape[st.radio("",("enlarging", "tapering"))]]

st.header("stalk-root: ")
if "stalk-root" not in st.session_state:
    st.session_state["stalk-root"] = ""
encoder_stalk_root = {v: int(k) for k,v in mappings[11].items()}
dico_stalk_root = {"bulbous":"b","club":"c","equal":"e","rooted":"r","missing":"?"}
st.session_state["stalk-root"] = encoder_stalk_root[dico_stalk_root[st.radio("",("bulbous", "club", "equal", "rooted", "missing"))]]

st.header("stalk-surface-above-ring: ")
if "stalk-surface-above-ring" not in st.session_state:
    st.session_state["stalk-surface-above-ring"] = ""
encoder_stalk_surface_above_ring = {v: int(k) for k,v in mappings[12].items()}
dico_stalk_surface_above_ring = {"fibrous":"f","scaly":"y","silky":"k","smooth":"s"}
st.session_state["stalk-surface-above-ring"] = encoder_stalk_surface_above_ring[dico_stalk_surface_above_ring[st.radio("",("fibrous", "scaly", "silky", "smooth"))]]

st.header("stalk-surface-below-ring: ")
if "stalk-surface-below-ring" not in st.session_state:
    st.session_state["stalk-surface-below-ring"] = ""
encoder_stalk_surface_below_ring = {v: int(k) for k,v in mappings[13].items()}
st.session_state["stalk-surface-below-ring"] = encoder_stalk_surface_below_ring[dico_stalk_surface_above_ring[st.radio(" ",("fibrous", "scaly", "silky", "smooth"))]]

st.header("stalk-color-above-ring: ")
if "stalk-color-above-ring" not in st.session_state:
    st.session_state["stalk-color-above-ring"] = ""
encoder_stalk_color_above_ring = {v: int(k) for k,v in mappings[14].items()}
dico_stalk_color_above_ring = {"brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"}
st.session_state["stalk-color-above-ring"] = encoder_stalk_color_above_ring[dico_stalk_color_above_ring[st.radio("",("brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"))]]

st.header("stalk-color-below-ring: ")
if "stalk-color-below-ring" not in st.session_state:
    st.session_state["stalk-color-below-ring"] = ""
encoder_stalk_color_below_ring = {v: int(k) for k,v in mappings[15].items()}
st.session_state["stalk-color-below-ring"] = encoder_stalk_color_below_ring[dico_stalk_color_above_ring[st.radio(" ",("brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"))]]

st.header("veil-type: ")
if "veil-type" not in st.session_state:
    st.session_state["veil-type"] = ""
encoder_veil_type = {v: int(k) for k,v in mappings[16].items()}
dico_veil_type = {"partial":"p","universal":"u"}
st.session_state["veil-type"] = encoder_veil_type[dico_veil_type[st.radio("",("partial", "universal"))]]

st.header("veil-color: ")
if "veil-color" not in st.session_state:
    st.session_state["veil-color"] = ""
encoder_veil_color = {v: int(k) for k,v in mappings[17].items()}
dico_veil_color = {"brown":"n","orange":"o","white":"w","yellow":"y"}
st.session_state["veil-color"] = encoder_veil_color[dico_veil_color[st.radio("",("brown", "orange", "white", "yellow"))]]

st.header("ring-number: ")
if "ring-number" not in st.session_state:
    st.session_state["ring-number"] = ""
encoder_ring_number = {v: int(k) for k,v in mappings[18].items()}
dico_ring_number = {"none":"n","one":"o","two":"t"}
st.session_state["ring-number"] = encoder_ring_number[dico_ring_number[st.radio("",("none", "one", "two"))]]

st.header("ring-type: ")
if "ring-type" not in st.session_state:
    st.session_state["ring-type"] = ""
encoder_ring_type = {v: int(k) for k,v in mappings[19].items()}
dico_ring_type = {"evanescent":"e","flaring":"f","large":"l","none":"n","pendant":"p"}
st.session_state["ring-type"] = encoder_ring_type[dico_ring_type[st.radio("",("evanescent", "flaring", "large", "none", "pendant"))]]

st.header("spore-print-color: ")
if "spore-print-color" not in st.session_state:
    st.session_state["spore-print-color"] = ""
encoder_spore_print_color = {v: int(k) for k,v in mappings[20].items()}
dico_spore_print_color = {"black":"k","brown":"n","buff":"b","chocolate":"h","green":"r","orange":"o","purple":"u","white":"w","yellow":"y"}
st.session_state["spore-print-color"] = encoder_spore_print_color[dico_spore_print_color[st.radio("",("black", "brown", "buff", "chocolate", "green", "orange", "purple", "white", "yellow"))]]

st.header("population: ")
if "population" not in st.session_state:
    st.session_state["population"] = ""
encoder_population = {v: int(k) for k,v in mappings[21].items()}
dico_population = { "abundant":"a","clustered":"c","numerous":"n","scattered":"s","several":"v","solitary":"y"}
st.session_state["population"] = encoder_population[dico_population[st.radio("",("abundant", "clustered", "numerous", "scattered", "several", "solitary"))]]

st.header("habitat: ")
if "habitat" not in st.session_state:
    st.session_state["habitat"] = ""
encoder_habitat = {v: int(k) for k,v in mappings[22].items()}
dico_habitat = {"grasses":"g","leaves":"l","meadows":"m","paths":"p","urban":"u","waste":"w","woods":"d"}
st.session_state["habitat"] = encoder_habitat[dico_habitat[st.radio("",("grasses", "leaves", "meadows", "paths", "urban", "waste", "woods"))]]

image2 = Image.open("dish.jpg")
st.image(image2, caption="Bon appétit!", use_column_width="auto")

model = load(open("mushroom_pipeline.pkl", "rb"))

X_test = [
    st.session_state["cap-shape"],
    st.session_state["cap-surface"],
    st.session_state["cap-color"],
    st.session_state["bruises?"],
    st.session_state["odor"],
    st.session_state["gill-attachment"],
    st.session_state["gill-spacing"],
    st.session_state["gill-size"],
    st.session_state["gill-color"],
    st.session_state["stalk-shape"],
    st.session_state["stalk-root"],
    st.session_state["stalk-surface-above-ring"],
    st.session_state["stalk-surface-below-ring"],
    st.session_state["stalk-color-above-ring"],
    st.session_state["stalk-color-below-ring"],
    st.session_state["veil-type"],
    st.session_state["veil-color"],
    st.session_state["ring-number"],
    st.session_state["ring-type"],
    st.session_state["spore-print-color"],
    st.session_state["population"],
    st.session_state["habitat"]
]


if st.button("Make prediction!"):
    prediction = model.predict([np.asarray(X_test)])

    if prediction == 0:
        st.markdown("### :fork_and_knife: The mushroom is edible!")
    else:
        st.markdown("### :skull: The mushroom is poisonous be careful!")
else:
    pass


if st.button("Reset"):
    pass
