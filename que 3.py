# Python object ko json string mai convert karne ka program likho?

import json
print(json.dumps({"name":"priya","age":"20"}))
print(json.dumps(["priya","amisha"]))
print(json.dumps(("pune","delhi")))
print(json.dumps(("13","45")))
print(json.dumps((10.3)))
print(json.dumps((True)))
print(json.dumps((False)))



