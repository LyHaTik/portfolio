import pprint
import re

async def _parse_call(call):
    result = re.split('/', call.data)
    command = result[0]
    photo_id = result[1]
    return command, photo_id