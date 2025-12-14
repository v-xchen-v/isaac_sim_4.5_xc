from isaacsim.core.prims import SingleXFormPrim
import numpy as np

# Method 1: Using world poses
link1 = SingleXFormPrim("/World/Robot/link1")
link2 = SingleXFormPrim("/World/Robot/link2")

pos1, quat1 = link1.get_world_pose()
pos2, quat2 = link2.get_world_pose()

# Compute relative position
relative_position = pos2 - pos1

# For full transformation, convert quaternions to rotation matrices
# and compute: T_relative = T1_inverse * T2
from scipy.spatial.transform import Rotation

R1 = Rotation.from_quat([quat1[1], quat1[2], quat1[3], quat1[0]]).as_matrix()  # w,x,y,z -> x,y,z,w
R2 = Rotation.from_quat([quat2[1], quat2[2], quat2[3], quat2[0]]).as_matrix()

# Relative rotation: R1^T * R2
relative_rotation = R1.T @ R2

# Relative position in link1 frame
relative_pos_in_link1_frame = R1.T @ (pos2 - pos1)

# save the relative pose to a json file
import json
relative_pose = {
    "relative_position": relative_pos_in_link1_frame.tolist(),
    "relative_rotation": relative_rotation.tolist()
}
with open("relative_pose.json", "w") as f:
    json.dump(relative_pose, f, indent=4)