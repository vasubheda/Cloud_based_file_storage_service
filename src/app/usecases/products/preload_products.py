import httpx
from fastapi import HTTPException
from app.repositories.product_repository import ProductRepository

DUMMY_JSON_URL = "https://dummyjson.com/products"

async def preload_products_usecase(db):
    """Fetches products from DummyJSON and preloads them into MongoDB if not already present."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(DUMMY_JSON_URL)

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to fetch products")

        data = response.json()
        products = data.get("products", [])

        if not products:
            raise HTTPException(status_code=404, detail="No products found in DummyJSON")

        product_repo = ProductRepository(db)

        # Check if products are already preloaded
        existing_count = await product_repo.count_products()
        if existing_count > 0:
            return {"message": "Products already preloaded, skipping import"}

        # Transform products and randomly assign a seller ID
        formatted_products = []
        for p in products:
            seller_id = await product_repo.get_random_seller_id()
            formatted_products.append({
                "title": p.get("title", "No Title"),
                "description": p.get("description", "No Description"),
                "category": p.get("category", "Unknown Category"),
                "price": p.get("price", 0.0),
                "rating": p.get("rating", 0.0),
                "brand": p.get("brand", "Unknown"),
                "images": p.get("images", []),  
                "thumbnail": p.get("thumbnail", ""),
                "seller_id": seller_id,
                "createdAt": p.get("createdAt", None),
                "updatedAt": p.get("updatedAt", None)
            })

        # Insert into MongoDB
        await product_repo.insert_products(formatted_products)

        return {"message": "Products preloaded successfully", "count": len(formatted_products)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
