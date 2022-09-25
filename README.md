# Recognition-of-Mexican-identification-with-pytesseract-flask-and-cell-phone-camera

#Tesseract
1. Install Tesseract for Windows : https://github.com/UB-Mannheim/tesseract/wiki  in the installation choose spanish language
2. Install pytesseract : pip install pytesseract in cmd Python

#Flask
1. Install Flask in Python : https://pypi.org/project/Flask/

#Phone Camara
1. In main.py, in the line of app.run add host = 'cell IP' found in cmd with the ipconfig command
2. Two buttons were created in the index template, one of file type to open the cell phone camera and another submit button to send the image to be processed to the optical character recognition system.
