from typing import List, TypedDict

class CameraInfo(TypedDict):
    name: str
    index: int

def camera_list() -> List[CameraInfo]:
    """カメラの一覧を取得する

    Returns:
        List[CameraInfo]: カメラ情報のリスト
    """
    ...
