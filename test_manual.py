# Script para probar la API manualmente
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    """
    Script para probar todos los endpoints de la API
    Ejecutar cuando la API esté corriendo (python proyecto_api.py)
    """
    
    print("🚀 Probando API FastAPI...")
    print("=" * 50)
    
    # Test 1: Root endpoint
    print("\n1. Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Test 2: Crear item
    print("\n2. Creating new item...")
    item_data = {
        "name": "Smartphone",
        "description": "Latest model smartphone",
        "price": 599.99
    }
    
    try:
        response = requests.post(f"{BASE_URL}/items", json=item_data)
        print(f"Status: {response.status_code}")
        created_item = response.json()
        print(f"Created item: {created_item}")
        item_id = created_item.get("id")
    except Exception as e:
        print(f"Error creating item: {e}")
        return
    
    # Test 3: Listar items
    print("\n3. Listing all items...")
    try:
        response = requests.get(f"{BASE_URL}/items")
        print(f"Status: {response.status_code}")
        items = response.json()
        print(f"Items count: {len(items)}")
        for item in items:
            print(f"  - {item['name']}: ${item['price']}")
    except Exception as e:
        print(f"Error listing items: {e}")
    
    # Test 4: Obtener item específico
    print(f"\n4. Getting item {item_id}...")
    try:
        response = requests.get(f"{BASE_URL}/items/{item_id}")
        print(f"Status: {response.status_code}")
        item = response.json()
        print(f"Item: {item}")
    except Exception as e:
        print(f"Error getting item: {e}")
    
    # Test 5: Actualizar item
    print(f"\n5. Updating item {item_id}...")
    update_data = {
        "name": "Smartphone Pro",
        "description": "Premium smartphone with extra features",
        "price": 799.99
    }
    
    try:
        response = requests.put(f"{BASE_URL}/items/{item_id}", json=update_data)
        print(f"Status: {response.status_code}")
        updated_item = response.json()
        print(f"Updated item: {updated_item}")
    except Exception as e:
        print(f"Error updating item: {e}")
    
    # Test 6: Crear otro item para tener más datos
    print("\n6. Creating second item...")
    item_data_2 = {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1299.99
    }
    
    try:
        response = requests.post(f"{BASE_URL}/items", json=item_data_2)
        print(f"Status: {response.status_code}")
        second_item = response.json()
        print(f"Created second item: {second_item}")
        second_item_id = second_item.get("id")
    except Exception as e:
        print(f"Error creating second item: {e}")
        second_item_id = None
    
    # Test 7: Listar items actualizada
    print("\n7. Listing all items (updated)...")
    try:
        response = requests.get(f"{BASE_URL}/items")
        print(f"Status: {response.status_code}")
        items = response.json()
        print(f"Total items: {len(items)}")
        for item in items:
            print(f"  - ID {item['id']}: {item['name']} - ${item['price']}")
    except Exception as e:
        print(f"Error listing items: {e}")
    
    # Test 8: Error handling - item no existente
    print("\n8. Testing error handling (non-existent item)...")
    try:
        response = requests.get(f"{BASE_URL}/items/999")
        print(f"Status: {response.status_code}")
        error_response = response.json()
        print(f"Error response: {error_response}")
    except Exception as e:
        print(f"Error testing 404: {e}")
    
    # Test 9: Eliminar item
    print(f"\n9. Deleting item {item_id}...")
    try:
        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        print(f"Status: {response.status_code}")
        print("Item deleted successfully" if response.status_code == 204 else "Deletion failed")
    except Exception as e:
        print(f"Error deleting item: {e}")
    
    # Test 10: Verificar eliminación
    print(f"\n10. Verifying deletion...")
    try:
        response = requests.get(f"{BASE_URL}/items/{item_id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 404:
            print("✅ Item successfully deleted (404 as expected)")
        else:
            print("❌ Item still exists")
    except Exception as e:
        print(f"Error verifying deletion: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed!")
    print("\n💡 Tip: Visit http://127.0.0.1:8000/docs for interactive documentation")

if __name__ == "__main__":
    test_api()