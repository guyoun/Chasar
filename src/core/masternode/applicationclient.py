import zmq


class ApplicationClient:
    """
    Class send data received in master node to application example.
    """
    def __init__(self, port=6666):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://*:%s" % port)
        self.socket.sndhwm = 1

    def send(self, data_json, client_id):
        print(data_json)
        channel_name = ("Chasar-Client:%s" % client_id)

        self.socket.send_multipart([channel_name.encode('utf-8'), data_json])