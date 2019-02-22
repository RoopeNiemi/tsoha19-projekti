# Asennusohje

1. Lataa repositorio omalle koneellesi ja mene komentorivillä repositorion juureen.
2. Asenna python virtual env jos sitä ei ole jo koneellasi (python3 -m venv venv repositorion juuressa)
3. Käynnistä venv (source venv/bin/activate repositorion juuressa)
4. Asenna ohjelman dependencyt (pip install -r requirements.txt)
5. Ohjelma käynnistyy lokaalisti komennolla python3 run.py. Menemällä sivulle 127.0.0.1:5000 nettiselaimella pääset käyttämään ohjelmaa.
6. Tietokantaa voit käyttää sqlitella. Jos olet repositorion juuressa, komennolla sqlite3 application/forum.db pääset käyttämään tietokantaa.
