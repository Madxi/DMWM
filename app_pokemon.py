
import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "finalized_model.sav"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model


def main():

	st.set_page_config(page_title="Aplikacja do predykcji przeżycia ofiary pokemona")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://img.gaming.gentside.com/s3/frgsg/1280/pokemon/default_2020-02-26_0f506adc-13c9-4895-8046-1a0eebf5538b.jpeg")

	with overview:
		st.title("Aplikacja do predykcji przeżycia ofiary pokemona")

	with left:
		st.subheader("Czy taka osoba przeżyłaby katastrofę?")

	with right:
		znaczek_slider = st.slider("Podaj wartosc szczescia pokemona", value=1, min_value=1, max_value=100, step=1)
		total_slider = st.slider("Podaj wartosc totala pokemona", min_value=0, max_value=10, step=1)
		HP_slider = st.slider("Podaj wartosc zycia", min_value=0, max_value=10, step=1)
		Attack_slider = st.slider("Podaj wartosc ataku", min_value=0, max_value=500, step=1)
		defense_slider = st.slider("Podaj wartosc obrony", value=1, min_value=1, max_value=100, step=1)
		spattack_slider = st.slider("Podaj wartosc specjalnego ataku", min_value=0, max_value=10, step=1)
		spdef_slider = st.slider("podaj wartosc specjalnej obrony", min_value=0, max_value=10, step=1)
		speed_slider = st.slider("Podaj wartosc szybkosci", min_value=0, max_value=500, step=1)
		generation_slider = st.slider("Podaj numer generacji", min_value=0, max_value=6, step=1)
		legendary_slider = st.slider("CZY JEST LEGENDARNY?", min_value=0, max_value=1, step=1)


	data = [[znaczek_slider, total_slider, HP_slider, Attack_slider, defense_slider, spattack_slider, spdef_slider, speed_slider, generation_slider, legendary_slider]]
	survival = model.predict(data)
	#s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy taka osoba przeżyłaby katastrofę?")
		st.subheader(("Tak" if survival[0] < 79 else "Nie"))
		#st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
