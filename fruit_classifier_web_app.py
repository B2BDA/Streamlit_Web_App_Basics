from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image, ImageOps
import streamlit as st
model = keras.models.load_model(r"/mnt/d/B2B_Git_Instance/CNN_Keras/fruit_classifier.h5")
st.title("Fruit Classification")
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
class_dict = {'0': 'Apple Braeburn',
 '1': 'Apple Golden 1',
 '2': 'Apple Golden 2',
 '3': 'Apple Golden 3',
 '4': 'Apple Granny Smith',
 '5': 'Apple Red 1',
 '6': 'Apple Red 2',
 '7': 'Apple Red 3',
 '8': 'Apple Red Delicious',
 '9': 'Apple Red Yellow',
 '10': 'Apricot',
 '11': 'Avocado',
 '12': 'Avocado ripe',
 '13': 'Banana',
 '14': 'Banana Red',
 '15': 'Cactus fruit',
 '16': 'Cantaloupe 1',
 '17': 'Cantaloupe 2',
 '18': 'Carambula',
 '19': 'Cherry 1',
 '20': 'Cherry 2',
 '21': 'Cherry Rainier',
 '22': 'Cherry Wax Black',
 '23': 'Cherry Wax Red',
 '24': 'Cherry Wax Yellow',
 '25': 'Clementine',
 '26': 'Cocos',
 '27': 'Dates',
 '28': 'Granadilla',
 '29': 'Grape Pink',
 '30': 'Grape White',
 '31': 'Grape White 2',
 '32': 'Grapefruit Pink',
 '33': 'Grapefruit White',
 '34': 'Guava',
 '35': 'Huckleberry',
 '36': 'Kaki',
 '37': 'Kiwi',
 '38': 'Kumquats',
 '39': 'Lemon',
 '40': 'Lemon Meyer',
 '41': 'Limes',
 '42': 'Lychee',
 '43': 'Mandarine',
 '44': 'Mango',
 '45': 'Maracuja',
 '46': 'Melon Piel de Sapo',
 '47': 'Mulberry',
 '48': 'Nectarine',
 '49': 'Orange',
 '50': 'Papaya',
 '51': 'Passion Fruit',
 '52': 'Peach',
 '53': 'Peach Flat',
 '54': 'Pear',
 '55': 'Pear Abate',
 '56': 'Pear Monster',
 '57': 'Pear Williams',
 '58': 'Pepino',
 '59': 'Physalis',
 '60': 'Physalis with Husk',
 '61': 'Pineapple',
 '62': 'Pineapple Mini',
 '63': 'Pitahaya Red',
 '64': 'Plum',
 '65': 'Pomegranate',
 '66': 'Quince',
 '67': 'Rambutan',
 '68': 'Raspberry',
 '69': 'Salak',
 '70': 'Strawberry',
 '71': 'Strawberry Wedge',
 '72': 'Tamarillo',
 '73': 'Tangelo',
 '74': 'Tomato 1',
 '75': 'Tomato 2',
 '76': 'Tomato 3',
 '77': 'Tomato 4',
 '78': 'Tomato Cherry Red',
 '79': 'Tomato Maroon',
 '80': 'Walnut'}
 
print(uploaded_file)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # this image goes into the predict function of the model
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
 
    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 32, 21, 3), dtype=np.float32)
    #image sizing
    size = (32, 32)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    img = np.expand_dims(image_array, axis = 0)

    
    if st.button("Predict"):
        predict = np.argmax(model.predict(img), axis = -1)
        predict = class_dict.get(str(np.argmax(model.predict(img), axis = -1)[0]))
        st.write("Predicted Class is: %s"%str(predict))
        # make a predicted_class variable and append in the above statement