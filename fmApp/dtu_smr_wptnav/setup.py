from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=[
  'mission/simple_mission.py',
  'navigation/waypoint_navigation_node.py',
  'monitor/robot_track_map_node.py'],
)

setup(**d)


