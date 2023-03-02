def interface(uchar):
  ext=[]
  sen=''
  print('Urdu Huroof-e-tahajji to Braille code')
  print('**********************************************\n')
  x=uchar.split()
  for i in range(len(x)):
    if ('1' in x[i]) or ('2' in x[i]) or ('3' in x[i]) or ('4' in x[i]) or ('5' in x[i]) or ('6' in x[i]) or ('7' in x[i]) or ('8' in x[i]) or ('9' in x[i]) or ('0' in x[i]):
      ext.append('no')
    for b in range(len(x[i])):
      ext.append((x[i])[b])
    ext.append(' ')
  a={'آ': '⠜',
  'ا': '⠁',
  'أ':'⠌',
 'ب': '⠃',
 'پ': '⠏',
 'ت': '⠞',
 'ٹ': '⠪',
 'ث': '⠹',
 'ج': '⠚',
 'چ': '⠉',
 'ح': '⠱',
 'خ': '⠭',
 'د': '⠙',
 'ڈ': '⠬',
 'ذ': '⠮',
 'ر': '⠗',
 'ڑ': '⠟',
 'ز':'⠵',
 'ژ': '⠷',
 'س': '⠎',
 'ش': '⠩',
 'ص': '⠯',
 'ض': '⠫',
 'ط': '⠾',
 'ظ': '⠿',
 'ع': '⠷',
 'غ': '⠣',
 'ف': '⠋',
 'ق': '⠟',
 'ک': '⠅',
 'گ': '⠛',
 'ل': '⠇',
 'م': '⠍',
 'ن': '⠝',
 'ں': '⠰',
 'و': '⠺',
 'ؤ':'⠳',
 'ه': '⠓',
 'ہ':'⠓',
 'ھ': '⠦',
 'ة':'⠡',
 'ء': '⠄',
 'ي': '⠊',
 'ی': '⠊',
 'ئ': '⠄',
 'ے': '⠌',
 '-': '⠤',
 '۔':'⠲',
 ',':'⠐',
 '،':'⠐',
 '؟':'⠦',
 '؛':'⠰',
 'ُ':'⠥',
 'َ':'⠂',
 'ِ':'⠑',
 'ً':'⠆',
 'ٍ ':'⠔',
 ':':'⠒',
 '!':'⠖',
 'ْ':'⠒',
 'ّ':'⠠',
 'no':'⠼',
 '1':'⠁',
 '2':'⠃',
 '3':'⠉',
 '4':'⠙',
 '5':'⠑',
 '6':'⠋',
 '7':'⠛',
 '8':'⠓',
 '9':'⠊',
 '0':'⠚',
 ' ':' '}
  for k in range(len(ext)):
    search=a[ext[k]]
    sen=sen+search+' '
  return str(sen)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():   
    return render_template("index.html")

@app.route("/translated", methods=['GET','POST'])
def method():
    if request.method=="POST":
        urduText=request.form.get('urdu')
        print(urduText)
        braileText=interface(urduText)
    return render_template("index2.html",urduText=urduText,braile=braileText)
    
if __name__ == '__main__':
   app.run()

