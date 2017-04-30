import time
from functools import wraps
from flask.json import jsonify


def json_response_with_time(fn):
    @wraps(fn)
    def with_json_time(*args, **kwargs):
        start_time = time.time()

        ret = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time
        if isinstance(ret, dict):
            ret['time'] = elapsed_time
            return jsonify(ret)
        else:
            return ret

    return with_json_time
