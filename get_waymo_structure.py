import tensorflow as tf
import yaml


def get_feature_description(example_proto):
    # Create a description of the features
    feature_description = {}
    for key, feature in example_proto.features.feature.items():
        kind = feature.WhichOneof("kind")
        if kind == "bytes_list":
            dtype = tf.string
            feature_description[key] = tf.io.VarLenFeature(dtype)
        elif kind == "float_list":
            dtype = tf.float32
            feature_description[key] = tf.io.VarLenFeature(dtype)
        elif kind == "int64_list":
            dtype = tf.int64
            feature_description[key] = tf.io.VarLenFeature(dtype)
        else:
            raise ValueError(f"Unsupported feature type: {kind}")

    return feature_description


def parse_tfrecord(tfrecord_path) -> str:
    """This function parses one tfrecord file.
       Please give the path to the tfrecord file in the config of this repo.

    Args:
        tfrecord_path (str): Path to TFRecord file.
                             This is the standard file format when you download the Waymo Open Dataset.

    Returns:
        str: A description of the contents of the TFRecord file.
             This is really useful for later parsing the data in your specific application.
    """

    # Load the dataset
    dataset = tf.data.TFRecordDataset(tfrecord_path)
    output = ""
    for raw_record in dataset.take(1):  # Taking only one record to infer structure
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())

        feature_description = get_feature_description(example)

        # Parse the record into tensors
        parsed_record = tf.io.parse_single_example(raw_record, feature_description)

        for key, feature in parsed_record.items():
            if isinstance(feature, tf.SparseTensor):
                value = tf.sparse.to_dense(feature).numpy()
            else:
                value = feature.numpy()
            output = output + "\n" + f"Feature: {key}"
            output = output + "\n" + f" - Value: {value}"
            output = output + "\n" + f" - Shape: {value.shape}"
            output = output + "\n" + f" - DataType: {feature.dtype}\n"

    return output


# Provide the path to your TFRecord file
with open("config.yml") as config:
    config = yaml.safe_load(config)
    tfrecord_path = config["tfrecord_path"]

structure = parse_tfrecord(tfrecord_path)


with open("data/scenario_structure.txt", "w") as file:
    file.write(str(structure))
