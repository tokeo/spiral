from google.protobuf import empty_pb2
from tokeo.ext.appshare import app
from spiral.core import tasks
from .proto import spiral_pb2  # noqa: F401
from .proto import spiral_pb2_grpc  # noqa: F401


class SpiralServicer(spiral_pb2_grpc.SpiralServicer):

    def CountWords(self, request, context):
        app.print('SpiralServicer CountWords called for: ', request.url)
        tasks.actors.count_words.send(request.url)
        return empty_pb2.Empty()
