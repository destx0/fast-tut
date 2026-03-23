from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"hii": "worls"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Not found")


def main():
    print("Hello from fast-tut!")


if __name__ == "__main__":
    main()
