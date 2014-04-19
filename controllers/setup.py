# -*- coding: utf-8 -*-

"""
    Setup Tool
"""

import time
from os.path import join

module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)

def index():
    """ Show the index """

    return dict()

def deploy():
    s3db.configure("setup_deploy", create_onaccept=schedule)
    s3.actions = [
                    {
                        "label": str(current.T("View Status")),
                        "url": URL(c="setup", f="deploy", args=["[id]", "read"]),
                        "_class": "action-btn",
                    },
                 ]

    output =  s3_rest_controller()

    s3.scripts.append(URL("static", "themes/setup/lightbox/js/lightbox-2.6.min.js"))

    # TODO: Add hook to call the backend code

    return output

def schedule(form):
    """
        Schedule a deployment using s3task.
    """

    deployment = {}
    configs = {
        "hostname": form.vars.name,
        "key_path": join(request.folder, "uploads", form.vars.pemkey)
    }


    # add webserver
    if form.vars.web_server == "apache":
        deployment["setup_apache"] = {}
    else:
        deployment["setup_cherokee"] = {}

    # add database
    if form.vars.database_type == "mysql":
        deployment["setup_mysql"] = {}
    else:
        deployment["setup_postgresql"] = {}

    deployment["setup_eden"] = {"repo": form.vars.repo, "template": form.vars.template}

    if form.vars.coapps:
        for coapp in form.vars.coapps:
            deployment["setup_%s" % coapp.lower()] = {}

    task = "deployment_%d" % int(time.time())
    row = current.s3task.schedule_task(
        task,
        vars={"fab_tasks": deployment, "configs": configs},
        function_name="execute_tasks",
        repeats=1
    )
