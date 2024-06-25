from ultralytics import YOLO  # Import YOLO model from the ultralytics library
import cv2  # Import OpenCV library for computer vision tasks
import numpy as np  # Import numpy for numerical operations
from typing import Any, Generator  # Import typing for type hints


class YOLOModel:
    """Class for our YOLO model for cone detection"""

    def __init__(
        self,
        model_path="weights/best.pt",  # Path to the YOLO model weights
        cone_dimensions={
            "width": 0.228,
            "height": 0.325,
            "depth": 0.228,
        },  # Cone dimensions in meters
        camera_parameters={
            "width": 1280,
            "height": 720,
            "fov": 90,
        },  # Default camera parameters
    ) -> None:
        self.model_path = model_path  # Store model path
        self.model = YOLO(model_path)  # Load YOLO model with the specified weights
        self.camera_parameters = self.get_camera_parameters(
            camera_parameters
        )  # Store camera parameters
        self.cone_dimensions = cone_dimensions  # Store cone dimensions

        # Define cone classes
        self.classes: dict[int, str] = {
            0: "blue_cone",
            1: "yellow_cone",
            2: "orange_cone",
            3: "small_orange_cone",
            4: "large_orange_cone",
            5: "other_cone",
            6: "unknown_cone",
        }

        # Map class names to integer labels
        self.classes_to_int: dict[str, int] = {
            "blue_cone": 0,
            "yellow_cone": 1,
            "orange_cone": 2,
            "small_orange_cone": 3,
            "large_orange_cone": 4,
            "other_cone": 5,
            "unknown_cone": 6,
        }

    def get_camera_parameters(self, camera_params):
        cx = camera_params["width"] / 2
        cy = camera_params["height"] / 2
        denominator = 2 * np.tan(np.deg2rad(camera_params["fov"]) / 2)
        fx = camera_params["width"] / denominator
        fy = camera_params["height"] / denominator
        return {
            "fx": fx,
            "fy": fy,
            "cx": cx,
            "cy": cy,
        }

    def predict(self, image) -> None:
        preds = self.model.predict(image)[0]  # Run prediction on the input image
        return (
            preds.boxes.cls.detach()
            .cpu()
            .numpy(),  # Get predicted classes and convert to numpy array
            preds.boxes.xyxy.detach()
            .cpu()
            .numpy(),  # Get bounding boxes and convert to numpy array
        )

    def get_points(self, image) -> Generator[tuple[tuple, str], Any, None]:
        cone_classes, boxes = self.predict(
            image
        )  # Predict classes and bounding boxes for cones
        return self.pnp(cone_classes, boxes)  # Get 3D positions of cones

    def pnp(self, cone_classes, boxes) -> Generator[tuple[tuple, str], Any, None]:
        """PnP code to get 3D positions of cones"""

        image_points = []  # Initialize list for image points
        cone_types = []  # Initialize list for cone types

        for cone_class, box in zip(cone_classes, boxes):
            x1, y1, x2, y2 = box  # Extract box coordinates
            image_points.append(
                np.array(
                    [
                        [x1, y1],
                        [x2, y2],
                        [x1, y2],
                        [x2, y1],
                        [(x1 + x2) // 2, y1],  # Mid-point of top edge
                        [(x1 + x2) // 2, y2],  # Mid-point of bottom edge
                    ],
                    dtype=float,
                )
            )
            cone_types.append(int(cone_class))  # Store cone type

        # Extract camera intrinsic parameters
        fx = self.camera_parameters["fx"]
        fy = self.camera_parameters["fy"]
        cx = self.camera_parameters["cx"]
        cy = self.camera_parameters["cy"]

        # Camera calibration matrix
        camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=float)

        # Define known dimensions of the cones in meters
        cone_width = self.cone_dimensions["width"]
        cone_height = self.cone_dimensions["height"]
        # cone_depth = self.cone_dimensions["depth"]

        dist_coeffs = np.zeros(
            (4, 1)
        )  # Distortion coefficients, assuming zero distortion

        flag = cv2.SOLVEPNP_EPNP  # PnP method flag

        # 3D model points of the cone in the world coordinate system
        pnp_array = np.array(
            [
                [0, 0, 0],  # Top-left corner
                [cone_width, cone_height, 0.01],
                [0, cone_height, 0.01],  # Bottom-left corner
                [cone_width, 0, 0],  # Top-right corner
                [cone_width // 2, 0, 0],  # Mid-point of top edge
                [cone_width // 2, cone_height, 0],  # Mid-point of bottom edge
            ],
            dtype=float,
        )

        # 3D positions of the cones in the camera coordinate system
        cone_positions_camera_coords = np.array(
            [
                [0, 0, 0],
                [cone_width, 0, 0],
                [0, cone_height, 0],
                [cone_width, cone_height, 0],
            ],
            dtype=float,
        )

        for type_cone, image_point in zip(cone_types, image_points):
            retval, rvec, tvec = cv2.solvePnP(
                pnp_array,
                image_point,
                camera_matrix,
                dist_coeffs,
                flags=flag,
            )

            # rvec is the rotation vector, and tvec is the translation vector

            # Transform the 3D positions from camera coordinates to world coordinates
            try:
                rotation_matrix, _ = cv2.Rodrigues(
                    rvec
                )  # Convert rotation vector to matrix
                translation_vector = tvec  # Translation vector
                camera_to_world = np.hstack(
                    (rotation_matrix, translation_vector)
                )  # Create transformation matrix
                camera_to_world = np.vstack(
                    (camera_to_world, [0, 0, 0, 1])
                )  # Convert to 4x4 matrix

                # Transform the 3D positions of the cones into world coordinates
                cone_positions_world_coords = []
                for cone_position in cone_positions_camera_coords:
                    cone_position = np.hstack(
                        (cone_position, 1)
                    )  # Convert to homogeneous coordinates
                    cone_position_world = np.dot(
                        camera_to_world, cone_position
                    )  # Transform to world coordinates
                    cone_positions_world_coords.append(
                        cone_position_world[:3]
                    )  # Append the 3D position

                # Yield the 2D position and cone type
                yield (
                    (
                        cone_positions_world_coords[0][0],
                        cone_positions_world_coords[0][2],
                    ),
                    self.classes[type_cone],
                )

            except Exception as e:
                pass  # Handle exceptions silently


if __name__ == "__main__":

    path_weights = "weights/best.pt"  # Path to the YOLO model weights
    path_img = "images/amz_00000.jpg"  # Path to the input image

    # Camera parameters
    camera_parameters = {
        "width": 1280,
        "height": 720,
        "fov": 90,
    }

    # Cone dimensions in meters
    cone_dimensions = {
        "width": 0.228,
        "height": 0.325,
        "depth": 0.228,
    }

    # Initialize YOLOModel object
    model = YOLOModel(
        model_path=path_weights,
        camera_parameters=camera_parameters,
        cone_dimensions=cone_dimensions,
    )

    img = cv2.imread(path_img)  # Read the image

    img = model.get_points(
        img
    )  # Get points from the model, can work with path_img as well

    for i in img:
        print(i)  # Print the detected cone positions and types
