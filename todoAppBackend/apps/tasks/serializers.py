import serpy

class TasksSerializers(serpy.Serializer):
    
    """
        This class convert tasks data into json
    """
    id = serpy.Field()
    # username = serpy.Field()
    title = serpy.Field()
    description = serpy.Field()
    created = serpy.Field()