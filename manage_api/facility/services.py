from .models import DeliveryItem, Facility


class WasteQuantityService:
    def get_total_waste_quantity(self):
        delivery_items = DeliveryItem.objects.all()
        category_list = self.get_delivery_category_list(delivery_items)

        return {
            "catagory_list": category_list,
        }

    def get_waste_quantity_by_facility(self, facility_id):
        facility = Facility.objects.get(id=facility_id)
        delivery_items = DeliveryItem.objects.filter(facility=facility)

        category_list = self.get_delivery_category_list(delivery_items)

        return {
            "facility_id": facility.id,
            "facility_name": facility.name,
            "catagory_list": category_list,
        }

    def get_waste_quantity_by_facility_b(self, facility_id):
        facility = Facility.objects.get(id=facility_id)
        items = DeliveryItem.objects.filter(facility=facility)
        category_list = []
        categories_dict = {}
        for item in items:
            if item.waste_category.id in category_list:
                categories_dict[item.waste_category.id]["weight"] += item.weight
            else:
                category_list.append(item.waste_category.id)
                categories_dict[item.waste_category.id] = {
                    "category_id": item.waste_category.id,
                    "category_name": item.waste_category.name,
                    "waste_type": item.waste_category.waste_type.name,
                    "material_type": item.waste_category.material_type.name,
                    "weight": item.weight,
                }

        for i in range(len(category_list)):
            item = category_list[i]
            category_list[i] = categories_dict[item]

        return {
            "facility_id": facility.id,
            "facility_name": facility.name,
            "catagory_list": category_list,
        }

    def get_delivery_category_list(self, delivery_items):
        category_list = []
        categories_dict = {}
        for item in delivery_items:
            if item.waste_category.id in category_list:
                categories_dict[item.waste_category.id]["weight"] += item.weight
            else:
                category_list.append(item.waste_category.id)
                categories_dict[item.waste_category.id] = {
                    "category_id": item.waste_category.id,
                    "category_name": item.waste_category.name,
                    "waste_type": item.waste_category.waste_type.name,
                    "material_type": item.waste_category.material_type.name,
                    "weight": item.weight,
                }

        for i in range(len(category_list)):
            item = category_list[i]
            category_list[i] = categories_dict[item]
        return category_list
