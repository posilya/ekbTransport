#-*-coding=utf-8-*-
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = "text/html; charset=UTF-8"
        self.response.write('''
            <!DOCTYPE html>
            <head>
                <meta charset="UTF-8">
                <title>Простейший сайт на Python</title>
                <style>body {font-family: Helvetica, sans-serif;}</style>
            </head>
            <body>
                <div style="text-align: center; margin-top:70px">
                    <h2>Простейший сайт на Python</h2>
                    <p style="margin-top:100px">Сайт реализован на платформе Google App Engine</p>
                    <p>Движок - Python 2.7, standard environment.</p>
                </div>
            </body>
            </html>
        ''')

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
