from feast import FeatureStore, Entity, FeatureView, Field
from feast.types import Int64
from datetime import timedelta

store = FeatureStore(repo_path=".")

entity = Entity(name="sku_store", join_keys=["store", "sku"])

sales_view = FeatureView(
    name="daily_sales",
    entities=[entity],
    ttl=timedelta(days=1),
    schema=[Field(name="sales", dtype=Int64)],
    online=True,
)
