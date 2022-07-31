from manage_api.facility.models import DeliveryItem
from .models import WasteCategory


class WasteCategoryHistoryService:
    def get_waste_history_by_category(self, category_id):
        waste_category = WasteCategory.objects.get(id=category_id)
        history_items = DeliveryItem.objects.filter(waste_category=waste_category)

        history_list = []
        for i in range(len(history_items)):
            item = history_items[i]
            history_list.append(
                {
                    "username": item.user.__str__(),
                    "time": item.created,
                    "quantity": item.weight,
                }
            )

        return {
            "category_id": category_id,
            "catagory_list": history_list,
        }
