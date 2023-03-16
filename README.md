# rdw_kenteken
Dit is een programma waarin je een kenteken kan schrijven en het programma haalt automatisch alle data dat in de rdw's open database staat.

# Taal
Python v3.9.13

# Wat heb ik geleerd

 * Werken met API's
 * Het maken van een GUI met python
 * Herhalen van de 'docx' library
 

# Gebruikte files

 * car_app.py : Main file, hierin staat de code wat te maken heeft met de basics van tkinter
 * license_plate.py : Side file, hierin staat de code dat alle data sort en nieuwe tabs maakt in de app
 * car_data.py : Data file, staan dingen zoals de base_url etc.
 * car_api_response.py : Functie file, hierin staat de functie die de data opvraagt van de API
 * car_output.py : functie file, hierin staat de functie die alle data export naar een '.DOCX' file


# Bedoeling van het programma

De bedoeling van het programma is dat je het programma kan openen en in de tekstbox links boven een kenteken kan schrijven, waarna het programma alle data opvraagt
en dit laat zien in de tabs. Als in de database een andere API staat, moet het programma een nieuwe tab maken en deze API afgaan en alle data weergeven.
Als laatst moet het programma het aangeven als bij het gegeven kenteken geen informatie is en je moet een nieuw kenteken kunnen invoeren, zonder het programma te sluiten.


# Waar liep ik tegen aan

Het grootste probleem bij dit project was toch de tkinter lib. Het duurde best lang voordat ik erachter kwam hoe grid en pack niet met elkaar werkten.
Ook kwam ik niet verder met het verwijderen van data uit tabs. Ik heb uiteindelijk een oplossing gevonden door simpele apps te maken in een andere file
en daar manieren uit te proberen. Verder is dit project best soepel gegaan.

# Bijlage

![example_screen](https://user-images.githubusercontent.com/107985687/225565690-ef2d5e44-40e9-43bd-a302-3163cbfbe1a6.png)
^ voorbeeld van de app met data erin


![example_word](https://user-images.githubusercontent.com/107985687/225567514-3f2c1ca0-c148-4b79-a278-af1f90da01ed.png)

^ Example van word bestand export



