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

    return dict()

def deploy():
    output =  s3_rest_controller()
    s3.scripts.append(URL('static', 'themes/setup/lightbox/js/lightbox-2.6.min.js'))

    # TODO: Add hook to call the backend code

    return output