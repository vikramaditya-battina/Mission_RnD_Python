from bottle import route, run, template,static_file,redirect,abort,request,response
@route('/hello')
@route('/hello/<na:int>')
def index():
    return 'this is great'
@route('/image')
def someimage():
    key=request.query_string

    print key
    return key

@route('/hello/<name>')
def vikram(name):
    print response.body
    return 'vikram'


@route('/upload',method='GET')
def forms():

    return '''
              <form action="/upload" method="post" enctype="multipart/form-data">
  <input type="text" name="name" />
  <input type="file" name="data" />
</form>'''


@route('/myip',method="POST")
def itsmyip():
    name= request.body

    print  name
    age=21

    return 'name is '+name+'age is'+age


@route('/upload', method='POST')
def do_upload():

    name = request.forms.name
    data = request.files.data
    if name and data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(raw))
    return "You missed a field."

run(host='localhost', port=8080,reloader=True,debug=True)