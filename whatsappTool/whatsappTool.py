import pywhatkit
import time
import json
import webbrowser
import win32clipboard 
file = open("../yad2/phone_numbers/kiryat krenitzi_2023-06-26.txt")
numbersArr = json.loads(file.read())
webbrowser.open('https://www.google.co.il/')
imgPath = 'C:\\Users\\Lior\\Desktop\\selenium\\python\\whatsappTool\\image.jpeg'
rent_text = 'היי\n נעים מאוד\n שמי אורנה אהרון\n שיווק נכסים (תיווך)\n אשמח להציע הצעה מפתה\n שלא תוכלו לסרב לה\n *לא גובה עמלת מיכם\n *חודש בלעדיות\n *מביאה לקוחות V.I.P\n עובדת כמעט 24/7\n יש לי מאגר גדולות של שוכרים\n שפונים אליי יום יום\n משכירים/מלווה שוכרים\n יד ביד עד חתימת חוזה\n השכרתי למעלה מ60\n דירות בשכונת בית בפארק\n עם מכתבי המלצה\n יש ברשותי מכתבי המלצה מבעלי דירות בבית בפארק מרוצים מאוד\n אוכל לשלוח אם תרצו\n ואשמח שנפגש\n לא גובה עמלת תיווך\n לאישור הקש 1\n להסר הקש 2\n *הנכסים שלי לא צוברים אבק*'
sale_text = 'שמי אורנה \n ואני יועצת נדלן \n ההתמחות שלי היא מכירת דירות. \n *מבצע עמלת תיווך 1% עבור המוכרים* \n ראיתי שאתם מפרסמים דירה \n אשמח אם נפגש ללא התחייבות \n ואראה לכם פרסום של שיווק נכס ברמה גבוהה.. \n לקוחות פונים אליי יום יום על מנת שאמצא להם דירה.. \n אני מוכרת את הנכסים בפרק זמן קצר \n אשמח לתגובתכם \n אורנה אהרון שיווק נכסים מ \n 0504215530 \n לאישור הקש 1 \n להסרה הקש 2'
def tool() :
    for number in numbersArr:
       try:
           time.sleep(4)
           pywhatkit.sendwhats_image(f'+972{number}', imgPath,rent_text,20,True,5)
           time.sleep(4) 
       except Exception as error :
        print(error)
    print("done")       
   
tool()
while (True):
     pass
