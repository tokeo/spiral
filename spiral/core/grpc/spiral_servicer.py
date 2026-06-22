"""
gRPC servicer for the Spiral service.

Implements the service defined in the .proto file. The generated
spiral_pb2 and spiral_pb2_grpc modules provide the message
and stub classes; SpiralServicer subclasses the generated
servicer base and fills in the actual rpc methods.

### Notes

- The running app is reached through the shared instance from
    tokeo.ext.appshare, so the servicer needs no app reference passed in
- An rpc method should stay short: long running work is handed to background
    workers via Dramatiq (tasks.actors.*) instead of blocking the call
- Ping is a sync example: it answers 'pong' immediately, no worker dispatch,
    useful as a connectivity smoke test
- CountWords is the shipped example. It logs the incoming url, dispatches the
    count_words actor and returns an empty response right away

To add a new rpc method:

1. define it in the .proto file
1. regenerate the stubs with protoc (spiral_pb2 / spiral_pb2_grpc)
1. implement it on SpiralServicer
1. expose it as a command in the grpccall controller if needed

"""

from google.protobuf import empty_pb2
from tokeo.ext.appshare import app
from spiral.core import tasks
from .proto import spiral_pb2
from .proto import spiral_pb2_grpc  # noqa: F401


class SpiralServicer(spiral_pb2_grpc.SpiralServicer):

    def Ping(self, request, context):
        # sync, no dispatch: handy as a connectivity smoke test
        return spiral_pb2.PingResponse(message='pong')

    def CountWords(self, request, context):
        app.print('SpiralServicer CountWords called for: ', request.url)
        tasks.actors.count_words.send(request.url)
        return empty_pb2.Empty()
