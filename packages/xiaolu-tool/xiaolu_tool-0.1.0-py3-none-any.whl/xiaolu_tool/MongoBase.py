from pymodm import MongoModel
from pymodm.base.models import TopLevelMongoModelMetaclass
from .DBHelper import MongoDBManager


class BaseMongoMeta(TopLevelMongoModelMetaclass):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        # 检查是否为Base类或其子类（排除Base类本身）
        if bases and MongoModel not in bases:
            cls.ensure_connect()  # 调用conn方法


class MongoBaseModel(MongoModel, metaclass=BaseMongoMeta):
    @classmethod
    def ensure_connect(cls):
        alias = cls.Meta.connection_alias
        database = cls.Meta.database
        MongoDBManager.get_connection(database, alias)

    class Meta:
        abstract = True  # 指明这是一个抽象模型