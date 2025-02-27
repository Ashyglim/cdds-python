from .runtime import Runtime
from .dds_binding import DDSKeyValue

class TopicType(object):
    def gen_key(self): None


class FlexyTopic:
    def __init__(self, dp, name, keygen=None, qos=None):
        self.rt = Runtime.get_runtime()
        if keygen is None:
            self.keygen = lambda x: x.gen_key()
        else:
            self.keygen = keygen

        self.qos = self.rt.to_rw_qos(qos)
        self.type_support = self.rt.get_key_value_type_support()
        self.topic = self.rt.ddslib.dds_create_topic(dp.handle, self.type_support , name.encode(), self.qos, None)
        self.handle = self.topic
        assert (self.topic > 0)
        self.data_type = DDSKeyValue
        self.dp = dp
        self.namestr = name

    def gen_key(self, s):
        return self.keygen(s)


class Topic:
    def __init__(self, dp, topic_name, type_support, data_type, qos):
        self.rt = Runtime.get_runtime()
        self.topic_name = topic_name
        self.type_support = type_support
        self.data_type = data_type
        self.qos = self.rt.to_rw_qos(qos)

        self.topic = self.rt.ddslib.dds_create_topic(dp.handle, type_support, topic_name.encode(), self.qos, None)
        self.handle = self.topic
        assert (self.handle > 0)
