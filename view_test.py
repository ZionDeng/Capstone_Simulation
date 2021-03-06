from mujoco_py import load_model_from_path, MjSim, MjViewer

model_path = "xml/bot_env_v1.xml"
model = load_model_from_path(model_path)
sim = MjSim(model)
viewer = MjViewer(sim)

for i in range(15000):
    sim.step()
    viewer.render()