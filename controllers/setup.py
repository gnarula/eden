# -*- coding: utf-8 -*-

"""
    Setup Tool
"""

module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)

def index():
    """ Show the index """

    return dict()

def deploy():
    s3.actions = [
                    {
                        "label": str(current.T("View Status")),
                        "url": URL(c="setup", f="deploy", args=["[id]", "read"]),
                        "_class": "action-btn",
                    },
                 ]

    output =  s3_rest_controller()

    s3.scripts.append(URL('static', 'themes/setup/lightbox/js/lightbox-2.6.min.js'))

    # TODO: Add hook to call the backend code

    return output