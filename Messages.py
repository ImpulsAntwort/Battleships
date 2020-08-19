

class MessageHub:

    def __init__(self, player1, player2):
        player1.register_observer_msg(self)
        player2.register_observer_msg(self)
        self.msg_buffer = []

    def notify(self, plr_name, msg):
        self.msg_buffer.append([plr_name, msg])
        if len(self.msg_buffer) > 6:
            self.msg_buffer = self.msg_buffer[-6:]

    def msg_out(self):
        msg = []
        for line in self.msg_buffer:
            msg.append(self.create_output_txt(line))
        return msg

    @staticmethod
    def create_output_txt(line):
        return line[0] + " " + line[1]
