# waymo_demystifier
This repository collects a set of scripts and documentation to explore the Waymo Open Dataset. It given a detailed overview of the structure of this dataset which makes parsing for specific applications easier

![](waymo_demystified.png)

# Installation

```bash
git clone https://github.com/PaulKMueller/waymo_demystifier.git

cd waymo_demystifier

conda env create --file environment.yml

# This command creates the file "scenario_structure".
# The path for the TFRecord file to be parsed should be included in the config.yml.
python get_waymo_structure
```

An example of a parsed scenario is included (see data/scenario_example_structure.txt).

# Explanation of the Waymo Features
Unfortunately, it can be quite hard to get into doing research with the Waymo Open Dataset because it is hard
to get your hands on explicit information on how the dataset is structured and what the different features mean.
This repository tries to solve this issue.
The following is a list of all the tfrecord-files' features with an explcit interpretation of what they mean.
For more information on how the features are represented, see the usage of the script above and the file data/scenario_example_structure.txt.

## Features

### Traffic Light State Features:

1. **traffic_light_state/current/id**: Identifier for a traffic light in the current state.
2. **traffic_light_state/current/state**: The current state of the traffic light (like red, yellow, green).
3. **traffic_light_state/current/timestamp_micros**: The timestamp of the current traffic light state in microseconds.
4. **traffic_light_state/current/valid**: Indicates whether the current traffic light data is valid or reliable.
5. **traffic_light_state/current/x**: The X-coordinate of a traffic light's position in the current state.
6. **traffic_light_state/current/y**: The Y-coordinate of a traffic light's position in the current state.
7. **traffic_light_state/current/z**: The Z-coordinate of a traffic light's position in the current state.
8. **traffic_light_state/future/id**: Identifier for a traffic light in a future state.
9. **traffic_light_state/future/state**: The state of the traffic light (like red, yellow, green) in the future.
10. **traffic_light_state/future/timestamp_micros**: The timestamp of the future traffic light state in microseconds.
11. **traffic_light_state/future/valid**: Indicates whether the data about future traffic light states is valid or reliable.
12. **traffic_light_state/future/x**: The X-coordinate of a traffic light's position in a future state.
13. **traffic_light_state/future/y**: The Y-coordinate of a traffic light's position in a future state.
14. **traffic_light_state/future/z**: The Z-coordinate of a traffic light's position in a future state.
15. **traffic_light_state/past/id**: Identifier for a traffic light in the past state.
16. **traffic_light_state/past/state**: The state of the traffic light in the past.
17. **traffic_light_state/past/timestamp_micros**: The timestamp of the past traffic light state in microseconds.
18. **traffic_light_state/past/valid**: Indicates whether the data about past traffic light states is valid or reliable.
19. **traffic_light_state/past/x**: The X-coordinate of a traffic light's position in a past state.
20. **traffic_light_state/past/y**: The Y-coordinate of a traffic light's position in the past state.
21. **traffic_light_state/past/z**: The Z-coordinate of a traffic light's position in a past state.

### State Features:

1. **state/current/bbox_yaw**: The current yaw angle of a bounding box surrounding an object or vehicle.
2. **state/current/height**: The current height of an object or vehicle.
3. **state/current/length**: The current length of an object or vehicle.
4. **state/current/speed**: The current speed of an object or vehicle.
5. **state/current/timestamp_micros**: The timestamp of the current state in microseconds.
6. **state/current/valid**: Indicates whether the current state data is valid or reliable.
7. **state/current/velocity_x**: The component of the velocity in the X-axis direction currently.
8. **state/current/velocity_y**: The component of the velocity in the Y-axis direction currently.
9. **state/current/vel_yaw**: The current yaw velocity (rate of change of orientation).
10. **state/current/width**: The current width of an object or vehicle.
11. **state/current/x**: The current X-coordinate position of an object or vehicle.
12. **state/current/y**: The current Y-coordinate position of an object or vehicle.
13. **state/current/z**: The current Z-coordinate position of an object or vehicle.
14. **state/difficulty_level**: May refer to the difficulty level of a scenario or task, possibly in a simulation or test environment.
15. **state/future/bbox_yaw**: The future yaw angle of a bounding box surrounding an object or vehicle.
16. **state/future/height**: The height of an object or vehicle in the future state.
17. **state/future/length**: The length of an object or vehicle in the future state.
18. **state/future/speed**: The speed of an object or vehicle in the future state.
19. **state/future/timestamp_micros**: The timestamp of the future state in microseconds.
20. **state/future/valid**: Indicates whether the data about the future state is valid or reliable.
21. **state/future/velocity_x**: The component of the velocity in the X-axis direction in the future.
22. **state/future/velocity_y**: The component of the velocity in the Y-axis direction in the future.
23. **state/future/vel_yaw**: The future yaw velocity.
24. **state/future/width**: The width of an object or vehicle in the future state.
25. **state/future/x**: The X-coordinate position of an object or vehicle in a future state.
26. **state/future/y**: The Y-coordinate position of an object or vehicle in a future state.
27. **state/future/z**: The Z-coordinate position of an object or vehicle in a future state.
28. **state/id**: A unique identifier for the state being described or analyzed.
29. **state/is_sdc**: Indicates whether the current state is of a self-driving car (SDC).
30. **state/objects_of_interest**: Likely refers to objects in the scenario that are of particular interest, possibly for an autonomous vehicle or traffic analysis.
31. **state/past/bbox_yaw**: The past yaw angle of a bounding box surrounding an object or vehicle.
32. **state/past/height**: The height of an object or vehicle in the past state.
33. **state/past/length**: The length of an object or vehicle in the past state.
34. **state/past/speed**: The speed of an object or vehicle in the past.
35. **state/past/timestamp_micros**: The timestamp of the past state in microseconds.
36. **state/past/valid**: Indicates whether the data about the past state is valid or reliable.
37. **state/past/velocity_x**: The component of the velocity in the X-axis direction in the past.
38. **state/past/velocity_y**: The component of the velocity in the Y-axis direction in the past.
39. **state/past/vel_yaw**: The yaw velocity (rate of change of orientation) in the past.
40. **state/past/width**: The width of an object or vehicle in the past state.
41. **state/past/x**: The X-coordinate position of an object or vehicle in the past.
42. **state/past/y**: The Y-coordinate position of an object or vehicle in the past.
43. **state/past/z**: The Z-coordinate position of an object or vehicle in the past.
44. **state/scenario/id**: A unique identifier for the scenario being described or analyzed.
45. **state/tracks_to_predict**: Likely refers to the tracks or paths that are being predicted for certain objects or vehicles.
46. **state/type**: Likely refers to the type of the state or the type of an object or scenario being analyzed.

### Roadgraph Samples Features:

1. **roadgraph_samples/dir**: Direction of the road graph samples, possibly indicating the flow or layout of roads.
2. **roadgraph_samples/id**: Identifier for each road graph sample.
3. **roadgraph_samples/type**: The type of road graph samples, possibly indicating different features of the road or environment.
4. **roadgraph_samples/valid**: Indicates whether the road graph samples are valid.
5. **roadgraph_samples/xyz**: Coordinates (X, Y, Z) samples from a road graph or map.

### Other Features:

1. **scenario/id**: A unique identifier for the scenario being described or analyzed.
