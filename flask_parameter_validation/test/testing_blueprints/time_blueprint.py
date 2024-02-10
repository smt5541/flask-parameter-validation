import datetime
from typing import Optional

from flask import Blueprint, jsonify

from flask_parameter_validation import ValidateParameters
from flask_parameter_validation.parameter_types.parameter import Parameter


def get_time_blueprint(ParamType: type[Parameter], bp_name: str) -> Blueprint:
    time_bp = Blueprint(bp_name, __name__, url_prefix="/time")

    @time_bp.get("/required")
    @ValidateParameters()
    def required(v: datetime.time = ParamType()):
        assert type(v) is datetime.time
        return jsonify({"v": v.isoformat()})

    @time_bp.get("/optional")
    @ValidateParameters()
    def optional(v: Optional[datetime.time] = ParamType()):
        if v:
            return jsonify({"v": v.isoformat()})
        return jsonify({"v": None})

    @time_bp.get("/default")
    @ValidateParameters()
    def default(
            n_opt: datetime.time = ParamType(default=datetime.time(23, 21, 23)),
            opt: Optional[datetime.time] = ParamType(default=datetime.time(23, 21, 35))
    ):
        return jsonify({
            "n_opt": n_opt.isoformat(),
            "opt": opt.isoformat()
        })

    def is_am(v):
        assert type(v) is datetime.time
        return v.hour < 12

    @time_bp.get("/func")
    @ValidateParameters()
    def func(v: datetime.time = ParamType(func=is_am)):
        return jsonify({"v": v.isoformat()})

    return time_bp