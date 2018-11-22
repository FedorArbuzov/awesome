from sanic import Sanic, response
from sanic.response import json as jsonify
import xlrd

app = Sanic()


@app.route("/")
async def test(request):
    return response.html('''
    <!DOCTYPE html>
<html>
<body>

<form action="http://127.0.0.15:5050/upload" method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
</form>

</body>
</html>
    
    ''')


@app.post('/upload')
async def upload(request):
    print(request.body)
    f = open('test.xlsx', 'wb')
    f.write(request.files['fileToUpload'][0].body)
    f.close()
    book = xlrd.open_workbook('test.xlsx')
    print("The number of worksheets is {0}".format(book.nsheets))
    print("Worksheet name(s): {0}".format(book.sheet_names()))
    sh = book.sheet_by_index(0)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    for rx in range(sh.nrows):
        print(sh.row(rx))
    return jsonify({'result': 'ok'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
