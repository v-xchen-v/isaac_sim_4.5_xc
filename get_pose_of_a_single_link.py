from isaacsim.core.prims import SingleXFormPrim

# get pose of a specific link
link_prim = SingleXFormPrim("/G1/head_link2")
position, orientation = link_prim.get_world_pose()
# position: (x, y, z) in world frame
# orientation: quaternion (w, x, y, z)

# save the position and orientaiton to a json file
import json
pose = {
    "position": position.tolist(),
    "orientation": orientation.tolist()
}
with open("link_pose.json", "w") as f:
    json.dump(pose, f, indent=4)