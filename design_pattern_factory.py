from project.core import createCore

core = createCore()

try:
    core.start()
    core.stop()
except:
    print("[Start] Uncaught error!")