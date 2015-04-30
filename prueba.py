from dateutil import dateutil


def on_post(req, resp):
    if req.method == 'POST':
        print "Something to do on POST"
        print dateutil.dateutil.now()
    else:
        print "something to do on NO POST"
        print "end"
