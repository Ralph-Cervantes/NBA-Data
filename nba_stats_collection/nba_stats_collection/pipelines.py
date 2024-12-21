from itemadapter import ItemAdapter


class NbaStatsCollectionPipeline:
    def process_item(self, item, spider):
        return item


class BookScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for name in field_names:
            if name != 'description':
                value = adapter.get(name)
                adapter[name] = value.strip()
                
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()
        
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)
        
        return item
    
class SaveToSQLPipeline:
    def __init__(self):
        pass