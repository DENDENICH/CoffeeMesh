from uuid import UUID

from datetime import datetime

from flask.views import MethodView
from flask_smorest import Blueprint


blueprint_kitchen = Blueprint("kitchen", __name__, description="Kitchen API")

@blueprint_kitchen.route("/kitchen/schedules")
class KitchenSchedules(MethodView):
    """API для endpoints получения и создания новых планирований заказов"""

    def get(self):
        """Получение планирований заказов"""
        pass

    def post(self, poyload):
        """Создание нового планирования заказов"""
        pass


@blueprint_kitchen.route("/kitchen/schedules/{schedule_id}")
class KitchenSchedules(MethodView):
    """API для endpoints получения, обновления и удаления планирования"""

    def get(self, schedule_id: UUID):
        """Получение планирования по schedule_id"""
        pass

    def put(self, schedule_id: UUID):
        """Обновление планированния по schedule_id"""
        pass

    def delete(self, schedule_id: UUID):
        """Удаление планирования по schedule_id"""
        pass


@blueprint_kitchen.route(
    "/kitchen/schedules/{schedule_id}/cancel",
    methods=["POST"]
)
def cancel_shedule(shedule_id: UUID):
    """Представление на основе функции для отмены заказа"""
    pass


@blueprint_kitchen.route(
    "/kitchen/schedules/{schedule_id}/status",
    methods=["GET"]
)
def cancel_shedule(shedule_id: UUID):
    """Представление на основе функции для получения заказа"""
    pass
