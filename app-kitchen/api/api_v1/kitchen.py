from uuid import UUID

from datetime import datetime

from flask.views import MethodView
from flask_smorest import Blueprint

from .schemas.kitchen import (
    GetScheduleOrderSchema,
    GetScheduleOrdersSchema,
    ScheduleStatusSchema,

    ScheduleOrderSchema,
    GetSheduleParameters,
)


blueprint_kitchen = Blueprint("kitchen", __name__, description="Kitchen API")

@blueprint_kitchen.route("/kitchen/schedules")
class KitchenSchedules(MethodView):
    """API для endpoints получения и создания новых планирований заказов"""

    @blueprint_kitchen.arguments(GetSheduleParameters, location="query") # аргументы запроса
    @blueprint_kitchen.response(status_code=200, schema=GetScheduleOrdersSchema) # представление ответа
    def get(self, parameters):
        """Получение планирований заказов"""
        pass
    
    @blueprint_kitchen.arguments(ScheduleOrderSchema)
    @blueprint_kitchen.response(status_code=201, schema=GetScheduleOrderSchema)
    def post(self, poyload):
        """Создание нового планирования заказов"""
        pass


@blueprint_kitchen.route("/kitchen/schedules/{schedule_id}")
class KitchenSchedules(MethodView):
    """API для endpoints получения, обновления и удаления планирования"""

    @blueprint_kitchen.response(status_code=200, schema=GetScheduleOrderSchema)
    def get(self, schedule_id: UUID):
        """Получение планирования по schedule_id"""
        pass
    
    @blueprint_kitchen.arguments(ScheduleOrderSchema)
    @blueprint_kitchen.response(status_code=200, schema=GetScheduleOrderSchema)
    def put(self, schedule_id: UUID):
        """Обновление планированния по schedule_id"""
        pass

    @blueprint_kitchen.response(status_code=204, schema=GetScheduleOrderSchema)
    def delete(self, schedule_id: UUID):
        """Удаление планирования по schedule_id"""
        pass


@blueprint_kitchen.response(status_code=200, schema=GetScheduleOrderSchema)
@blueprint_kitchen.route(
    "/kitchen/schedules/{schedule_id}/cancel",
    methods=["POST"]
)
def cancel_shedule(shedule_id: UUID):
    """Представление на основе функции для отмены заказа"""
    pass


@blueprint_kitchen.response(status_code=200, schema=ScheduleStatusSchema)
@blueprint_kitchen.route(
    "/kitchen/schedules/{schedule_id}/status",
    methods=["GET"]
)
def cancel_shedule(shedule_id: UUID):
    """Представление на основе функции для получения заказа"""
    pass
