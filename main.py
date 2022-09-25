from flask import Flask,request,render_template,Response
import cv2
import numpy
from pytesseract import pytesseract

app = Flask(__name__)

def ocr(text):                       #Limpieza de datos OCR
    try: 
        datos = text 
        cic_sp = datos.split("MEX")[1]
        cic = cic_sp.split("<")[0]
        cic = cic[:-1]
        ic_sp = datos.split("<<")[1]
        ic = ic_sp[4:13]
        ocr_sp = ic_sp
        ocr = ocr_sp[:13]
    
        datos_ine = {
        "cic" : cic,
        "identificadorCiudadano" : ic,
        "OCR" : ocr
        }    
        print(datos_ine)
        return render_template('ocr.html',datos = datos_ine)
      
    except:
        
        return render_template('error.html')
           
       	
@app.route("/",methods = ["GET","POST"])
def upload_image():

	if request.method == "POST":
		filestr = request.files['file'].read()	#obtener imagen o abrir camara del celular
		file_bytes = numpy.fromstring(filestr, numpy.uint8)
		image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED) #leer imagen
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray,(5,5),0)
		path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		pytesseract.tesseract_cmd = path_to_tesseract  
		text = pytesseract.image_to_string(blurred,lang='spa') #instanciar el metodo de pytesseract (reconocimiento de caracteres Ã³ptico )
    
		return Response(ocr(text))
        
	return render_template('index.html')
	

if __name__ == "__main__":
	app.run(debug=True,  port=5000) #host = 'IPv4', :  colocar la ip del celular obteniendola del cmd con el comando ipconfig, usar ipv4
