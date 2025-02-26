from marshmallow import Schema, fields, validate, EXCLUDE


class OrderItemSchema(Schema):
    """Представление схемы одной вещи"""
    class Meta:
        unknow = EXCLUDE # запрет неизвестных свойств

    product = fields.String(required=True)
    size = fields.String(
        required=True,
        validate=validate.OneOf(["small", "medium", "big"])
    )
    quantity = fields.Integer(
        required=True,
        validate=validate.Range(1, min_inclusive=True)
    )


class ScheduleOrderSchema(Schema):
    """Представление списка вещей"""
    class Meta:
        unknow = EXCLUDE # запрет неизвестных свойств

    order = fields.List(
        fields.Nested(OrderItemSchema),
        required=True,
    )


class GetScheduleOrderSchema(ScheduleOrderSchema):
    """Представление заказа"""
    id = fields.UUID(required=True)
    created = fields.DateTime(required=True)
    status = fields.String(
        required=True,
        validate=validate.OneOf(
            ["pending", "progress", "cancelled", "finished"]
        )
    )



class GetScheduleOrdersSchema(Schema):
    """Представление заказов"""
    class Meta:
        unknow = EXCLUDE # запрет неизвестных свойств

    shedules = fields.List(
        fields.Nested(GetScheduleOrderSchema),
        required=True,
    )


class GetSheduleParameters(Schema):
    """Параметры для получения заказов"""
    class Meta:
        unknow = EXCLUDE # запрет неизвестных свойств

    progress = fields.Bool()
    limit = fields.Integer()
    since = fields.DateTime()


class ScheduleStatusSchema(Schema):
    """Представление статуса заказа"""
    class Meta:
        unknow = EXCLUDE # запрет неизвестных свойств

    status = fields.String(
        required=True,
        validate=validate.OneOf(
            ["pending", "progress", "cancelled", "finished"]
        )
    )
    