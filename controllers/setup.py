# -*- coding: utf-8 -*-

"""
    Setup Tool
"""

module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)

def index():
    """ Redirect to default index """

    return redirect(URL('eden', 'default/index'))

def deploy():
    output =  s3_rest_controller("setup", "deploy")
    s3.scripts.append(URL('static', 'themes/setup/lightbox/js/lightbox-2.6.min.js'))

    # TODO: Add hook to call the backend code
    if request.args(0) == 'create':
        response.view = 'setup/create.html'

    return output