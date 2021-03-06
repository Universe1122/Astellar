from flask import Blueprint, render_template, current_app, abort
from views.func import getFileNames, getFolderNames

bp = Blueprint("detail", __name__, url_prefix = "/detail")

@bp.route("/<target_name>", methods=["GET"])
def detail(target_name):

    if target_name.find(".") != -1 or target_name.find("/") != -1:
        abort(403, description = "Forbidden")

    target_path = current_app.config["SAVE_DIR_PATH"] + target_name
    folder_names = getFolderNames(current_app.config["SAVE_DIR_PATH"])

    if not target_name in folder_names:
        abort(400, description = "Can't find target site.")
    
    abort(500, description = "asdf")